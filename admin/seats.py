from message.hall import show_hall

def set_seats_empty(rows, columns):
  """Crea la sala de cine"""
  seats = []

  for _ in range(rows): seats.append([0] * columns)

  return seats

def set_busy_seat(row, col, hall): hall[row][col] = 'X'

def get_coords_seat(hall):
  """Retorna las coordenadas de una butaca"""
  total_rows = len(hall)
  total_cols = len(hall[0])
  
  show_hall(hall)

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
  
def get_free_seats(hall):
  """Retorna la cantidad de butacas libres."""
  
  free_total = 0
  for row in hall:
    for seat in row:
      if seat == 0: free_total += 1
  return free_total
  
"""None (inhabilitada), False (ocupada), True (libre)"""
get_status_seat = lambda seat: None if seat == ' ' else (False if seat == 'X' else True)
  
