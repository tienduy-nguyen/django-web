import { combineReducers } from 'redux';
import alert from './alert';
import leads from './leads';

export default combineReducers({
  leads,
  alert,
});
