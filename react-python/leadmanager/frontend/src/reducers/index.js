import { combineReducers } from 'redux';
import alert from './alert';
import leads from './leads';
import messages from './messages';
import errors from './errors';
import auth from './auth';

export default combineReducers({
  leads,
  alert,
  messages,
  errors,
  auth,
});
