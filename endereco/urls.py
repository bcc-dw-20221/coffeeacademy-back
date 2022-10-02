"""academico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from unicodedata import name
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static
from endereco.api.viewsets import EnderecoViewSet 
from endereco import views

router = routers.DefaultRouter()
router.register(r'endereco', EnderecoViewSet)

urlpatterns = [
    path('endereco2/', views.get_enderecos, name="get_enderecos"),
    path('add/', views.post_endereco, name="post_endereco"),
    path("get/<endereco_id>/", views.get_endereco_id, name="get_endereco_id"),
    path("remove/<endereco_id>/", views.delete_endereco, name="delete_endereco"),
    path('', include(router.urls)),
    # path('admin/', admin.site.urls),
]
