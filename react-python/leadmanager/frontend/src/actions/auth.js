import * as Types from '../constants/types';
import { setAlert } from './alert';
import axios from 'axios';
import setAuthToken from '../utils/setAuthToken';
import { async } from 'regenerator-runtime';
import { returnErrors } from './messages';

//Load user
export const loadUser = () => async (dispatch) => {
  try {
    const res = await axios.get('/api/auth/user');
    dispatch({
      type: Types.USER_LOADED,
      payload: res.data,
    });
  } catch (err) {
    dispatch(returnErrors(err.response.data, err.response.status));
    dispatch({
      type: Types.AUTH_ERROR,
    });
  }
};

// Register user
export const register = ({ username, email, password }) => async (dispatch) => {
  const config = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const body = JSON.stringify({ username, email, password });
  try {
    const res = await axios.post('/api/auth/register', body, config);
    dispatch({
      type: Types.REGISTER_SUCCESS,
      payload: res.data,
    });
    dispatch(loadUser());
  } catch (err) {
    const errors = err.response.data.errors;

    if (errors) {
      errors.forEach((error) => dispatch(setAlert(error.msg, 'danger')));
    }
    dispatch(returnErrors(err.response.data, err.response.status));
    dispatch({
      type: Types.REGISTER_FAIL,
    });
  }
};

// Login user
export const login = (username, password) => async (dispatch) => {
  const config = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const body = { username, password };
  try {
    const res = await axios.post('/api/auth/login', body, config);
    dispatch({
      type: Types.LOGIN_SUCCESS,
      payload: res.data,
    });
    dispatch(loadUser());
  } catch (err) {
    const errors = err.response.data.errors;

    if (errors) {
      errors.forEach((error) => dispatch(setAlert(error.msg, 'danger')));
    }
    dispatch(returnErrors(err.response.data, err.response.status));
    dispatch({
      type: Types.LOGIN_FAIL,
    });
  }
};

// Logout
export const logout = () => async (dispatch) => {
  try {
    await axios.post('/api/auth/logout');
    dispatch({ type: Types.CLEAR_LEADS });
    dispatch({ type: Types.LOGOUT_SUCCESS });
  } catch (err) {
    dispatch(returnErrors(err.response.data, err.response.status));
  }
};
