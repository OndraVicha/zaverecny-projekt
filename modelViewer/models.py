from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
import os
from django.db.models import Avg

def validate_gltf_file(value):
    valid_extensions = ['.glb', '.gltf']
    ext = os.path.splitext(value.name)[1]  # Get the file extension

    if ext.lower() not in valid_extensions:
        raise ValidationError('Invalid file format. Please upload a .glb or .gltf file.')

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ThreeDModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=User)
    title = models.CharField(max_length=255, unique=False, verbose_name="Title")
    description = models.TextField(blank=True, null=True, verbose_name="description")
    upload_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='3dmodel_images/', blank=True, null=True, help_text='Upload an image')
    file = models.FileField(upload_to='3dmodels/', help_text='Please use only .glb or .gltf file', validators=[validate_gltf_file])
    categories = models.ManyToManyField(Category)

    def average_rating(self):
        return Rating.objects.filter(model=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.title}: {self.average_rating()}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey('ThreeDModel', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    class Meta:
        unique_together = ('user', 'model')  # Ensures the uniqueness of ratings for each user and model

    def __str__(self):
        return f"{self.model.title}: {self.rating}"

