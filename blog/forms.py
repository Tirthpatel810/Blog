from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'profile_photo']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email