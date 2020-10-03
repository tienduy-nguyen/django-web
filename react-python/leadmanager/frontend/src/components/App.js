import React, { Fragment, useEffect } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './layout/Header';
import Dashboard from './leads/Dashboard';

const App = () => {
  return (
    <Router>
      <Fragment>
        <Header></Header>
        <Dashboard></Dashboard>
      </Fragment>
    </Router>
  );
};

export default App;
