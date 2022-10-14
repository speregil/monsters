from game.cards import *

def draw_main_menu() -> None:
    print('Plese, select an option:')
    print('( 1 ) Search Library')
    print('( 2 ) Create a new card')
    print('( 3 ) Eliminate a card')
    print('( 4 ) Create a new deck')
    print('( 5 ) Eliminate a deck')
    print('( 6 ) Play a 1v1 game')
    print('( 0 ) Exit')

def draw_search_menu() -> None:
    print('What do you want to search for?')
    print('( 1 ) Search card by ID')
    print('( 2 ) Search card by Name')
    print('( 3 ) Search cards by Type')
    print('( 4 ) Search Monster cards by Attack')
    print('( 5 ) Search Monster cards by Defense')
    print('( 6 ) Search Hunter cards by Power')
    print('( 0 ) Return to the previous menu')

def draw_card_list(cards:list) -> None:
    for card in cards:
        print(card.to_str())
        print('( 1 ) Continue')
        print('( 2 ) Stop')
        option = input()
        if option == '1': continue
        else: return