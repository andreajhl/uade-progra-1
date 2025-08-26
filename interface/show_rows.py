def show_rows(hall:list[list], width_seat:int, width_row:int):
  rows = len(hall)
  columns = len(hall[0])

  for f in range(rows):
    print(f"Fila{f+1:>{width_row}}:", end="  ")
    for c in range(columns):print(f"{hall[f][c]:>{width_seat + 2}}", end=" ")
    print()
