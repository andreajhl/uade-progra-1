from tools.loggin.admin_loggin import handle_user_loggin
from tools.json.index import read_json

def loggin() -> bool:
    """Ejecuta el login del administrador."""
    users_db,_ = read_json("users.json")
    return handle_user_loggin(users_db) 
if __name__ == "__main__":
    loggin()
