# List of useful commands:

## Creating a python virtual environment
#### <i>python3 -m venv venv</i>

## Activating a python venv
#### <i>source venv/bin/activate</i>

## Deactivating a python venv
#### deactivate [Just typing "<b>deactivate</b>" is Ok]

## Creating a django project in our virtual env.
#### <i>pip install django</i>
#### <i>django-admin startproject < projectName >

## Starting Django Server
#### python manage.py runserver < server_ip >:< port >

## Creating an App
#### python manage.py startapp < app_name >

## Saving requirements for later use:
#### pip freeze > requirements.txt

## Database Migrations 

### After making changes in models
#### python manage.py makemigrations [makes a migration file]
#### python manage.py migrate

### Show All Migrations
#### python manage.py showmigrations < app_name >

### Reversing Migrations

#### You can revert by migrating to the previous migration.

#### For example, if your last two migrations are:

### 0010_previous_migration
### 0011_migration_to_revert
#### Then you would do:

### python manage.py migrate my_app 0010_previous_migration 

#### You can then delete migration 0011_migration_to_revert.

#### If you're using Django 1.8+, you can show the names of all the migrations with

### python manage.py showmigrations my_app
#### To reverse all migrations for an app, you can run:

### python manage.py migrate my_app zero


# POSTGRES
## <B>Install</B>: sudo apt-get install postgresql postgresql-contrib
## <B>Installing PostGis </B>: required for geoDjango: sudo apt install postgis 

## <B>Logging into postresql shell(terminal based alternative to pg-admin):</B>
### 1. sudo su postgres
### 2. psql (doesnt connect to a specific db, connects to pgAdmin)
### 3. In order to connect to a specific db: psql -d <database_name> -U  <user_name> -W
##  PSQL Commands: https://www.postgresqltutorial.com/psql-commands/

## Creating a database: First log in to psql with 
### 1. create database epidemap

### DJANGO
## POSTGIS: 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'epidemap',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PASSWORD': 'postgres',
        'PORT': '5432',
    }
}
```

