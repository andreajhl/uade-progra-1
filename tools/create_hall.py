
def create_halls(rows:int, columns:int)->list[list]:
  """Crea la sala de cine"""
  
  seats = []

  for _ in range(rows): seats.append([0] * columns)

  return seats