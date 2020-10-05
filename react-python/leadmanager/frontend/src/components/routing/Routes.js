import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Lead from '../lead/Lead';
import LeadForm from '../lead/LeadForm';
import NotFound from '../layout/NotFound';
import Dashboard from '../leads/Dashboard';
import Register from '../accounts/Register';
import Login from '../accounts/Login';

const Routes = (props) => {
  return (
    <section>
      <Switch>
        <Route exact path='/' component={Dashboard} />
        <Route exact path='/leads' component={Dashboard} />
        <Route exact path='/leads/new' component={LeadForm} />
        <Route exact path='/leads/:id' component={Lead} />
        <Route exact path='/leads/:id/edit' component={LeadForm} />
        <Route exact path='/register' component={Register} />
        <Route exact path='/login' component={Login} />
        <Route component={NotFound} />
      </Switch>
    </section>
  );
};

export default Routes;
