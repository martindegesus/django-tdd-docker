import json
import pytest

from movies.models import Movie

@pytest.mark.django_db
def test_add_movie(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    res = client.post("/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": 1998,
        },
        content_type="application/json"
    )
    assert res.status_code == 201
    assert res.data['title'] == 'The Big Lebowski'

    movies = Movie.objects.all()
    assert len(movies) == 1

@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    res = client.post('/api/movies/',
        {},
        content_type='application/json'
    )
    assert res.status_code ==400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    res = client.post('/api/movies/',
        {
            "title": "Borat",
            "genre": "Comedy"
        },
        content_type='application/json'
    )
    assert res.status_code ==400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_get_single_movie(client, add_movie):
    movie = add_movie(
        title="The Big Lebowski",
        genre="Comedy",
        year="1998"
    )
    res = client.get(f"/api/movies/{movie.id}/")
    assert res.status_code == 200
    assert res.data['title'] == "The Big Lebowski"

@pytest.mark.django_db
def test_get_single_movie_incorrect_id(client):
    res = client.get(f"/api/movies/foo/")
    assert res.status_code == 404

@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    movie_one = add_movie(
        title='The Big Lebowski', genre='comedy', year='1998')
    movie_two = add_movie(
        'No Country for Old Men', 'thriller', '2007')
    res = client.get(f'/api/movies/')
    assert res.status_code == 200
    assert res.data[0]['title'] == movie_one.title
    assert res.data[1]['title'] == movie_two.title