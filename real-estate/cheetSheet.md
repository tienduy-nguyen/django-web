
### Create models:

  - After create model: 
    python manage.py makemigrations --> Create initial.py in migration folder
  - Creat model listings:
    python manage.py sqlmigrate listings 0001
  - Apply all migrations
    python manage.py migrate

### Create a super user

  python manage.py createsuperuser