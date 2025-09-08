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
