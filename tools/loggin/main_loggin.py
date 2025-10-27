# tools/loggin/main_loggin.py
import os
import json
from tools.loggin.admin_loggin import handle_user_loggin


def load_users_db(filepath: str) -> dict:
    """Carga la base de datos de usuarios (JSON)."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️ No se encontró el archivo de usuarios en {filepath}")
        return {}
    except json.JSONDecodeError:
        print("❌ Error: el archivo de usuarios está corrupto.")
        return {}


def loggin() -> bool:
    """Ejecuta el login del administrador."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "users.json")

    users_db = load_users_db(db_path)
    return handle_user_loggin(users_db)  #True o False


if __name__ == "__main__":
    loggin()
