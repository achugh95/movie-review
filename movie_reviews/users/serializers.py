from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password, check_password
from movie_reviews.users.models import UserMovie
from movie_reviews.users.model_managers.user_movie import UserMovieManager
from movie_reviews.config import CONFIG


class SignupSerializer(serializers.ModelSerializer):

    token = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True, style={"input_type": "passsword"})

    class Meta:
        model = User
        fields = ("id", "username", "password", "token", "password")
        read_only_fields = ("id",)

    def validate(self, data):
        """
        override user serializer to hash password before saving user
        """
        if self.instance:
            return super(SignupSerializer, self).validate(data)
        else:
            user = User(username=data["username"])
            data["password"] = make_password(data["password"])
            return data

    def create(self, validated_data):
        """
        overriding default create to insert token
        """
        instance = super(SignupSerializer, self).create(validated_data)
        instance.set_password(validated_data["password"])
        token = Token.objects.create(user=instance)
        instance.token = token
        return instance


class UserMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovie
        fields = "__all__"

    def get_unique_together_validators(self):
        """
        Overriding method to disable unique together checks
        """
        return []

    def get_user_movie(self, validated_data):

        filters = {
            "user_id": validated_data.get("user"),
            "movie_id": validated_data.get("movie"),
        }
        return UserMovieManager.get_object(filters)

    def add_or_update_movie(self, validated_data):

        obj = self.get_user_movie(validated_data)

        data = {
            "user_id": validated_data.pop("user"),
            "movie_id": validated_data.pop("movie"),
        }
        if validated_data["action"] == "to_watch":
            data["to_watch"] = 1
        elif validated_data["action"] == "is_watched":
            data["is_watched"] = 1

        if obj == CONFIG.DB.OBJECT_NOT_FOUND:
            obj = UserMovieManager.create_object(data)
        elif obj == CONFIG.GENERIC.FAILURE:
            return obj
        obj = UserMovieManager.update_object(obj, data)
        return obj

    def remove_movie(self, validated_data):

        obj = self.get_user_movie(validated_data)
        if obj in [CONFIG.DB.OBJECT_NOT_FOUND, CONFIG.GENERIC.FAILURE]:
            return obj

        data = {
            "user_id": validated_data.pop("user"),
            "movie_id": validated_data.pop("movie"),
        }
        if validated_data["action"] == "to_watch":
            data["to_watch"] = 0
        elif validated_data["action"] == "is_watched":
            data["is_watched"] = 0
        obj = UserMovieManager.update_object(obj, data)
        return obj
