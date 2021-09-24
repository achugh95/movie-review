# Use-case:

For a movie rating app, create a django rest api using django rest framework. The app needs to have the following capabilities:
- users should be able to sign up and login, use token authentication.
- to list movies.
- logged in users can save movies to a watchlist or mark them watched.  
- logged in users can view a list of movies in their watchlist or watched list.
- take care of permissions - users cannot delete a movie, view other users’ watched list etc

Build the corresponding rest APIs.

To populate the movies in your database, create a scraper to scrape IMDb’s top list (https://www.imdb.com/chart/top/). The scrapper should follow each movie’s url and extract details from the movie’s page. The details you want to save are up to you. The more the better.
This scraper should ideally be triggered by an endpoint in your django api and accept any similar url e.g. https://www.imdb.com/india/top-rated-indian-movies.
Already existing movies should be only updated. Not replaced/duplicated.


# System Requirements
python3.7 or higher


# Development setup (for Ubuntu):

## Open Terminal :

Ctrl + Alt + T

`sudo apt-get install python-pip`

## Clone Project to your directory

`git clone https://github.com/achugh95/movie-review.git`

`cd movie-review`

## Check python version on your development system

`python --version or python3 --version`


# Setup environment:

## Create an environment 
`python3 -m venv <path>`

## Activate virtual environment: 
`source <path_to_virtual_environment>/bin/activate`

## Install requirements. Use the package manager(pip) to install the dependencies. 
`pip install -r requirements.txt`


## Run migrations

`python manage.py makemigrations`

`python manage.py migrate`

## Run Project

Open terminal and run the following commands:

`python3 manage.py runserver`
