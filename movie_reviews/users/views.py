from django.shortcuts import render
from rest_framework import viewsets, mixins, views
from rest_framework.response import Response
from rest_framework import status as rest_status
from movie_reviews.users.serializers import SignupSerializer, UserMovieSerializer
from movie_reviews.users.models import UserMovie
from movie_reviews.config import CONFIG


class SignUp(views.APIView):

    serializer_class = SignupSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = serializer.create(serializer.validated_data)
        if response == 1:
            Response(status=rest_status.HTTP_500_INTERNAL_SERVER_ERROR)
        response = self.serializer_class(response).data
        return Response(response, status=rest_status.HTTP_201_CREATED)


class Logout(views.APIView):
    def delete(self, request):

        request.user.auth_token.delete()
        return Response(status=rest_status.HTTP_204_NO_CONTENT)


class UserMovieViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = UserMovieSerializer

    def get_queryset(self):

        action = self.request.query_params.get("action")
        if action == "to_watch":
            return UserMovie.objects.filter(user__id=self.request.user.id, to_watch=1)
        elif action == "is_watched":
            return UserMovie.objects.filter(user__id=self.request.user.id, is_watched=1)
        return UserMovie.objects.filter(user__id=self.request.user.id)

    def post(self, request, *args, **kwargs):

        request.data["user"] = request.user.id
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = serializer.add_or_update_movie(request.data)
        if response == CONFIG.GENERIC.FAILURE:
            Response(status=rest_status.HTTP_500_INTERNAL_SERVER_ERROR)

        serialized_data = self.serializer_class(response).data
        return Response(serialized_data, status=rest_status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):

        request.data["user"] = request.user.id
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = serializer.remove_movie(request.data)
        if response == CONFIG.DB.OBJECT_NOT_FOUND:
            return Response(status=rest_status.HTTP_404_NOT_FOUND)
        if response == CONFIG.GENERIC.FAILURE:
            return Response(status=rest_status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=rest_status.HTTP_204_NO_CONTENT)
