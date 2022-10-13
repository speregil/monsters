from game.cards import *
import data.data_manager as data

class Library:
    """ 
    Represents the library of cards loaded in the current game.

    ...

    Atributes
    ---------
    library : dict
        Dictionary in the form id - Card. Holds all current Cards of the game
        as defined in the library.json file. Cards can be MonsterCards or HunterCards.

    Methods
    -------
    search_card_by_id(id_number)
        Returns the Card identified with id_number, None if the card does not exist.

    create_monster_card(name, description, attack_points, defense_points)
        Creates a new MonsterCard and adds it to the current library. The library file is not modified.
    
    create_hunter_card(name, description, power_points)
        Creates a new HunterCard and adds it to the current library. The library file is not modified.
    
    get_next_id_number()
        Returns the next free id that can be used for a new Card addtion to the current library.

    save_library()
        Promts the data manager to save the current library in local memory
    """

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

    def search_card_by_id(self, id_number:str) -> Card:
        """" Returns the Card identified with id_number, None if the card does not exist

        Parameters
        ----------
        id_number : int
            Unique id of the required Card

        Returns
        -------
        Card
            The card associated with the given id
        """

        return self.library.get(id_number,None)
    
    def create_monster_card(self, name:str, description:str, attack_points:int, defense_points:int) -> MonsterCard:
        """" Creates a new MonsterCard and adds it to the current library. The library file is not modified

        Parameters
        ----------
        name : str
            Name of the new MonsterCard
        description : str
            Flavour description of the new MonsterCard
        attack_points : int
            Total attack points of the new MonsterCard
        defense_points : int
            Total defense point of the new MonsterCard

        Returns
        -------
        MonsterCard
            New MonsterCard created
        """

        id = self.get_next_id_number()
        new_card = MonsterCard(id, name, description, attack_points, defense_points)
        self.library[id] = new_card
        return new_card

    def create_hunter_card(self, name:str, description:str, power_points:int) -> HunterCard:
        """" Creates a new HunterCard and adds it to the current library. The library file is not modified

        Parameters
        ----------
        name : str
            Name of the new MonsterCard
        description : str
            Flavour description of the new HunterCard
        apower_points : int
            Total power points of the new HunterCard

        Returns
        -------
        HunterCard
            New HunterCard created
        """
        
        id = self.get_next_id_number()
        new_card = HunterCard(id, name, description, power_points)
        self.library[id] = new_card
        return new_card

    def get_next_id_number(self) -> int:
        """" Returns the next free id that can be used for a new Card addtion to the current library.

        Returns
        -------
        int
            Next id that can be used in a new Card. The new id is the highest id in the current library + 1.
        """
        
        ids = self.library.keys
        last_id = 0
        for id in ids:
            if id > last_id:
                last_id = id
        return last_id + 1

    def save_library(self) -> None:
        """ Converts the current library in a plain dictionary and asks
            the data manager to save it in local memory
        """
        
        raw_library = {}
        for id in self.library:
            card = self.library[id]
            card_dict = {}
            card_dict['name'] = card.name
            card_dict['description'] = card.description
            if card.type == Card.HUNTER_TYPE:
                card_dict['type'] = 'hunter'
                card_dict['power'] = card.power_points
            else:
                card_dict['type'] = 'monster'
                card_dict['attack'] = card.attack_points
                card_dict['defense'] = card.defense_points
            raw_library[id] = card_dict
        data.save_library({'library':raw_library})