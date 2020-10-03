import * as Types from '../constants/types';

const initialState = {
  leads: [],
  error: {},
};

export default function (state = initialState, action) {
  const { type, payload } = action;
  switch (type) {
    case Types.GET_LEADS:
      return { ...state, leads: payload };
    case Types.GET_ERRORS:
      return { ...state, error: payload };
    default:
      return state;
  }
}
