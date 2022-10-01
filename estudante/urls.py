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

    ### PATH ESTUDANTES ### 
    path('alunos2/', views.get_alunos, name="get_alunos"),
    path('alunos/add/', views.post_alunos, name="post_alunos"),
    path("alunos/get/<matricula>/", views.get_alunos_matricula, name="get_alunos_matricula"),
    path(
        "alunos/remove/<matricula>/", views.delete_aluno, name="delete_aluno"
    ),

    ### PATH MATRICULA ###
    path('matricula2/', views.get_matricula, name="get_matricula"),
    path('matricula/add/', views.post_matricula, name="post_matricula"),
    path("matricula/get/<id_matricula>/", views.get_matricula_id, name="get_matricula_id"),
    path(
        "matricula/remove/<id_matricula>/", views.delete_matricula, name="delete_matricula"
    ),

    ### PATH PAIS ###
    path('pais2/', views.get_pais, name="get_pais"),
    path('pais/add/', views.post_pais, name="post_pais"),
    path("pais/get/<pais_id>/", views.get_pais_id, name="get_pais_id"),
    path(
        "pais/remove/<pais_id>/", views.delete_pais, name="delete_pais"
    ),

    ### PATH EGRESSO ###
    path('egresso2/', views.get_egresso, name="get_egresso"),
    path('egresso/add/', views.post_egresso, name="post_egresso"),
    path("egresso/get/<id_matricula_egresso>/", views.get_egresso_id, name="id_matricula_egresso"),
    path(
        "egresso/remove/<id_matricula_egresso>/", views.delete_egresso, name="id_matricula_egresso"
    ),

    path('', include(router.urls)),
    #path('admin/', admin.site.urls),
]
