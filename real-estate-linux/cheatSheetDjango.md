### Start project Django in Linux

#### Virtual enviroment setup

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

#### Django install and setup

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

#### Change in settings.py global of project

- urls.py global: Define roots parents of project

  ```python
  urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  ```

- Add some configs of project in INSTALLED_APPS
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
