# Django Movies

## Description

Django movies is an assignment to get an understanding of django with the 
[Movielens](http://grouplens.org/datasets/movielens/) dataset.

## Learning Objectives
* Create a new django project
* Create a new django app
* Create models in django
* Create a migration
* Run database migration

## Details

### Deliverables
* Django project with models and migrations
* Working admin with previously mentioned models

### Requirements
* No pep8 errors
* All packages in the requirements.txt

## Normal Mode
Use the `movielens` data from previous homework as a roadmap for the following:

Create a `movieratings` django project. 

Create a new application in the `movieratings` project

Create Django models to represent the data.  Make sure that the data has the 
appropriate data types.  For simplicity sake you may skip the genre_movies table and skip the many to many relationship between movie and genre.

Make sure each model has 2 additional fields to track the date added and the
date modified.

Create django admin pages for your models.

Use the Django admin to add at least 3 entries into the movies, links, and tags models.  Put all of the genres into the genre model.

## Hard Mode
Using Datagrip export the data from the movielens database from previous homework as a csv file.  It is recommended that this is done one table at a time to save hassle later.  Once the data is exported create a data migration to pull the data from the csv files and import them into the database.

Using the django shell create User objects to represent the user ids in the 
ratings table. `python manage.py shell`

## Nightmare Mode

Create the many to many relationship between the movie and genre models.  Dump the data from the movielens database and import the data into the system using migrations.
