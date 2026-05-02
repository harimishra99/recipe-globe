from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
import uuid


class RegionalLanguage(models.Model):
    """A language spoken in India (or any future country)."""
    code        = models.CharField(max_length=10, unique=True)
    name        = models.CharField(max_length=100)          # English name
    native_name = models.CharField(max_length=100, blank=True)  # e.g. हिन्दी
    script      = models.CharField(max_length=80, blank=True)   # e.g. Devanagari
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Regional Language'

    def __str__(self):
        return f"{self.name} ({self.native_name})"


class Country(models.Model):
    """Top-level geography. Currently only India; scalable to others."""
    name             = models.CharField(max_length=100, unique=True)
    code             = models.CharField(max_length=3, unique=True)   # ISO 3166-1 alpha-3
    flag_emoji       = models.CharField(max_length=10, blank=True)
    default_language = models.ForeignKey(
        RegionalLanguage, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='default_for_countries'
    )
    is_active        = models.BooleanField(default=True)
    description      = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name']

    def __str__(self):
        return f"{self.flag_emoji} {self.name}"


class State(models.Model):
    """
    An Indian state (or any sub-national region in a future country).
    Stores its primary language for the language-switcher feature.
    """
    REGION_CHOICES = [
        ('north',     'North India'),
        ('south',     'South India'),
        ('east',      'East India'),
        ('west',      'West India'),
        ('central',   'Central India'),
        ('northeast', 'Northeast India'),
        ('union',     'Union Territory'),
    ]

    country          = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    name             = models.CharField(max_length=120)
    slug             = models.SlugField(unique=True, blank=True)
    native_name      = models.CharField(max_length=120, blank=True)   # e.g. महाराष्ट्र
    code             = models.CharField(max_length=5, unique=True)     # e.g. MH, UP, KA
    capital          = models.CharField(max_length=100, blank=True)
    region           = models.CharField(max_length=20, choices=REGION_CHOICES, blank=True)
    primary_language = models.ForeignKey(
        RegionalLanguage, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='primary_states',
        help_text='Main language of this state — used for language switcher'
    )
    additional_languages = models.ManyToManyField(
        RegionalLanguage, blank=True,
        related_name='additional_states',
        help_text='Other languages spoken in this state'
    )
    description      = models.TextField(blank=True)
    cuisine_summary  = models.TextField(blank=True,
        help_text='Brief summary of the state\'s cuisine for the state page')
    banner_image_url = models.URLField(blank=True)
    is_active        = models.BooleanField(default=True)
    order            = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('state_recipes', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Cuisine(models.Model):
    """
    A named culinary tradition — can span multiple states or countries.
    E.g. 'Mughlai', 'Chettinad', 'Awadhi', 'Bengali', 'Konkani'.
    """
    name        = models.CharField(max_length=120, unique=True)
    slug        = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    states      = models.ManyToManyField(State, blank=True, related_name='cuisines')
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Recipe categories: time-based, occasion, meal type, diet, etc.
    Fully generic — works for any country.
    """
    TYPE_CHOICES = [
        ('time',      'Time-Based'),
        ('occasion',  'Occasion'),
        ('meal',      'Meal Type'),
        ('diet',      'Dietary'),
        ('course',    'Course'),
        ('festival',  'Festival / Seasonal'),
    ]

    name             = models.CharField(max_length=100)
    slug             = models.SlugField(unique=True, blank=True)
    category_type    = models.CharField(max_length=20, choices=TYPE_CHOICES, default='occasion')
    icon             = models.CharField(max_length=60, blank=True,
                           help_text='Font Awesome class e.g. fa-bolt')
    emoji            = models.CharField(max_length=8, blank=True)
    color            = models.CharField(max_length=7, default='#FF6B35')
    description      = models.TextField(blank=True)
    max_time_minutes = models.PositiveIntegerField(null=True, blank=True)
    order            = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy',   'Easy'),
        ('medium', 'Medium'),
        ('hard',   'Hard'),
    ]
    DIET_CHOICES = [
        ('veg',    'Vegetarian 🥦'),
        ('nonveg', 'Non-Vegetarian 🍗'),
        ('vegan',  'Vegan 🌱'),
        ('jain',   'Jain 🌿'),
        ('eggt',   'Eggetarian 🥚'),
    ]

    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title       = models.CharField(max_length=220)
    slug        = models.SlugField(unique=True, blank=True, max_length=240)
    description = models.TextField()
    author      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                      related_name='recipes')

    # Geography (scalable)
    country     = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True,
                      related_name='recipes')
    state       = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True,
                      related_name='recipes',
                      help_text='Indian state this recipe originates from')
    cuisine     = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True, blank=True,
                      related_name='recipes')

    # Classification
    categories  = models.ManyToManyField(Category, related_name='recipes', blank=True)
    diet_type   = models.CharField(max_length=10, choices=DIET_CHOICES, default='veg')
    difficulty  = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')

    # Timing
    prep_time   = models.PositiveIntegerField(default=0, help_text='minutes')
    cook_time   = models.PositiveIntegerField(default=0, help_text='minutes')
    servings    = models.PositiveIntegerField(default=4)
    calories_per_serving = models.PositiveIntegerField(null=True, blank=True)

    # Media
    image       = models.ImageField(upload_to='recipes/', blank=True, null=True)
    image_url   = models.URLField(blank=True,
                      help_text='External image URL (Unsplash etc.) — used when no file uploaded')

    # Status
    is_trending  = models.BooleanField(default=False)
    is_featured  = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    view_count   = models.PositiveIntegerField(default=0)

    # Festival / season tag
    festival_tag = models.CharField(max_length=80, blank=True,
                       help_text='e.g. Diwali Special, Eid Special, Pongal')

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def total_time(self):
        return self.prep_time + self.cook_time

    @property
    def image_display(self):
        if self.image:
            return self.image.url
        return self.image_url or 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&q=80'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            self.slug = base
            n = 1
            while Recipe.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base}-{n}"
                n += 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class RecipeTranslation(models.Model):
    """
    Stores a translated version of a recipe's title + description in a regional language.
    Steps and ingredients can also be translated via TranslatedStep / TranslatedIngredient
    if needed in future.
    """
    recipe      = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='translations')
    language    = models.ForeignKey(RegionalLanguage, on_delete=models.CASCADE)
    title       = models.CharField(max_length=220)
    description = models.TextField()

    class Meta:
        unique_together = ['recipe', 'language']

    def __str__(self):
        return f"{self.recipe.title} [{self.language.code}]"


class Ingredient(models.Model):
    recipe   = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name     = models.CharField(max_length=200)
    quantity = models.CharField(max_length=60, blank=True)
    unit     = models.CharField(max_length=60, blank=True)
    notes    = models.CharField(max_length=200, blank=True)
    order    = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}".strip()


class RecipeStep(models.Model):
    recipe      = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
    step_number = models.PositiveIntegerField()
    instruction = models.TextField()
    tip         = models.CharField(max_length=400, blank=True)
    time_minutes= models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['step_number']
        unique_together = ['recipe', 'step_number']

    def __str__(self):
        return f"Step {self.step_number} – {self.recipe.title}"


class UserSavedRecipe(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_recipes')
    recipe   = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='saved_by')
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'recipe']
        ordering = ['-saved_at']


class RecipeRating(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe     = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    rating     = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'recipe']
