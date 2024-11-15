import os
from pydub import AudioSegment
from pydub.utils import make_chunks
import sys

# Çıkış kodlamasını utf-8 olarak ayarla
sys.stdout.reconfigure(encoding='utf-8')

# Giriş ve çıkış klasör yolları
input_base_folder = "C:/Users/tsekm/Desktop/python.py/Tüm Veriler wav/"
output_base_folder = "C:/Users/tsekm/Desktop/python.py/Tüm Veriler wav"

# Alt klasörlerin adları
subfolders = ['Hüzünlü Müzikler wav', 'Neşeli Müzikler wav']

# Her alt klasördeki tüm wav dosyalarını işleyin
for subfolder in subfolders:
    input_subfolder_path = os.path.join(input_base_folder, subfolder)
    output_subfolder_path = os.path.join(output_base_folder, subfolder)
    os.makedirs(output_subfolder_path, exist_ok=True)  # Çıkış klasörünü oluştur veya varsa geç
    for root, _, files in os.walk(input_subfolder_path):
        for file in files:
            if file.endswith('.wav'):
                input_wav_file_path = os.path.join(root, file)
                try:
                    audio = AudioSegment.from_wav(input_wav_file_path)
                    # Ses dosyasını 15 saniyelik parçalara bölme
                    chunk_length_ms = 15 * 1000  # 15 saniye
                    chunks = make_chunks(audio, chunk_length_ms)
                    
                    # Her parçayı ayrı bir dosya olarak kaydetme (15 saniyeden kısa olanlar hariç)
                    for i, chunk in enumerate(chunks):
                        if len(chunk) < chunk_length_ms:
                            print(f"Son parça 15 saniyeden kısa olduğu için atlandı: {file}")
                            continue
                        chunk_name = f"{os.path.splitext(file)[0]}_chunk{i}.wav"
                        chunk_output_path = os.path.join(output_subfolder_path, chunk_name)
                        chunk.export(chunk_output_path, format="wav")
                        print(f"Eklendi: {chunk_output_path}")
                    
                    # Orijinal dosyayı silme
                    os.remove(input_wav_file_path)
                    print(f"Silindi: {input_wav_file_path}")

                except Exception as e:
                    print(f"{file} işlenirken hata oluştu: {e}")
                    
print("Ses dosyaları 15 saniyelik parçalara bölündü ve orijinal dosyalar silindi.")
