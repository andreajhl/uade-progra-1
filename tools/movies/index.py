from constants.index import (CATEGORY_PATH, CLASSIFICATION_PATH, DEFAULT_CATEGORY, DEFAULT_CLASSIFICATION)
from tools.json.index import (read_json)
import re
from custom_types import Movie, MoviesDatabase, MovieCategory, AgeClassification, CinemaHall


def create_empty_movies_database() -> MoviesDatabase:
    """Crea una base de datos de películas vacía."""
    return {}


def generate_movie_id(title: str, movie_number: int) -> str:
    """Genera ID único de película basado en título y número."""
    normalized = re.sub(r'[^a-zA-Z0-9]', '_', title.lower())
    normalized = re.sub(r'_+', '_', normalized).strip('_')
    
    if not normalized:
        normalized = "pelicula"
    return f"mov_{movie_number:03d}_{normalized}"


def create_movie(
    title: str,
    hall: CinemaHall,
    category: MovieCategory = "A",
    classification: AgeClassification = "ATP",
    schedule: str = "01/01/2025"
) -> Movie:
    """Crea diccionario de película."""
    return {
        "title": title,
        "hall": hall,
        "category": category,
        "classification": classification,
        "schedule": schedule
    }


def add_movie_to_database(
    movies_db: MoviesDatabase,
    title: str,
    hall: CinemaHall,
    category: MovieCategory = "A",
    classification: AgeClassification = "ATP",
    schedule: str = "01/01/2025"
) -> tuple[MoviesDatabase, str]:
    """Agrega nueva película a la base de datos."""
    movie_number = len(movies_db) + 1
    movie_id = generate_movie_id(title, movie_number)
    
    base_id = movie_id
    counter = 1
    while movie_id in movies_db:
        movie_id = f"{base_id}_{counter}"
        counter += 1
    movie = create_movie(title, hall, category, classification, schedule)
    movies_db[movie_id] = movie
    
    return movies_db, movie_id


def remove_movie_from_database(movies_db: MoviesDatabase, movie_id: str) -> MoviesDatabase:
    """
    Removes a movie from the database.
    
    Args:
        movies_db: Movies database
        movie_id: ID of movie to remove
        
    Returns:
        Updated movies database
    """
    if movie_id in movies_db:
        del movies_db[movie_id]
    return movies_db


delete_movie = remove_movie_from_database


def get_movie_by_id(movies_db: MoviesDatabase, movie_id: str) -> Movie | None:
    """
    Gets a movie by its ID.
    
    Args:
        movies_db: Movies database
        movie_id: Movie ID
        
    Returns:
        Movie dictionary or None if not found
    """
    return movies_db.get(movie_id)


def get_movies_count(movies_db: MoviesDatabase) -> int:
    """
    Gets the total number of movies in the database.
    
    Args:
        movies_db: Movies database
        
    Returns:
        Number of movies
    """
    return len(movies_db)


def get_all_movie_ids(movies_db: MoviesDatabase) -> list[str]:
    """
    Gets a list of all movie IDs.
    
    Args:
        movies_db: Movies database
        
    Returns:
        List of movie IDs
    """
    return list(movies_db.keys())


def get_movies_by_category(movies_db: MoviesDatabase, category: MovieCategory) -> dict[str, Movie]:
    """
    Gets all movies of a specific category.
    
    Args:
        movies_db: Movies database
        category: Category to filter by
        
    Returns:
        Dictionary of movies with the specified category
    """
    return {
        movie_id: movie for movie_id, movie in movies_db.items()
        if movie["category"] == category
    }


def get_movies_by_classification(movies_db: MoviesDatabase, classification: AgeClassification) -> dict[str, Movie]:
    """
    Gets all movies of a specific age classification.
    
    Args:
        movies_db: Movies database
        classification: Classification to filter by
        
    Returns:
        Dictionary of movies with the specified classification
    """
    return {
        movie_id: movie for movie_id, movie in movies_db.items()
        if movie["classification"] == classification
    }


def update_movie_field(movies_db: MoviesDatabase, movie_id: str, field: str, value) -> bool:
    """
    Updates a specific field of a movie.
    
    Args:
        movies_db: Movies database
        movie_id: Movie ID
        field: Field name to update
        value: New value
        
    Returns:
        True if update successful, False otherwise
    """
    if movie_id not in movies_db:
        return False
    
    if field in movies_db[movie_id]:
        movies_db[movie_id][field] = value
        return True
    
    return False


def validate_movie_data(
    title: str,
    category: MovieCategory,
    classification: AgeClassification,
    schedule: str
) -> tuple[bool, str]:
    """
    Validates movie data before creation.
    
    Args:
        title: Movie title
        category: Movie category
        classification: Age classification
        schedule: Schedule string
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not title or not title.strip():
        return False, "El título no puede estar vacío"
    
    if category not in ["A", "B", "C", "D"]:
        return False, "Categoría inválida. Debe ser A, B, C o D"
    
    if classification not in ["ATP", "+13", "+16", "+18"]:
        return False, "Clasificación inválida. Debe ser ATP, +13, +16 o +18"
    
    if not validate_date_format(schedule):
        return False, "Formato de fecha inválido. Use dd/mm/yyyy"
    
    return True, ""


def validate_date_format(date_str: str) -> bool:
    """
    Validates date format (dd/mm/yyyy).
    
    Args:
        date_str: Date string to validate
        
    Returns:
        True if valid, False otherwise
    """
    try:
        parts = date_str.split('/')
        if len(parts) != 3:
            return False
        
        day, month, year = map(int, parts)
        
        if not (1 <= day <= 31):
            return False
        if not (1 <= month <= 12):
            return False
        if not (1900 <= year <= 2100):
            return False
        
        return True
    except (ValueError, AttributeError):
        return False


def search_movies_by_name(movies_db: MoviesDatabase, search_term: str) -> list[tuple[str, Movie]]:
    """
    Searches movies by name (partial match, case insensitive).
    
    Args:
        movies_db: Movies database
        search_term: Term to search for in movie titles
        
    Returns:
        List of tuples (movie_id, movie) matching the search term
    """
    results = []
    search_term_lower = search_term.lower()
    
    for movie_id, movie in movies_db.items():
        if search_term_lower in movie["title"].lower():
            results.append((movie_id, movie))
    
    return results


def search_movies_by_category(movies_db: MoviesDatabase, category: MovieCategory) -> list[tuple[str, Movie]]:
    """
    Searches movies by category.
    
    Args:
        movies_db: Movies database
        category: Category to search for
        
    Returns:
        List of tuples (movie_id, movie) matching the category
    """
    results = []
    
    for movie_id, movie in movies_db.items():
        if movie["category"] == category:
            results.append((movie_id, movie))
    
    return results


def get_all_movies_list(movies_db: MoviesDatabase) -> list[tuple[str, Movie]]:
    """
    Gets all movies as a list of tuples.
    
    Args:
        movies_db: Movies database
        
    Returns:
        List of tuples (movie_id, movie) for all movies
    """
    return list(movies_db.items())

def get_category():
    category = read_json(CATEGORY_PATH)[0]
    if not category:
        return DEFAULT_CATEGORY
    else:
        return category

def get_classification():
    classification = read_json(CLASSIFICATION_PATH)[0]
    if not classification:
        return DEFAULT_CLASSIFICATION
    else:
        return classification    
