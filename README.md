# System Requirements
python3.7 or higher


# Development setup (for Ubuntu):
# Open Terminal :

Ctrl + Alt + T

sudo apt-get install python-pip

# Clone Project to your directory
git clone https://github.com/achugh95/movie-review.git

cd movie-review

# Check python version on your development system
python --version or python3 --version


# Setup environment:
# create an environment 
python3 -m venv <path>

# Activate virtual environment: 
source <path_to_virtual_environment>/bin/activate

# Install requirements. Use the package manager pip to install the dependencies. 
pip install -r requirements.txt


# Run migrations

python manage.py makemigrations

python manage.py migrate

# Run Project
Open terminal and run the following commands:

python3 manage.py runserver
