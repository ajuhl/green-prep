from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
