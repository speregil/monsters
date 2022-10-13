import json

def load_library() -> dict:
    f = open('./library.json','r')
    data = json.load(f)
    return data['library']

def save_library(raw_library:dict) -> None:
    jsonString = json.dumps(raw_library)
    jsonFile = open("./library.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()