from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ThreeDModel)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(UserProfile)
