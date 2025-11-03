from tools.input.index import custom_input
from custom_types import UserDatabase
from tools.loggin.decrypt_encrypt import decrypt

def get_admin_loggin_data() -> str:
    """Solicita el nombre de usuario."""
    return custom_input(
        "Ingrese el nombre de Usuario: ",
        str,
        validator=lambda name: (
            ("El nombre no puede estar vacío.", None)
            if not name.strip()
            else (None, name.strip())
        )
    )

def get_password_input() -> str:
    """Solicita la contraseña del usuario."""
    return custom_input(
        "Ingrese la contraseña (o 9 para salir):",
        str,
        validator=lambda pwd: (
            ("La contraseña no puede estar vacía.", None)
            if not pwd.strip()
            else (None, pwd.strip())
        )
    )

def handle_user_loggin(users_db: UserDatabase) -> bool:
    """Maneja el inicio de sesión del usuario.
    Retorna True si el login es exitoso, False en caso contrario.
    """
    password_input=None
    username_input = get_admin_loggin_data()
    user = find_user(users_db, username_input)

    if not user:
        print(f"🔍 Usuario inexistente: '{username_input}'")
        input("Presiona Enter para continuar...")
        return False
    password_input = decrypt(get_password_input(),4)
    while password_input != user["password"]:
        print("\n❌ Contraseña incorrecta.")
        password_input = decrypt(get_password_input(),4)
        if password_input==decrypt("9"):
            print(f"\n Acceso denegado.")
            return False
  
    print(f"\n Acceso concedido.")
    return True


def find_user(users_db: UserDatabase, username: str) -> dict | None:
    """Busca un usuario por nombre (sin distinguir mayúsculas/minúsculas)."""
    username_lower = username.lower()
    for user in users_db.values():
        if user["username"].lower() == username_lower:
            return user
    return None
