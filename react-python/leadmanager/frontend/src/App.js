import React, { Fragment, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/layout/Navbar';
import Routes from './components/routing/Routes';
import Alert from './components/layout/Alert';
import setAuthToken from './utils/setAuthToken';
import { loadUser } from './actions/auth';
import store from './store';
import * as Types from './constants/types';

const App = () => {
  useEffect(() => {
    // check for token in LS
    if (localStorage.token) {
      setAuthToken(localStorage.token);
    }
    store.dispatch(loadUser());

    // log user out from all tabs if they log out in one tab
    window.addEventListener('storage', () => {
      if (!localStorage.token) store.dispatch({ type: Types.LOGOUT_SUCCESS });
    });
  }, []);

  return (
    <Router>
      <Fragment>
        <Navbar></Navbar>
        <div className='container'>
          <Alert></Alert>
          <Switch>
            <Route component={Routes} />
          </Switch>
        </div>
      </Fragment>
    </Router>
  );
};

export default App;
