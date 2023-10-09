from django import forms
from .models import Model3D

class ModelUploadForm(forms.ModelForm):
    class Meta:
        model = Model3D
        fields = ['title', 'description', 'file']