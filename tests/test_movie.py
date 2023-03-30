import pytest
from viewing_party.movie import Movie
from viewing_party.person import Person

def test_create_movie():
    movie = Movie("Cow Factory", "Documentary", 5)

    assert movie.title == "Cow Factory"
    assert movie.genre == "Documentary"
    assert movie.rating == 5