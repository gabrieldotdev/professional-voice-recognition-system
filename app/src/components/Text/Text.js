import React, { useMemo, memo } from 'react';
import PropTypes from 'prop-types';
import sls from './Text.module.scss';

//NOTE: Destructuring Assignment for props
const Text = ({ text, classNames, styles, children }) => {
    //NOTE: useMemo for performance (prevent re-render when props change)
    const txt = useMemo(() => text || children, [text, children]);

    return (
        <p className={classNames} style={styles}>
            {txt}
        </p>
    );
};

Text.propTypes = {
    text: PropTypes.string,
    classNames: PropTypes.string,
    styles: PropTypes.object,
    children: PropTypes.node,
};

Text.defaultProps = {
    text: '',
    classNames: sls.text__default,
    styles: {},
};

export default memo(Text);
