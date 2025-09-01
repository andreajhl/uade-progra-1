from string import ascii_uppercase as ALPHABET

ALPHABET_LEN = ALPHABET.__len__()

def numbers_into_letters(number: int) -> str:
    """
    Convierte un número entero no negativo a su correspondiente en letras, 
    siguiendo la notación de las columnas de Excel (ej: 0=A, 25=Z, 26=AA, 27=AB).
    """
    result = []
    
    current_number = number + 1

    while current_number > 0:
        remainder = (current_number - 1) % ALPHABET_LEN
        result.append(ALPHABET[remainder])
        current_number = (current_number - 1) // ALPHABET_LEN

    result.reverse()
    return "".join(result)
