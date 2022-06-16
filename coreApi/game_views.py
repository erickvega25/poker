from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from corePoker.models import Game
from corePoker.serializers import GameSerializer
from corePoker.services.PlayServices import PlayService

def game(request,gameId):
    if request.method !="GET":
        return HttpResponseForbidden()
    try:
        game = Game.objects.get(pk=gameId)
    except Game.DoesNotExist:
        return HttpResponse(status=404)
    serializer = GameSerializer(game)
    return JsonResponse(serializer.data,safe=False)

def comprobarGanador(request,gameId):
    if request.method !="PUT":
        return HttpResponseForbidden()
    try:
        game = Game.objects.get(pk=gameId)
    except Game.DoesNotExist:
        return HttpResponse(status=404)
    PlayService.calculateWinner(game)
    game.fase = Game.FINALIZADA
    game.save()
    serializer = GameSerializer(game)
    return JsonResponse(serializer.data, safe=False)