# VOICE GENDER RECOGNITION USING MACHINE LEARNING ALGORITHMS AND DEEP LEARNING

## Introduction (Giới thiệu)

This repository is about building a deep learning model using TensorFlow 2 to recognize gender of a given speaker's audio. Read this tutorial for more information.

## Dataset

## Requirements (Yêu cầu)

- SpeechRecognition
- TensorFlow
- Scikit-learn
- NumPy
- Pandas
- PyAudio
- Librosa
- Flask
- Flask-Cors

## Usage (Sử dụng)

- Installation (Cài đặt)

```bash
pip3 install -r requirements.txt
```

- Testing (Kiểm tra)

```bash
python test.py --file "datas\audio\19-227-0005.wav"
```
hoặc
```bash
python test.py --f "datas\audio\19-227-0005.wav"
```

- Installation app (Cài đặt ứng dụng)

```bash
cd app
npm install
```
- Run APP & Run API

```bash
#APP
npm start
```
```bash
#API
python app.py
```
