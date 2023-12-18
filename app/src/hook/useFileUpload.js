import { useState } from 'react';
import { predict } from '../api/axios';

// Constants
const NO_RECORDING_MESSAGE = 'Không có bản ghi âm nào được thực hiện.';
const PROCESSING_MESSAGE = 'Đang xử lý...';
const ERROR_MESSAGE = 'Đã xảy ra lỗi khi xử lý.';

// Custom hook to handle file upload and prediction
const useFileUpload = () => {
    const [file, setFile] = useState(null);
    const [result, setResult] = useState('');
    const [language, setLanguage] = useState("en-US");
    const [recordingStatus, setRecordingStatus] = useState(NO_RECORDING_MESSAGE);

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        setFile(selectedFile);
    };

    const handleRecordingComplete = (blob) => {
        setFile(blob);
    }

    const handleFormSubmit = async (event) => {
        event.preventDefault();

        if (!file) {
            alert('Vui lòng chọn một file âm thanh.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);
        formData.append("language", language);

        try {
            setRecordingStatus(PROCESSING_MESSAGE);

            const res = await predict(formData);

            setResult(res.data);
            setRecordingStatus('Đã xử lý xong.');
        } catch (error) {
            console.error('Error:', error);
            setRecordingStatus(ERROR_MESSAGE);
        }
    };

    const handleLanguageChange = (e) => {
        // Set the language to the event target value
        setLanguage(e.target.value);
      };

    return {
        file,
        result,
        language,
        handleLanguageChange,
        recordingStatus,
        handleFileChange,
        handleRecordingComplete,
        handleFormSubmit
    };
};

export default useFileUpload;
