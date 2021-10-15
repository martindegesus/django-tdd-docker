from django.urls import path
from django.urls.resolvers import URLPattern

from .views import MovieViewset

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/movies', MovieViewset)

urlpatterns = router.urls