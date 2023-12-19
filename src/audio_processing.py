import pyaudio
import wave
import librosa
import numpy as np
from sys import byteorder
from array import array
from struct import pack


THRESHOLD = 500 #NOTE: Ngưỡng tiếng ồn
CHUNK_SIZE = 1024 #NOTE: Kích thước mẫu âm thanh (1 mẫu = 1 byte) đuợc ghi lại và xử lý mỗi lần gọi hàm record()
FORMAT = pyaudio.paInt16 #NOTE: Định dạng âm thanh (16 bit = 2 byte)
RATE = 16000 #NOTE: Tốc độ lấy mẫu âm thanh (16KHz = 16000 mẫu/s)

SILENCE = 30 #NOTE: Ngưỡng thời gian âm thanh yên lặng (30 mẫu = 30/16000 = 0.001875s) => 0.001875s âm thanh yên lặng thì dừng ghi âm

def is_silent(snd_data):
    #NOTE: "Trả về 'True' nếu âm thanh nhỏ hơn ngưỡng 'silent'"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    #NOTE: "Làm cho âm thanh có cường độ trung bình bằng 0"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    #NOTE: "Cắt bỏ âm thanh yên lặng ở đầu và cuối"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    #NOTE: Cắt bỏ âm thanh yên lặng ở đầu
    snd_data = _trim(snd_data)

    #NOTE: Cắt bỏ âm thanh yên lặng ở cuối
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    #NOTE: Thêm âm thanh yên lặng vào đầu và cuối 'snd_data' với độ dài 'seconds' (float)
    r = array('h', [0 for i in range(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds*RATE))])
    return r

def record():
    """
    #NOTE: Ghi âm một từ hoặc một vài từ từ microphone và
    #NOTE: trả về dữ liệu dưới dạng một mảng các số nguyên có dấu
    #NOTE: Chuẩn hóa âm thanh, cắt bỏ âm thanh yên lặng ở đầu và cuối
    #NOTE: và thêm 0.5s âm thanh yên lặng vào đầu và cuối
    #NOTE: để đảm bảo VLC có thể phát
    #NOTE: mà không bị cắt bỏ.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        #NOTE: little endian: byte thấp nhất ở địa chỉ nhỏ nhất
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > SILENCE:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r

def record_to_file(path):
    #NOTE: "Ghi âm từ microphone và xuất dữ liệu ra 'path'"
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()


# NOTE: Hàm extract_feature được sử dụng để trích xuất các đặc trưng từ file audio
def extract_feature(file_name, **kwargs):
    """
    # NOTE: Trích xuất feature từ file audio `file_name`
        # NOTE: Các feature được hỗ trợ:
            - MFCC (mfcc)
            - Chroma (chroma)
            - MEL Spectrogram Frequency (mel)
            - Contrast (contrast)
            - Tonnetz (tonnetz)
        # NOTE: Ví dụ:
        `features = extract_feature(path, mel=True, mfcc=True)`
    """
    mfcc = kwargs.get("mfcc")
    chroma = kwargs.get("chroma")
    mel = kwargs.get("mel")
    contrast = kwargs.get("contrast")
    tonnetz = kwargs.get("tonnetz")
    
    X, sample_rate = librosa.core.load(file_name)
    if chroma or contrast:
        stft = np.abs(librosa.stft(X))
    result = np.array([])
    if mfcc:
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        result = np.hstack((result, mfccs))
    if chroma:
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
        result = np.hstack((result, chroma))
    if mel:
        mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T,axis=0)
        result = np.hstack((result, mel))
    if contrast:
        contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
        result = np.hstack((result, contrast))
    if tonnetz:
        tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
        result = np.hstack((result, tonnetz))
    return result