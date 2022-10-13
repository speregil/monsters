import json
from pathlib import Path

def load_library() -> dict:
    script_dir = Path(__file__).parent
    data_dir = (script_dir / 'library.json').resolve()
    f = open(data_dir,'r')
    data = json.load(f)
    return data['library']

def save_library(raw_library:dict) -> None:
    jsonString = json.dumps(raw_library)
    script_dir = Path(__file__).parent
    data_dir = (script_dir / 'library.json').resolve()
    jsonFile = open(data_dir, "w")
    jsonFile.write(jsonString)
    jsonFile.close()