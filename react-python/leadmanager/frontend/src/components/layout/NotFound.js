import React, { Fragment } from 'react';

const NotFound = () => {
  return (
    <Fragment>
      <div className='container mt-4'>
        <div className='row'>
          <div className='col-12 mx-auto text-center'>
            <h2>
              <i className='fas fa-exclamation-triangle mr-2'></i>
              Page Not Found
            </h2>
            <p className='large'>Sorry, this page does not exist</p>
          </div>
        </div>
      </div>
    </Fragment>
  );
};

export default NotFound;
