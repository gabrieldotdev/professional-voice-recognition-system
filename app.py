from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from src.audio_processing import extract_feature
from src.gender_classification_model import create_model
import speech_recognition as sr

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'message': 'Voice Gender Recognition!'})

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file found'}), 400

    # NOTE: Lấy file từ request và lưu vào thư mục "datas/audio"
    file = request.files['file']
    filename = os.path.join("datas/audio", file.filename)
    file.save(filename)

    # NOTE: Lấy tham số ngôn ngữ từ request, mặc định là "en-US"
    language = request.args.get("language", "en-US")

    # NOTE: Kiểm tra xem ngôn ngữ có hợp lệ không
    supported_languages = ["en-US", "vi-VN", "zh-CN", "fr-FR"]
    if language not in supported_languages:
        return jsonify({'error': 'Invalid language'}), 400

    try:
        # NOTE: Tạo và load mô hình dự đoán giới tính
        model = create_model()
        model.load_weights("results/model.h5")

        # NOTE: Trích xuất đặc trưng từ file âm thanh và chuẩn hóa để dự đoán
        features = extract_feature(filename, mel=True).reshape(1, -1)
        male_prob = model.predict(features)[0][0]
        female_prob = 1 - male_prob
        gender = "male" if male_prob > female_prob else "female"

        # NOTE: Chuyển đổi âm thanh thành văn bản sử dụng thư viện SpeechRecognition
        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile(filename)

        with audio_file as source:
            audio_data = recognizer.record(source)

        # NOTE: Sử dụng tham số ngôn ngữ để nhận dạng văn bản từ âm thanh
        text_result = recognizer.recognize_google(audio_data, language=language)

        result = {
            "gender": gender,
            "maleProb": f"{male_prob * 100:.2f}%",
            "femaleProb": f"{female_prob * 100:.2f}%",
            "transcription": text_result
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
