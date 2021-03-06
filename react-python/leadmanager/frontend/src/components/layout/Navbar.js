import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { logout } from '../../actions/auth';

const Navbar = ({ auth: { isAuthenticated, loading, user }, logout }) => {
  const authLinks = (
    <ul className='navbar-nav ml-auto mt-2 mt-lg-0'>
      <a className='navbar-brand mr-3' href='/leads'>
        Leads
      </a>
      <span className='navbar-text mr-3'>
        <strong>{user ? `Welcome ${user.username}` : ''}</strong>
      </span>
      <li className='nav-item'>
        <button
          onClick={logout}
          className='nav-link btn btn-info btn-sm text-light'
        >
          Logout
        </button>
      </li>
    </ul>
  );

  const guestLinks = (
    <ul className='navbar-nav ml-auto mt-2 mt-lg-0'>
      <li className='nav-item'>
        <Link to='/register' className='nav-link'>
          Register
        </Link>
      </li>
      <li className='nav-item'>
        <Link to='/login' className='nav-link'>
          Login
        </Link>
      </li>
    </ul>
  );

  return (
    <nav className='navbar navbar-expand-sm navbar-light bg-light'>
      <div className='container'>
        <button
          className='navbar-toggler'
          type='button'
          data-toggle='collapse'
          data-target='#navbarTogglerDemo01'
          aria-controls='navbarTogglerDemo01'
          aria-expanded='false'
          aria-label='Toggle navigation'
        >
          <span className='navbar-toggler-icon' />
        </button>
        <div className='collapse navbar-collapse' id='navbarTogglerDemo01'>
          <a className='navbar-brand mr-3' href='/'>
            Lead Manager
          </a>
        </div>
        <Fragment>
          {isAuthenticated && !loading ? authLinks : guestLinks}
        </Fragment>
      </div>
    </nav>
  );
};

Navbar.propTypes = {
  logout: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired,
};

const mapStateToProps = (state) => ({
  auth: state.auth,
});
export default connect(mapStateToProps, { logout })(Navbar);
