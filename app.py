from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from src.audio_processing import extract_feature, record_to_file
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

    file = request.files['file']
    filename = os.path.join("datas/audio", file.filename)
    file.save(filename)

    # Get the language parameter from the request, default to "en-US"
    language = request.args.get("language", "en-US")

    # Check if the language is valid
    supported_languages = ["en-US", "vi-VN", "zh-CN", "fr-FR"]
    if language not in supported_languages:
        return jsonify({'error': 'Invalid language'}), 400

    try:
        model = create_model()
        model.load_weights("results/model.h5")
        features = extract_feature(filename, mel=True).reshape(1, -1)
        male_prob = model.predict(features)[0][0]
        female_prob = 1 - male_prob
        gender = "male" if male_prob > female_prob else "female"

        # Chuyển đổi âm thanh thành văn bản sử dụng thư viện SpeechRecognition
        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile(filename)

        with audio_file as source:
            audio_data = recognizer.record(source)

        # Use the language parameter to recognize the speech
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
