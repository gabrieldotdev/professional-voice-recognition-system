// import { Fragment, useRef } from 'react';
// import Form from '../../components/Form/Form';
// import useFileUpload from '../../hook/useFileUpload';
// import ReactPlayer from 'react-player';
// import Result from '../../components/Result';
// import Text from '../../components/Text/Text';
// import sls from './Home.module.scss';

// function Home() {
//     const { file, result, language, recordingStatus, handleFormSubmit, handleFileChange, handleRecordingComplete } =
//         useFileUpload();

//     const audioRef = useRef(null);

//     return (
//         <Fragment>
//             <Form
//                 onSubmit={handleFormSubmit}
//                 onChange={handleFileChange}
//                 language={language}
//                 onRecordingComplete={handleRecordingComplete}
//             />
//             <div className={sls.recording_status}>
//                 {file && <Text>Tên file: {file.name}</Text>}
//                 {recordingStatus && <Text>{recordingStatus}</Text>}
//                 {file && (
//                     <div>
//                         <ReactPlayer
//                             ref={audioRef}
//                             url={URL.createObjectURL(file)}
//                             controls
//                             className={sls.react_player}
//                             width="100%"
//                             height="100%"
//                             muted={true}
//                         />
//                     </div>
//                 )}
//             </div>
//             <div className={sls.result_container}>
//                 <span className={sls.span_result}>Kết quả:</span>
//                 {/* <!-- KẾT QUẢ XỬ LÝ --> */}
//                 <div className={sls.processing_results}>
//                     {result && (
//                         <Result
//                             gender={result.gender}
//                             maleProb={result.maleProb}
//                             femaleProb={result.femaleProb}
//                             transcription={result.transcription}
//                         />
//                     )}
//                 </div>
//             </div>
//         </Fragment>
//     );
// }

// export default Home;

import { useRef, useState } from 'react';
import ReactPlayer from 'react-player';
import Text from '../../components/Text/Text';
import sls from './Home.module.scss';
import Form from '../../components/Form/Form';
import { predict } from '../../api/axios';
import Result from '../../components/Result';

// Constants
const NO_RECORDING_MESSAGE = 'Không có bản ghi âm nào được thực hiện.';
const PROCESSING_MESSAGE = 'Đang xử lý...';
const ERROR_MESSAGE = 'Đã xảy ra lỗi khi xử lý.';

function App() {
    const [file, setFile] = useState(null);
    const [language, setLanguage] = useState('en-US');
    const [result, setResult] = useState(null);
    const [recordingStatus, setRecordingStatus] = useState(NO_RECORDING_MESSAGE);
    const audioRef = useRef(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleLanguageChange = (event) => {
        setLanguage(event.target.value);
    };

    const handleRecordingComplete = (blob) => {
        setFile(blob);
    };

    const handlePredict = async () => {
        const formData = new FormData();
        formData.append('file', file);
        try {
            setRecordingStatus(PROCESSING_MESSAGE);
            const res = await predict(formData, language);

            setResult(res.data);
            setRecordingStatus('Đã xử lý xong.');

        } catch (error) {
            console.error('Error predicting gender:', error);
            setRecordingStatus(ERROR_MESSAGE);
        }
    };

    return (
        <div>
            <Form
                onSubmit={handlePredict}
                onChange={handleFileChange}
                language={language}
                handleLanguageChange={handleLanguageChange}
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
                    {result && (
                        <Result
                            gender={result.gender}
                            maleProb={result.maleProb}
                            femaleProb={result.femaleProb}
                            transcription={result.transcription}
                        />
                    )}
                </div>
            </div>
        </div>
    );
}

export default App;
