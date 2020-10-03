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
  