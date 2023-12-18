import { Fragment, useRef } from 'react';
import Form from '../../components/Form/Form';
import useFileUpload from '../../hook/useFileUpload';
import ReactPlayer from 'react-player';
import Result from '../../components/Result';
import Text from '../../components/Text/Text';
import sls from './Home.module.scss';

function Home() {
    const { file, result, recordingStatus, handleFormSubmit, handleFileChange, handleRecordingComplete } =
        useFileUpload();

    const audioRef = useRef(null);

    return (
        <Fragment>
            <Form
                onSubmit={handleFormSubmit}
                onChange={handleFileChange}
                onRecordingComplete={handleRecordingComplete}
            />
            <div className={sls.recording_status}>
                {file && <Text>Tên file: {file.name}</Text>}
                {recordingStatus && <Text>{recordingStatus}</Text>}
                {file && (
                    <div>
                        <ReactPlayer
                            ref={audioRef}
                            url={URL.createObjectURL(file)}
                            controls
                            className={sls.react_player}
                            width="100%"
                            height="100%"
                            muted={true}
                        />
                    </div>
                )}
            </div>
            <div className={sls.result_container}>
                <span className={sls.span_result}>Kết quả:</span>
                {/* <!-- KẾT QUẢ XỬ LÝ --> */}
                <div className={sls.processing_results}>
                    <Result gender={result.gender} maleProb={result.maleProb} femaleProb={result.femaleProb} transcription={result.transcription} />
                </div>
            </div>
        </Fragment>
    );
}

export default Home;
