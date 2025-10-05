import re
def validate_a_Z_string(string:str):
    patron = r"^[a-zA-Z]+$" 

    if re.match(patron, string):
        return True
    
    return False