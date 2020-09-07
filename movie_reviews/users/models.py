from django.db import models
from django.contrib.auth.models import User
from movie_reviews.movies.models import Movie


class UserMovie(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    to_watch = models.BooleanField(null=True)
    is_watched = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_movie"
        unique_together = ("user", "movie")

    def __str__(self):
        return str(self.user) + " " + str(self.movie)
