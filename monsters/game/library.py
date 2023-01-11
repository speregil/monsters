from game.cards import *
from game.deck import Deck
import data.data_manager as data
from typing import List

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
    load_library()
        Loads the library from the data file of cards and returns it

    search_card_by_id(id_number)
        Returns the Card identified with id_number, None if the card does not exist.

    search_card_by_name(name)
        Returns the Card with the given name, None if the card does not exist

    search_cards_by_type(type)
        Returns a list of cards with the type given
    
    search_monsters_by_attack(attack)
        Returns a list of monster cards with the given attack points

    search_monsters_by_defense(defense)
        Returns a list of monster cards with the given defense points

    create_monster_card(name, description, attack_points, defense_points)
        Creates a new MonsterCard and adds it to the current library. The library file is not modified.
    
    create_hunter_card(name, description, power_points)
        Creates a new HunterCard and adds it to the current library. The library file is not modified.
    
    eliminate_card(id)
        Removes from the library the card with the provided ID. The library file is not modified
    
    get_next_id_number()
        Returns the next free id that can be used for a new Card addtion to the current library.

    save_library()
        Promts the data manager to save the current library in local memory
    """

    def __init__(self):
        self.library = self.load_library()
        self.decks:List[Deck] = []
        self.load_decks()

    def load_library(self) -> dict:
        """ Loads the library from the data file of cards and returns it

        Returns
        -------
        dict
            A dictionary with all the cards in the library with the form id:card
        """
        library = {}
        raw_library = data.load_data('library')
        for id in raw_library:
            card = raw_library[id]
            if card['type'] == 'monster':
                new_card = MonsterCard(int(id),card['name'],card['description'],card['attack'],card['defense'])
                library[int(id)] = new_card
            else:
                new_card = HunterCard(int(id),card['name'],card['description'],card['power'])
                library[int(id)] = new_card
        return library


    def search_card_by_id(self, id_number:str) -> Card:
        """ Returns the Card identified with id_number, None if the card does not exist

        Parameters
        ----------
        id_number : int
            Unique id of the required Card

        Returns
        -------
        Card
            The card associated with the given id
        """

        return self.library.get(int(id_number),None)
    
    def search_card_by_name(self, name:str) -> Card:
        """ Returns the Card with the given name, None if the card does not exist

        Parameters
        ----------
        name : str
            Name to search for
        
        Returns
        -------
        Card
            The card associated with the given name
        """

        for id in self.library:
            current_card = self.library[id]
            if current_card.name.lower() == name.lower():
                return current_card
        return None

    def search_cards_by_type(self, type:int) -> list:
        """ Returns a list of cards with the type given

        Parameters
        ----------
        type : int
            Type of card to search for
        
        Returns
        -------
        list
            A list of cards with the given type
        """

        cards_list = []
        for id in self.library:
            card = self.library[id]
            if card.type == type:
                cards_list.append(card)
        return cards_list

    def search_monsters_by_attack(self, attack:int) -> list:
        """ Returns a list of monster cards with the given attack points

        Parameters
        ----------
        attack : int
            Attack points of the cards to search

        Returns
        -------
        list
            A list of monster cards with the given attack points 
        """

        cards_list = []
        for id in self.library:
            card = self.library[id]
            if card.type == Card.MONSTER_TYPE and card.attack_points == attack:
                cards_list.append(card)
        return cards_list

    def search_monsters_by_defense(self, defense:int) -> list:
        """ Returns a list of monster cards with the given defense points

        Parameters
        ----------
        defense : int
            Defense points of the cards to search

        Returns
        -------
        list
            A list of monster cards with the given defense points 
        """

        cards_list = []
        for id in self.library:
            card = self.library[id]
            if card.type == Card.MONSTER_TYPE and card.defense_points == defense:
                cards_list.append(card)
        return cards_list

    def search_hunters_by_power(self, power:int) -> list:
        """ Returns a list of hunter cards with the given power points

        Parameters
        ----------
        power : int
            Power points of the cards to search

        Returns
        -------
        list
            A list of hunter cards with the given power points 
        """

        cards_list = []
        for id in self.library:
            card = self.library[id]
            if card.type == Card.HUNTER_TYPE and card.power_points == power:
                cards_list.append(card)
        return cards_list

    def create_monster_card(self, name:str, description:str, attack_points:int, defense_points:int) -> MonsterCard:
        """ Creates a new MonsterCard and adds it to the current library. The library file is not modified

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
        """ Creates a new HunterCard and adds it to the current library. The library file is not modified

        Parameters
        ----------
        name : str
            Name of the new MonsterCard
        description : str
            Flavour description of the new HunterCard
        power_points : int
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

    def eliminate_card(self, id:int) -> Card:
        """ Removes from the library the card with the provided ID. The library file is not modified
        
        Parameters
        ----------
        id : int
            Unique ID of the card to be eliminated

        Returns
        -------
        Card
            The card that was eliminated from the library
        """

        card = self.search_card_by_id(id)
        del self.library[id]
        return card

    def get_next_id_number(self) -> int:
        """ Returns the next free id that can be used for a new Card addtion to the current library.

        Returns
        -------
        int
            Next id that can be used in a new Card. The new id is the highest id in the current library + 1.
        """
        
        ids = list(self.library.keys())
        last_id = max(ids)
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
        data.save_data({'data':raw_library},'library')

    def load_decks(self) -> None:
        raw_decks = data.load_data('decks')
        for name in raw_decks:
            new_deck = Deck(name)
            card_list = raw_decks[name]
            for id in card_list:
                card = self.get_deck(int(id))
                if card: new_deck.add_card(card)
            self.decks.append(new_deck)

    def get_deck(self, name:str) -> Deck:
        for deck in self.decks:
            if deck.name == name : return deck
        return None
    
    def is_deck_name_available(self, name:str) -> bool:
        for deck in self.decks:
            if deck.name == name: 
                return False
        return True

    def create_deck(self, name:str) -> None:
        if self.is_deck_name_available(name):
            new_deck = Deck(name)
            self.decks.append(new_deck)
        else:
            raise DeckNameError()
    
    def get_deck_by_id(self, id:int) -> Deck:
        return self.decks[id]
        
    def add_card(self, deck_name:str, card:Card) -> None:
        deck = self.get_deck(deck_name)
        if deck:
            deck.add_card(card)
        else:
            raise NoSuchDeckError()

    def remove_card(self, deck_name:str, id:int) -> Card:
        deck = self.get_deck(deck_name)
        if deck:
            return deck.remove_card(id)
        else:
            raise NoSuchDeckError()

    def save_decks(self):
        raw_decks = {}
        for deck in self.decks:
            card_list = []
            for card in deck.deck_list:
                card_list.append(card.id_number)
            raw_decks[deck.name] = card_list
        data.save_data({'data':raw_decks},'decks')

            
class DeckNameError(Exception):
    pass

class NoSuchDeckError(Exception):
    pass