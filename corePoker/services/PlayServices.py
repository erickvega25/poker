from typing import Union
from corePoker.models import Card, Game, Player
class PlayService:

    NO_PLAY = 0
    PAREJA = 1
    DOBLE_PAREJA = 2
    TRIO = 3
    ESCALERA = 4
    COLOR = 5
    FULL = 6
    ESCALERA_DE_COLOR = 7
    POKER = 8
    ESCALERA_REAL = 9

    ESCALERA_REAL_NUMBERS =[1,10,11,12,13]

    def desmarcarCartasImplicadas(player: Player) -> None:
        for card in player.hand.all():
            card.implicadaEnJugada = False
            card.save()

    def hasPareja(player: Player) -> Union[int,int]:
        hasPareja = False
        numeroMasAlto = 0
        cartasImplicadas = []
        for carta in player.hand.all():
            for carta2 in player.hand.all():
                if carta.id == carta2.id:
                    continue
                if carta.number == carta2.number:
                    hasPareja = True
                    if numeroMasAlto < carta.number:
                        cartasImplicadas = []
                        cartasImplicadas.append(carta)
                        cartasImplicadas.append(carta2)
                        numeroMasAlto = carta.number
        if hasPareja:
            for card in cartasImplicadas:
                card.implicadaEnJugada = True
                card.save()
            return PlayService.PAREJA, numeroMasAlto
        return PlayService.NO_PLAY,None

    def hasDoblePareja(player:Player):
        numeroMasAlto = 0
        numeroDeParejas = 0
        parejasEncontradas = []
        cartasImplicadas = []
        for carta in player.hand.all():
            for carta2 in player.hand.all():
                if carta.id == carta2.id:
                    continue
                if carta.number == carta2.number and carta.number not in parejasEncontradas:
                    cartasImplicadas.append(carta)
                    cartasImplicadas.append(carta2)
                    numeroDeParejas = numeroDeParejas +1
                    parejasEncontradas.append(carta.number)
                    if numeroMasAlto < carta.number:
                        numeroMasAlto = carta.number
                if numeroDeParejas == 2:
                    for card in cartasImplicadas:
                        card.implicadaEnJugada = True
                        card.save()
                    return PlayService.DOBLE_PAREJA, numeroMasAlto
            
        return PlayService.NO_PLAY,None

    def hasTrio(player:Player) -> Union[int,int]:
        cartasImplicadas = []
        for carta in player.hand.all():
            repeticiones = 0
            for carta2 in player.hand.all():
                if carta.id == carta2.id:
                    continue
                if carta.number == carta2.number:
                    cartasImplicadas.append(carta)
                    cartasImplicadas.append(carta2)
                    repeticiones += 1
                if repeticiones == 2:
                    cartasImplicadas.append(carta2)
                    for card in cartasImplicadas:
                        card.implicadaEnJugada = True
                        card.save()
                    return PlayService.TRIO, carta.number
        return PlayService.NO_PLAY, None

    def hasEscalera(player:Player):
        cartasOrdenadas = player.hand.all().order_by('number')
        numeroDeCarta = None
        cartasImplicadas = []
        for card in cartasOrdenadas:
            cartasImplicadas.append(card)
            if not numeroDeCarta:
                numeroDeCarta = card.number
                continue
            if card.number != numeroDeCarta +1:
                cartasImplicadas.clear()
                return PlayService.NO_PLAY, None
            numeroDeCarta = card.number
        for card in cartasImplicadas:
            card.implicadaEnJugada = True
            card.save()
        return PlayService.ESCALERA, numeroDeCarta

    def hasColor(player:Player):
        paloCarta = None
        numeroMasAlto = 0
        cartasImplicadas = []
        for card in player.hand.all():
            cartasImplicadas.append(card)
            if not paloCarta:
                paloCarta = card.suit
            if paloCarta != card.suit:
                cartasImplicadas.clear()
                return PlayService.NO_PLAY, None
            if card.number > numeroMasAlto:
                numeroMasAlto = card.number
        for card in cartasImplicadas:
            card.implicadaEnJugada = True
            card.save() 
        return PlayService.COLOR, numeroMasAlto


    def hasFull(player:Player) ->Union[int,int]:
        hasPareja, parejaNumber = PlayService.hasPareja(player)
        hasTrio, trioNumber = PlayService.hasTrio(player)
        if hasPareja == PlayService.PAREJA and hasTrio == PlayService.TRIO and parejaNumber != trioNumber:
            for card in player.hand.all():
                card.implicadaEnJugada = True
                card.save()
            return PlayService.FULL, trioNumber
        return PlayService.NO_PLAY, None


    def hasEscaleraDeColor(player:Player):
        hasEscalera, escaleraNumber = PlayService.hasEscalera(player)
        hasColor, numeroMasAlto = PlayService.hasColor(player)
        if hasEscalera == PlayService.NO_PLAY or hasColor == PlayService.NO_PLAY:
            return PlayService.NO_PLAY, None
        for card in player.hand.all():
            card.implicadaEnJugada = True
            card.save()
        return PlayService.ESCALERA_DE_COLOR, escaleraNumber

    def hasPoker(player:Player):
        cartasImplicadas = []
        for carta in player.hand.all():
            repeticiones = 0
            for carta2 in player.hand.all():
                if carta.id == carta2.id:
                    continue
                if carta.number == carta2.number:
                    cartasImplicadas.append(carta)
                    cartasImplicadas.append(carta2)
                    if len(cartasImplicadas) == 2:
                        cartasImplicadas.append(carta2)
                    repeticiones += 1
                if repeticiones == 3:
                    cartasImplicadas.append(carta2)
                    for card in cartasImplicadas:
                        card.implicadaEnJugada = True
                        card.save()
                    return PlayService.POKER, carta.number
        return PlayService.NO_PLAY, None

    def hasEscaleraReal(player:Player):
        hasColor, numeroMasAlto = PlayService.hasColor(player)
        if hasColor == PlayService.NO_PLAY:
            return PlayService.NO_PLAY, None
        for card in player.hand.all():
            if not card.number in PlayService.ESCALERA_REAL_NUMBERS:
                return PlayService.NO_PLAY, None
        for card in player.hand.all():
            card.implicadaEnJugada = True
            card.save()
        return PlayService.ESCALERA_REAL, numeroMasAlto


    def calculateHigherPlay(player:Player) -> None:
        player.jugada = PlayService.NO_PLAY
        player.numMasAlto = 0
        jugada, numeroMasAlto = PlayService.hasPareja(player)
        if jugada > player.jugada:
            player.jugada = jugada
            player.numMasAlto = numeroMasAlto
        jugada, numeroMasAlto = PlayService.hasDoblePareja(player)
        if jugada > player.jugada:
            player.jugada = jugada
            player.numMasAlto = numeroMasAlto
        jugada, numeroMasAlto = PlayService.hasTrio(player)
        if jugada > player.jugada:
            player.jugada = jugada
            player.numMasAlto = numeroMasAlto
        jugada, numeroMasAlto = PlayService.hasEscalera(player)
        if jugada > player.jugada:
            player.jugada = jugada
            player.numMasAlto = numeroMasAlto
        jugada, numeroMasAlto = PlayService.hasColor(player)
        if jugada > player.jugada:
            player.jugada = jugada
            player.numMasAlto = numeroMasAlto
        jugada, numeroMasAlto = PlayService.hasFull(player)
        if jugada > player.jugada:
            player.jugada = jugada
            player.numMasAlto = numeroMasAlto
        jugada, numeroMasAlto = PlayService.hasEscaleraDeColor(player)
        if jugada > player.jugada:
            player.jugada = jugada
            player.numMasAlto = numeroMasAlto
        jugada, numeroMasAlto = PlayService.hasPoker(player)
        if jugada > player.jugada:
            player.jugada = jugada
            player.numMasAlto = numeroMasAlto
        jugada, numeroMasAlto = PlayService.hasEscaleraReal(player)
        if jugada > player.jugada:
            player.jugada = jugada
            player.numMasAlto = numeroMasAlto
        player.save()

    def calculateWinner (game:Game):
        players = game.player_set.all()
        winner = None
        jugadaMasAlta = PlayService.NO_PLAY
        numeroMasAlto = 0
        for player in players:
            PlayService.calculateHigherPlay(player)
            if player.jugada > jugadaMasAlta:
                jugadaMasAlta = player.jugada
                numeroMasAlto = player.numMasAlto
                winner = player
            if player.jugada == jugadaMasAlta:
                if player.numMasAlto > numeroMasAlto:
                    jugadaMasAlta = player.jugada
                    numeroMasAlto = player.numMasAlto
                    winner = player
        game.winner = winner
        game.save()

