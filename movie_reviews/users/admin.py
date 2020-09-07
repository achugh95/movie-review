from django.contrib import admin
from movie_reviews.users.models import UserMovie

# Register your models here.


@admin.register(UserMovie)
class UserMovieAdmin(admin.ModelAdmin):
    pass
