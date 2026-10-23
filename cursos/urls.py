from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  
    path('curso/<int:pk>/', views.detalhes_curso, name='detalhes_curso'),   
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='cursos/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('minhas_matriculas/', views.minhas_matriculas, name='minhas_matriculas'),             
]