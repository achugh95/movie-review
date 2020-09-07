from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views as AuthTokenViews
from movie_reviews.users.views import SignUp, Logout, UserMovieViewSet

router = routers.SimpleRouter()
urlpatterns = [
    path("sign-up/", SignUp.as_view(), name="sign_up"),
    path("login/", AuthTokenViews.ObtainAuthToken.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]


router.register(r"personal", UserMovieViewSet, basename="personal")

urlpatterns += router.urls
