from vars import SEAT_ICON

def create_halls(rows:int, columns:int)->list[list]:
  """Crea la sala de cine"""
  
  seats = []

  for _ in range(rows): seats.append([SEAT_ICON] * columns)

  return seats