from game.cards import Card
from typing import List

class Deck:
    DECK_SIZE = 5

    def __init__(self, name:str):
        self.name = name
        self.deck_list:List[Card] = []

    def add_card(self, card:Card) -> None:
        if len(self.deck_list) < self.DECK_SIZE:
            self.deck_list.append(card)
        else:
            raise FullDeckError()

    def remove_card(self, id:int) -> Card:
        i = 0
        remove = None
        while i < len(self.deck_list):
            card = self.deck_list[i]
            if card.id_number == id:
                remove = self.deck_list.pop(i)
                break
            i += 1
        return remove

    def is_valid(self) -> bool:
        if len(self.deck_list) == 5:
            for card in self.deck_list:
                if card.type == Card.MONSTER_TYPE : return True
        return False
        
class FullDeckError(Exception):
    pass