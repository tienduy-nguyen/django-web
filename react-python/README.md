# REACT & Django REST API

Project fullstack: LEAD MANAGER

[Video Tutorial](https://www.youtube.com/watch?v=Uyei2iDA4Hs&list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60)


## Tutorials doc

- [Django REST framework](https://www.django-rest-framework.org/)
- [Turorial Django with REACT](https://www.valentinog.com/blog/drf/#Django_REST_with_React_Django_and_React_together)
- [Tutorial Django with REACT #b](http://v1k45.com/blog/modern-django-part-1-setting-up-django-and-react/)
- [Original repository](https://github.com/bradtraversy/lead_manager_react_django)

## Installation

- Make sure `python3` installed on your machine
- Create `pipenv` file to create an enviroment virtual for project
  ```
  $ pip3 install pipenv
  $ pipenv shell
  ```
- Install django, django rest framework

  ```
  $ pipenv install django djangorestframework django-rest-knox
  ```
- Create project with django-admin
  ```
  $ django-admin startproject leadmanager
  
  ```
- Generate django app
  ```
  $ python3 manage.py startapp leads
  ```
- Add `leads app` and framework to `settings.py` file
  ```python
  # leadmanager/settings.py
  INSTALLED_APPS = [
     '...',
      'leads',
      'rest_framework'
  ]
  ```
- Config database for postgreSQL
    ```python
  # leadmanager/settings.py
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': env('DATABASE_NAME'),
          'USER': env('DATABASE_USER'),
          'PASSWORD': env('DATABASE_PWD'),
          'HOST': env('DATABASE_HOST'),
          'PORT': env('DATABASE_PORT')
      }
  }
  ```
- Tips: how to use `dotenv` in django app

  - Install django-environ, check[Official doc](https://django-environ.readthedocs.io/en/latest/)

    ```bash
    $ pip3 install django-environ
    ```
  - Config in `settings.py` file
    ```python
    # settings.py file example
    import environ
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )
    # reading .env file
    environ.Env.read_env()

    # False if not in os.environ
    DEBUG = env('DEBUG')

    # Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
    SECRET_KEY = env('SECRET_KEY')

    # Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
    DATABASES = {
        # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
        'default': env.db(),
        # read os.environ['SQLITE_URL']
        'extra': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db')
    }

    CACHES = {
        # read os.environ['CACHE_URL'] and raises ImproperlyConfigured exception if not found
        'default': env.cache(),
        # read os.environ['REDIS_URL']
        'redis': env.cache('REDIS_URL')
    }
    ```
  - And create `.env` file and add your secrets key. Don't forget add .env in your `.gitignore`

    ```
    # .env file
    DEBUG=on
    SECRET_KEY=your-secret-key
    DATABASE_URL=psql://urser:un-githubbedpassword@127.0.0.1:8458/database
    SQLITE_URL=sqlite:///my-local-sqlite.db
    CACHE_URL=memcache://127.0.0.1:11211,127.0.0.1:11212,127.0.0.1:11213
    REDIS_URL=rediscache://127.0.0.1:6379/1?client_class=django_redis.client.DefaultClient&password=ungithubbed-secret
    ```
## Config leads App

### Create leads models
