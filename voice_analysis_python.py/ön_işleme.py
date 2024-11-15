import os
import librosa
import numpy as np

# Klasör yollarını tanımla
input_folders = {
    "agresif": r"C:\Users\tsekm\Desktop\python.py\Tüm Veriler wav\Agresif Müzikler wav",
    "hüzünlü": r"C:\Users\tsekm\Desktop\python.py\Tüm Veriler wav\Hüzünlü Müzikler wav",
    "neşeli": r"C:\Users\tsekm\Desktop\python.py\Tüm Veriler wav\Neşeli Müzikler wav"
}
output_folders = {
    "agresif": r"C:\Users\tsekm\Desktop\python.py\Ön İşlenmiş Veriler\agresif",
    "hüzünlü": r"C:\Users\tsekm\Desktop\python.py\Ön İşlenmiş Veriler\hüzünlü",
    "neşeli": r"C:\Users\tsekm\Desktop\python.py\Ön İşlenmiş Veriler\neşeli"
}

# Eğer çıktı klasörleri yoksa oluştur
for folder in output_folders.values():
    os.makedirs(folder, exist_ok=True)

# Ses normalizasyonu fonksiyonu
def normalize_audio(audio):
    max_val = np.max(np.abs(audio))
    return audio / max_val if max_val > 0 else audio

# MFCC çıkarma ve işlenmiş dosyayı kaydetme fonksiyonu
def process_and_save(input_path, output_path):
    # Ses dosyasını yükle
    audio, sr = librosa.load(input_path, sr=None)

    # Ses normalizasyonu
    audio = normalize_audio(audio)

    # MFCC çıkarma
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc.T, axis=0)  # Ortalama değerleri al

    # İşlenmiş veriyi .npy formatında kaydet
    np.save(output_path, mfcc_mean)

# Her klasördeki ses dosyalarını işle ve kaydet
for emotion, input_folder in input_folders.items():
    output_folder = output_folders[emotion]
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):  # Yalnızca wav dosyalarını işle
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.wav', '.npy'))
            process_and_save(input_path, output_path)

print("Ses işleme tamamlandı.")
