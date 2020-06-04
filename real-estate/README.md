### Some command lines using in django project in window system

#### Django project deployement

##### Virtual enviroment setup

- Make sure we installed python verion > 3 and virtualenv

  ```bash
  python -m pip install --user virtualenv
  ```

- Create a virtual enviroment

  ```bash
  python -m venv lenv   >([comments]: <> (lenv: Name of folder contains virtualenv))
  ```

- Activating a virtual enviroment

  ```bash
  cd lenv/Scripts
  activate.bat
  ```

- Leaving the virtual enviroment

  ```bash
  deactivate
  ```

##### Django install and setup

  ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
  `Attention: Always using python manage.py ... in virtual enviroment (activate.bat)`

- Start project with django-admin

  ```bash
  py -m venv project-name
  ```

- Install in virtual enviroment

  ```bash
  py -m pip install Django
  ```

- Start server (in virtual en)

  ```bash
  python manage.py runserver
  ```

- Check packages installed with pip

  ```bash
  pip freeze
  ```

- Migrations

  ```bash
  python manage.py miragrations
  ```

>All next step are the same with the others systems. See detail in repository [real-estate-linux](https://github.com/tienduy-nguyen/django-web/tree/master/real-estate-linux)
