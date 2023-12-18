import React, { memo } from 'react';
import PropTypes from 'prop-types';
import sls from './Button.module.scss';

//NOTE: Destructuring Assignment for props
const Button = ({ type, text, children, classNames, styles, onClick }) => {
    return (
        <button type={type}  className={classNames} style={styles} onClick={onClick}>
            {text || children}
        </button>
    );
};

Button.propTypes = {
    type: PropTypes.string,
    text: PropTypes.string.isRequired,
    classNames: PropTypes.string,
    styles: PropTypes.object,
    onClick: PropTypes.func.isRequired,
};

Button.defaultProps = {
    type: 'button',
    classNames: sls.button__default,
    styles: {},
};

export default memo(Button);
