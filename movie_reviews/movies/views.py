from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from movie_reviews.movies.models import Movie
from movie_reviews.movies.serializers import MovieSerializer, MovieListSerializer
from rest_framework.response import Response
from rest_framework import status as rest_status
from movie_reviews.config import CONFIG


class MovieViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Movie.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ("title",)

    def get_serializer_class(self):

        if self.action == "retrieve":
            return MovieSerializer
        elif self.action == "list":
            return MovieListSerializer

    def retrieve(self, request, *args, **kwargs):

        return super(MovieViewSet, self).retrieve(self, request, *args, **kwargs)

    def list(self, request, *args, **kwargs):

        return super(MovieViewSet, self).list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        url = request.data.get("url")
        if not url:
            response = {CONFIG.MOVIE.MISSING.URL}
            return Response(response, status=rest_status.HTTP_400_BAD_REQUEST)

        response = MovieSerializer().scrape_data(url)
        if response == CONFIG.DB.INVALID_OPERATION_REQUESTED:
            return Response(status=rest_status.HTTP_406_NOT_ACCEPTABLE)
        if response == CONFIG.GENERIC.FAILURE:
            return Response(status=rest_status.HTTP_500_INTERNAL_SERVER_ERROR)

        response = MovieSerializer(response, many=True).data
        return Response(response, status=rest_status.HTTP_201_CREATED)
