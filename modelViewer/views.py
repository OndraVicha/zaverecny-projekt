from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.urls import reverse

from .forms import ThreeDModelForm,StyledAuthenticationForm,ChangePasswordForm,UserProfileForm
from .models import ThreeDModel,Category,Rating
from django.contrib import messages
from django.db.models import Q
from django.db.models import Avg
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages

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
    categories = Category.objects.all()

    # Získání hodnot z formuláře
    category_id = request.GET.get('category')
    upload_date = request.GET.get('upload_date')
    model_name = request.GET.get('model_name')
    sort_by = request.GET.get('sort_by')
    # Filtrujeme podle kategorie
    if category_id:
        user_uploaded_models = user_uploaded_models.filter(categories__id=category_id)
    # Filtrujeme podle data uploadu
    if upload_date:
        user_uploaded_models = user_uploaded_models.filter(upload_date=upload_date)
    # Filtrujeme podle jména modelu (necitlivě na diakritiku)
    if model_name:
        user_uploaded_models = user_uploaded_models.filter(Q(title__icontains=model_name))
    # Třídíme podle nejnovějších nebo nejstarších
    if sort_by == 'newest':
        user_uploaded_models = user_uploaded_models.order_by('-upload_date')
    elif sort_by == 'oldest':
        user_uploaded_models = user_uploaded_models.order_by('upload_date')
    return render(request, 'user/profile.html', {'user_uploaded_models': user_uploaded_models,'categories': categories})

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
            form.save_m2m()
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

def model(request, model_id):
    model = get_object_or_404(ThreeDModel, pk=model_id)
    context = {
        'model': model,
    }
    return render(request, 'models/view_3dmodel.html', context)

def model_list(request):
    models = ThreeDModel.objects.all()
    categories = Category.objects.all()

    # Získání hodnot z formuláře
    category_id = request.GET.get('category')
    upload_date = request.GET.get('upload_date')
    model_name = request.GET.get('model_name')
    sort_by = request.GET.get('sort_by')

    # Filtrujeme podle kategorie
    if category_id:
        models = models.filter(categories__id=category_id)

    # Filtrujeme podle data uploadu
    if upload_date:
        models = models.filter(upload_date=upload_date)

    # Filtrujeme podle jména modelu (necitlivě na diakritiku)
    if model_name:
        models = models.filter(Q(title__icontains=model_name))

    # Třídíme podle nejnovějších nebo nejstarších
    if sort_by == 'newest':
        models = models.order_by('-upload_date')
    elif sort_by == 'oldest':
        models = models.order_by('upload_date')

    for model in models:
        rating = Rating.objects.filter(model=model).first()
        model.user_rating = rating.rating if rating else 0

    return render(request, 'models/search_model.html', {'models': models, 'categories': categories})

def rate(request: HttpRequest, model_id: int, rating: int) -> HttpResponse:
    model = get_object_or_404(ThreeDModel, id=model_id)
    if request.user == model.user:
        return JsonResponse({'error': 'You cannot rate your own model.'}, status=400)
    Rating.objects.filter(model=model, user=request.user).delete()
    model.rating_set.create(user=request.user, rating=rating)
    return model_list(request)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Aktualizuje hash v session, aby uživatel nebyl odhlášen
            messages.success(request, 'Heslo bylo úspěšně změněno.')
            return redirect('/modelViewer/profile')  # Přesměrování na profilovou stránku
        else:
            messages.error(request, 'Omlouváme se, došlo k chybě při změně hesla. Zkontrolujte formulář.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'user/change_password.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil byl úspěšně aktualizován.')
            return redirect('/modelViewer/profile')  # Přesměrování na profilovou stránku
        else:
            messages.error(request, 'Omlouváme se, došlo k chybě při aktualizaci profilu. Zkontrolujte formulář.')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'user/edit_profile.html', {'form': form})