from django.contrib import admin
from .models import Model3D, Image2D, Comment, Rating

admin.site.register(Model3D)
admin.site.register(Image2D)
admin.site.register(Comment)
admin.site.register(Rating)