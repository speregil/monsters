from game.cards import *
from game.deck import *

def draw_menu_title(title:str) -> None:
    print('-----------------------------------------')
    print(title)
    print('-----------------------------------------')
    print('\n')

def draw_main_menu() -> None:
    print('\n')
    draw_menu_title('Welcome to Monster Fighting')
    print('Plese, select an option:')
    print('( 1 ) Search Library')
    print('( 2 ) Create a new card')
    print('( 3 ) Eliminate a card')
    print('( 4 ) Manage all card Decks')
    print('( 5 ) Play a 1v1 game')
    print('( 0 ) Exit')

def draw_search_menu() -> None:
    print('\n')
    draw_menu_title('Cards Library')
    print('What do you want to search for?')
    print('( 1 ) Search card by ID')
    print('( 2 ) Search card by Name')
    print('( 3 ) Search cards by Type')
    print('( 4 ) Search Monster cards by Attack')
    print('( 5 ) Search Monster cards by Defense')
    print('( 6 ) Search Hunter cards by Power')
    print('( 0 ) Return to the previous menu')

def draw_create_menu() -> None:
    print('\n')
    draw_menu_title('Create a new Card')
    print('What type of card do you want to create?')
    print('( 1 ) A monster card')
    print('( 2 ) A hunter card')
    print('( 0 ) Return to the previous menu')

def draw_deck_menu() -> None:
    print('\n')
    draw_menu_title('Decks Library')
    print('Plese, select an option:')
    print('( 1 ) Create a new Deck')
    print('( 2 ) List all Decks')
    print('( 3 ) Delete a Deck')
    print('( 0 ) Return to the previous menu')

def draw_deck_edit_menu(deck:Deck) -> None:
    print('\n')
    draw_menu_title(deck.name)
    if deck.deck_size() > 0:
        for i in range(len(deck.deck_list)):
            card = deck.deck_list[i]
            info = "( " + str(i) + ") "
            info += card.name + " "
            info += "[" + card.type + "]"
            print(info)
    else:
        print('No cards in this deck')

    print('Plese, select an option:')
    print('( 1 ) Add card to', deck.name)
    print('( 2 ) Remove card from',deck.name)
    print('( 0 ) Return to the previous menu')

def draw_card_list(cards:list) -> None:
    for card in cards:
        print(card.to_str())
        print('( 1 ) Continue')
        print('( 2 ) Stop')
        option = input()
        if option == '1': continue
        else: return