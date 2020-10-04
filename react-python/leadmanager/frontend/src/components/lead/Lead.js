import React, { Fragment, useEffect } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import { getLead, deleteLead } from '../../actions/leads';

const Lead = ({ getLead, deleteLead, lead, match }) => {
  useEffect(() => {
    getLead(match.params.id);
  }, [getLead, match.params.id]);

  return lead === null ? (
    <Fragment>
      <h2>Lead not found</h2>
    </Fragment>
  ) : (
    <Fragment>
      <Link to='/' className='btn btn-light my-4'>
        Back To Home Page
      </Link>
      <div className='card'>
        <div className='card-header px-3'>Name: {lead.name}</div>
        <div className='card-body'>
          <p className='card-text'>Email: {lead.email}</p>
          <span className='lead'>Message: {lead.message}</span>
        </div>
      </div>
      <div className='mt-2'>
        <Link className='btn btn-info mr-2' to={`/leads/${lead.id}/edit`}>
          Edit
        </Link>
        <button className='btn btn-danger' onClick={() => deleteLead(lead.id)}>
          Delete
        </button>
      </div>
    </Fragment>
  );
};

Lead.propTypes = {
  getLead: PropTypes.func.isRequired,
  deleteLead: PropTypes.func.isRequired,
  lead: PropTypes.object.isRequired,
};

const mapStateToProps = (state) => ({
  lead: state.leads,
});
export default connect(mapStateToProps, { getLead, deleteLead })(Lead);
