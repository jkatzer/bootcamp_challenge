Alex's Buzzfeed Bootcamp
==============================


## About
This is a single page webapp with the function of an anonymous forum.

## External Credits
First time building out completely single-page frontend and managing front-end with npm and grunt. Attemping best pracices with help from: 
https://lincolnloop.com/blog/simplifying-your-django-frontend-tasks-grunt/

Using some tools taken from / inspired by Fred Diego's Django Heroku Boilerplate:
https://github.com/fidiego/django_heroku_boilerplate/tree/master 

## What's going on?
- Config holds all settings wsgi
- forum_backend holds application logic
- frontend contains all front-end resources including all routing through Angular
- node_moduls contains dependencies

## Setup
1. Setup new virtual environment
2. cd new_env, activate it
3. clone repo, cd repo
4. $ pip install -r requirements.txt
5. $ npm install
6. $ manage.py gruntserver