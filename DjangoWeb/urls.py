
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('models/', views.ModelList.as_view(), name='model-list'),
    path('models/<int:pk>/', views.ModelDetail.as_view(), name='model-detail'),
    path('comments/', views.CommentList.as_view(), name='comment-list'),
    path('ratings/', views.RatingList.as_view(), name='rating-list'),
]
