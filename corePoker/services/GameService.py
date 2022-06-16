from corePoker.models import Game

class GameService:

    @staticmethod
    def checkPlayersHanCambiado(game: Game):
        for player in game.player_set.all():
            if not player.haCambiado:
                return False
        return True

    @staticmethod
    def setGameComprobado(game: Game):
        if GameService.checkPlayersHanCambiado(game):
            game.fase = Game.COMPROBACION
            game.save()
