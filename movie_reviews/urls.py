from django.contrib import admin
from django.urls import path, include
from movie_reviews.users import urls as user_urls
from movie_reviews.movies import urls as movie_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "v1/",
        include(
            [
                path("users/", include(user_urls.urlpatterns)),
                path("movies/", include(movie_urls.urlpatterns)),
            ]
        ),
    ),
]
