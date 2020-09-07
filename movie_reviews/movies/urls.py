from django.urls import path
from rest_framework import routers
from movie_reviews.movies.views import MovieViewSet


urlpatterns = [
    path("list/", MovieViewSet.as_view({"get": "list"})),
    path("list/<int:pk>/", MovieViewSet.as_view({"get": "retrieve"})),
    path("fetch/", MovieViewSet.as_view({"post": "post"})),
]
