
from modelViewer.models import Model3D
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    num_models = Model3D.objects.all().count()
    context = {
        'num_models': num_models,
    }
    return render(request, 'index.html', context=context)

