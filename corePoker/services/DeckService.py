from corePoker.models import Deck, Card, Game, Player
from random import randrange, shuffle

from corePoker.services.PlayServices import PlayService

class DeckService:

    INITIAL_CARDS = 5

    @staticmethod
    def createCards(deck: Deck) -> None:
        positionInDeck = 1
        for palo in range (Card.DIAMANTE,Card.CORAZON+1):
            for numero in range (1,14):
                carta = Card(number=numero,suit=Card.SUIT_NAMES[palo],deck=deck,positionInDeck=positionInDeck)
                carta.save()
                positionInDeck = positionInDeck +1


    @staticmethod
    def shuffleDeck(deck: Deck) -> None:
        posicionesGeneradas = []
        for card in deck.card_set.all():
            numeroRandom = randrange(1,53)
            while numeroRandom in posicionesGeneradas:
                numeroRandom = randrange(1, 53)     
            card.positionInDeck = numeroRandom
            posicionesGeneradas.append(numeroRandom)
            card.save()

    @staticmethod
    def distributeCards(game: Game) -> None:
        position = 0
        while position in range(DeckService.INITIAL_CARDS):
            for player in game.player_set.all():
                DeckService.giveCards(game.deck,player,1)
            position = position +1

        
    @staticmethod
    def giveCards(deck:Deck, player:Player, numberOfCards) -> None:
        cards = deck.card_set.all().order_by("positionInDeck")
        cartasEntregadas = 0
        for card in cards:
            card.deck = None
            card.positionInDeck = None
            card.player = player
            card.save()
            cartasEntregadas += 1
            if cartasEntregadas == numberOfCards:
                break
                
    @staticmethod
    def changeCards(player:Player, cardsToChangeIds: list):
        for idCard in cardsToChangeIds:
            card = Card.objects.get(pk=idCard)
            card.player = None
            card.save()
        DeckService.giveCards(player.game.deck, player, len(cardsToChangeIds))
        player.haCambiado = True
        player.save()


    @staticmethod
    def changeCardsToIA(player:Player) :
        PlayService.calculateHigherPlay(player)
        cartasAcambiar = []
        for card in player.hand.all():
            if card.implicadaEnJugada == False:
                cartasAcambiar.append(card.id)
        DeckService.changeCards(player, cartasAcambiar)
        
