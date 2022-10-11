from game.library import Library

print('Welcome to Monster Fighting')

print('Loading Library...')
current_library = Library()
print('Load complete')
test_card = current_library.get_card('1')
print(test_card.name)