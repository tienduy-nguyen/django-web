import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { getLeads } from '../../actions/leads';

const Leads = ({ getLeads, leads: { leads } }) => {
  useEffect(() => {
    getLeads();
  }, [getLeads]);
  return (
    <div>
      <h1>Leads list</h1>
    </div>
  );
};

Leads.propTypes = {
  getLeads: PropTypes.func.isRequired,
  leads: PropTypes.object.isRequired,
};

const mapStateToProps = (state) => ({
  leads: state.leads.leads,
});

export default connect(mapStateToProps, { getLeads })(Leads);
