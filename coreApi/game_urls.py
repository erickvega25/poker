from django.urls import path
from coreApi import game_views

urlpatterns = [
    path('game/<int:gameId>/',game_views.game),  
    path('comprobarGanador/<int:gameId>/',game_views.comprobarGanador)
]