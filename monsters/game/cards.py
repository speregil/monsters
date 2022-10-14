class Card:
    """
    Represents any type of card

    ...

    Atributes
    ---------
    id_number : int
        The unique identification of the card
    
    name : str
        The name of the card

    description : str
        The flavour description of the card

    Methods
    -------
    to_str()
        Converts the information of the card into a printable string
    """
    MONSTER_TYPE = 0    # Codes the Monster type of a card
    HUNTER_TYPE = 1     # Codes the Hunter type of a card

    def __init__(self, id_number:int, name:str, description:str ):
        self.id_number = id_number
        self.name = name
        self.description = description

    def to_str(self) -> str:
        """ Converts the information of the card into a printable string

        Returns
        -------
        str:
            A string of the information of the card
        """

        card_str = 'ID: ' + str(self.id_number) + '\n'
        card_str += 'Name: ' + self.name + '\n'
        card_str += self.description + '\n'
        return card_str

class HunterCard(Card):
    """
    Represents a Hunter card. Inherits from Card

    ...

    Atributes
    ---------
    power_points : int
        The ammount of Power points of the Hunter
    
    type : int
        The type of the card. Type is HUNTER

    Methods
    -------
    to_str()
        Converts the information of the card into a printable string
    """
    def __init__(self, id_number:int, name:str, description:str, power_points:int ):
        super().__init__(id_number,name,description)
        self.power_points = power_points
        self.type = Card.HUNTER_TYPE

    def to_str(self) -> str:
        """ Converts the information of the card into a printable string

        Returns
        -------
        str:
            A string of the information of the card
        """

        card_str = super().to_str()
        card_str += 'Power: ' + str(self.power_points)
        return card_str

class MonsterCard(Card):
    """
    Represents a Monster card. Inherits from Card

    ...

    Atributes
    ---------
    attack_points : int
        The ammount of Attack points of the Monster

    defense_points : int
        The ammount of Defense points of the Monster
    
    type : int
        The type of the card. Type is MONSTER

    Methods
    -------
    to_str()
        Converts the information of the card into a printable string
    """

    def __init__(self, id_number:int, name:str, description:str, attack_points:int, defense_points:int ):
        super().__init__(id_number,name,description)
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.type = Card.MONSTER_TYPE

    def to_str(self) -> str:
        """ Converts the information of the card into a printable string

        Returns
        -------
        str:
            A string of the information of the card
        """
        
        card_str = super().to_str()
        card_str += 'Attack: ' + str(self.attack_points) + '\n'
        card_str += 'Defense: ' + str(self.defense_points) + '\n'
        return card_str