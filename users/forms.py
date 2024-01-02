from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserSignupForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'password1', 'password2', 'bio', 'profile_image']
        labels = {
            'name': 'Name',
        }
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'input'}),
            'password2': forms.PasswordInput(attrs={'class': 'input'}),
        }

    #def __init__(self, *args, **kwargs):
    #    super(UserSignupForm, self).__init__(*args, **kwargs)
#
    #    for name, field in self.fields.items():
    #        field.widget.attrs.update({'class': 'input'})


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'bio', 'profile_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'username': forms.TextInput(attrs={'class': 'input'}),
        }
        
    #def __init__(self, *args, **kwargs):
    #    super(UserProfileForm, self).__init__(*args, **kwargs)
#
    #    for name, field in self.fields.items():
    #        field.widget.attrs.update({'class': 'input'})


"""
class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ['business', 'body']
"""