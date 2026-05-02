from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display  = ['user', 'preferred_language', 'state', 'created_at']
    list_filter   = ['state', 'preferred_language']
    search_fields = ['user__username', 'user__email']
    autocomplete_fields = ['preferred_language', 'state']
