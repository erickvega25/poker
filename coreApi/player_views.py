import json
from corePoker.models import Game,Player
from corePoker.serializers import PlayerSerializer
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from corePoker.services.DeckService import DeckService
from corePoker.services.GameService import GameService




def players(request,gameId):
    if request.method == "GET":
        players = Player.objects.filter(game__id=gameId)
        serializer = PlayerSerializer(players,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == "POST":
        return HttpResponseForbidden()


def player(request,playerId):
    try:
        player = Player.objects.get(pk=playerId)
    except Player.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "GET":
        serializer = PlayerSerializer(player)
        return JsonResponse(serializer.data,safe=False)
    if request.method == "PUT":
        print("hola")
    if request.method == "DELETE":
        if request.user.username == "admin":
            player.delete()
        else: 
            return HttpResponseForbidden()

def changeCards(request,playerId):
    if request.method != "PUT":
        return HttpResponseForbidden()
    try:
        player = Player.objects.get(pk=playerId)
    except Player.DoesNotExist:
        return HttpResponse(status=404)
    if not player.user:
        return HttpResponseForbidden()
    if player.haCambiado:
        return JsonResponse({"status":"KO","message":"Este jugador ya ha cambiado"})
    content = json.loads(request.body)
    cardsToChangeIds = content["markedCards"]
    DeckService.changeCards(player, cardsToChangeIds)
    game = player.game
    playerBoots = Player.objects.filter(game=game, user=None)
    for player in playerBoots:
        DeckService.changeCardsToIA(player)
    GameService.setGameComprobado(player.game)
    serializer = PlayerSerializer(player)
    return JsonResponse(serializer.data,safe=False)