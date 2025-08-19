def calculate_width(hall):
  """Devuelve (ancho_butaca, ancho_etiqueta_fila, ancho_total_linea)."""
  PADDING = 2

  rows = len(hall)
  columns = len(hall[0])

  width_seat = len(str(columns)) + PADDING  
  width_row = len(str(rows))
  width_total = (width_seat + 3) + columns * (width_seat + 1)

  return width_seat, width_row, width_total

def show_columns(columns, width_row):
  print("Columns", end=" ")
  for c in range(columns): print(f"{c+1:>{width_row + 5}}", end="")
  print()

def show_rows(sala, width_seat, width_row):
  rows = len(sala)
  columns = len(sala[0])

  for f in range(rows):
    print(f"Fila{f+1:>{width_row}}:", end="  ")
    for c in range(columns):print(f"{sala[f][c]:>{width_seat + 2}}", end=" ")
    print()

def show_hall(hall):
  if not hall or not hall[0]:
    print("Sala de Cine (sin butacas)")
    return

  width_seat, width_row, width_total = calculate_width(hall)

  print("Sala de Cine".center(width_total))
  show_columns(len(hall[0]), width_row)
  show_rows(hall, width_seat, width_row)
