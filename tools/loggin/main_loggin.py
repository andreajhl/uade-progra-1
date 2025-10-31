# tools/loggin/main_loggin.py
import os
from tools.loggin.admin_loggin import handle_user_loggin
from tools.json.index import read_json

def loggin() -> bool:
    """Ejecuta el login del administrador."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "users.json")
    #Busca la ruta absoluta del archivo "user.json"
    users_db = read_json(db_path)[0]
    return handle_user_loggin(users_db)  #True o False

if __name__ == "__main__":
    loggin()
