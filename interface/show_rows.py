def show_rows(sala, width_seat, width_row):
  rows = len(sala)
  columns = len(sala[0])

  for f in range(rows):
    print(f"Fila{f+1:>{width_row}}:", end="  ")
    for c in range(columns):print(f"{sala[f][c]:>{width_seat + 2}}", end=" ")
    print()
