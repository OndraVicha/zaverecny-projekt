from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

def validate_blend_file(value):
    if not value.name.endswith('.blend'):
        raise ValidationError('Invalid file format. Please upload a .blend file.')

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ThreeDModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=User)
    title = models.CharField(max_length=255,unique=False, verbose_name="Title")
    description = models.TextField(blank=True, null=True, verbose_name="description")
    upload_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='3dmodel_images/', blank=True, null=True, help_text='Upload an image')
    file = models.FileField(upload_to='3dmodels/',help_text='Please use only .blend files', validators=[validate_blend_file])
    rating_average = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.title