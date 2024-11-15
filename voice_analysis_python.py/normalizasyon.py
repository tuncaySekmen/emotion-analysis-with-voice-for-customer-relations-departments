import os
import librosa
import soundfile as sf
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Girdi ve çıktı klasörlerini tanımla
input_folder = r"C:\Users\tsekm\Desktop\python.py\Tüm Veriler wav\neseli"
output_folder = r"C:\Users\tsekm\Desktop\python.py\Normalleştirilmiş Veriler\neseli"

# Çıktı klasörünü oluştur
os.makedirs(output_folder, exist_ok=True)

# Ses normalizasyonu fonksiyonu
def normalize_audio(audio):
    max_val = np.max(np.abs(audio))
    return audio / max_val if max_val > 0 else audio

# Klasördeki tüm dosyaları işle
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):  # Yalnızca WAV dosyalarını işle
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        try:
            # Ses dosyasını yükle
            audio, sr = librosa.load(input_path, sr=None)
            
            # Orijinal maksimum genliği kontrol et
            max_genlik_orjinal = np.max(np.abs(audio))
            
            # Ses normalizasyonu uygula
            audio_normalized = normalize_audio(audio)
            
            # Normalleştirilmiş sesi kaydet
            sf.write(output_path, audio_normalized, sr)
            
            # Kaydedilen dosyayı yeniden yükle ve genliği kontrol et
            audio_reloaded, _ = librosa.load(output_path, sr=None)
            max_genlik_normalized = np.max(np.abs(audio_reloaded))
            
            # Sonuçları yazdır
            print(f"{filename}:")
            print(f"  Normalizasyon öncesi maksimum genlik: {max_genlik_orjinal}")
            print(f"  Normalizasyon sonrası maksimum genlik: {max_genlik_normalized}")
        
        except Exception as e:
            print(f"Hata: {filename} işlenemedi. Sebep: {e}")

print("Tüm dosyalar başarıyla işlenmiştir.")
