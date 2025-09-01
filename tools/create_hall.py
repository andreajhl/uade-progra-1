from vars import SEAT_ICON
from custom_types import CinemaHall

def create_halls(rows: int, columns: int) -> CinemaHall:
  """Crea la sala de cine"""
  
  seats = []

  for _ in range(rows): seats.append([SEAT_ICON] * columns)

  return seats