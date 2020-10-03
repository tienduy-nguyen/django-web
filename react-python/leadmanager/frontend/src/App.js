import React, { Fragment, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/layout/Header';
import Dashboard from './components/leads/Dashboard';

const App = () => {
  return (
    <Router>
      <Fragment>
        <Header></Header>
        <div className='container'>
          <Dashboard></Dashboard>
        </div>
      </Fragment>
    </Router>
  );
};

export default App;
