import pandas as pd
import numpy as np
import os
import tqdm
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.model_selection import train_test_split

#NOTE: Dictionary chuyển nhãn về số nguyên
label2int = {
    "male": 1,
    "female": 0
}

#NOTE: Hàm load_data() sẽ trả về 2 numpy array là X và ys
def load_data(vector_length=128):
    """
    #NOTE: Một hàm để load dữ liệu từ thư mục `data`
    #NOTE: Sau lần chạy thứ 2, hàm này sẽ load dữ liệu từ file results/features.npy và results/labels.npy
    #NOTE: vì nó nhanh hơn nhiều!
    """
    #NOTE: Tạo thư mục results nếu chưa tồn tại
    if not os.path.isdir("results"):
        os.mkdir("results")
    #NOTE: Nếu các đặc trưng và nhãn đã được load riêng lẻ và được đóng gói, hãy tải chúng từ đó thay vì tải lại từ đầu
    if os.path.isfile("results/features.npy") and os.path.isfile("results/labels.npy"):
        X = np.load("results/features.npy")
        y = np.load("results/labels.npy")
        return X, y
    #NOTE: Đọc dataframe từ file csv
    df = pd.read_csv("datas/balanced-all.csv")
    #NOTE: Lấy tổng số mẫu
    n_samples = len(df)
    #NOTE: Lấy tổng số mẫu nam
    n_male_samples = len(df[df['gender'] == 'male'])
    #NOTE: Lấy tổng số mẫu nữ
    n_female_samples = len(df[df['gender'] == 'female'])
    print("Total samples:", n_samples)
    print("Total male samples:", n_male_samples)
    print("Total female samples:", n_female_samples)
    #NOTE: Khởi tạo một mảng rỗng cho tất cả các đặc trưng âm thanh
    X = np.zeros((n_samples, vector_length))
    #NOTE: Khởi tạo một mảng rỗng cho tất cả các nhãn âm thanh (1 cho nam và 0 cho nữ)
    y = np.zeros((n_samples, 1))
    for i, (filename, gender) in tqdm.tqdm(enumerate(zip(df['filename'], df['gender'])), "Loading data", total=n_samples):
        features = np.load(filename)
        X[i] = features
        y[i] = label2int[gender]
    #NOTE: Lưu các đặc trưng và nhãn vào file để không phải load lại
    #NOTE: mỗi lần chạy lại không cần phải load lại
    np.save("results/features", X)
    np.save("results/labels", y)
    return X, y

#NOTE: Hàm split_data() sẽ chia dữ liệu thành 3 phần: train, validation và test
def split_data(X, y, test_size=0.1, valid_size=0.1):
    #NOTE: Chia dữ liệu thành 2 phần: train và test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=7)
    #NOTE: Chia dữ liệu train thành 2 phần: train và validation
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=valid_size, random_state=7)
    #NOTE: Trả về một dictionary các giá trị
    return {
        "X_train": X_train,
        "X_valid": X_valid,
        "X_test": X_test,
        "y_train": y_train,
        "y_valid": y_valid,
        "y_test": y_test
    }

#NOTE: Hàm create_model() sẽ tạo ra một mạng neural network với 5 hidden dense layers
def create_model(vector_length=128):
    #NOTE: """5 lớp ẩn dense từ 256 units đến 64"""
    model = Sequential()
    model.add(Dense(256, input_shape=(vector_length,)))
    model.add(Dropout(0.3))
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(64, activation="relu"))
    model.add(Dropout(0.3))
    #NOTE: 1 neuron với hàm sigmoid, 0 là nữ, 1 là nam
    model.add(Dense(1, activation="sigmoid"))
    #NOTE: Sử dụng binary_crossentropy vì đây là bài toán phân loại giới tính
    model.compile(loss="binary_crossentropy", metrics=["accuracy"], optimizer="adam")
    #NOTE: In ra thông tin của mô hình
    model.summary()
    return model