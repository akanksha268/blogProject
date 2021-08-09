from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmPassword = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    # To hash the password
    def save(self, commit=True):
        User = super().save(commit=False)
        User.set_password(self.cleaned_data["password"])
        if commit:
            User.save()
        return User


    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')





class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('about', 'profile_pic')
