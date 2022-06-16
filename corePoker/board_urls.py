from django.http.response import BadHeaderError
from django.urls import path
from corePoker import board_views

app_name = "board"

urlpatterns = [
    path('', board_views.board, name='board'),
    path("game/<int:gameId>/",board_views.game,name="game"),
    path("cambios/<int:gameId>/",board_views.cambios,name="cambios"),
    path("play/<int:gameId>/",board_views.play, name="play"),
    path("simular_partida/",board_views.simulateGame),
    path("getPlayers/<int:gameId>/",board_views.getPlayers),
    path("putCambioCartas/",board_views.putCambioCartas)
]