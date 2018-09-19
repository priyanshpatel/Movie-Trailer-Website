import media
import fresh_tomatoes

interstellar = media.Movie("Interstellar", "In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life.", "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=2LqzF5WauAw")

movies = [interstellar]
fresh_tomatoes.open_movies_page(movies)
