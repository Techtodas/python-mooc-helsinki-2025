# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movies = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }
    database.append(movies)