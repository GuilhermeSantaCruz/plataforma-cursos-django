from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cidade


class CadastroUsuarioForm(UserCreationForm):
    nome = forms.CharField(
        label="Nome completo",
        max_length=100
    )

    cidade = forms.ModelChoiceField(
        queryset=Cidade.objects.all().order_by("nome"),
        label="Cidade"
    )

    class Meta:
        model = User
        fields = ["username", "email"]
        labels = {
            "username": "Nome de usuário",
            "email": "E-mail",
        }

    def clean_email(self):
        email = self.cleaned_data["email"]

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Já existe uma conta cadastrada com este e-mail."
            )

        return email