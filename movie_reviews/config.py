class CONFIG:
    class GENERIC:
        SUCCESS = 0
        FAILURE = 1

    class DB:
        OBJECT_NOT_FOUND = 1
        MULTIPLE_OBJECTS_EXIST = 2
        FAILURE = 3
        INVALID_OPERATION_REQUESTED = 4

    class USER_MOVIE:
        class MISSING:
            USER_ID = "User Id is missing"
            MOVIE_ID = "Movie Id is missing"

    class MOVIE:
        class MISSING:
            URL = "Url is missing"
        class IMDB:
            URL = "http://www.imdb.com"