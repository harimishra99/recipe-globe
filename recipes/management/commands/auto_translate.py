"""
Management command to auto-translate all recipes into Indian regional languages.

Usage:
    python manage.py auto_translate
    python manage.py auto_translate --lang hi          # only Hindi
    python manage.py auto_translate --recipe dal-makhani  # one recipe only

Uses deep-translator (Google Translate free API) — no API key needed.
Safe to run multiple times — skips already translated recipes.
"""

from django.core.management.base import BaseCommand
from recipes.models import Recipe, RecipeTranslation, RegionalLanguage

try:
    from deep_translator import GoogleTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False


# Map our language codes to Google Translate codes
LANG_MAP = {
    'hi':  'hi',   # Hindi
    'bn':  'bn',   # Bengali
    'te':  'te',   # Telugu
    'mr':  'mr',   # Marathi
    'ta':  'ta',   # Tamil
    'gu':  'gu',   # Gujarati
    'kn':  'kn',   # Kannada
    'ml':  'ml',   # Malayalam
    'pa':  'pa',   # Punjabi
    'or':  'or',   # Odia
    'as':  'as',   # Assamese
    'ur':  'ur',   # Urdu
    'ne':  'ne',   # Nepali
    'kok': 'gom',  # Konkani (closest Google code)
}


def translate_text(text, target_lang_code):
    """Translate text to target language. Returns original if translation fails."""
    try:
        google_code = LANG_MAP.get(target_lang_code, target_lang_code)
        translator  = GoogleTranslator(source='en', target=google_code)

        # Google Translate has a 5000 char limit per call
        if len(text) <= 4800:
            return translator.translate(text)

        # Split long text into chunks and translate each
        chunks = [text[i:i+4800] for i in range(0, len(text), 4800)]
        return ' '.join(translator.translate(chunk) for chunk in chunks)

    except Exception as e:
        return None


class Command(BaseCommand):
    help = 'Auto-translate all recipes into Indian regional languages using Google Translate'

    def add_arguments(self, parser):
        parser.add_argument(
            '--lang',
            type=str,
            default=None,
            help='Only translate into this language code (e.g. hi, ta, bn). Default: all languages.',
        )
        parser.add_argument(
            '--recipe',
            type=str,
            default=None,
            help='Only translate this recipe slug. Default: all recipes.',
        )
        parser.add_argument(
            '--overwrite',
            action='store_true',
            default=False,
            help='Overwrite existing translations. Default: skip existing.',
        )

    def handle(self, *args, **options):
        if not TRANSLATOR_AVAILABLE:
            self.stdout.write(self.style.ERROR(
                '❌ deep-translator not installed. Run: pip install deep-translator'
            ))
            return

        # Get languages to translate into
        lang_filter = options['lang']
        if lang_filter:
            languages = RegionalLanguage.objects.filter(
                code=lang_filter, is_active=True
            )
            if not languages.exists():
                self.stdout.write(self.style.ERROR(
                    f'❌ Language code "{lang_filter}" not found in database.'
                ))
                return
        else:
            # All languages except English
            languages = RegionalLanguage.objects.filter(
                is_active=True
            ).exclude(code='en')

        # Get recipes to translate
        recipe_filter = options['recipe']
        if recipe_filter:
            recipes = Recipe.objects.filter(slug=recipe_filter, is_published=True)
            if not recipes.exists():
                self.stdout.write(self.style.ERROR(
                    f'❌ Recipe slug "{recipe_filter}" not found.'
                ))
                return
        else:
            recipes = Recipe.objects.filter(is_published=True)

        overwrite   = options['overwrite']
        total_done  = 0
        total_skip  = 0
        total_fail  = 0

        self.stdout.write(self.style.MIGRATE_HEADING(
            f'\n🌐 Translating {recipes.count()} recipes into {languages.count()} languages...\n'
        ))

        for recipe in recipes:
            self.stdout.write(f'📖 {recipe.title}')

            for lang in languages:
                # Skip if translation already exists and overwrite is False
                exists = RecipeTranslation.objects.filter(
                    recipe=recipe, language=lang
                ).exists()

                if exists and not overwrite:
                    self.stdout.write(f'   ⏭️  {lang.name} — already exists, skipping')
                    total_skip += 1
                    continue

                # Translate title
                translated_title = translate_text(recipe.title, lang.code)
                if not translated_title:
                    self.stdout.write(
                        self.style.WARNING(f'   ⚠️  {lang.name} — title translation failed')
                    )
                    total_fail += 1
                    continue

                # Translate description
                translated_desc = translate_text(recipe.description, lang.code)
                if not translated_desc:
                    self.stdout.write(
                        self.style.WARNING(f'   ⚠️  {lang.name} — description translation failed')
                    )
                    total_fail += 1
                    continue

                # Save to database
                RecipeTranslation.objects.update_or_create(
                    recipe=recipe,
                    language=lang,
                    defaults={
                        'title':       translated_title,
                        'description': translated_desc,
                    }
                )

                self.stdout.write(
                    self.style.SUCCESS(f'   ✅ {lang.name} — "{translated_title}"')
                )
                total_done += 1

            self.stdout.write('')

        # Summary
        self.stdout.write(self.style.SUCCESS(
            f'\n🎉 Done!\n'
            f'   ✅ Translated : {total_done}\n'
            f'   ⏭️  Skipped   : {total_skip}\n'
            f'   ⚠️  Failed    : {total_fail}\n'
        ))