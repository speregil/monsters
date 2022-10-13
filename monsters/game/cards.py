class Card:
    MONSTER_TYPE = 0
    HUNTER_TYPE = 1

    def __init__(self, id_number:int, name:str, description:str ):
        self.id_number = id_number
        self.name = name
        self.description = description

    def to_str(self) -> str:
        card_str = 'ID: ' + str(self.id_number) + '\n'
        card_str += 'Name: ' + self.name + '\n'
        card_str += self.description + '\n'
        return card_str

class HunterCard(Card):
    def __init__(self, id_number:int, name:str, description:str, power_points:int ):
        super().__init__(id_number,name,description)
        self.power_points = power_points
        self.type = Card.HUNTER_TYPE

    def to_str(self) -> str:
        card_str = super().to_str()
        card_str += 'Power: ' + str(self.power_points)
        return card_str

class MonsterCard(Card):
    def __init__(self, id_number:int, name:str, description:str, attack_points:int, defense_points:int ):
        super().__init__(id_number,name,description)
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.type = Card.MONSTER_TYPE

    def to_str(self) -> str:
        card_str = super().to_str()
        card_str += 'Attack: ' + str(self.attack_points) + '\n'
        card_str += 'Defense: ' + str(self.defense_points) + '\n'
        return card_str