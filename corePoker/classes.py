class Deck:

    def __init__(self) -> None:
        self.cards = []


class Card:

    DIAMANTE = 0
    PICA = 1
    TREBOL = 2
    CORAZON = 3

    SUIT_NAMES = ["DIAMANTE","PICA","TREBOL","CORAZON"]

    def __init__(self,suit,number) -> None:
        self.suit = suit
        self.number = number

    def __str__(self) -> str:
        return str(self.number) + "de" +self.SUIT_NAMES[self.suit]


class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

