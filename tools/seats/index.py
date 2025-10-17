from constants.index import DISABLED_SEAT_ICON, BUSY_SEAT_ICON, SEAT_ICON


count_seats = lambda hall, custom_filter=lambda seat: seat == SEAT_ICON: sum(
    1 for row in hall for seat in row if custom_filter(seat)
)
"""Retorna la cantidad de butacas libres."""


def set_seat_status(row: int, col: int, hall: list[list], icon=BUSY_SEAT_ICON):
    """Cambia de estado la butaca del asiento solicitado (fila, columna, icon(estado al que quiero modificar))"""
    hall[row][col] = icon


get_seat_status = lambda seat: (
    None if seat == DISABLED_SEAT_ICON else (False if seat == BUSY_SEAT_ICON else True)
)
"""Devuelve el estado de la butaca indicada (None si desabilitada, False si ocupado, True si libre)"""


def maximum_consecutive_in_matrix(matrix: list[list], element) -> int:
    """Devuelve el numero de veces que se repite consecutivamente el elemento en la matriz (Matriz, Elemento)"""
    count = 0
    result = 0

    for row in matrix:
        for row_element in row:

            if row_element == element:
                count += 1

        if count > result:
            result = count

        count = 0

    return result
