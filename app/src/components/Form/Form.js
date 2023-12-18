import { AudioRecorder } from 'react-audio-voice-recorder';
import sls from './Form.module.scss';

const Form = ({ language, onSubmit, onChange, onRecordingComplete, handleLanguageChange }) => {
    return (
        <form onSubmit={onSubmit}>
            <div className={sls.form__container}>
                {/* <!-- Write code here... --> */}
                <div className={sls.choose__file_btn}>
                    <div className={sls.choose__file}>
                        <label for="file-upload" className={sls.choose__file_label}>
                            <span>Chọn file</span>
                            <input
                                type="file"
                                accept="audio/*"
                                id="file-upload"
                                className={sls.choose__file_input}
                                onChange={onChange}
                            />
                        </label>
                        <select value={language} onChange={handleLanguageChange}>
                            <option value="en-US">English</option>
                            <option value="vi-VN">Tiếng Việt</option>
                            <option value="zh-CN">中文</option>
                            <option value="fr-FR">Français</option>
                        </select>
                        <AudioRecorder onRecordingComplete={onRecordingComplete} className={sls.audio__recorder} />
                    </div>
                </div>
                <div className={sls.submit__btn}>
                    <button type="submit" className={sls.submit}>
                        Gửi và xử lý
                    </button>
                </div>
            </div>
        </form>
    );
};
export default Form;
