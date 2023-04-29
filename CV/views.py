from django.shortcuts import render
from .models import curriculum
from .forms import CurriculumForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def mi_cv(request):
    curriculums = curriculum.objects.all()
    return render(request, 'CV/mi_cv.html', {'curriculums': curriculums})

def mi_cv_v2(request):
    curriculums = curriculum.objects.all()
    return render(request, 'CV/mi_cv_v2.html', {'curriculums': curriculums})

def cv_create(request):
    # si el pedido es POST tenemos que procesar la data del formulario
    if request.method == "POST":
        # Tenemos que instanciar el formulario con la informacion que nos envio el usuario
        form = CurriculumForm(request.POST)
        print(request.POST)
        # Preguntamos si el formulario es valido
        if form.is_valid():
            # Guardamos el nuevo CV
            form.save()
            # Redirecionamos a gracias
            return HttpResponseRedirect('/thanks/')
    else:
        # Formulario vacio
        form = CurriculumForm()
    return render(request, 'CV/cv_create.html', {"form": form})

def cv_update(request,pk):
    curriculums = curriculum.objects.get(pk=pk)
    form = CurriculumForm(instance=curriculums)
    if request.method == "POST":
        form = CurriculumForm(request.POST, instance=curriculums)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mi_cv_v2'))
    return render(request, 'CV/cv_create.html', {"form": form})


def thanks(request):
    return render(request, 'CV/thanks.html')
