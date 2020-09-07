from django.db.utils import IntegrityError
from movie_reviews.movies.models import Movie
from movie_reviews.config import CONFIG


class MovieManager:
    @staticmethod
    def create_object(create_data):

        print("Create object function called")
        print(f"Create Data: {create_data}")
        try:
            obj = Movie.objects.create(**create_data)
            return obj
        except Exception as e:
            print(f"Error: {e}")
            return CONFIG.DB.FAILURE

    @staticmethod
    def bulk_create(create_data_list):

        print("Bulk create function called")
        print(f"Create Data List: {create_data_list}")
        try:
            objs = Movie.objects.bulk_create(create_data_list)
            return objs
        except Exception as e:
            print(f"Error: {e}")
            return CONFIG.DB.FAILURE

    @staticmethod
    def update_objects(update_data_list):

        print("Update object function called")
        # print(f"Object: {obj}")
        print(f"Update Data: {update_data_list}")
        create_data_list = []
        try:
            for obj in update_data_list:
                print(f"OBJ: {obj}")
                updated = Movie.objects.filter(title=obj.title).update(
                    rating=obj.rating,
                    running_time=obj.running_time,
                    genre=obj.genre,
                    description=obj.description,
                    release_date=obj.release_date,
                )
                print(f"Updated: {updated}")
                if not updated:
                    create_data_list.append(obj)

            print(f"For loop exited: {create_data_list}")
            return create_data_list
        except Exception as e:
            print(f"Error while updating: {e}")
            return CONFIG.DB.FAILURE
