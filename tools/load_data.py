from .read_json import read_json
from constants.index import DATA_PATH, HALLS_NAME_IN_FILE, FILMS_NAMES_IN_FILE

def load_data():
    data, err = read_json(DATA_PATH)
    
    if err: return None, None
    
    return data[HALLS_NAME_IN_FILE], data[FILMS_NAMES_IN_FILE]

    