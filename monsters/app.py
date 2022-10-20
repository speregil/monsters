from game.library import Library
from game.cards import *
import interface.menu_ui as menu
"""
Main script of the program

...

Functions
---------

main()
    Main function that controls the main menu and flow of the program

load_library()
    Loads the library to using during the current game

save_library(current_library)
    Saves any change done to the current library

search_cards(current_library)
    Controls the Search Cards menu

"""

def main():
    """ Main function that controls the main menu and flow of the program
    """
    print('Welcome to Monster Fighting')
    current_library = load_library()    # Loads the library from data/library.json
    app_running = True

    while app_running:
        menu.draw_main_menu()
        option = int(input('Select and option:\t'))
        # Exit option
        if option == 0:
            app_running = False
        # Search cards menu
        elif option == 1:
            search_cards(current_library)
        # Create cards menu
        elif option == 2:
            create_card(current_library)
    
    save_library(current_library) # Saves any changes to the current library in data/library.json
    print('Thanks for playing!')

def load_library() -> Library:
    """ Loads the library to using during the current game

    Return
    ------
    Library
        The current loaded Library object
    """

    print('Loading Library...')
    current_library = Library()
    print('Load complete')
    return current_library

def save_library(current_library:Library) -> None:
    """ Saves any change done to the current library

    Parameters
    ----------
    current_library : Library
        Current state of the loaded library
    """

    print('Saving library...')
    current_library.save_library()
    print('Save Complete')

def search_cards(current_library:Library) -> None:
    """ Controls the Search Cards menu

    Parameters
    ----------
    current_library : Library
        Current state of the loaded library
    """

    routine_running = True
    while routine_running:
        menu.draw_search_menu()
        option = int(input('Select and option:\t'))
        if option == 0: # Exit option
            routine_running = False
        elif option == 1:   # Search by ID option
            id = input('Input the ID you are searching:\t')
            card = current_library.search_card_by_id(id)
            if card == None:
                print('Sorry, no card with such ID')
            else:
                print(card.to_str())
        elif option == 2:   # Seach by Name option
            name = input('Input the Name you are searching:\t')
            card = current_library.search_card_by_name(name)
            if card == None:
                print('Sorry, no card with such Name')
            else:
                print(card.to_str())
        elif option == 3: # Search by Type option
            print('Select the type you want to search:')
            print('( 1 ) Monsters')
            print('( 2 ) Hunters')
            type = input()
            if type == '1':
                cards = current_library.search_cards_by_type(Card.MONSTER_TYPE)
            elif type == '2':
                cards = current_library.search_cards_by_type(Card.HUNTER_TYPE)
            if len(cards) <= 0:
                print('No cards of that Type')
            else:
                menu.draw_card_list(cards)
        elif option == 4: # Search by Attack option
            attack = int(input('Input the attack points to search for:\t'))
            cards = current_library.search_monsters_by_attack(attack)
            if len(cards) <= 0:
                print('No cards of that much Attack Points')
            else:
                menu.draw_card_list(cards)
        elif option == 5: # Search by Defense option
            defense = int(input('Input the defense points to search for:\t'))
            cards = current_library.search_monsters_by_defense(defense)
            if len(cards) <= 0:
                print('No cards of that much Defense Points')
            else:
                menu.draw_card_list(cards)
        elif option == 6: #Search by Power option
            power = int(input('Input the power points to search for:\t'))
            cards = current_library.search_hunters_by_power(power)
            if len(cards) <= 0:
                print('No cards of that much Power Points')
            else:
                menu.draw_card_list(cards)


def create_card(current_library:Library) -> None:
    return None

if __name__ == "__main__":
    main()