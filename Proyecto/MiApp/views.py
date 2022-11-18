from django.shortcuts import render
from MiApp.models import Jugadores, Torneos, Entrenadores
from .forms import CrearJugadorForm, CrearEntrenadorForm, CrearTorneosForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def inicio(request):
    return render(request, 'MiApp/index2.html')

def mostrar_jugadores(request):
    j1 = Jugadores(nombre="Rafael",apellido="Gonzalez", edad = 36, nacionalidad = "Espania" )
    j2 = Jugadores(nombre="Miguel",apellido="Juarez", edad = 40, nacionalidad = "Argentina" )
    j1.save()
    j2.save()
    return render (request, 'MiApp/jugadores.html' , {'jugadores': [j1 , j2]})


def mostrar_torneos(request):
    t1 = Torneos(nombre="French Open", pais="Francia", puntos_otorgados = 2000)
    t1.save()
    t2 = Torneos(nombre="US Open", pais="USA", puntos_otorgados = 1500)
    t2.save()
    return render (request, 'MiApp/torneos.html' , {'torneos': [t1, t2]})


def mostrar_entrenadores(request):
    e1 = Entrenadores(nombre="Carlos",apellido="Alberdi", entrenado = "Rafeal Gonzalez", email = "cmoya@hotmail.com" )
    e2 = Entrenadores(nombre="Juan",apellido="Garcia", entrenado = "Ramiro Alvarez", email = "jg@hotmail.com" )
    e1.save()
    e2.save()
    return render (request, 'MiApp/entrenadores.html' , {'entrenadores': [e1, e2]})

def mostrar_jugadores_pagina(request):
    return render(request, 'MiApp/jugadores.html')

def formulario_jugadores(request):
    if request.method == 'POST':
        formulario = CrearJugadorForm(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            jugador = Jugadores(nombre = formulario_limpio["nombre"], apellido = formulario_limpio["apellido"], edad = formulario_limpio["edad"], nacionalidad = formulario_limpio["nacionalidad"])
            jugador.save()
            return render(request, 'MiApp/index2.html')
    else:
        formulario = CrearJugadorForm()

    return render(request, 'MiApp/crear_jugador.html', {'formulario': formulario})

def formulario_entrenadores(request):
    if request.method == 'POST':
        formulario = CrearEntrenadorForm(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            entrenador = Entrenadores(nombre = formulario_limpio["nombre"], apellido = formulario_limpio["apellido"], entrenado = formulario_limpio["entrenado"], email = formulario_limpio["email"])
            entrenador.save()
            return render(request, 'MiApp/index2.html')
    else:
        formulario = CrearEntrenadorForm()

    return render(request, 'MiApp/crear_entrenador.html', {'formulario': formulario})

def formulario_torneos(request):
    if request.method == 'POST':
        formulario = CrearTorneosForm(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            torneo = Torneos(nombre = formulario_limpio["nombre"], pais = formulario_limpio["pais"], puntos_otorgados = formulario_limpio["puntos_otorgados"])
            torneo.save()
            return render(request, 'MiApp/index2.html')
    else:
        formulario = CrearTorneosForm()

    return render(request, 'MiApp/crear_torneo.html', {'formulario': formulario})

def buscar_jugador(request):
    
    if request.GET.get('apellido', False):
        apellido = request.GET["apellido"]
        jugador = Jugadores.objects.filter(apellido__icontains=apellido)
        return render(request, 'MiApp/buscar_jugador.html', {'jugadores': jugador})

    else:
        respuesta = "No hay datos"
    return render(request, 'MiApp/buscar_jugador.html', {'respuesta': respuesta})

def mostrar_jugadores_todos(request):
    jugadores = Jugadores.objects.all()
    context = {'jugadores': jugadores}
    return render(request,'MiApp/mostrar_jugadores.html', context=context)

def eliminar_jugador(request, apellido):
    jugadores = Jugadores.objects.get(apellido=apellido)
    jugadores.delete()
    jugadores = Jugadores.objects.all()
    context = {'jugadores': jugadores}
    return render(request,'MiApp/mostrar_jugadores.html', context=context)


def actualizar_jugadores(request, jugador_id):
    jugador = Jugadores.objects.get(id=jugador_id)
    
    if request.method == 'POST':
        formulario = CrearJugadorForm(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            jugador.nombre = formulario_limpio['nombre']
            jugador.apellido = formulario_limpio['apellido']
            jugador.edad = formulario_limpio['edad']
            jugador.nacionalidad = formulario_limpio['nacionalidad']
            jugador.save()
            return render(request, 'MiApp/index2.html')
    else:
        formulario = CrearJugadorForm(initial={'nombre':jugador.nombre,'apellido':jugador.apellido,'edad':jugador.edad,'nacionalidad':jugador.nacionalidad})

    return render(request, 'MiApp/modificar_jugador.html', {'formulario': formulario})

class JugadoresList(ListView):

    model = Jugadores
    template_name = 'MiApp/MiApp/jugadores_list.html'


class JugadoresDetailView(DetailView):

    model = Jugadores
    template_name = 'MiApp/MiApp/jugadores_detalle.html'

class JugadoresDeleteView(DeleteView):
    model = Jugadores
    success_url = '/MiApp/jugadores_list'

class JugadoresUpdateView(UpdateView):
    model = Jugadores
    success_url = '/MiApp/jugadores_list'
    fields = ['nombre' , 'apellido']

class JugadoresCreateView(CreateView):
    model = Jugadores
    success_url = '/MiApp/jugadores_list'
    fields = ['nombre' , 'apellido', 'edad', 'nacionalidad']