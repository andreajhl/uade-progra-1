def count_free_seats(hall):
  """Retorna la cantidad de butacas libres."""
  
  free_total = 0
  for row in hall:
    for seat in row:
      if seat == 0: free_total += 1
  return free_total