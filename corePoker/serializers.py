from rest_framework import serializers
from corePoker.models import Player, Card, Game
from django.contrib.auth.models import User


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['id','number','suit']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

class PlayerSerializer(serializers.ModelSerializer):
    hand = CardSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'name','haCambiado','hand','user']

class GameSerializer(serializers.ModelSerializer):
    winner = PlayerSerializer(read_only=True)
    
    class Meta:
        model = Game
        fields = ['fase','winner']