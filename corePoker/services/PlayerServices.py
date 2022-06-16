from django.contrib.auth.models import User
from corePoker.models import Game, Player
class PlayerService:

    @staticmethod
    def createPlayers(game : Game, user: User) -> None:
        player1 = Player(name="Pepe",game=game,)
        player2 = Player(name="Juan",game=game,)
        player3 = Player(name=user.username,user=user,game=game)
        player1.save()
        player2.save()
        player3.save()