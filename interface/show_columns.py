def show_columns(columns:int, width_row:int):
    print("Columns", end=" ")
    for c in range(columns): print(f"{c+1:>{width_row + 5}}", end="")
    print()