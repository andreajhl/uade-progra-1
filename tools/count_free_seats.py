from typing import Callable
from vars import SEAT_ICON
from custom_types import CinemaHall

#cambiar nombre a count_seats
def count_free_seats(hall:CinemaHall, custom_filter:Callable = lambda seat: seat == SEAT_ICON):
  """Retorna la cantidad de butacas libres."""
  
  free_total = 0
  for row in hall:
    for seat in row:
      if custom_filter(seat): free_total += 1
  return free_total