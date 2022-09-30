from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static
from estudante import views
from estudante.api.viewsets import AlunosViewSet, MatriculaViewSet,  PaisViewSet, EgressoViewSet

router = routers.DefaultRouter()
router.register(r'alunos', AlunosViewSet)
router.register(r'matricula', MatriculaViewSet)
router.register(r'pais', PaisViewSet)
router.register(r'egresso', EgressoViewSet)

urlpatterns = [
    path('', views.get_alunos, name="get_alunos"),
    path('add/', views.post_alunos, name="post_alunos"),
    path("get/<matricula>/", views.get_alunos_matricula, name="get_alunos_matricula"),
    path(
        "remove/<matricula>/", views.delete_aluno, name="delete_aluno"
    ),
    path('', include(router.urls)),
    #path('admin/', admin.site.urls),
]
