import axios from 'axios';
import * as Types from '../constants/types';
import { setAlert } from './alert';
import regeneratorRuntime from 'regenerator-runtime'; // To use async with webpack

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

// DELETE leads
export const deleteLeads = (id) => async (dispatch) => {
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
