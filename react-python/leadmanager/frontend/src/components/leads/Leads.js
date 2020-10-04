import React, { useEffect, Fragment } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import {
  getLeads,
  deleteLead,
  addLead,
  updateLead,
  getLead,
} from '../../actions/leads';

const Leads = ({ getLeads, deleteLead, addLead, updateLead, leads }) => {
  useEffect(() => {
    getLeads();
  }, [getLeads]);
  return (
    <Fragment>
      <div className='d-flex justify-content-between mt-5'>
        <h2>Leads</h2>
        <button
          className='btn btn-success btn-sm py-0'
          onClick={() => addLead()}
        >
          Add Lead
        </button>
      </div>
      <table className='table table-stripped'>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Message</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {leads.map((lead) => (
            <tr key={lead.id}>
              <td>{lead.id}</td>
              <td>{lead.name}</td>
              <td>{lead.email}</td>
              <td>{lead.message}</td>
              <td>
                <div className='ml-auto'>
                  <button
                    className='btn btn-info btn-sm'
                    onClick={() => getLead(lead.id)}
                  >
                    Edit
                  </button>
                  <button
                    className='btn btn-danger btn-sm'
                    onClick={() => deleteLead(lead.id)}
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </Fragment>
  );
};

Leads.propTypes = {
  getLeads: PropTypes.func.isRequired,
  deleteLead: PropTypes.func.isRequired,
  addLead: PropTypes.func.isRequired,
  updateLead: PropTypes.func.isRequired,
  getLead: PropTypes.func.isRequired,
  leads: PropTypes.array.isRequired,
};

const mapStateToProps = (state) => ({
  leads: state.leads.leads,
});

export default connect(mapStateToProps, {
  getLeads,
  deleteLead,
  addLead,
  updateLead,
  getLead,
})(Leads);
