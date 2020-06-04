## Notes of steps when I learned create web app with Django (For Linux system)

### Django project deployement

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
  source lenv/bin/activate
  ```

- Leaving the virtual enviroment

  ```bash
  deactivate
  ```

#### Django install and setup

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
  `Attention: Always using python3 manage.py ... in virtual enviroment (source lenv/bin/activate)`


- Install globally (without virtual enviroment)

  ```bash
  sudo apt install python3-django
  ```

- Install in virtual enviroment

  ```bash
  pip3 install django
  ```

- Start project with django-admin

  ```bash
  django-admin startproject <name-project>
  ```
  >project named in this repo is: btre

- Start server (in virtual en)

  ```bash
  python3 manage.py runserver
  ```

- Check packages installed with pip

  ```bash
  pip3 freeze
  ```

- Migrations

  ```bash
  python3 manage.py miragrations
  ```

### Urls templates in Django project

#### Create container (pages, lists, users ....)

- Using startapp
  
  ```bash
  python3 manage.py startapp pages
  python3 manage.py startapp realtors
  python3 manage.py startapp listings
  ```
- After created those folders containers, we must config the apps of them in the INSTALLED_APPS in the settings config of project

- Create a static files & paths
  
  >Create a folder named static in project folder which contains public file of web site.
  > We need set path of it in the settings global file


  ```bash
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static')
  ]

  ```
  Now, we collect this static folders config of django project

  ```bash
  python3 manage.py collectstatic
  ```
- Install apps

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

- urls.py global: Define roots parents of project

  ```python
  urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  ```
#### Create Model
- Pre-install (in virtual enviroment) to connect with postgresql
  
  ```bash
  pip3 install psycopg2
  pip3 install psycopg2-binary
  ```

- Config
  
  ```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database name>',
        'USER': 'postgres',
        'PASSWORD': '<database password>',
        'HOST': 'localhost'
    }
  }

  ```
- Migrate postgres to django project
 
  ```bash
  python3 manage.py migrate
  ```
  Check if everything is <span style='color: green'>OK</span> in the terminal.
  
- Create databases in the models.py

- Mirage models
 
  ```bash
  python3 manage.py makemigrations
  ```
- Create a super user
  
  ```bash
  python3 manage.py createsuperuser
  ```
#### Data in admin page

- Now we put models in the admin.py file
   
  For the listings container, firstly, we must add the data of model to show in admin page
  ```python
  from django.contrib import admin
  from .models import Listing

  admin.site.import(Listing)
  ```
  We do the same things in admin.py file of Realtor
  ```python
  from django.contrib import admin
  from .models import Realtor

  admin.site.import(Realtor)
  ```
- Register models with admin page

  Now we check on admin page on the browser. In the admin area, we get 'Listings' and 'Realtor' fields.
  We need create new realtors and new listings of items here.

- Custom admin display data

  We can customize the display of admin data after created the information

  listings/admin.py
  ```python
  from django.contrib import admin
  from .models import Listing


  class ListingAdmin(admin.ModelAdmin):
      list_display = ('id', 'title', 'is_published',
                      'price', 'list_date', 'realtor')
      list_display_links = ('id', 'title')
      list_filter = ('realtor',)
      list_editable = ('is_published',)
      search_fields = ('title', 'description', 'address',
                      'city', 'state', 'zipcode', 'price')
      list_per_page = 25


  ```

  reators/admin.py

  ```python
  from django.contrib import admin
  from .models import Realtor


  class RealtorAdmin(admin.ModelAdmin):
      list_display = ('id', 'name', 'email', 'hire_date')
      list_display_links = ('id', 'name')
      search_fields = ('name', 'email')
      list_per_page = 25


  admin.site.register(Realtor, RealtorAdmin)
  ```
#### Display data in root page from model database

- Pull data from models
  
  Work in views.py file, an example in listings/views.py file
  ```python
  from django.shotcuts import render
  from .models import Listing

  def index(request):
    listings = Listing.objects.all()
    context ={
      'listings': listings
    }
    return render(request, 'listings/listings.html',context)

  ```
- Make the homepage listings dynamic
  Do the same like we do in with listings and realtors

- Get listing by id from model

  >Using get_object_or_404
  ```python
  #listings/views.py
  from django.shortcuts import render, get_object_or_404
  from django.http import HttpResponse
  from .models import Listing

  def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)
  ```
- Search in python
  
  ```python
  # listings/view.py
  def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)  # accept case sensitive
    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)  # less than
    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)  # less than

    context = {
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'value': request.GET
    }
    return render(request, 'listings/search.html', context)
  ```

### Authentication in Django project

#### Account apps and urls
- Create a container app: accounts
  ```bash
  python3 manage.py accounts
  ```
  By default Django create a table auth_user for us in database. So we don't need create a new one.
- Create templates login, register, dasboard
- Logout in Django
  ```python
  # accounts/view.py
  def logout(request):
    return redirect('index')
  ```
- CSRF token
  It's can be very simple implemented in Django project
  ```html
  <form action="{% url 'login' %}" method='POST'>
    {% csrf_token %}
    <div>Content of form</div>
  </form>
  ```
