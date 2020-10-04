# REACT In Django Rest Framework

## Installation

- Create `frontend` folder in leadmanager root folder
  ```bash 
  $ python3 manage.py startapp frontend
  ```
- Create `src/components` folder in frontend folder
  ```bash
  $ mkdir -p ./frontend/src/components
  ```
- Create `static/frontend` and `templates/frontend` folder in frontend folder
  ```bash
  $ mkdir -p ./frontend/{static, templates}/frontend
  ```
- Init `npm` in the root folder: `leadmanager`
  ```bash
  $ npm init
  ```
- Install webpack (as DevDependencies)
  ```bash
  $ npm i -D webpack webpack-cli
  ```
- Install babel
  ```bash
  $ npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties
  ```
- Install REACT
  ```bash
  $ npm i react react-dom prop-types react-router-dom react-redux redux-thunk
  ```
- Create `.babelrc` in the root folder
  ```json
  {
    "presets": ["@babel/preset-env", "@babel/preset-react"],
    "plugins": ["transform-class-properties"]
  }
  ```
- Create `webpack.config.js` file
  ```js
  module.exports = {
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: 'babel-loader',
          },
        },
      ],
    },
  };

  ```
- Config `scripts` in `package.json` file
  ```json
   "scripts": {
    "dev": "webpack --mode development ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js",
    "build": "webpack --mode production ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js"
  },
  ```
## Components, templates

- Don't forget add `frontend` folder in `leadmanager/settings.py` file
  ```py
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'leads',
      'rest_framework',
      'frontend'
  ]
  ```
- Create `src/index.js` and `components/App.js`
  ```js
  //src/index.js
  import React from 'react';
  import ReactDOM from 'react-dom';
  import App from './components/App';

  // //Redux
  // import store from './store'
  // import {Provider} from 'react-redux'

  ReactDOM.render(
    <React.StrictMode>
      <App></App>
    </React.StrictMode>,
    document.getElementById('app')
  );

  ```

  ```js
  // src/components/App.js
  import React, { Fragment, useEffect } from 'react';
  import ReactDOM from 'react-dom';
  import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

  const App = () => {
    return (
      <Router>
        <Fragment>
          <h1>Hi every one</h1>
        </Fragment>
      </Router>
    );
  };

  export default App;
  ```
- Modify `fronend/views.py`
  ```py
  # frontend/views.py
  from django.shortcuts import render

  # Create your views here.
  def index(request):
    return render(request, 'fronend/index.html')
  ```
- Update `frontend/urls.py`
  ```py
  # frontend/urls.py
  from django.urls import path
  from . import views

  urlpatterns = [
    path('', views.index)
  ]
  ```
- Update `leadmanager/urls.py`
  ```py
  # leadmanager/urls.py
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
    path('', include('leads.urls')), # home page
    path('', include('frontend.urls'))
  ]
  ```
- Run `npm run dev` to build webpack to `static/fronend/main.js` file
- Reload server
  ```bash
  $ python3 manage.py runserver
  ```
  Make sure environment is active: `pipenv shell`

- Create components : `layouts`, `leads`
  
  `rce, rcf`: shorcut to create class component and function components in REACT
- Make `npm run dev` to recompile
  
  If not, we need to modify scripts in package.json with the flag --watch in "dev"

  ```json
   "scripts": {
    "dev": "webpack --mode development --watch ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js",
    "build": "webpack --mode production ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js"
  },
  ```

- Using Redux

...

## Django Token Authentication

- Update ower in leads models, using authentication models of django
  ```python
  # leads/models.py
  from django.db import models
  from django.contrib.auth.models import User

  # Create your models here.
  class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

  ```
- Make migration and migrate
  ```bash
  $ python3 manage.py makemigrations
  $ python3 manage.py migrate
  $ python3 manage.py runserver
  ```
- Update `leads/api.py`
  ```py
  # leads/api.py
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
      permissions.IsAuthenticated
    ]
    serializer_class = LeadSerializer

    def get_queryset(self):
      return self.request.user.leads.all()
      
    def perform_create(self, serializer):
      serializer.save(owner=self.request.user)
  ```
## Authentication module for django rest auth with django-rest-knox

- Config `django-rest-knox`
  
  Update in `INSTALLED_APPS` and `REST_FRAMEWORK` in `leadmanager/settings.py` file
    ```python
    # leadmanager/settings.py
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leads',
    'rest_framework',
    'frontend',
    'knox',
    'accounts',

  ]
  REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':('knox.auth.TokenAuthentication',)
  }
  ```
- Run migrate
  ```bash
  $ python3 manage.py migrate
  ```
## Accounts app for User auth
- Create accounts app
  ```bash
  $ python3 manage.py startapp  accounts
  ```
- Create `serializers.py` file
  ```python
  from rest_framework import serializers
  from django.contrib.auth.models import User

  # User serializer
  class UserSerializer(serializer.ModelSerializer):
    class Meta:
      model = User
      fields= ('id', 'username', 'email')


  # Register serializer
  class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('id', 'username', 'email', 'password')
      extra_kwargs={'password': {'write_only': True}}

    def create(self, validated_data):
      user = User.objects.create_user(validated_data['username'], 
      validated_data['email'], 
      validated_data['password'])

      return user

  # Login serializer
  class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):
      user = authenticate(**data)
      if user:
        return user
      raise serializers.ValidationError('Incorrect credentials')

  ```
- Create `accounts/api.py`
  
  ```python
  # accounts/api.py
  from rest_framework import generics, permissions
  from rest_framework.response import Response
  from knox.models import AuthToken
  from .serializers import UserSerializer, RegisterSerializer

  # Register api
  class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
      })


  # Login API
  class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

  # Get User API
  class UserAPI(generics.RetrieveAPIView):
  permissions_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user
  ```
- Create `accounts/urls.py`
  ```python
  from django.urls import path, include
  from .api import RegisterAPI, LoginAPI, UserAPI
  from knox import views as know_views

  urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
  ]
  ```
  Attention for error TokenAuthen [stackoverflow](https://stackoverflow.com/questions/55668375/object-of-type-authtoken-is-not-json-serializable)

