from rest_framework import serializers
from movie_reviews.movies.models import Movie
from movie_reviews.movies.model_managers.movie import MovieManager
from bs4 import BeautifulSoup
import requests
from movie_reviews.config import CONFIG


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ("id",)

    def scrape_data(self, url):

        try:
            r = requests.get(url)
        except requests.exceptions.RequestException:
            print(f"Error while calling the given URL: {url}")
            return CONFIG.GENERIC.FAILURE

        content = r.content
        soup = BeautifulSoup(content, features="html.parser")

        movie_objects = []
        count = 0
        tableName = soup.find("tbody", attrs={"class": "lister-list"})
        for r in tableName.findAll("tr"):

            col1 = r.find("td", attrs={"class": "titleColumn"})

            link = col1.a["href"]
            # print(link)

            r1 = requests.get(CONFIG.MOVIE.IMDB.URL + link)
            content1 = r1.content
            soup1 = BeautifulSoup(content1, features="html.parser")

            title_wrapper = soup1.find("div", attrs={"class": "title_wrapper"})
            try:
                title_wrapper = " ".join(title_wrapper.text.split())
                title = ""
                for ch in title_wrapper:
                    title += ch
                    if ch == ")":
                        break
            except:
                title = None

            subtext = soup1.find("div", attrs={"class": "subtext"})
            try:
                subtext = " ".join(subtext.text.split())
                subtext = subtext.split("|")
                if len(subtext) > 3:
                    running_time = subtext[1]
                    genre = subtext[2]
                    release_date = subtext[3]
                else:
                    running_time = subtext[0]
                    genre = subtext[1]
                    release_date = subtext[2]
            except:
                running_time = genre = release_date = None

            rating = soup1.find("span", attrs={"itemprop": "ratingValue"})
            try:
                rating = " ".join(rating.text.split())
            except:
                rating = None

            summary = soup1.find("div", attrs={"class": "summary_text"})
            try:
                desc = " ".join(summary.text.split())
            except:
                desc = None

            print(f"title: {title}")
            print(f"running_time: {running_time}")
            print(f"genre: {genre}")
            print(f"release date: {release_date}")
            print(f"rating: {rating}")
            print(f"Description: {desc}")
            print("\n \n --------------------- \n \n")
            movie_objects.append(
                Movie(
                    title=title,
                    rating=rating,
                    running_time=running_time,
                    genre=genre,
                    description=desc,
                    release_date=release_date,
                )
            )
            # count += 1
            # if count > 10:
            #     break

        # Can use Redis if the data size is high
        existing_titles = MovieManager.fetch_all_titles()
        existing_titles_dict = dict()
        for title in existing_titles:
            existing_titles_dict[title] = True  # Can even further optimize by mapping all the details 
                                                # and matching their values to decide the update call 
                                                # but will be costly as data grows

        update_object_list = []
        create_object_list = []
        for movie_object in movie_objects:
            if existing_titles_dict.get(movie_object.title):
                update_object_list.append(movie_object)
            else:
                create_object_list.append(movie_object)

        response = MovieManager.update_objects(update_object_list)
        print(f"Response from update serilalizer: {response}")

        if response == CONFIG.GENERIC.SUCCESS:
            response = MovieManager.bulk_create(create_object_list)
            print(f"Response from update serilalizer: {response}")
    
        return response


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "rating", "release_date", "created_at", "updated_at"]
        read_only_fields = ("id",)
