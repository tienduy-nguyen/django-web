import React, { Component, useState, useEffect } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addLead, updateLead, getLead } from '../../actions/leads';

const initialState = {
  name: '',
  email: '',
  message: '',
};
const Form = ({ lead, getLead, addLead, updateLead, history }) => {
  const [formData, setFormData] = useState(initialState);
  const { name, email, message } = formData;

  useEffect(() => {
    const id = match.params['id'];
    console.log(id);
  });

  const onChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };
  const onSubmit = (e) => {
    e.preventDefault();
  };
  return (
    <div className='card card-body mt-4 mb-4'>
      <h2>{lead ? 'Add Lead' : 'Update Lead'}</h2>
      <form onSubmit={this.onSubmit}>
        <div className='form-group'>
          <label>Name</label>
          <input
            className='form-control'
            type='text'
            name='name'
            onChange={this.onChange}
            value={name}
          />
        </div>
        <div className='form-group'>
          <label>Email</label>
          <input
            className='form-control'
            type='email'
            name='email'
            onChange={this.onChange}
            value={email}
          />
        </div>
        <div className='form-group'>
          <label>Message</label>
          <textarea
            className='form-control'
            type='text'
            name='message'
            onChange={this.onChange}
            value={message}
          />
        </div>
        <div className='form-group'>
          <button type='submit' className='btn btn-primary'>
            Submit
          </button>
        </div>
      </form>
    </div>
  );
};

Form.propTypes = {
  addLead: PropTypes.func.isRequired,
  getLead: PropTypes.func.isRequired,
  updateLead: PropTypes.func.isRequired,
  lead: PropTypes.object.isRequired,
};

const mapStateToProps = (state) => {
  lead: state.leads.lead;
};
export default connect(mapStateToProps, { addLead, getLead, updateLead })(Form);
