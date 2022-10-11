import json

def load_library() -> dict:
    f = open('C:/Users/prt4539/Documents/monsters/data/library.json','r')
    data = json.load(f)
    return data['library']

def save_monster_card(id:int, name:str, description:str, attack_points:int, defense_points:int) -> None:
    return None

def save_hunter_card(id:int, name:str, description:str, power_points:int) -> None:
    return None