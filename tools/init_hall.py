from tools.create_hall import create_halls
from tools.disable_seats import disable_seats
from tools.get_seat_status import get_seat_status

from interface.input_coords_seat import input_coords_seat

def init_hall():
  """Crea la sala de cine"""

  # Establecer filas y columnas  
  rows = int(input('Ingresa el numero de filas que tendra la sala: '))
  columns = int(input('Ingresa el numero de columnas que tendra la sala: '))

  hall = create_halls(rows, columns)

  # Deshabilitar butacas
  option = None
  while option != 2:
    option = int(input("¿Desea inhabilitar alguna butaca? (1=Sí, 2=No): "))

    if option == 2:
      print("Finalizó la inhabilitación de butacas.")
      break
    if option != 1:
      print("Opción inválida. Ingrese 1 o 2.")
      continue
    
    row, column = input_coords_seat(hall)
    row_label, col_label = row + 1, column + 1

    seat_status = get_seat_status(hall[row][column])

    if seat_status is None:
      print(f"La butaca F{row_label}-C{col_label} ya está inhabilitada.")
      continue
  
    if seat_status is False:
      print(f"No se puede inhabilitar: la butaca F{row_label}-C{col_label} está ocupada.")
      continue

    disable_seats(hall, row, column)

  return hall