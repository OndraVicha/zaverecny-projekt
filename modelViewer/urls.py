from django.urls import path
from . import views
from .views import upload_3d_model,user_uploaded_models

urlpatterns = [
    path("", views.index, name="index"),
    path('profile/', views.profile, name='profile'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('upload_3d_model/', views.upload_3d_model, name='upload_3d_model'),
    path('delete_model/<int:model_id>/', views.delete_model, name='delete_model'),
    path('edit_3d_model/<int:model_id>/', views.edit_3d_model, name='edit_3d_model'),
    path('model/<int:model_id>/', views.model, name='model'),
    path('model_list/', views.model_list, name='model_list'),
    path('rate_model/<int:model_id>/<int:rating>/', views.rate_model, name='rate_model'),
]