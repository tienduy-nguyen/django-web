# Blog with Django

(All command line is using for Linux)

## Pre-installation

- Install Django
  ```bash
  $ pip3 install django
  $ python3 -m django --version
  ```
  Check all commands of django
  ```bash
  $ django-admin
  ```

## Create Django application

- Creating a project

  ```bash
  $ django-admin startproject django_blog
  ```

  A new folder will be created and contains somes files template of django app.
  Check details of these files in the [documentation official of Django](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

- Run project django on browser
  ```bash
  $ python3 manage.py runserver
  ```
  > By default the site will start on port 8000
  > If we want to change the server's port, we run the command
  ```bash
  $ python3 manage.py runserver 8080
  ```
- Create a blog app for the site

  ```bash
  $ python3 manage.py startapp blog
  ```

  Django will create a blog directory

- Make sure we add blog apps to the INSTALLED_APP in settings.py file config of project

  ```python
  # django_blog/settings.py
  INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  ]
  ```

  blog --> directory name

  BlogConfig --> name of class declared in blog/apps.py

## Write views and urls in blog app

- Create a urls.py file in blog directory

  It will be used for call the view. The simple version of urls.py should look like

  ```python
  # blog/urls.py
  from django.urls import path
  from . import views

  urlpatterns = [
    path('',views.index,name='index')
  ]
  ```

- Write the first view

  ```python
  # django_blog/views.py
  from django.shortcuts import render
  from django.http import HttpRequest

  def home(request):
      return render(request, 'blog/home.html')

  def about(request):
      return render(request, 'blog/about.html')
  ```

- Point blog/urls.py to root urls.py

  The next step is to point the root URLconf at the blog.urls module. In django_blog/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so we have:

  ```python
  # django_blog/
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('blog.urls'))
  ]
  ```

- Create a templates folder which contain all file html of project
- Then config DIRS in TEMPLATE of the settings.py file project
  ```python
  # django_blog/settings.py
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'templates')], #Config directory "templates"
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```
- Complete file htmls with dummy data for ours projects

## Admin page and create models database
- Create a superuser for admin page
  ```bash
  $ python3 manage.py createsuperuser
  ```
- Create models in models.py file
- After creating a model, we need make migrations models to the django apps
  
  Makemigration: make whatever changes we need.
  ```bash
  $ python3 manage.py makemigrations
  ```
- Check command line how SQL create a table from python
  ```bash
  $ python3 manage.py sqlmigrate blog 0001
  ```
  >blog: name directory
  >0001: number file migration - 0001___init__.py
- Run migrate to update the changes
  ```bash
  $ python3 manage.py migrate
  ```
- Run Django python sheel
  
  It will allow us to work with the models interactively line by line to create record in SQLite in python
  ```bash
  $ python3 manage.py shell
  ```
  eg some querry using in interactiveconsole
  ```python
  # Terminal
  from blog.models import Post
  from django.contrib.auth.models import User
  
  User.objects.all()
  User.objects.first()
  User.objects.filter(username='tienduy')
  User.objects.filter(username='tienduy').first()
  user = User.objects.filter().first()

  ```
- Put models in the admin.py file

  For the listings container, firstly, we must add the data of model to show in admin page

  ```python
  # blog/admin.py
  from django.contrib import admin
  from .models import Post

  admin.site.register(Post)
  ```
- Create a static media folder to upload images, videos, files
  
  Firstly, we need add MEDIA_ROOT and MEDIA_URL in settings.py file of project
  ```python
  # django_blog/settings.py
  MEDIA_ROOT = os.path.join(BASE_DIR,'media')
  MEDIA_URL = '/media/' # name of static folder contains the files uploaded
  ```
  And make sure we need add static url to urls.py of project
  > + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```python
  #django_blog/urls.py
  from django.contrib import admin
  from django.urls import path, include
  from django.conf import settings
  from django.conf.urls.static import static


  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('blog.urls'))
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```
## Using django-taggit

  >django-taggit is a reusable able Django application designed to make adding tagging to your project esasy to your project easy.
- Installation
  ```bash
  $ pip3 install django-taggit
  ```
- Add "taggit" in INSTALLED_APPS of settings.py file
  ```python
  # django_blog
  INSTALLED_APPS = [
      ...,
      'taggit'
  ]
  ```
- Using in the models.py
  ```python
  # blog/models.py
  from django.db import models

  from taggit.managers import TaggableManager

  class Post(models.Model):
      # ... fields here

      tags = TaggableManager()
  ```
  >Plugging TAGGIT_CASE_INSENSITIVE = True into settings.py if we xant django-taggit to be case insensitive when looing up exiting tags

  .............. to complete

## Authenticatin (login, register, logout)
- Create users apps
  ```bash
  $ python3 manage.py startapps users
  ```
  
  Make sure you add it in INSTALLED_APPS to settings.py file of project
  ```python
  INSTALLED_APPS =[
    .....,
    users.apps.UsersConfig,
    ....,
  ]
  ```
