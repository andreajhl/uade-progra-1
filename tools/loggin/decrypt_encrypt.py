def decrypt(enc_psw,displacement=4):
    """Desencriptado
    Args:
        enc_psw: contraseña encriptada
        desplazo (int, optional): desp. encriptado. Defaults to 4.
    """
    decrypted=""
    for character in enc_psw:
        decrypted += chr((ord(character) + displacement) % 256)
    return decrypted

def encrypt(dec_psw,displacement=4):
    """Encriptado
    Args:
        dec_psw: contraseña sin encriptar
        desplazo (int, optional): desp. encriptado. Defaults to 4.
    """
    encrypted=""
    for character in dec_psw:
        encrypted += chr((ord(character) - displacement) % 256)
    return encrypted