from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name',
                     widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name  = forms.CharField(max_length=30, label='Last Name', required=False,
                     widget=forms.TextInput(attrs={'placeholder': 'Last name (optional)'}))

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data.get('last_name', '')
        user.save()
        return user
