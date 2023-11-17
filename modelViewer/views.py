from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import ThreeDModelForm,StyledAuthenticationForm
from .models import ThreeDModel,Category
from django.contrib import messages
from django.db import models

def index(request):
	return render(request, 'index.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'user/signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'user/profile.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/modelViewer/profile')  # profile
        else:
            msg = 'Error Login'
            form = StyledAuthenticationForm(request.POST)
            return render(request, 'user/login.html', {'form': form, 'msg': msg})
    else:
        form = StyledAuthenticationForm()
        return render(request, 'user/login.html', {'form': form})

def user_uploaded_models(request):
    # Získání všech modelů ThreeDModel pro aktuálně přihlášeného uživatele
    user_uploaded_models = ThreeDModel.objects.filter(user=request.user)

    return render(request, 'user/user.html', {'user_uploaded_models': user_uploaded_models})

def profile(request):

    user_uploaded_models = ThreeDModel.objects.filter(user=request.user)
    return render(request, 'user/profile.html', {'user_uploaded_models': user_uploaded_models})

def signout(request):
    logout(request)
    return redirect('/')

def upload_3d_model(request):
    if request.method == 'POST':
        form = ThreeDModelForm(request.POST, request.FILES)
        if form.is_valid():
            three_d_model = form.save(commit=False)
            three_d_model.user = request.user
            three_d_model.save()
            messages.success(request, '3D model uploaded successfully.')
            return redirect('/modelViewer/profile')  # Přesměrování na domovskou stránku nebo kamkoliv jinam
        else:
            messages.error(request, 'Error uploading the 3D model. Please check the form.')
    else:
        form = ThreeDModelForm()

    return render(request, 'models/upload_3d_model.html', {'form': form})

def delete_model(request, model_id):
    model = get_object_or_404(ThreeDModel, id=model_id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Model deleted successfully.')
        return redirect('/modelViewer/profile')  # Redirect to the profile view

    return render(request, 'models/delete_model_confirm.html', {'model': model})

def edit_3d_model(request, model_id):
    instance = get_object_or_404(ThreeDModel, id=model_id)

    if request.method == 'POST':
        form = ThreeDModelForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            # Upraveno úspěšně, můžete přidat zprávu nebo přesměrování
            return redirect('/modelViewer/profile', model_id=model_id)
    else:
        form = ThreeDModelForm(instance=instance)

    return render(request, 'models/edit_3d_model.html', {'form': form, 'instance': instance})
