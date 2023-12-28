from django.urls import path
from django.contrib.auth.views import PasswordChangeView
from .views import user_detail,user_list,clear_profile_fields,index,profile,signin,signout,signup,upload_3d_model,delete_model,edit_3d_model,model,model_list,rate,change_password,edit_profile

urlpatterns = [
    path("", index, name="index"),
    path('profile/', profile, name='profile'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
    path('upload_3d_model/', upload_3d_model, name='upload_3d_model'),
    path('delete_model/<int:model_id>/', delete_model, name='delete_model'),
    path('edit_3d_model/<int:model_id>/', edit_3d_model, name='edit_3d_model'),
    path('model/<int:model_id>/', model, name='model'),
    path('model_list/', model_list, name='model_list'),
    path('model_list/rate/<int:model_id>/<int:rating>/', rate, name='rate'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('edit_profile/change_password/', change_password, name='change_password'),
    path('clear_profile_fields/', clear_profile_fields, name='clear_profile_fields'),
    path('user_list/', user_list, name='user_list'),
    path('user_detail/<str:username>/', user_detail, name='user_detail'),
]