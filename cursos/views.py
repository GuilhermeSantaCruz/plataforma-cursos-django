from django.shortcuts import render
from .models import Curso


def home(request):
    cursos = Curso.objects.all()
    context = {"cursos": cursos}
    return render(request, 'cursos/home.html', context)