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
  ```bash
  $ pip3 install pipenv
  $ pipenv shell
  ```
- Install django, django rest framework

  ```bash
  $ pipenv install django djangorestframework django-rest-knox
  ```
- Create project with django-admin
  ```
  $ django-admin startproject leadmanager
  
  ```
- Generate django app
  ```bash
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
- Pre-install (in virtual enviroment) to connect with postgresql

  ```bash
  $ pip3 install psycopg2
  $ pip3 install psycopg2-binary
  ```
  or using Pipenv

  ```bash
  $ pipenv install psycopg2 psycopg2-binary
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

## Models in Django

- Check the [official doc](https://docs.djangoproject.com/en/3.1/topics/db/models/)

  ```python
  # persons/models.py file
  from django.db import models

  class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
  ```
- Important for relationship in django
  - One to one: `OneToOneField`
  - Many to one: `ForeignKey`
  - Many to many: `ManyToManyField`
  
  - Example: [OneToOne](https://docs.djangoproject.com/fr/2.2/topics/db/examples/one_to_one/) and  [ManyToOne](https://docs.djangoproject.com/fr/2.2/topics/db/examples/one_to_one/)
  ```python
  from django.db import models

  class Place(models.Model):
      name = models.CharField(max_length=50)
      address = models.CharField(max_length=80)

      def __str__(self):
          return "%s the place" % self.name

  class Restaurant(models.Model):
      place = models.OneToOneField(
          Place,
          on_delete=models.CASCADE,
          primary_key=True,
      )
      serves_hot_dogs = models.BooleanField(default=False)
      serves_pizza = models.BooleanField(default=False)

      def __str__(self):
          return "%s the restaurant" % self.place.name

  class Waiter(models.Model):
      restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
      name = models.CharField(max_length=50)

      def __str__(self):
          return "%s the waiter at %s" % (self.name, self.restaurant)
  ```

  - Example [ManyToMany](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ManyToManyField)

  ```python
  from django.db import models

  class Person(models.Model):
      friends = models.ManyToManyField("self")
  ```

  - Using intermediate models (join table): [ManyToManyField.though](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ManyToManyField)
  ```python
  from django.db import models

  class Person(models.Model):
      name = models.CharField(max_length=50)

  class Group(models.Model):
      name = models.CharField(max_length=128)
      members = models.ManyToManyField(
          Person,
          through='Membership',
          through_fields=('group', 'person'),
      )

  class Membership(models.Model):
      group = models.ForeignKey(Group, on_delete=models.CASCADE)
      person = models.ForeignKey(Person, on_delete=models.CASCADE)
      inviter = models.ForeignKey(
          Person,
          on_delete=models.CASCADE,
          related_name="membership_invites",
      )
      invite_reason = models.CharField(max_length=64)
    ```
- All the field types in django : check [doc](https://docs.djangoproject.com/fr/2.2/topics/db/examples/one_to_one/)

## Create leads models
- In the `leads/models.py`, create `leads models`

  ```python
  class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
  ```
- Make migration
  ```bash
  $ python3 manage.py makemigrations leads
  $ python3 manage.py migrate
  ```
## Serializer with djangorestframework

Read the [Doc](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)

- Create `serializers.py` file in `leads` folder
  ```py
  # leads/serializers.py
  from rest_framework import serializers
  from leads.models import Lead

  # Lead serializers
  class LeadSerializer(serializers.ModelSerializer):
    class Meta:
      model  = Lead
      fields = '__all__'
  ```
- Create `api.py` file in `leads` folder
  ```py
  from leads.models import Lead
  from rest_framework import viewsets, permissions
  from .serializers import LeadSerializer

  # Lead Viewset
  class LeadViewSet(viewsets.ModelViewSet):
    """
      A viewset for viewing and editing lead instances.
    """
    queryset = Lead.objects.all()
    permission_classes = [
      permissions.AlowAny
    ]
    serializer_class = LeadSerializer

  ```  

  Read more about [Viewset](https://www.django-rest-framework.org/api-guide/viewsets/)

- Create a `urls.py` in `leads` folder

  Edit `leadmanager/urls.py` file
  ```py
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
    path('', include('leads.urls')), # home page
  ]
  ```
- Edit `leads/urls.py`

  Import `routers` from rest_framework
  ```py
  from rest_framework import routers
  from .api import LeadViewSet

  router = routers.DefaultRouter()
  router.register('api/leads', LeadViewSet, 'leads')

  urlpatterns = router.urls
  ```
- Run server
  ```bash
  $ python3 manage.py runserver

  ```
  Using postman to check the data.

  Now we can have automatically the routes : GET, POST, DELETE
  ```
  GET http://localhost:8000/leads
  POST http://localhost:8000/leads/
  DELETE http://localhost:8000/:id/
  ```

### Check how to use REACT With Python [REACT Guide](react-guide.md)

Check also [the tutorial](https://www.valentinog.com/blog/drf/#django-rest-with-react-what-you-will-learn)