from django.contrib import admin
from movie_reviews.movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
