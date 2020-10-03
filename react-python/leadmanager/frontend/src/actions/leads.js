import axios from 'axios';
import * as Types from '../constants/types';

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
      type: Types.GET_ERRORS,
      payload: { msg: err.response.statusText, status: err.response.status },
    });
  }
};
