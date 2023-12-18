import PropTypes from 'prop-types';
import Text from './Text/Text';
import { Fragment } from 'react';

const Result = ({ gender, maleProb, femaleProb, transcription }) => {
    const cls_gender =
        'text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl from-[#34a0a4] via-[#76c893] to-[#76c893] bg-gradient-to-r bg-clip-text text-transparent';
    const cls__transcription = 'text-md tracking-tight';

    return (
        <Fragment>
            <Text text={`Xác nhận giới tính: ${gender}`} classNames={cls_gender} />
            <Text text={`Xác suất là nam: ${maleProb}`} />
            <Text text={`Xác suất là nữ: ${femaleProb}`} />
            <div className="flex flex-col">
                <span className="text-md font-bold tracking-tight">Xuất băn bản: </span>
                <Text text={`"${transcription}"`} classNames={cls__transcription} />
            </div>
        </Fragment>
    );
};

Result.propTypes = {
    gender: PropTypes.string,
    maleProb: PropTypes.number,
    femaleProb: PropTypes.number,
    transcription: PropTypes.string,
};

export default Result;
