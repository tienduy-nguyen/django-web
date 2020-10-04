import * as Types from '../constants/types';

const initialState = {
  leads: [],
  lead: null,
  error: {},
};

export default function (state = initialState, action) {
  const { type, payload } = action;
  switch (type) {
    case Types.GET_LEADS:
      return { ...state, leads: payload };
    case Types.LEAD_ERRORS:
      return { ...state, error: payload, lead: null };
    case Types.DELETE_LEAD:
      return {
        ...state,
        leads: state.leads.filter((lead) => lead.id !== payload),
        lead: null,
      };
    case Types.GET_LEAD:
      return {
        ...state,
        lead: payload,
      };
    case Types.UPDATE_LEAD:
      return {
        ...state,
        lead: payload,
      };
    case Types.ADD_LEAD:
      return {
        ...state,
        leads: [payload, ...state.leads],
      };
    case Types.CLEAR_LEADS:
      return {
        ...state,
        leads: [],
      };
    default:
      return state;
  }
}
