from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from recipes.models import RegionalLanguage, State, UserSavedRecipe


@login_required
def profile_view(request):
    profile = request.user.profile
    saved   = UserSavedRecipe.objects.filter(user=request.user).select_related('recipe')[:12]
    return render(request, 'accounts/profile.html', {'profile': profile, 'saved': saved})


@login_required
def edit_profile(request):
    profile   = request.user.profile
    languages = RegionalLanguage.objects.filter(is_active=True)
    states    = State.objects.filter(is_active=True).order_by('name')

    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name  = request.POST.get('last_name', '')
        request.user.save()

        profile.bio = request.POST.get('bio', '')

        lang_id  = request.POST.get('preferred_language')
        state_id = request.POST.get('state')

        profile.preferred_language = RegionalLanguage.objects.filter(id=lang_id).first() if lang_id else None
        profile.state              = State.objects.filter(id=state_id).first() if state_id else None

        if request.FILES.get('avatar'):
            profile.avatar = request.FILES['avatar']

        profile.save()
        messages.success(request, '✅ Profile updated successfully!')
        return redirect('profile')

    return render(request, 'accounts/edit_profile.html', {
        'profile': profile, 'languages': languages, 'states': states
    })


@login_required
def saved_recipes(request):
    saved = UserSavedRecipe.objects.filter(user=request.user).select_related('recipe')
    return render(request, 'accounts/saved_recipes.html', {'saved': saved})
