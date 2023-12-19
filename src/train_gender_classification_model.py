from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard, EarlyStopping
from gender_classification_model import load_data, split_data, create_model

# NOTE: Load dữ liệu từ dataset
X, y = load_data()

# NOTE: Chia dữ liệu thành tập huấn luyện, tập validation, và tập kiểm thử
data = split_data(X, y, test_size=0.1, valid_size=0.1)

# NOTE: Tạo mô hình
model = create_model()

# NOTE: Sử dụng TensorBoard để xem các chỉ số
tensorboard = TensorBoard(log_dir="logs")

# NOTE: Định nghĩa early stopping để dừng huấn luyện sau 5 epochs không cải thiện
early_stopping = EarlyStopping(mode="min", patience=5, restore_best_weights=True)

# NOTE: Thiết lập kích thước batch và số epochs
batch_size = 64
epochs = 100

# NOTE: Huấn luyện mô hình sử dụng tập huấn luyện và kiểm thử sử dụng tập validation
model.fit(data["X_train"], data["y_train"], epochs=epochs, batch_size=batch_size, validation_data=(data["X_valid"], data["y_valid"]),
          callbacks=[tensorboard, early_stopping])

# NOTE: Lưu mô hình vào một file
model.save("results/model.h5")

# NOTE: Đánh giá mô hình sử dụng tập kiểm thử
print(f"Đánh giá mô hình sử dụng {len(data['X_test'])} mẫu...")
loss, accuracy = model.evaluate(data["X_test"], data["y_test"], verbose=0)
print(f"Mất mát: {loss:.4f}")
print(f"Độ chính xác: {accuracy*100:.2f}%")
