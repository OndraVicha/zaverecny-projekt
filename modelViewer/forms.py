from django import forms
from .models import ThreeDModel, Category, UserProfile
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm

class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add classes to form fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class ThreeDModelForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = ThreeDModel
        fields = ['title', 'file', 'textures', 'image', 'description', 'categories']

    textures = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
    )

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        'textures': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'categories': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    }

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'bio', 'pronouns','profile_picture']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(),
            'pronouns':  forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }