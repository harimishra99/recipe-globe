from .models import Category, State, Cuisine

def site_context(request):
    return {
        'nav_categories': Category.objects.all().order_by('order')[:8],
        'nav_states':     State.objects.filter(is_active=True).order_by('name')[:30],
        'nav_cuisines':   Cuisine.objects.filter(is_active=True)[:10],
    }
