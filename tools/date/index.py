from constants.index import CONST_MESES

def leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def split_date(date):
    """Separa componenetes de la fecha"""
    day=int(date[:2])
    if int(date[3])==0:
        month=int(date[4:5])
    else:
        month=int(date[3:5])        
    year=int(date[6:10])

    return(day, month, year)

def valid_day(day,mont_comp, year):
    """Valida que el dia este """
    meses = CONST_MESES.copy()
    
    if leap_year(year):
        meses[2] = 29

    return 1 <= day <= meses[mont_comp]