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

- Create components
- Make `npm run dev` to recompile
  
  If not, we need to modify scripts in package.json with the flag --watch in "dev"

  ```json
   "scripts": {
    "dev": "webpack --mode development --watch ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js",
    "build": "webpack --mode production ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js"
  },
  ```