from django.shortcuts import render
from .models import Curso


def home(request):
    categoria = request.GET.get("categoria")
    if categoria:
        cursos = Curso.objects.filter(idcategoria__nome=categoria)
    else:
        cursos = Curso.objects.all()
    context = {"cursos": cursos, "categoria": categoria}
    return render(request, 'cursos/home.html', context)

def detalhes_curso(request, pk):
    curso = Curso.objects.get(idcurso=pk)
    context = {"curso": curso}
    return render(request, 'cursos/detalhes_curso.html', context)