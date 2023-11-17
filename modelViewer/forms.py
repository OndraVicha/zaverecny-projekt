from django import forms
from django.shortcuts import render
from .models import ThreeDModel, Category
from django.contrib.auth.forms import AuthenticationForm

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
        fields = ['title', 'file','image','description','categories']

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'categories': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    }
