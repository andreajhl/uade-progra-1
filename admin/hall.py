from admin.seats import get_coords_seat, set_seats_empty, get_status_seat

def get_percentage_busy(hall):
  """Obtener porcentage de la sala ocupado"""
  pass

def disable_seats(hall):
  """Deshabilita butacas marcándolas con 'X'. Modifica la matriz en el lugar."""

  option = None

  while option != 2:
    option = int(input("¿Desea inhabilitar alguna butaca? (1=Sí, 2=No): "))

    if option == 2:
      print("Finalizó la inhabilitación de butacas.")
      break
    if option != 1:
      print("Opción inválida. Ingrese 1 o 2.")
      continue

    i, j = get_coords_seat(hall)
    row_label, col_label = i + 1, j + 1

    status = get_status_seat(hall[i][j])

    if status is None:
      print(f"La butaca F{row_label}-C{col_label} ya está inhabilitada.")
      continue
  
    if status is False:
      print(f"No se puede inhabilitar: la butaca F{row_label}-C{col_label} está ocupada.")
      continue

    hall[i][j] = ' '
    print(f"Butaca F{row_label}-C{col_label} inhabilitada correctamente.")

def create_halls():
  """Crea sala de cine"""

  rows = int(input('Ingresa el numero de filas que tendra la sala: '))
  columns = int(input('Ingresa el numero de columnas que tendra la sala: '))

  hall = set_seats_empty(rows, columns)

  disable_seats(hall)

  return hall