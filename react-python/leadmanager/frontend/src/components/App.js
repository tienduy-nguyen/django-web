import React, { Fragment, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './layout/Header';
import Lead from './lead/Lead';
import LeadForm from './lead/LeadForm';
import NotFound from './layout/NotFound';
import Dashboard from './leads/Dashboard';
import Alert from './layout/Alert';

const App = () => {
  return (
    <Router>
      <Fragment>
        <Header></Header>
        <div className='container'>
          <Alert></Alert>
          <Switch>
            <Route exact path='/' component={Dashboard} />
            <Route exact path='/leads' component={Dashboard} />
            <Route exact path='/leads/new' component={LeadForm} />
            <Route exact path='/leads/:id' component={Lead} />
            <Route exact path='/leads/:id/edit' component={LeadForm} />
            <Route component={NotFound} />
          </Switch>
        </div>
      </Fragment>
    </Router>
  );
};

export default App;
