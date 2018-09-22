<<<<<<< HEAD
import webbrowser

class Movie():
    """Class used to create movies instances.

    Attributes:
    title: A string containing name of the movie.
    storyline: A string containing the plot of the movie.
    poster_image_url: A string containing URL of the poster image of the movie.
    trailer_youtube_url: A string containing the URL the of trailer of the movie.
    release_year: A string containing the year of release of the movie.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = release_year

    def show_trailer(self):
        """Opens the web browser and plays the movie trailer."""
        webbrowser.open(self.trailer_youtube_url)
=======
import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = release_year

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
>>>>>>> e2feb0126b9ebb1d6c994d01f500fbeb75ce3331
