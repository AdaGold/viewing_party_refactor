import pytest
from viewing_party.movie import Movie
from viewing_party.person import Person

def test_create_person():
    person = Person("Xenophon")
    assert person.friends == []
    assert person.watched == []
    assert person.watchlist == []
    assert person.name == "Xenophon"

def test_add_friend_to_empty_person():
    person = Person("Kendall")
    new_friend = Person("Nancy")

    person.add_friend(new_friend)

    assert person.friends == [new_friend]

def test_adding_friend_multiple_times_does_not_create_duplicate_friends():
    person = Person("Kendall")
    new_friend = Person("Nancy")

    person.add_friend(new_friend)
    person.add_friend(new_friend)

    assert person.friends == [new_friend]

def test_adding_different_friends():
    person = Person("Kendall")
    new_friend = Person("Nancy")
    newer_friend = Person("Simon")

    person.add_friend(new_friend)
    person.add_friend(newer_friend)

    assert person.friends == [new_friend, newer_friend]

def test_add_to_watchlist_with_empty_person():
    movie = Movie("Cow", "Documentary", 5)
    person = Person("Auberon")

    person.add_to_watchlist(movie)

    assert person.watchlist == [movie]
    assert person.watched == []

def test_adding_to_watchlist_multiple_times_does_not_create_duplicates():
    movie = Movie("Cow Factory", "Documentary", 5)
    person = Person("Auberon")

    person.add_to_watchlist(movie)
    person.add_to_watchlist(movie)

    assert person.watchlist == [movie]
    assert person.watched == []

def test_watch_movie_not_in_watchlist_gets_added_to_watched():
    movie = Movie("Cow Factory", "Documentary", 5)
    person = Person("Auberon")

    person.watch(movie)

    assert person.watched == [movie]
    assert person.watchlist == []

def test_watching_movie_multiple_times_does_not_create_duplicates():
    movie = Movie("Cow Factory", "Documentary", 5)
    person = Person("Auberon")

    person.watch(movie)
    person.watch(movie)

    assert person.watched == [movie]
    assert person.watchlist == []


def test_watching_movie_removes_movie_from_watchlist():
    cow_factory = Movie("Cow Factory", "Documentary", 5)
    first_cow = Movie("First Cow", "Drama", 5)
    person = Person("Auberon")

    person.add_to_watchlist(cow_factory)
    person.add_to_watchlist(first_cow)
    person.watch(cow_factory)

    assert person.watched == [cow_factory]
    assert person.watchlist == [first_cow]
    
# def test_watch_one_movie_with_empty_person():
#     person = Person()