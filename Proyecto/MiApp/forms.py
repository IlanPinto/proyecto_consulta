from django import forms

class CrearJugadorForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    nacionalidad = forms.CharField(max_length=40)

class CrearEntrenadorForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    entrenado = forms.CharField(max_length=40)
    email = forms.EmailField()

class CrearTorneosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)
    puntos_otorgados = forms.IntegerField()


