import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Lead from '../lead/Lead';
import LeadForm from '../lead/LeadForm';
import NotFound from '../layout/NotFound';
import Dashboard from '../leads/Dashboard';
import Alert from '../layout/Alert';

const Routes = (props) => {
  return (
    <section className='container'>
      <Alert></Alert>
      <Switch>
        <Route exact path='/' component={Dashboard} />
        <Route exact path='/leads' component={Dashboard} />
        <Route exact path='/leads/new' component={LeadForm} />
        <Route exact path='/leads/:id' component={Lead} />
        <Route exact path='/leads/:id/edit' component={LeadForm} />
        <Route component={NotFound} />
      </Switch>
    </section>
  );
};

export default Routes;
