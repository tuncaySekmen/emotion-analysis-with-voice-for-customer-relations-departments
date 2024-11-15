import os
from pydub import AudioSegment
import sys
sys.stdout.reconfigure(encoding='utf-8')  # stdout akışını UTF-8 olarak yapılandırın


def convert_m4a_to_wav(m4a_file, wav_file):
    audio = AudioSegment.from_file(m4a_file, format='m4a')
    audio.export(wav_file, format='wav')

def convert_directory_m4a_to_wav(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.m4a'):
                # Giriş ve çıkış dosya yollarını oluştur
                m4a_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir)
                wav_output_dir = os.path.join(output_dir, relative_path)
                wav_file_path = os.path.join(wav_output_dir, os.path.splitext(file)[0] + '.wav')

                # Çıkış dizinini oluştur
                os.makedirs(wav_output_dir, exist_ok=True)

                # Dönüştürme işlemini gerçekleştir
                convert_m4a_to_wav(m4a_file_path, wav_file_path)
                print(f"Converted: {m4a_file_path} -> {wav_file_path}")

# Ana dizinleri belirtin
input_directory = r'C:\Users\tsekm\Desktop\python.py\Neşeli Müzikler m4a'  # m4a path
output_directory = r'C:\Users\tsekm\Desktop\python.py\Neşeli Müzikler wav'  # wav path

# Dönüştürme işlemini başlat
convert_directory_m4a_to_wav(input_directory, output_directory)
