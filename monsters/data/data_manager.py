import json
from pathlib import Path

def load_data(save_file:str) -> dict:
    script_dir = Path(__file__).parent
    file_name = save_file + '.json'
    data_dir = (script_dir / file_name).resolve()
    f = open(data_dir,'r')
    data = json.load(f)
    return data['data']

def save_data(data:dict, save_file:str) -> None:
    jsonString = json.dumps(data)
    script_dir = Path(__file__).parent
    file_name = save_file + '.json'
    data_dir = (script_dir / file_name).resolve()
    jsonFile = open(data_dir, "w")
    jsonFile.write(jsonString)
    jsonFile.close()
