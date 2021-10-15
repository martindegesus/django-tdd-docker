from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializers import MovieSerializer

class MovieViewset(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
