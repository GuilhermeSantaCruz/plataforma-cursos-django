from django.shortcuts import render, redirect
from .models import Curso, Aluno, PerfilAluno, Matricula
from .forms import CadastroUsuarioForm
from django.contrib.auth import login
from django.db import transaction
from django.contrib.auth.decorators import login_required
from datetime import date
from django.views.decorators.http import require_POST


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



def cadastro(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]

            if Aluno.objects.filter(email=email).exists():
                form.add_error(
                    "email",
                    "Já existe um aluno cadastrado com este e-mail."
                )
            else:
                with transaction.atomic():
                    usuario = form.save(commit=False)
                    usuario.first_name = form.cleaned_data["nome"]
                    usuario.save()

                    aluno = Aluno.objects.create(
                        nome=form.cleaned_data["nome"],
                        email=email,
                        idcidade=form.cleaned_data["cidade"],
                    )

                    PerfilAluno.objects.create(
                        usuario=usuario,
                        aluno=aluno,
                    )

                login(request, usuario)
                return redirect("home")
    else:
        form = CadastroUsuarioForm()

    context = {"form": form}
    return render(request, "cursos/cadastro.html", context)


@login_required
def minhas_matriculas(request):
    perfil = PerfilAluno.objects.get(usuario=request.user)
    matriculas = Matricula.objects.filter(idaluno=perfil.aluno).select_related('idcurso')
    context = {"matriculas": matriculas}

    return render(request, 'cursos/minhas_matriculas.html', context)   


@login_required
@require_POST
def matricular_curso(request, pk):
    curso = Curso.objects.get(idcurso=pk)
    perfil = PerfilAluno.objects.get(usuario=request.user)
    matricula_existente = Matricula.objects.filter(
        idaluno=perfil.aluno,
        idcurso=curso
    ).exists()
    if matricula_existente:
        return redirect("minhas_matriculas")
    Matricula.objects.create(
        idaluno=perfil.aluno,
        idcurso=curso,
        data_matricula=date.today(),
        status="Cursando"
    )
    return redirect("minhas_matriculas")