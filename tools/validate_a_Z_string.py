from string import ascii_lowercase

def validate_a_Z_string(string:str)->bool:
    for letter in string:
        if not(letter.lower() in ascii_lowercase):
            return False
    return True
