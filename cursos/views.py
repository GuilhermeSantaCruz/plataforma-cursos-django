from django.shortcuts import render
from .models import Curso


def home(request):
    cursos = Curso.objects.all()
    context = {"cursos": cursos}
    return render(request, 'cursos/home.html', context)

def detalhes_curso(request, pk):
    curso = Curso.objects.get(idcurso=pk)
    context = {"curso": curso}
    return render(request, 'cursos/detalhes_curso.html', context)