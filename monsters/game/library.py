from game.cards import *
import data.data_manager as data

class Library:
    def __init__(self):
        library = {}
        raw_library = data.load_library()
        for id in raw_library:
            card = raw_library[id]
            if card['type'] == 'monster':
                new_card = MonsterCard(id,card['name'],card['description'],card['attack'],card['defense'])
                library[id] = new_card
            else:
                new_card = HunterCard(id,card['name'],card['description'],card['power'])
                library[id] = new_card
        self.library = library

    def get_card(self, id_number:int) -> Card:
        return self.library.get(id_number,None)
    
    def create_monster_card(self, name:str, description:str, attack_points:int) -> MonsterCard:
        return None

    def create_hunter_card(self, name:str, description:str, power_points:int) -> HunterCard:
        return None

    def get_next_id_number(self) -> int:
        return 0