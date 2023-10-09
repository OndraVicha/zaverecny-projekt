from django.db import models
from django.contrib.auth.models import User

class Model3D(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='model_uploads/')
    rating_average = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class Image2D(models.Model):
    model3D = models.ForeignKey(Model3D, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image_uploads/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model3D = models.ForeignKey(Model3D, on_delete=models.CASCADE)
    text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model3D = models.ForeignKey(Model3D, on_delete=models.CASCADE)
    value = models.IntegerField()