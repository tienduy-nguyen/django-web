import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Redux
import store from './store';
import { Provider } from 'react-redux';

ReactDOM.render(
  <Provider store={store}>
    <React.StrictMode>
      <App></App>
    </React.StrictMode>
  </Provider>,
  document.getElementById('app')
);
