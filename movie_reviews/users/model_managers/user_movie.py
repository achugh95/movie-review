from movie_reviews.users.models import UserMovie
from movie_reviews.config import CONFIG


class UserMovieManager:
    @staticmethod
    def get_object(filters):

        print("Get object function called")
        print(f"Filters: {filters}")
        try:
            obj = UserMovie.objects.get(**filters)
            return obj
        except UserMovie.DoesNotExist:
            print("Object does not exist")
            return CONFIG.DB.OBJECT_NOT_FOUND
        except Exception as e:
            print(f"Error: {e}")
            return CONFIG.DB.FAILURE

    @staticmethod
    def update_object(obj, update_data):

        print("Update object function called")
        print(f"Object: {obj}")
        print(f"Update Data: {update_data}")
        try:
            for key, value in update_data.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        except Exception as e:
            print(f"Error while updating: {e}")
            return CONFIG.DB.FAILURE

    @staticmethod
    def create_object(create_data):

        print("Create object function called")
        print(f"Create Data: {create_data}")
        try:
            obj = UserMovie.objects.create(**create_data)
            return obj
        except Exception as e:
            print(f"Error: {e}")
            return CONFIG.DB.FAILURE
