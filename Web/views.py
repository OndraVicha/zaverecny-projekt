from django.shortcuts import render
from django.http import JsonResponse
from .models import Model3D
from .forms import ModelUploadForm

def upload_3d_model(request):
    if request.method == 'POST':
        form = ModelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Uložte metadata o modelu do databáze
            model = form.save(commit=False)
            model.user = request.user  # Přiřaďte aktuálního uživatele jako vlastníka modelu
            model.save()
            return JsonResponse({'success': True})
    else:
        form = ModelUploadForm()
    return render(request, 'upload_3d_model.html', {'form': form})