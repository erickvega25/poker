from typing import Union
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):

    INICIALIZACION = 0
    REPARTO = 1
    CAMBIO = 2
    COMPROBACION = 3
    FINALIZADA = 4

    name = models.CharField(max_length=255)
    winner = models.ForeignKey("Player",on_delete=models.SET_NULL,null=True,related_name='winner')
    fase = models.IntegerField(default=INICIALIZACION)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)


class Deck(models.Model):
    game = models.OneToOneField(Game,on_delete=models.CASCADE)

    
class Player(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    lastname = models.CharField(max_length=255,default="")
    jugada = models.IntegerField(null=True)
    numMasAlto = models.IntegerField(null=True)
    haCambiado = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return self.name + " " + str(self.lastname)

class Card(models.Model):
    
    DIAMANTE = 0
    PICA = 1
    TREBOL = 2
    CORAZON = 3

    BLACK = 0
    RED = 1

    SUIT_NAMES = ["DIAMANTE","PICA","TREBOL","CORAZON"]
    BLACK_SUITS = ["TREBOL","PICA"]
    RED_SUITS = ["DIAMANTE","CORAZON"]

    
    number = models.IntegerField(null=False)
    suit = models.CharField(max_length=20,null=False)
    deck = models.ForeignKey(Deck,on_delete=models.CASCADE,null=True)
    positionInDeck = models.IntegerField(null=True)
    player = models.ForeignKey(Player,on_delete=models.CASCADE,null=True,related_name='hand')
    implicadaEnJugada = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.number) + " de " +self.suit

    def getColor(self) -> int:
        if self.suit in self.BLACK_SUITS:
            return self.BLACK
        return self.RED



    