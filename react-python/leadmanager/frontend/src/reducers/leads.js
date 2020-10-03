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
    case Types.LEAD_ERRORS:
      return { ...state, error: payload };
    case Types.DELETE_LEAD:
      return {
        ...state,
        leads: state.leads.filter((lead) => lead.id !== payload),
      };
    default:
      return state;
  }
}
