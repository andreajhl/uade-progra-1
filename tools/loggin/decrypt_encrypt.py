#Funcion de desencriptado para contraseñas
def decrypt(enc_psw,desplazo=4):
    """Desencriptado
    Args:
        enc_psw: contraseña encriptada
        desplazo (int, optional): desp. encriptado. Defaults to 4.
    """
    decrypted=""
    for caracter in enc_psw:
        decrypted += chr((ord(caracter) + desplazo) % 256)
    return decrypted

#Funcion de encriptado por si implementamos crear usuarios de forma dinamica
def encipt(dec_psw,desplazo=4):
    """Encriptado
    Args:
        dec_psw: contraseña sin encriptar
        desplazo (int, optional): desp. encriptado. Defaults to 4.
    """
    encrypted=""
    for caracter in dec_psw:
        encrypted += chr((ord(caracter) - desplazo) % 256)
    return encrypted