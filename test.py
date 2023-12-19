import os
import argparse
from src.audio_processing import extract_feature, record_to_file
from src.gender_classification_model import create_model

def main():
    # NOTE: Thiết lập trình phân tích đối số dòng lệnh
    parser = argparse.ArgumentParser(description="Gender recognition script")
    parser.add_argument("-f", "--file", help="Path to the WAV file")
    args = parser.parse_args()

    # NOTE: Lấy đường dẫn đến file âm thanh từ đối số dòng lệnh
    file = args.file
    model = create_model()
    model.load_weights("results/model.h5")

    # NOTE: Nếu không có đường dẫn file hoặc file không tồn tại, ghi âm từ microphone
    if not file or not os.path.isfile(file):
        print("Please talk")
        file = "test.wav"
        record_to_file(file)

    # NOTE: Trích xuất đặc trưng từ file âm thanh và chuẩn hóa để dự đoán
    features = extract_feature(file, mel=True).reshape(1, -1)

    # NOTE: Dự đoán giới tính và tính toán xác suất
    male_prob = model.predict(features)[0][0]
    female_prob = 1 - male_prob
    gender = "male" if male_prob > female_prob else "female"

    # NOTE: In kết quả dự đoán và xác suất
    print("Result:", gender)
    print(f"Probabilities: Male: {male_prob*100:.2f}% Female: {female_prob*100:.2f}%")

if __name__ == "__main__":
    main()
    # COMMAND: python test.py -f "datas/audio/16-122828-0002.wav"