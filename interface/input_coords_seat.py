
def input_coords_seat(hall):
    """Retorna las coordenadas de una butaca"""
    total_rows = len(hall)
    total_cols = len(hall[0])

    while True:
        row = int(input(f"Ingrese la FILA (1-{total_rows}): "))
        if row < 1 or row > total_rows:
            print("Fila fuera de rango.")
            continue

        col = int(input(f"Ingrese la COLUMNA (1-{total_cols}) para la fila {row}: "))
        
        if col < 1 or col > total_cols:
            print("Columna fuera de rango.")
            continue

        return (row - 1, col - 1)
