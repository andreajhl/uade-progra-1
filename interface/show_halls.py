from constants.index import SEAT_ICON, BUSY_SEAT_ICON
from tools.seats.index import count_seats, maximum_consecutive_in_matrix


def show_halls(all_halls, all_films_names):
    print(
        """Catalogo:

Sala \t Pelicula \t Espacios \t Espacios consecutivos maximos"""
    )

    halls_indexes = range(all_films_names.__len__())
    for hall_index in halls_indexes:
        total_free_seats = count_seats(all_halls[hall_index])
        total_number_of_available_seats = count_seats(
            all_halls[hall_index], lambda seat: seat in [SEAT_ICON, BUSY_SEAT_ICON]
        )
        print(
            f"{hall_index+1} \t {all_films_names[hall_index]} \t {total_free_seats}/{total_number_of_available_seats} \t {maximum_consecutive_in_matrix(all_halls[hall_index], SEAT_ICON)}"
        )
    print()
