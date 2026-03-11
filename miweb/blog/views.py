from django.shortcuts import render
from .forms import AutorFormulario
from .models import Autor


def inicio(request):

    return render(request, "blog/inicio.html")


def crear_autor(request):

    if request.method == "POST":

        form = AutorFormulario(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            autor = Autor(
                nombre=data["nombre"],
                email=data["email"]
            )

            autor.save()

            return render(request, "blog/inicio.html")

    else:

        form = AutorFormulario()

    return render(request, "blog/form_autor.html", {"form": form})
