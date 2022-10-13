from game.library import Library
import interface.menu_ui as menu

print('Welcome to Monster Fighting')

print('Loading Library...')
current_library = Library()
print('Load complete')

app_running = True
while app_running:
    menu.draw_menu()
    option = int(input('Select and option:\t'))
    if option == 0:
        app_running = False

print('Saving library...')
current_library.save_library()
print('Save Complete')
print('Thanks for playing!')