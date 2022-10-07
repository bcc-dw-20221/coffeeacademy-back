from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static
from cursos.api.viewsets import NotaViewSet, CursoViewSet,  DisciplinaViewSet, FrequenciaViewSet
from cursos import views

router = routers.DefaultRouter()
router.register(r'notas/main', NotaViewSet)
router.register(r'cursos/main', CursoViewSet)
router.register(r'disciplinas/main', DisciplinaViewSet)
router.register(r'frequencias/main', FrequenciaViewSet)

urlpatterns = [
    path('cursos/', views.get_cursos, name="get_cursos"),
    path('cursos/get/<curso_id>/', views.get_curso, name="get_curso"),
    path('cursos/add/', views.post_curso, name="post_curso"),
    path('cursos/del/<curso_id>/', views.delete_curso, name="delete_curso"),

    path('notas/', views.get_notas, name="get_notas"),
    path('notas/get/<nota_id>/', views.get_nota, name="get_nota"),
    path('notas/add/', views.post_nota, name="post_nota"),
    path('notas/del/<nota_id>/', views.delete_nota, name="delete_nota"),

    path('disciplinas/', views.get_disciplinas, name="get_disciplinas"),
    path('disciplinas/get/<disciplina_id>/', views.get_disciplina, name="get_disciplina"),
    path('disciplinas/add', views.post_disciplina, name="post_disciplina"),
    path('disciplinas/del/<disciplina_id>/', views.delete_disciplina, name="delete_disciplina"),

    path('frequencias/', views.get_frequencias, name="get_frequencias"),
    path('frequencias/get/<frequencia_id>/', views.get_frequencia, name="get_frequencia"),
    path('frequencias/add/', views.post_frequencia, name="post_frequencia"),
    path('frequencias/del/<frequencia_id>/', views.delete_frequencia, name="delete_frequencia"),

    path('', include(router.urls)),
]
