from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static
from estudante import views
from estudante.api.viewsets import AlunosViewSet, MatriculaViewSet,  PaisViewSet, EgressoViewSet

router = routers.DefaultRouter()
router.register(r'alunos/main', AlunosViewSet)
router.register(r'matricula/main', MatriculaViewSet)
router.register(r'pais/main', PaisViewSet)
router.register(r'egresso/main', EgressoViewSet)

urlpatterns = [

    ### PATH ESTUDANTES ### 
    path('alunos/', views.get_alunos, name="get_alunos"),
    path("alunos/get/<matricula>/", views.get_alunos_matricula, name="get_alunos_matricula"),
    path('alunos/add/', views.post_alunos, name="post_alunos"),
    path("alunos/remove/<matricula>/", views.delete_aluno, name="delete_aluno"),
    path("alunos/login/", views.login_alunos, name="login_alunos"),
    path("alunos/logout/", views.logout_alunos, name="logout_alunos"),
    path("alunos/test/", views.test_alunos, name="test_alunos"),

    ### PATH MATRICULA ###
    path('matricula/', views.get_matricula, name="get_matricula"),
    path("matricula/get/<id_matricula>/", views.get_matricula_id, name="get_matricula_id"),
    path('matricula/add/', views.post_matricula, name="post_matricula"),
    path("matricula/remove/<id_matricula>/", views.delete_matricula, name="delete_matricula"),

    ### PATH PAIS ###
    path('pais/', views.get_pais, name="get_pais"),
    path("pais/get/<pais_id>/", views.get_pais_id, name="get_pais_id"),
    path('pais/add/', views.post_pais, name="post_pais"),
    path("pais/remove/<pais_id>/", views.delete_pais, name="delete_pais"),
    path("pais/login/", views.login_pais, name="login_pais"),
    path("pais/logout/", views.logout_pais, name="logout_pais"),
    path("pais/test/", views.test_pais, name="test_pais"),

    ### PATH EGRESSO ###
    path('egresso/', views.get_egresso, name="get_egresso"),
    path("egresso/get/<id_matricula_egresso>/", views.get_egresso_id, name="id_matricula_egresso"),
    path('egresso/add/', views.post_egresso, name="post_egresso"),
    path("egresso/remove/<id_matricula_egresso>/", views.delete_egresso, name="id_matricula_egresso"),
    path("egresso/login/", views.login_egresso, name="login_egresso"),
    path("egresso/logout/", views.logout_egresso, name="logout_egresso"),
    path("egresso/test/", views.test_egresso, name="test_egresso"),

    path('', include(router.urls)),
]
