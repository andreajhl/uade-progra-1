def disable_seats(hall, row, column):
    """Deshabilita butacas marcándolas con 'X'. Modifica la matriz en el lugar."""

    row_label, col_label = row + 1, column + 1

    hall[row][column] = ' '
    print(f"Butaca F{row_label}-C{col_label} inhabilitada correctamente.")