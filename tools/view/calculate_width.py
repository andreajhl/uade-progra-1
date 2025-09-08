def calculate_width(hall: list[list]):
    """Devuelve (ancho_butaca, ancho_etiqueta_fila, ancho_total_linea)."""
    PADDING = 2

    rows = len(hall)
    columns = len(hall[0])

    width_seat = len(str(columns)) + PADDING
    width_row = len(str(rows))
    width_total = (width_seat + 3) + columns * (width_seat + 1)

    return width_seat, width_row, width_total
