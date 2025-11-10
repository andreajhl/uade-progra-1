from tools.loggin.admin_loggin import handle_user_loggin
from tools.json.index import read_json
from constants.index import USER_PATH

def loggin() -> bool:
    """Ejecuta el login del administrador."""
    users_db,_ = read_json(USER_PATH)
    return handle_user_loggin(users_db) 
if __name__ == "__main__":
    loggin()