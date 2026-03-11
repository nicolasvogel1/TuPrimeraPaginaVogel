from .models import Post
from django.shortcuts import render
from .forms import AutorFormulario, PostFormulario
from .models import Autor, Post


def inicio(request):
    return render(request, "blog/inicio.html")


def crear_autor(request):

    if request.method == "POST":

        form = AutorFormulario(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            autor = Autor(
                nombre=data["nombre"],
                apellido=data["apellido"],
                email=data["email"]
            )

            autor.save()

            return render(request, "blog/inicio.html")

    else:

        form = AutorFormulario()

    return render(request, "blog/form_autor.html", {"form": form})


def crear_post(request):

    if request.method == "POST":

        form = PostFormulario(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            post = Post(
                titulo=data["titulo"],
                contenido=data["contenido"]
            )

            post.save()

            return render(request, "blog/inicio.html")

    else:

        form = PostFormulario()

    return render(request, "blog/form_post.html", {"form": form})


def buscar_post(request):

    if request.GET.get("titulo"):

        titulo = request.GET.get("titulo")

        posts = Post.objects.filter(titulo__icontains=titulo)

        return render(request, "blog/resultados_busqueda.html", {"posts": posts})

    return render(request, "blog/buscar_post.html")
