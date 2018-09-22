import media
import fresh_tomatoes

def main():
    """Initializes movie objects with attributes like title, storyline, poster image, youtube trailer URL and release year."""

    interstellar = media.Movie("Interstellar",
    "In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life.",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
    "https://www.youtube.com/watch?v=3WzHXI5HizQ",
    "2014")

    kung_fu_panda = media.Movie("Kung Fu Panda",
    "When an obese Po the Panda, a kung fu enthusiast, gets selected as the Dragon Warrior, he decides to team up with the Furious Five and destroy the evil forces that threaten the Valley of Peace.",
    "https://m.media-amazon.com/images/M/MV5BODJkZTZhMWItMDI3Yy00ZWZlLTk4NjQtOTI1ZjU5NjBjZTVjXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_QL50_SY1000_CR0,0,689,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=PXi3Mv6KMzY",
    "2008")

    fast_five = media.Movie("Fast Five",
    "Dom and Brian travel from one country to another trying to throw the authorities off their scent. Now they have to bring their team together one more time while being chased by a federal agent.",
    "https://m.media-amazon.com/images/M/MV5BMTUxNTk5MTE0OF5BMl5BanBnXkFtZTcwMjA2NzY3NA@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=OqjeOYeG5_A",
    "2011")

    the_avengers = media.Movie("The Avengers",
    "S.H.I.E.L.D. leader Nick Fury is compelled to launch the Avengers Initiative when Loki poses a threat to planet Earth. His squad of superheroes put their minds together to accomplish the task.",
    "https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8",
    "2012")

    whiplash = media.Movie("Whiplash",
    "Andrew enrols in a music conservatory to become a drummer. But he is mentored by Terence Fletcher, whose unconventional training methods push him beyond the boundaries of reason and sensibility.",
    "https://m.media-amazon.com/images/M/MV5BOTA5NDZlZGUtMjAxOS00YTRkLTkwYmMtYWQ0NWEwZDZiNjEzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_QL50_SX675_CR0,0,675,999_AL_.jpg",
    "https://www.youtube.com/watch?v=zIP_gtjDtfE",
    "2014")

    the_matrix = media.Movie("The Matrix",
    "Thomas Anderson, a computer programmer, is led to fight an underground war against powerful computers who have constructed his entire reality with a system called the Matrix.",
    "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_QL50_SY1000_CR0,0,665,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8",
    "1999")

    la_la_land = media.Movie("La La Land",
    "Sebastian (Ryan Gosling) and Mia (Emma Stone) are drawn together by their common desire to do what they love. But as success mounts they are faced with decisions that begin to fray the fragile fabric of their love affair, and the dreams they worked so hard to maintain in each other threaten to rip them apart.",
    "https://m.media-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_QL50_SY1000_SX675_AL_.jpg",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8",
    "2016")

    the_dark_knight = media.Movie("The Dark Knight",
    "After Gordon, Dent and Batman begin an assault on Gotham's organised crime, the mobs hire the Joker, a psychopathic criminal mastermind, who wants to bring all the heroes down to his level.",
    "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY",
    "2008")

    the_imitation_game = media.Movie("The Imitation Game",
    "British mathematician Alan Turing joins the cryptography team to help decrypt the Enigma code, but builds his own machine that is a prototype of the modern computer to decipher German codes.",
    "https://m.media-amazon.com/images/M/MV5BOTgwMzFiMWYtZDhlNS00ODNkLWJiODAtZDVhNzgyNzJhYjQ4L2ltYWdlXkEyXkFqcGdeQXVyNzEzOTYxNTQ@._V1_QL50_SY999_CR0,0,670,999_AL_.jpg",
    "https://www.youtube.com/watch?v=nuPZUUED5uk",
    "2014")

    movies = [interstellar, kung_fu_panda, fast_five, the_avengers, whiplash, the_matrix, la_la_land, the_dark_knight, the_imitation_game]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
