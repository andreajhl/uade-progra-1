from admin.seats import get_coords_seat, get_status_seat, set_busy_seat, get_free_seats
from message.hall import show_hall

def get_consecutive_seats(count_tickets, hall):
  """Obtiene una opcion de butacas disponibles continuas segun el numero de tickets a comprar"""
  pass

def ask_ticket_count(hall):
  """Pide la cantidad de entradas, valida que sea número > 0 y no supere las libres."""

  while True:
    free_total = get_free_seats(hall)

    if free_total == 0:
      print("No hay butacas disponibles.")
      return 0

    count = int(input(f'Ingrese el número de entradas a comprar (disponibles: {free_total}): '))
    if count < 1:
      print("La cantidad debe ser mayor que 0.")
      continue
    if count > free_total:
      print(f"No hay suficientes butacas libres. Disponibles: {free_total}.")
      continue

    return count

def choose_valid_seat(hall):
  """Pide una butaca hasta que sea válida (libre). Devuelve (i, j)"""
  while True:
    show_hall(hall)

    i, j = get_coords_seat(hall)
    row_label, col_label = i + 1, j + 1

    status = get_status_seat(hall[i][j])

    if status is None:
      print(f"La butaca F{row_label}-C{col_label} está inhabilitada.")
      continue
    if status is False:
      print(f"La butaca F{row_label}-C{col_label} está ocupada.")
      continue

    return i, j

def buy_tickets(hall):
  """Flujo principal: pide cantidad y repite selección hasta completar compras."""
  count = ask_ticket_count(hall)

  if count == 0: return

  purchased = 0

  while purchased < count:
    i, j = choose_valid_seat(hall)
    set_busy_seat(i, j, hall)

    print(f"Seleccionaste la butaca F{i+1}-C{j+1}.")
  
    purchased += 1

  print(f"Compra finalizada. Entradas adquiridas: {purchased}.")
  show_hall(hall)