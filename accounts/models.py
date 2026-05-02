from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user               = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio                = models.TextField(blank=True)
    avatar             = models.ImageField(upload_to='avatars/', blank=True, null=True)
    preferred_language = models.ForeignKey(
        'recipes.RegionalLanguage', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='users')
    state              = models.ForeignKey(
        'recipes.State', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='users',
        help_text='Your home state — personalises your recipe feed')
    created_at         = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile – {self.user.username}"

    @property
    def display_name(self):
        return self.user.get_full_name() or self.user.username

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        initials = self.display_name[:2].upper()
        return f"https://ui-avatars.com/api/?name={initials}&background=FF6B35&color=fff&size=128&bold=true"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
