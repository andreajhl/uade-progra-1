from string import ascii_uppercase as ALPHABET

ALPHABET_LEN = ALPHABET.__len__()


def letters_into_numbers(letters: str) -> int:
    """
    Convierte un número entero no negativo a su correspondiente en letras,
    siguiendo la notación de las columnas de Excel (ej: 0=A, 25=Z, 26=AA, 27=AB).
    """

    result = 0

    for letter_number in range(1, letters.__len__() + 1):
        letter = letters[-letter_number]
        result += (ALPHABET.index(letter) + 1) * (26 ** (letter_number - 1))

    return result - 1

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

def calculate_width(hall: list[list]):
    """Devuelve (ancho_butaca, ancho_etiqueta_fila, ancho_total_linea)."""
    PADDING = 2

    rows = len(hall)
    columns = len(hall[0])

    width_seat = len(str(columns)) + PADDING
    width_row = len(str(rows))
    width_total = (width_seat + 3) + columns * (width_seat + 1)

    return width_seat, width_row, width_total
