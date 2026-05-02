from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q, Avg
from django.views.decorators.http import require_POST
from .models import (Recipe, Category, State, Cuisine,
                     RegionalLanguage, UserSavedRecipe, RecipeRating)

INDIA_REGIONS = ['north', 'south', 'east', 'west', 'central', 'northeast', 'union']

def _user_state(request):
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        return request.user.profile.state
    return None


def home(request):
    user_state = _user_state(request)
    trending  = Recipe.objects.filter(is_published=True, is_trending=True).select_related('state').order_by('-view_count')[:10]
    featured  = Recipe.objects.filter(is_published=True, is_featured=True).order_by('-created_at')[:6]
    quick5    = Recipe.objects.filter(is_published=True, prep_time__lte=5,  cook_time__lte=5 ).order_by('-view_count')[:8]
    quick30   = Recipe.objects.filter(is_published=True, prep_time__lte=30, cook_time__lte=30).order_by('-view_count')[:8]
    states    = State.objects.filter(is_active=True).select_related('primary_language').order_by('order', 'name')
    categories= Category.objects.all().order_by('order')
    cuisines  = Cuisine.objects.filter(is_active=True)[:10]
    local_recipes = None
    if user_state:
        local_recipes = Recipe.objects.filter(is_published=True, state=user_state).order_by('-view_count')[:8]
    region_states = {}
    for r in INDIA_REGIONS:
        qs = states.filter(region=r)
        if qs.exists():
            region_states[r] = qs
    festival = Recipe.objects.filter(is_published=True).exclude(festival_tag='').order_by('-created_at')[:6]
    return render(request, 'recipes/home.html', {
        'trending': trending, 'featured': featured,
        'quick5': quick5, 'quick30': quick30,
        'states': states, 'region_states': region_states,
        'categories': categories, 'cuisines': cuisines,
        'local_recipes': local_recipes, 'user_state': user_state,
        'festival': festival,
    })


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, is_published=True)
    recipe.view_count += 1
    recipe.save(update_fields=['view_count'])

    lang_code   = request.GET.get('lang')
    translation = None
    if lang_code:
        translation = recipe.translations.filter(language__code=lang_code).first()

    # All languages for this state
    state_langs = []
    if recipe.state:
        if recipe.state.primary_language:
            state_langs.append(recipe.state.primary_language)
        extra = recipe.state.additional_languages.all()
        if recipe.state.primary_language:
            extra = extra.exclude(id=recipe.state.primary_language.id)
        state_langs += list(extra)

    ingredients = recipe.ingredients.all()
    steps       = recipe.steps.all()
    avg_rating  = recipe.ratings.aggregate(avg=Avg('rating'))['avg']
    user_rating = None
    is_saved    = False

    if request.user.is_authenticated:
        user_rating = recipe.ratings.filter(user=request.user).first()
        is_saved    = UserSavedRecipe.objects.filter(user=request.user, recipe=recipe).exists()

    related = Recipe.objects.filter(
        is_published=True, state=recipe.state
    ).exclude(id=recipe.id).order_by('-view_count')[:4]

    all_langs = RegionalLanguage.objects.filter(is_active=True)

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe, 'translation': translation,
        'state_langs': state_langs, 'all_langs': all_langs,
        'ingredients': ingredients, 'steps': steps,
        'avg_rating': avg_rating, 'user_rating': user_rating,
        'is_saved': is_saved, 'related': related,
    })


