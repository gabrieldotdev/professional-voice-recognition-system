import glob  # NOTE: Dùng để tìm kiếm các file trong thư mục
import os  # NOTE: Dùng để tạo thư mục
import pandas as pd  # NOTE: Dùng để đọc file csv
import numpy as np  # NOTE: Dùng để lưu các file audio dưới dạng numpy array
import librosa  # NOTE: Dùng để xử lý audio
from tqdm import tqdm  # NOTE: Dùng để hiển thị tiến trình
from src.audio_processing import extract_feature

# NOTE: Tạo thư mục 'data' nếu thư mục đó chưa tồn tại
dirname = "data"
if not os.path.isdir(dirname):
    os.mkdir(dirname)

# NOTE: Tìm tất cả các file CSV trong thư mục
csv_files = glob.glob("*.csv")

# NOTE: Duyệt qua từng file CSV để tiến hành xử lý
for j, csv_file in enumerate(csv_files):
    print("[+] Preprocessing", csv_file)
    df = pd.read_csv(csv_file)

    # NOTE: Chỉ lấy cột filename và gender
    new_df = df[["filename", "gender"]]
    print("Previously:", len(new_df), "rows")

    # NOTE: Chỉ lấy giới tính là male hoặc female, bỏ qua NaNs và giới tính 'other'
    new_df = new_df[np.logical_or(new_df['gender'] == 'female', new_df['gender'] == 'male')]
    print("Now:", len(new_df), "rows")

    # NOTE: Đặt tên cho file CSV đã xử lý và lưu lại
    new_csv_file = os.path.join(dirname, csv_file)
    new_df.to_csv(new_csv_file, index=False)

    # NOTE: Lấy tên thư mục và danh sách các file âm thanh trong thư mục đó
    folder_name, _ = csv_file.split(".")
    audio_files = glob.glob(f"{folder_name}/{folder_name}/*")
    all_audio_filenames = set(new_df["filename"])

    # NOTE: Duyệt qua từng file âm thanh để trích xuất đặc trưng
    for i, audio_file in tqdm(list(enumerate(audio_files)), f"Extracting features of {folder_name}"):
        splited = os.path.split(audio_file)
        audio_filename = f"{os.path.split(splited[0])[-1]}/{splited[-1]}"

        # NOTE: Nếu tên file âm thanh có trong danh sách, thì tiến hành trích xuất đặc trưng
        if audio_filename in all_audio_filenames:
            src_path = f"{folder_name}/{audio_filename}"
            target_path = f"{dirname}/{audio_filename}"

            # NOTE: Tạo thư mục nếu thư mục đó chưa tồn tại
            if not os.path.isdir(os.path.dirname(target_path)):
                os.mkdir(os.path.dirname(target_path))

            # NOTE: Trích xuất đặc trưng và lưu vào file numpy
            features = extract_feature(src_path, mel=True)
            target_filename = target_path.split(".")[0]
            np.save(target_filename, features)
