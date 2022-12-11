from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static
from gestao import views
from gestao.api.viewsets import GestorViewSet, ProfessorViewSet, CoordenadorViewSet, GestorSerializer

router = routers.DefaultRouter()
router.register(r'professor/main', ProfessorViewSet)
router.register(r'coordenador/main', CoordenadorViewSet)
router.register(r'gestor/main', GestorViewSet)


urlpatterns = [
    path('professor/', views.get_professor, name="get_professor"),
    path('professor/add/', views.post_professor, name="post_professor"),
    path("professor/get/<professor_id>/", views.get_professor_id, name="get_professor"),
    path("professor/remove/<professor_id>/", views.delete_professor, name="delete_professor"),
    path("professor/login/", views.login_professor, name="login_professor"),
    path("professor/logout/", views.logout_professor, name="logout_professor"),
    path("professor/test/", views.test_professor, name="test_professor"),

    path('coordenador/', views.get_coordenador, name="get_coordenador"),
    path('coordenador/add/', views.post_coordenador, name="post_coordenador"),
    path("coordenador/get/<coordenador_id>/", views.get_coordenador_id, name="get_coordenador"),
    path("coordenador/remove/<coordenador_id>/", views.delete_coordenador, name="delete_coordenador"),
    path("coordenador/login/", views.login_coordenador, name="login_coordenador"),
    path("coordenador/logout/", views.logout_coordenador, name="logout_coordenador"),
    path("coordenador/test/", views.test_coordenador, name="test_coordenador"),

    path('gestor/', views.get_gestor, name="get_gestor"),
    path('gestor/add/', views.post_gestor, name="post_gestor"),
    path("gestor/get/<gestor_id>/", views.get_gestor_id, name="get_gestor"),
    path("gestor/remove/<gestor_id>/", views.delete_gestor, name="delete_gestor"),
    path("gestor/login/", views.login_gestor, name="login_gestor"),
    path("gestor/logout/", views.logout_gestor, name="logout_gestor"),
    path("gestor/test/", views.test_gestor, name="test_gestor"),

    path('', include(router.urls)),
]