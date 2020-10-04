import axios from 'axios';
import * as Types from '../constants/types';
import { setAlert } from './alert';
import regeneratorRuntime, { async } from 'regenerator-runtime'; // To use async with webpack

// GET leads
export const getLeads = () => async (dispatch) => {
  try {
    const res = await axios.get('/api/leads/');

    dispatch({
      type: Types.GET_LEADS,
      payload: res.data,
    });
  } catch (err) {
    dispatch({
      type: Types.LEAD_ERRORS,
      payload: { msg: err.response.statusText, status: err.response.status },
    });
  }
};

// GET lead by id
export const getLead = (id) => async (dispatch) => {
  try {
    const res = await axios.get(`/api/leads/${id}/`);
    dispatch({
      type: Types.GET_LEAD,
      payload: res.data,
    });
  } catch (err) {
    dispatch({
      type: Types.LEAD_ERRORS,
      payload: { msg: err.response.statusText, status: err.response.status },
    });
  }
};

// POST Create lead
export const addLead = (formData, history) => async (dispatch) => {
  try {
    const config = {
      headers: {
        'Content-Type': 'application/json',
      },
    };
    const res = await axios.post(`/api/leads/`, formData, config);
    dispatch({
      type: Types.ADD_LEAD,
      payload: res.data,
    });
    dispatch(setAlert('Lead Created', 'success'));
    history.push('/');
  } catch (err) {
    const errors = err.response.data.errors;
    if (errors) {
      errors.forEach((error) => dispatch(setAlert(error.msg, 'danger')));
    }
    dispatch({
      type: Types.LEAD_ERRORS,
      payload: { msg: err.response.statusText, status: err.response.status },
    });
  }
};

// PUT Update lead
export const updateLead = (id, formData, history) => async (dispatch) => {
  try {
    const config = {
      headers: {
        'Content-Type': 'application/json',
      },
    };
    const res = await axios.put(`/api/leads/${id}/`, formData, config);
    dispatch({
      type: Types.UPDATE_LEAD,
      payload: res.data,
    });
    history.push('/');
  } catch (err) {
    const errors = err.response.data.errors;
    if (errors) {
      errors.forEach((error) => dispatch(setAlert(error.msg, 'danger')));
    }
    dispatch({
      type: Types.LEAD_ERRORS,
      payload: { msg: err.response.statusText, status: err.response.status },
    });
  }
};

// DELETE leads
export const deleteLead = (id) => async (dispatch) => {
  try {
    await axios.delete(`/api/leads/${id}/`);
    dispatch({
      type: Types.DELETE_LEAD,
      payload: id,
    });
    dispatch(setAlert('Lead removed', 'success'));
  } catch (err) {
    dispatch({
      type: Types.LEAD_ERRORS,
      payload: { msg: err.response.statusText, status: err.response.status },
    });
  }
};
