from vars import DISABLED_SEAT_ICON

def disable_seats(hall:list[list], row:int, column:int):
    """Marca una butaca como deshabilitada."""

    row_label, col_label = row + 1, column + 1

    hall[row][column] = DISABLED_SEAT_ICON
    print(f"Butaca F{row_label}-C{col_label} inhabilitada correctamente.")