import os, pytest

from django.conf import settings

from movies.models import Movie


DEFAULT_ENGINE = "django.db.backends.postgresql_psycopg2"


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": os.environ.get("DB_TEST_ENGINE", DEFAULT_ENGINE),
        "HOST": os.environ["DB_TEST_HOST"],
        "NAME": os.environ["DB_TEST_NAME"],
        "PORT": os.environ["DB_TEST_PORT"],
        "USER": os.environ["DB_TEST_USER"],
        "PASSWORD": os.environ["DB_TEST_PASSWORD"],
    }

@pytest.fixture(scope='function')
def add_movie():
    def _add_movie(title, genre, year):
        movie = Movie.objects.create(
            title=title,
            genre=genre,
            year=year
        )
        return movie
    return _add_movie