import json
from random import randrange
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from corePoker.models import Card, Deck,Game, Player
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from corePoker.serializers import PlayerSerializer
from corePoker.services.DeckService import DeckService
from corePoker.services.PlayerServices import PlayerService
from corePoker.services.PlayServices import PlayService
from corePoker.services.GameService import GameService

@login_required
def board(request):
    game = Game(name="Partida")
    game.save()
    deck = Deck(game=game)
    deck.save()
    DeckService.createCards(deck) 
    DeckService.shuffleDeck(deck)
    PlayerService.createPlayers(game,request.user)
    game.fase = Game.REPARTO    
    game.save()
    DeckService.distributeCards(game)
    game.fase = Game.CAMBIO
    game.save()
    return redirect("/board/game/"+str(game.id)+"/")

@login_required
def game(request,gameId):
    game = Game.objects.get(pk=gameId)
    return render(request,"base.html",{"game":game})

@csrf_exempt
def getPlayers(request,gameId):
    players = Player.objects.filter(game__id=gameId)
    serializer = PlayerSerializer(players,many=True)
    return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def putCambioCartas(request):
    if request.method != "PUT":
        return HttpResponseForbidden()
    else:
        content = json.dump(request.body)
        print(content)
        return HttpResponse("OK")

@login_required
def cambios(request,gameId):
    game = Game.objects.get(pk=gameId)
    for player in game.player_set.all():
        if not player.user:
            DeckService.changeCardsToIA(player)
        else:
            cardsToChangeIds = request.POST.getlist("selectedCards")
            DeckService.changeCards(player, cardsToChangeIds)
    GameService.setGameComprobado(player.game)
    return redirect("/board/game/"+str(player.game.id)+"/")

@login_required
def play(request,gameId):
    game = Game.objects.get(pk=gameId)
    PlayService.calculateWinner(game)
    game.fase = Game.FINALIZADA
    game.save()

    return redirect("/board/game/"+str(game.id)+"/")

def simulateGame(request):
    game = Game(name="Partida")
    game.save()
    player1 = Player(name="pepe",game=game)
    player1.save()
    player2 = Player(name="juan",game=game)
    player2.save()
    player3 = Player(name="eric",game=game)
    player3.save()
    
    card1 = Card(number=1,suit="DIAMANTE",player=player1)
    card1.save()
    card2 = Card(number=10,suit="DIAMANTE",player=player1)
    card2.save()
    card3 = Card(number=4,suit="PICA",player=player1)
    card3.save()
    card4 = Card(number=7,suit="TREBOL",player=player1)
    card4.save()
    card5 = Card(number=4,suit="CORAZON",player=player1)
    card5.save()

    PlayService.calculateHigherPlay(player1)
    print(player1.jugada)
    print(player1.numMasAlto)

    card1 = Card(number=2,suit="DIAMANTE",player=player2)
    card1.save()
    card2 = Card(number=7,suit="PICA",player=player2)
    card2.save()
    card3 = Card(number=2,suit="TREBOL",player=player2)
    card3.save()
    card4 = Card(number=11,suit="TREBOL",player=player2)
    card4.save()
    card5 = Card(number=11,suit="CORAZON",player=player2)
    card5.save()

    PlayService.calculateHigherPlay(player2)
    print(player2.jugada)
    print(player2.numMasAlto)


    return HttpResponse("sfdas")
