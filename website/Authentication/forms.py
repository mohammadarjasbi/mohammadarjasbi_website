from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "text-input-register", 'type': 'password'}))
    new_password1 = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"class": "text-input-register", 'type': 'password'}))
    new_password2 = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"class": "text-input-register", 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class UserProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "text-input-register"}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "text-input-register"}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "text-input-register"}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "text-input-register"}))

    password = ReadOnlyPasswordHashField(
        label=(''),
        help_text=('''You can change the password 
                   using <a href="change_password\">this form</a>.'''))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'username')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio')
