
# Great Chat | Django Chat Project with Tortoise ORM (SQlite ver)

This project is implementation for the following topics related to technologies used with Django

-Implemented Complete Auth Using Django Default Auth Model.
    
1. Used built in Django Auth Model
2. Implemented custom error View for customizing Templates
3. Login. SingUp, Logout, Account Views Implemented
4. In built views of PasswordChangeDoneView, PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView
5. Build Custom Templates for These Inbuilt Views

-Implemented Chat App using Django Channels/Redis/Tortoise ORM

1. build custom chat groups
2. as soon as a user register in the app, a signal is fired to create a room with every user
3. Room is just a Django Group with two users
4. Used simple Javascript/Django Channels/Redis to connect to Django Channels and perform these asynchronous chatting system
5. Connected Tortoise ORM with a SQlite Database for asynchronous data
6. User can delete their messages.
7. Used Postgres for Django Models

Similarly, we can build Chat Groups

-Deployed on Heroku

1. Used Heroku Postgres 
2. Used Daphene

-Containerized using Docker

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://www.javascript.com/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/docs/)
[![SQlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/docs.html)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/)
[![Heroku](https://img.shields.io/badge/-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/)
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/)

## Demo

Available at: http://django-chat-app-version1.herokuapp.com/

Note: Remmber to access this project at http because websockets are not configured to run over https in this project yet. 

admin login details:--
username: admin
password: showmecode
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation

Installing Pre requisites
```bash
  pip install -r requirements.txt
```

Create .env File
```bash
  add variables mentioned in .env.example
```

Making Migrations and Migrating them.
```bash
  python manage.py makemigrations
  python manage.py migrate
```

Creating Super User
```bash
  python manage.py createsuperuser
```
Note: if you try to access chat room with just one user it will be throwing error.So after creating a superuser
register from a new user using website and then enter into it. It must have at least two users to chat.

-------------------------

Installing Redis On Local (For ubuntu) for other Os Please refer to their website https://redis.io/
```bash
  curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
  echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
  sudo apt-get update
  sudo apt-get install redis
  sudo systemctl restart redis.service
```
to check if its running or not
```
  sudo systemctl status redis
```
--------------------------

Uncomment Channel Layers Setting for Local Machine on settings.py, line 137 to 144 
```bash
   CHANNEL_LAYERS = {
     'default': {
         'BACKEND': 'channels_redis.core.RedisChannelLayer',
         'CONFIG': {
             "hosts": [('127.0.0.1', 6379)],
         },
     },
   }
```
Comment Channel Layers Setting for Heroku on settings.py, line 147 to 154 
```bash
   CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [config('REDIS_URL')],
        },
    },
  }
```

Run Server
```bash
  python manage.py runserver
```

## Deployment on Heroku

Installing Heroku Cli from : https://devcenter.heroku.com/articles/heroku-cli
Create your account in Heroku.

Inside your project directory

Login Heroku CLI
```bash
  heroku login

```

Create Heroku App

```bash
  heroku create [app_name]

```

Push Heroku App
```
    git push heroku master
```

Configure Heroku App
```bash
  heroku config:set GITHUB_USERNAME=joesmith

```
Configuring Django App for Heroku

Install whitenoise 
```
pip install whitenoise 
```

Include it in Middlewares.
```
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```

Create Procfile and include this code snippet in it.
```
release: python manage.py migrate
web: daphne djangochatapplication.asgi:application --port $PORT --bind 0.0.0.0 -v2
```

## Documentation

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://www.javascript.com/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/docs/)
[![SQlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/docs.html)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/)
[![Heroku](https://img.shields.io/badge/-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/)
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

SECRET_KEY=

DEBUG=

DB_HOST=

DB_NAME=

DB_USER=

DB_PASSWORD=

DB_PORT=

EMAIL_USER=

EMAIL_PASS=

ALLOWED_HOSTS=

REDIS_URL=

SECRET_KEY=
