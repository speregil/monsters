class Card:
    MONSTER_TYPE = 0
    HUNTER_TYPE = 1

    def __init__(self, id_number:int, name:str, description:str ):
        self.id_number = id_number
        self.name = name
        self.description = description
        self.type = ""

class HunterCard(Card):
    def __init__(self, id_number:int, name:str, description:str, power_points:int ):
        super().__init__(id_number,name,description)
        self.power_points = power_points
        self.type = Card.HUNTER_TYPE

class MonsterCard(Card):
    def __init__(self, id_number:int, name:str, description:str, attack_points:int, defense_points:int ):
        super().__init__(id_number,name,description)
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.type = Card.MONSTER_TYPE