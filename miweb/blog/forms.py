from django import forms


class AutorFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    email = forms.EmailField()


class PostFormulario(forms.Form):

    titulo = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)


class ComentarioFormulario(forms.Form):

    texto = forms.CharField(widget=forms.Textarea)
    fecha = forms.DateField()


class BuscarPost(forms.Form):

    titulo = forms.CharField(max_length=100)
