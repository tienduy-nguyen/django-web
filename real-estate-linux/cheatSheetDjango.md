### Start project
  [x] Virtual enviroment setup
    - Make sure we installed python3 and virtualenv
      ```bash
      python3 -m pip install --user virtualenv
      ```
      
    - Create a virtual enviroment
      ```bash
      python3 -m venv lenv [//]: <> (lenv: Name of folder contains virtualenv)
      ```
    - Activating a virtual enviroment
      ```bash
      source env/bin/activate
      ```
    - Leaving the virtual enviroment
      ```bash
      deactivate
      ```
  [x] Django install and setup
    - Install globally
       ```bash
      sudo apt install python3-django
      ```
    - Install in lenv
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
    