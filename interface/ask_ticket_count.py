from tools.count_free_seats import count_free_seats

def ask_ticket_count(hall):
    """Pide la cantidad de entradas, valida que sea número > 0 y no supere las libres."""

    while True:
        free_total = count_free_seats(hall)

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
