# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings


class Aluno(models.Model):
    idaluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    idcidade = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='idcidade')

    class Meta:
        managed = False
        db_table = 'aluno'


class CategoriaCurso(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nome = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'categoria_curso'


class Cidade(models.Model):
    idcidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    estado = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'cidade'

    def __str__(self):
        return self.nome    


class Curso(models.Model):
    idcurso = models.AutoField(primary_key=True)
    nome = models.CharField(unique=True, max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    carga_horaria = models.IntegerField()
    idcategoria = models.ForeignKey(CategoriaCurso, models.DO_NOTHING, db_column='idcategoria')
    idinstrutor = models.ForeignKey('Instrutor', models.DO_NOTHING, db_column='idinstrutor')

    class Meta:
        managed = False
        db_table = 'curso'


class Instrutor(models.Model):
    idinstrutor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'instrutor'


class Matricula(models.Model):
    idmatricula = models.AutoField(primary_key=True)
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idaluno')
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='idcurso')
    data_matricula = models.DateField()
    status = models.CharField(max_length=20)
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matricula'


class PerfilAluno(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    aluno = models.OneToOneField(
        Aluno,
        on_delete=models.PROTECT
    )

    class Meta:
        db_table = 'cursos_perfilaluno'

    def __str__(self):
        return self.aluno.nome 