def recipe_list(request):
    recipes = Recipe.objects.filter(is_published=True).select_related('state', 'cuisine')
    q            = request.GET.get('q', '').strip()
    state_slug   = request.GET.get('state', '')
    cuisine_slug = request.GET.get('cuisine', '')
    cat_slug     = request.GET.get('category', '')
    diet         = request.GET.get('diet', '')
    difficulty   = request.GET.get('difficulty', '')
    max_time     = request.GET.get('max_time', '')
    region       = request.GET.get('region', '')
    if q:
        recipes = recipes.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(festival_tag__icontains=q))
    if state_slug:
        recipes = recipes.filter(state__slug=state_slug)
    if cuisine_slug:
        recipes = recipes.filter(cuisine__slug=cuisine_slug)
    if cat_slug:
        recipes = recipes.filter(categories__slug=cat_slug)
    if diet:
        recipes = recipes.filter(diet_type=diet)
    if difficulty:
        recipes = recipes.filter(difficulty=difficulty)
    if max_time:
        try:
            t = int(max_time)
            recipes = recipes.filter(prep_time__lte=t, cook_time__lte=t)
        except ValueError:
            pass
    if region:
        recipes = recipes.filter(state__region=region)
    recipes = recipes.distinct().order_by('-view_count', '-created_at')
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'states':      State.objects.filter(is_active=True).order_by('name'),
        'cuisines':    Cuisine.objects.filter(is_active=True),
        'categories':  Category.objects.all().order_by('order'),
        'q': q, 'selected_state': state_slug, 'selected_cuisine': cuisine_slug,
        'selected_cat': cat_slug, 'selected_diet': diet,
        'selected_difficulty': difficulty, 'selected_max_time': max_time,
        'selected_region': region,
        'diet_choices':   Recipe.DIET_CHOICES,
        'region_choices': State.REGION_CHOICES,
    })


def state_detail(request, slug):
    state    = get_object_or_404(State, slug=slug, is_active=True)
    recipes  = Recipe.objects.filter(is_published=True, state=state).order_by('-view_count')
    cuisines = Cuisine.objects.filter(states=state)
    state_langs = []
    if state.primary_language:
        state_langs.append(state.primary_language)
    state_langs += list(state.additional_languages.all())
    return render(request, 'recipes/state_detail.html', {
        'state': state, 'recipes': recipes,
        'cuisines': cuisines, 'state_langs': state_langs,
    })


def cuisine_detail(request, slug):
    cuisine = get_object_or_404(Cuisine, slug=slug, is_active=True)
    recipes = Recipe.objects.filter(is_published=True, cuisine=cuisine).order_by('-view_count')
    return render(request, 'recipes/cuisine_detail.html', {'cuisine': cuisine, 'recipes': recipes})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    recipes  = Recipe.objects.filter(is_published=True, categories=category).order_by('-view_count')
    return render(request, 'recipes/category_detail.html', {'category': category, 'recipes': recipes})


# ── AJAX endpoints ────────────────────────────────────────────────────────────

def get_translation(request, slug):
    """
    Returns translated title + description for a recipe in the requested language.
    Falls back to original English if no translation exists.
    """
    recipe    = get_object_or_404(Recipe, slug=slug)
    lang_code = request.GET.get('lang', 'en')

    if lang_code == 'en':
        return JsonResponse({
            'title':       recipe.title,
            'description': recipe.description,
            'found':       True,
            'is_original': True,
        })

    trans = recipe.translations.filter(language__code=lang_code).first()
    if trans:
        return JsonResponse({
            'title':       trans.title,
            'description': trans.description,
            'found':       True,
            'is_original': False,
        })

    # No translation exists — return original with a flag so JS can show a notice
    return JsonResponse({
        'title':       recipe.title,
        'description': recipe.description,
        'found':       False,
        'is_original': True,
        'message':     'Translation not available yet. Showing original.',
    })


@login_required
@require_POST
def toggle_save(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    obj, created = UserSavedRecipe.objects.get_or_create(user=request.user, recipe=recipe)
    if not created:
        obj.delete()
        return JsonResponse({'saved': False})
    return JsonResponse({'saved': True})


@login_required
@require_POST
def rate_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    try:
        val = int(request.POST.get('rating', 0))
    except ValueError:
        val = 0
    if 1 <= val <= 5:
        RecipeRating.objects.update_or_create(
            user=request.user, recipe=recipe, defaults={'rating': val})
    avg = recipe.ratings.aggregate(avg=Avg('rating'))['avg']
    return JsonResponse({'avg': round(avg, 1) if avg else 0})
