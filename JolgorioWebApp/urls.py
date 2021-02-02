"""JolgorioWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from JolgorioWebApp import views

urlpatterns = [
    path('api/actividades/', views.listar_actividades),
    path('api/actividades/completada', views.actividad_completada),
    path('api/actividades/<int:id>/', views.listar_actividades_completadas),
    path('api/materiales/<int:id>', views.listar_materiales),
    path('api/actividades/<int:id>/mesactual/', views.listar_actividades_ultimo_mes),
    path('api/usuario/id/<int:id>/', views.usuario_por_id),
    path('api/usuario/numero/<str:numero>/', views.usuario_por_telefono),
    path('api/usuario/correo/<str:correo>/', views.usuario_por_correo),
    path('api/logros/<int:tipo>/', views.listar_logros),
]
