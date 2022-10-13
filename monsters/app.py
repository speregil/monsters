from game.library import Library
import interface.menu_ui as menu

def search_cards(current_library:Library) -> None:
    routine_running = True
    while routine_running:
        menu.draw_search_menu()
        option = int(input('Select and option:\t'))
        if option == 0:
            routine_running = False
        elif option == 1:
            id = input('Input the ID you are searching:\t')
            card = current_library.search_card_by_id(id)
            if card == None:
                print('Sorry, no card with such ID')
            else:
                print(card.to_str())


def create_card(current_library:Library) -> None:
    return None

print('Welcome to Monster Fighting')

print('Loading Library...')
current_library = Library()
print('Load complete')

app_running = True
while app_running:
    menu.draw_main_menu()
    option = int(input('Select and option:\t'))
    if option == 0:
        app_running = False
    elif option == 1:
        search_cards(current_library)
    elif option == 2:
        create_card(current_library)

print('Saving library...')
current_library.save_library()
print('Save Complete')
print('Thanks for playing!')