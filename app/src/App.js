import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { PrivateRoutes, PublicRoutes } from './router/router';

// Kiểm tra xem người dùng đã đăng nhập hay chưa
const isAuthenticated = () => {
    return false;
};

export const RenderRoutes = ({ routes }) => {
    return (
        <Routes>
            {routes.map((route, i) => (
                <Route
                    key={i}
                    path={route.path}
                    element={
                        route.isPrivate && !isAuthenticated() ? (
                            <Navigate to="/" />
                        ) : (
                            <route.layout>
                                <route.component />
                            </route.layout>
                        )
                    }
                />
            ))}
        </Routes>
    );
};

function App() {
    return (
        <Router>
            <RenderRoutes routes={PublicRoutes} />
            <RenderRoutes routes={PrivateRoutes} />
        </Router>
    );
}

export default App;

// function App() {
//   const [file, setFile] = useState(null);
//   const [genderResult, setGenderResult] = useState('');
//   const [maleProbResult, setMaleProbResult] = useState('');
//   const [femaleProbResult, setFemaleProbResult] = useState('');
//   const [transcriptionResult, setTranscriptionResult] = useState('');
//   const [recordingStatus, setRecordingStatus] = useState('Không có bản ghi âm nào được thực hiện.');

//   const handleFileChange = (event) => {
//     const selectedFile = event.target.files[0];
//     setFile(selectedFile);
//   };

//   const handleFormSubmit = async (event) => {
//     event.preventDefault();

//     if (!file) {
//       alert('Vui lòng chọn một file âm thanh.');
//       return;
//     }

//     const formData = new FormData();
//     formData.append('file', file);

//     try {
//       setRecordingStatus('Đang xử lý...');

//       const res = await predict(formData);

//       setGenderResult(`Chuẩn đoán giới tính: ${res.data.gender}`);
//       setMaleProbResult(`Tỷ lệ xác suất là nam giới: ${res.data.male_prob}`);
//       setFemaleProbResult(`Tỷ lệ xác suất là nữ giới: ${res.data.female_prob}`);
//       setTranscriptionResult(`Ghi chú giọng nói: "${res.data.transcription}"`);
//       setRecordingStatus('Đã xử lý xong.');
//     } catch (error) {
//       console.error('Error:', error);
//       setRecordingStatus('Đã xảy ra lỗi khi xử lý.');
//     }
//   };

//   return (
//     <div>
//       <h1>Voice Recognition App</h1>
//       <form onSubmit={handleFormSubmit}>
//         <input type="file" onChange={handleFileChange} />
//         <button type="submit">Gửi</button>
//       </form>
//       <div>
//         <h2>Kết quả:</h2>
//         <p>{genderResult}</p>
//         <p>{maleProbResult}</p>
//         <p>{femaleProbResult}</p>
//         <p>{transcriptionResult}</p>
//         <p>{recordingStatus}</p>
//       </div>
//     </div>
//   );
// }

// export default App;
