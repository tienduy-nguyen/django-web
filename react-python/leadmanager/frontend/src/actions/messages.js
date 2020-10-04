import * as Types from '../constants/types';

// Create message
export const createMessage = (msg) => {
  return {
    type: Types.CREATE_MESSAGE,
    payload: msg,
  };
};

// Return error
export const returnErrors = (msg, status) => {
  return {
    type: Types.GET_ERRORS,
    payload: { msg, status },
  };
};
