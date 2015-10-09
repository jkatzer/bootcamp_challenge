Alex's Semi-self-inflicted Forum Bootcamp
==============================

## About
This is a single page anonymous-user forum webapp. It was built with Django, Django Rest Framework, AngularJS, Grunt, npm, Bootstrap, and Semantic UI.

## Setup
1. Setup new virtual environment
2. cd new_env, activate it
3. clone repo, cd repo
4. $ pip install -r requirements.txt
5. $ npm install (semantic UI will have a weird prompt. just throw it into node_modules)
6. $ manage.py gruntserver

## Peronsal Assesment
This was a tremendous learning experience for me. The previous projects I've built were built over more time than a week and were less complex. I had never actually used npm (or any package manager), grunt (or any comprehensive task manager), the django rest framework, implemented a real API, or built with a single-page-app-enabling front-end framework (though a few jQuery get calls here and there). In less than one week, I learned and integrated all of them. While I didn't get to implement testing (more on that below), other implementation strategies were based in some best-practices systems I saw across the web, but never copied. And I actually think my grunt tools are kind of nifty (want to expand for custom commands as well)! I'm slightly dissapointed by my speed, but can already see myself executing this kind of project much quicker in the future. Curious for your own thoughts.

## External Credits
I tried to reference sources I directly duplicated code from, however most code -even if once duplicated- has some of it's own originality.
 

## What's going on?
- config holds all settings, wsgi
- forum_backend holds API logic
- frontend contains all front-end resources including most routing through Angular. 
- tools was meant to have multiple components, but currently just stores intregrated grunt django commands
- base template is in forum_backend, partials are stored in frontend.
- node_moduls contains dependencies
- using bootstrap grid with Semantic UI components
- In order to keep all dependencies for front-end in npm, I installed semantic UI through it as well... This, however, also installed Gulp and a bunch of other things that don't really seem that necessary within the scope of this project.

##The To-Do List:
There were several items I wanted to do, but didn't get the chance. Thought they were better noted than not.
- Front-end validation. 
- Pagination
- Make sure "usernames" are in username-appropriate format
- Abstract angular methods for DRYer and more re-usable code
- Better handling of what should be 404's. Really, just handling them.
- Set up for production. Move settings to .env, switch to PostgreSql

###Most importantly, though: tests.
I didn't implement any test, and that is the weakest point in my engineering abilities. I had a lot to learn this week, and learning the syntax, operations, and best practices would've just been too much time. In past roles, I never had testing skills cultivated. But now, I'd like to start doing that on my own.

