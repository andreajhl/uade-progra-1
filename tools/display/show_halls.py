from constants.index import SEAT_ICON, BUSY_SEAT_ICON
from custom_types import MoviesDatabase
from tools.seats.index import count_seats, maximum_consecutive_in_matrix
from tools.movies.movie_utils import get_all_movie_ids, get_movie_by_id


def show_halls(movies_db: MoviesDatabase):
    """Display catalog of all movies and their hall information."""
    print(
        """Catalogo:

Sala \t Pelicula \t Espacios \t Espacios consecutivos maximos"""
    )

    movie_ids = get_all_movie_ids(movies_db)
    for hall_index, movie_id in enumerate(movie_ids):
        movie = get_movie_by_id(movies_db, movie_id)
        if movie:
            hall = movie["hall"]
            film_name = movie["title"]
            
            total_free_seats = count_seats(hall)
            total_number_of_available_seats = count_seats(
                hall, lambda seat: seat in [SEAT_ICON, BUSY_SEAT_ICON]
            )
            print(
                f"{hall_index+1} \t {film_name} \t {total_free_seats}/{total_number_of_available_seats} \t {maximum_consecutive_in_matrix(hall, SEAT_ICON)}"
            )
    print()
