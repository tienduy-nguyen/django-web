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
  > blog: name directory
  > 0001: number file migration - 0001**\_init**.py
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

  > - static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  ```python
  #django_blog/urls.py
  from django.contrib import admin
  from django.urls import path, include
  from django.conf import settings
  from django.conf.urls.static import static
  ```

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

````
## Using django-taggit

>django-taggit is a reusable able Django application designed to make adding tagging to your project esasy to your project easy.
- Installation
```bash
$ pip3 install django-taggit
````

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

  > Plugging TAGGIT_CASE_INSENSITIVE = True into settings.py if we xant django-taggit to be case insensitive when looing up exiting tags

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

- Create urls authentication account

  ```python
  # users/urls.py
  from django.urls import path
  from . import views

  urlpatterns = [
      path('login/', views.login, name='login'),
      path('register/', views.register, name='register'),
      path('logout/', views.logout, name='logout')
  ]

  ```

- Create def in views.py

  ```python
  # users/views.py

  ```

- How to customize a form of django framwork for registration
  ```python
  from django import forms
  from django.forms import ModelForm
  from django.contrib.auth.models import User
  from django.contrib.auth.forms import UserCreationForm
  ```

class RegistrationForm(UserCreationForm):
class Meta:
model = User
fields = (
'username',
'email',
'password1',
'password2',
)

````
- Call the field of Registration form in html
```html
<!-- register.html -->
  <form method="POST" action="">
      {% csrf_token %}
      {{form.username}}
      {{form.email}}
      {{form.password1}}
      {{form.password2}}
      <div class="d-flex justify-content-center mt-4 login_container">
        <input class="btn login_btn" type="submit" value="Register Account">
      </div>
  </form>
````

- Login method in django

  ```python
  # users/views.py
  # Make we import : from django.contrib.auth.models import User, auth
  def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect!')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
  ```

- Logout method in django

  ```python
  # users/views.py
  # Make we import : from django.contrib.auth.models import User, auth
  def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('home')

  ```

- Register in django (user form of django)

  ```python
  def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # Check if all field of form is valided
        if form.is_valid():
            fs = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            # Check password
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'That username is taken')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'That email is being used')
                        return redirect('register')
                    else:
                      # Look good
                        fs.save()
                        user = auth.authenticate(
                            username=username, password=password1)
                        auth.login(request, user)
                        fs.user = request.user
                        messages.success(
                            request, 'Account created for ' + username)
                        return redirect('home')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('register')

    context = {'form': form}
    return render(request, 'users/register.html', context)
  ```

## User profile

- Create a Profile models in users apps

  ```python
  # users/models.py
  from django.db import models
  from django.contrib.auth.model import User

  # One to one relation ship with user existed
  class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASADE)
    image = models.ImageField(default = 'default.png', upload_to='profile_pics')

    def __str__(self):
      return f'{self.user.username} Profile'
  ```

- Update in admin.py file

  ```python
  # users/admin.py
  from django.contrib import admin
  from .models import Profile

  admin.site.register(Profile)
  ```

- Create profile direct with django signals
  ```python
  # users/signals.py
  from django.db.models.signals import post_save
  from django.contrib.auth.models import User
  from django.dispatch import receiver
  from .models import Profile
  ```

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, \*\*kwargs):
if created:
Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, \*\*kwargs):
instance.profile.save()

````

and add signals in apps.py

```python
# users/apps.py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals

````

- Small css framwork for django: crispy

  ```bash
  pip3 install django-crispy-forms
  ```

  Configure in INSTALLED_APP of settings.py file of project

  ```python
  INSTALLED_APPS = [
    ...,
    'crispy_forms',
    ...
  ]
  # Crispy template
  CRISPY_TEMPLATE_PACK = 'bootstrap4'
  ```

  Check the documentation of [django-crispy-form](https://django-crispy-forms.readthedocs.io/en/latest/) for more details

  And using it in our html

  ```html
  <!-- profile.html -->
  {% extends 'base.html'%} {% load crispy_forms_tags %} {% block content %}
  <div class="content-section container py-4 ml-auto col-md-8 col-lg-4">
    <div class="media pb-5">
      <img
        src="{{ user.profile.image.url }}"
        alt=""
        class="rounded-circle account-img mr-4"
        style="height: 100px;"
      />
      <div class="media-body">
        <h2 class="account-heading">{{ user.username}}</h2>
        <p class="text-secondary">{{user.email}}</p>
      </div>
    </div>
    <!-- Form here -->
    <form method="POST">
      {% csrf_token %}
      <fieldset class="form-group">
        <legend class="border-bottom mb-4">Profile Info</legend>
        {{ userForm | crispy}} {{ profileForm | crispy}}
      </fieldset>
      <div class="form-group">
        <button class="btn btn-outline-info" type="submit">Update</button>
      </div>
    </form>
  </div>
  {% endblock%}
  ```

- Update user profile

  Create updateUser and updateProfile in users/forms.py file

  ```python
  # users/forms.py
  class UserUpdateForm(forms.ModelForm):
      email = forms.EmailField()

      class Meta:
          model = User
          fields = [
              'first_name',
              'last_name',
              'username',
              'email',
          ]
  ```

class ProfileUpdateForm(forms.ModelForm):
class Meta:
model = Profile
fields = ['image']

````

```python
# users/views.py file
from django.contrib.auth.decorators import login_required
@login_required
def editProfile(request):
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, isntance=request.user)
        profileForm = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
      if userForm is valid() and profileForm is valid():
        userForm.save()
        profileForm.save()
    else:
        userForm = UserUpdateForm(isntance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'userForm': userForm,
        'profileForm': profileForm
    }
    return render(request, 'users/profile.html', context)
````

## Create, update, post
