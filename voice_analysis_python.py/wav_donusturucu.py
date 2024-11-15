import os
from pydub import AudioSegment

def convert_m3a_to_wav(m3a_file, wav_file):
    audio = AudioSegment.from_file(m3a_file, format='m3a')
    audio.export(wav_file, format='wav')

def convert_directory_m3a_to_wav(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.m3a'):
                # Giriş ve çıkış dosya yollarını oluştur
                m3a_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir)
                wav_output_dir = os.path.join(output_dir, relative_path)
                wav_file_path = os.path.join(wav_output_dir, os.path.splitext(file)[0] + '.wav')

                # Çıkış dizinini oluştur
                os.makedirs(wav_output_dir, exist_ok=True)

                # Dönüştürme işlemini gerçekleştir
                convert_m3a_to_wav(m3a_file_path, wav_file_path)
                print(f"Converted: {m3a_file_path} -> {wav_file_path}")

# Ana dizinleri belirtin
input_directory = r'C:\Users\tsekm\Desktop\python.py\Agresif'  # m3a path
output_directory = r'C:\Users\tsekm\Desktop\python.py\Agresif'  # wav path

# Dönüştürme işlemini başlat
convert_directory_m3a_to_wav(input_directory, output_directory)