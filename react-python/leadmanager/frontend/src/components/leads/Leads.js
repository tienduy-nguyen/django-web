import React, { useEffect, Fragment } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { getLeads, deleteLeads } from '../../actions/leads';

const Leads = ({ getLeads, deleteLeads, leads }) => {
  useEffect(() => {
    getLeads();
  }, [getLeads]);
  return (
    <Fragment>
      <h2>Leads</h2>
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
                <button
                  className='btn btn-danger btn-sm'
                  onClick={() => deleteLeads(lead.id)}
                >
                  Delete
                </button>
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
  deleteLeads: PropTypes.func.isRequired,
  leads: PropTypes.array.isRequired,
};

const mapStateToProps = (state) => ({
  leads: state.leads.leads,
});

export default connect(mapStateToProps, { getLeads, deleteLeads })(Leads);
