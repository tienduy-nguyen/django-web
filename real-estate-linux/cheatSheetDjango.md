### Some command lines using in django project

#### Django project deployement

##### Virtual enviroment setup

- Make sure we installed python3 and virtualenv

  ```bash
  python3 -m pip install --user virtualenv
  ```

- Create a virtual enviroment

  ```bash
  python3 -m venv lenv [comments]: <> (lenv: Name of folder contains virtualenv)
  ```

- Activating a virtual enviroment

  ```bash
  source env/bin/activate
  ```

- Leaving the virtual enviroment

  ```bash
  deactivate
  ```

##### Django install and setup

<span style="color:red">
Attention: Always using python3 manage.py ... in virtual enviroment (source lenv/bin/activate
</span>

- Install globally

  ```bash
  sudo apt install python3-django
  ```

- Install

  ```bash
  pip install django
  ```

- Start project with django-admin

  ```bash
  django-admin startproject <name-project>
  ```

- Start server (in virtual en)

  ```bash
  python3 manage.py runserver
  ```

- Check packages installed with pip

  ```bash
  pip freeze
  ```

- Migrations

  ```bash
  python3 manage.py miragrations
  ```

#### Urls templates in Django project

##### Create container (pages, lists, users ....)

- Using startapp
  ```bash
  python3 manage.py startapp pages
  python3 manage.py startapp realtors
  python3 manage.py startapp listings
  ```
- After created those container folder, we must config the apps of them in the INSTALLED_APPS in the settings global of project

  ```python
  INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  ]
  ```

  <span style="color:cyan">
  The names: PagesConfig, ListingsConfig, RealtorsConfig are the name of apps

  We can find them in : pages/apps - listings/apps - realtors/apps
  </span>

- In each folder container, we create a urls.py file, that contains urls of site
  and urls.py file in folder of project contains roots of these urls

* urls.py global: Define roots parents of project

  ```python
  urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  ```
