from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=255, unique=True)
    rating = models.FloatField(null=True)
    running_time = models.CharField(max_length=255, null=True)
    genre = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    release_date = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "movie"

    def __str__(self):
        return self.title
