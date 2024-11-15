from pydub import AudioSegment
import os

# MP4 dosyalarının bulunduğu klasör
mp4_dizin = r"C:\Users\tsekm\Desktop\python.py\uzun süreli depresyon şarkıları"
# Dosyaların dönüştürüleceği klasör (aynı klasörde bırakılabilir)
m3a_dizin = r"C:\Users\tsekm\Desktop\python.py\uzun süreli depresyon şarkıları"

# MP4 dosyalarını al
for dosya_adı in os.listdir(mp4_dizin):
    if dosya_adı.endswith(".mp4"):
        mp4_dosya_yolu = os.path.join(mp4_dizin, dosya_adı)
        
        # MP4 dosyasını ses dosyasına dönüştür
        ses_dosya = AudioSegment.from_file(mp4_dosya_yolu, format="mp4")
        
        # Yeni dosya adını oluştur
        base, ext = os.path.splitext(dosya_adı)
        m3a_dosya_yolu = os.path.join(m3a_dizin, base + ".m3a")
        
        # Ses dosyasını M3A formatında kaydet
        ses_dosya.export(m3a_dosya_yolu, format="mp3")  # Burada 'mp3' kullanıyoruz çünkü m3a resmi bir format değil ama ses dosyası olarak kaydedilebilir
        print(f"{dosya_adı} m3a formatına dönüştürüldü.")
