import os
import sys

# Çıktı için UTF-8 kodlamasını kullan
sys.stdout.reconfigure(encoding='utf-8')

def change_extensions_in_directory(directory, old_extension, new_extension):
    # Belirtilen klasördeki tüm dosyaları kontrol et
    for filename in os.listdir(directory):
        if filename.endswith(old_extension):  # Dosya belirtilen uzantıya sahipse
            old_file_path = os.path.join(directory, filename)
            new_file_name = filename.replace(old_extension, new_extension)  # Uzantıyı değiştir
            new_file_path = os.path.join(directory, new_file_name)

            os.rename(old_file_path, new_file_path)  # Dosyayı yeniden adlandır
            print(f"{filename} -> {new_file_name}")

# Örnek kullanım:
directory = r"C:\Users\tsekm\Desktop\python.py\Neşeli Müzikler"  # Klasör yolu
old_extension = ".m3a"  # Eski uzantı
new_extension = ".m4a"  # Yeni uzantı

change_extensions_in_directory(directory, old_extension, new_extension)
