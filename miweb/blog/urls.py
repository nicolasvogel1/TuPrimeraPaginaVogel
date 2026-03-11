from django.urls import path
from .views import inicio, crear_autor, crear_post, buscar_post

urlpatterns = [
    path('', inicio, name="inicio"),
    path('autor/', crear_autor, name="crear_autor"),
    path('post/', crear_post, name="crear_post"),
    path('buscar/', buscar_post, name="buscar_post"),
]
