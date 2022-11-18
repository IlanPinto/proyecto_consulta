from django.urls import path
from MiApp import views
urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('jugadores/', views.mostrar_jugadores, name='jugadores'),
    path('entrenadores/', views.mostrar_entrenadores, name='entrenadores'),
    path('torneos/', views.mostrar_torneos, name='torneos'),
    path('pagina_jugadores/', views.mostrar_jugadores_pagina, name='Jugadores'),
    path('crear_jugadores/', views.formulario_jugadores, name='FormularioJugadores'),
    path('crear_entrenadores/', views.formulario_entrenadores, name='FormularioEntrenadores'),
    path('crear_torneos/', views.formulario_torneos, name='FormularioTorneos'),
    path('buscar_jugador/', views.buscar_jugador, name='BuscarJugador'),
    path('mostrar_jugadores/', views.mostrar_jugadores_todos, name='MostrarJugadores'),
    path('eliminar_jugadores/<apellido>', views.eliminar_jugador, name='EliminarJugadores'),
    path('actualizar_jugadores/<jugador_id>', views.actualizar_jugadores, name='ActualizarJugadores'),
    path('jugadores_list/', views.JugadoresList.as_view(), name='List'),
    path('jugadores_detail/<pk>', views.JugadoresDetailView.as_view(), name='Detail'),
    path('jugadores_confirm_delete/<pk>', views.JugadoresDeleteView.as_view(), name='Delete'),
    path('jugadores_edit/<pk>', views.JugadoresUpdateView.as_view(), name='Update'),
    path('jugadores_create/', views.JugadoresCreateView.as_view(), name='Create'),
]
