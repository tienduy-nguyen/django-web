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

## Admin page
- Create a superuser for admin page
  ```bash
  $ python3 manage.py createsuperuser
  ```