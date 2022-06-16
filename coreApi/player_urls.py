from django.http.response import BadHeaderError
from django.urls import path
from coreApi import player_views


urlpatterns = [
    path('player/change_cards/<int:playerId>/',player_views.changeCards),
    path('players/<int:gameId>/', player_views.players),
    path('player/<int:playerId>/',player_views.player),
    
]