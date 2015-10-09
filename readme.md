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
- frontend contains all front-end resources including most routing through Angular. 
- base template is in forum_backend, partials are stored in frontend.
- tools directory was meant to have multiple components, but currently just stores intregrated grunt django commands
- node_moduls contains dependencies
- using bootstrap grid with Semantic UI components
- In order to keep all dependencies for front-end in npm, I installed semantic UI through it as well... This, however, also installed Gulp and a bunch of other things that don't really seem that necessary within the scope of this project.

## Setup
1. Setup new virtual environment
2. cd new_env, activate it
3. clone repo, cd repo
4. $ pip install -r requirements.txt
5. $ npm install
6. $ manage.py gruntserver