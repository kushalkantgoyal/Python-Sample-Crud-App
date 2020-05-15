# CRUD App
This is a basic CRUD App which uses python with Django.


## Features
```
1) User can list all the cars and its price from the database.
2) User can list a single car and its price.
3) User can update the name and price of the car.
4) User can delete the car from the database.
```
## Installation and Working
```
1) Install python3 and above using the link:
        - https://realpython.com/installing-python/
        
2) Clone the project in a directory. To know how to clone use the link:
        - https://confluence.atlassian.com/bitbucket/clone-a-repository-223217891.html
   Or Download the Zip file of the project.
        
3) Create a virtual environment using the link
        - https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
        
3) Install the requirements from requirements.txt using:
        - pip install -r requirements.txt

NOTE - Please run the following command as well in the terminal:
        - sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev

4) Setup the database settings in settings.py:
        - DATABASES = {
                        'default': {
                            'ENGINE': 'django.db.backends.mysql',
                            'NAME': 'DBNAME',
                            'USER': 'USER',
                            'PASSWORD': 'PASSWORD',
                            'HOST': 'localhost',
                            'PORT': '3306',
                        }
                    }

5) Make the migrations and then migrate:
        - python manage.py makemigrations
        - python manage.py migrate

6) Create a superuser:
        - python manage.py createsuperuser
        
6) Run file main.py:
        - python manage.py runserver
```