Müşteri Duygu Analizi Projesi
Bu proje, müşteri ilişkileri ve satış departmanlarında çalışan profesyonellerin, telefon görüşmeleri sırasında müşterilerinin duygusal durumlarını daha doğru bir şekilde analiz edebilmelerini sağlamayı hedefliyor. Günümüzde, müşteri temsilcileri ve satış ekipleri, telefonla yapılan görüşmelerde müşterilerinin ruh halini anlamakta zorlanabiliyorlar. Bu projeyle, telefon görüşmeleri sırasında müşterilerin duygusal durumlarını tespit etmek için geliştirilen bir modelin nasıl çalıştığını ve bu süreçte kullanılan yöntemleri anlatmak istiyorum.

Proje, müşteri ilişkilerinde verimliliği artırmayı ve hizmet kalitesini üst seviyelere çıkarmayı amaçlıyor. Bunun için müzik verilerini kullanarak, farklı duygu sınıfları üzerinde çalıştım. Neşeli, hüzünlü ve agresif olmak üzere üç ana duygu sınıfı seçerek, bu sınıflara ait müzikleri analiz ettim. Bu müziklerden elde edilen ses verileri, telefon görüşmeleri sırasında müşterilerin ruh halini anlamak için kullanılabilecek bir modelin temelini oluşturdu.

Veri Toplama ve İşleme
Projede, YouTube platformundan müzik verisi toplamak için Selenium ve PyTube gibi araçlar kullandım. Müzikler, neşeli, hüzünlü ve agresif duygu türlerine göre kategorize edilerek toplandı. Her bir duygu sınıfından yaklaşık 1000 müzik parçası seçildi ve bu müzikler m3a formatında indirildi. Karakter hatalarını önlemek amacıyla UTF-8 kodlaması kullanıldı.

Sonrasında, müzik dosyalarını 15 saniyelik segmentlere ayırarak daha temiz bir ses kalitesi sağlamak için WAV formatına dönüştürdüm. Dönüştürülen dosyalar düzenli bir şekilde depolandı ve model eğitimi için hazır hale getirildi.

Ön İşleme ve Özellik Çıkartma
Verilerin model için uygun hale gelmesi adına bir dizi ön işleme adımı uygulandı. İlk olarak, ses dosyalarının genlik değerlerini normalleştirerek ses seviyelerini dengeleştirdim. Bu işlem, farklı ses dosyalarındaki ses seviyelerinin tutarsızlıklarını ortadan kaldırarak modelin daha doğru sonuçlar üretmesini sağladı.

Ayrıca, Mel-Frekans Kepstral Katsayıları (MFCC) çıkararak, ses dosyalarından daha anlamlı özellikler elde ettim. MFCC, ses sinyalini insan kulağının algılama şekline benzer bir şekilde modelleyerek daha etkili sınıflandırmalar yapılmasına olanak sağlıyor.

Model Eğitimi ve Sonuçlar
Elde edilen verilerle, hüzünlü, neşeli ve agresif duygu türlerini sınıflandırabilen bir model geliştirdim. 27.000'den fazla 15 saniyelik ses segmenti kullanılarak model eğitildi. Proje sonunda, bu duygu sınıflarını başarıyla ayırt edebilen bir sınıflandırma sistemi elde edildi.

Hubert,Wav2Vec,AST gibi ses transformatörleri bu verilerle eğitildi. Aralarında karşılaştırmalar yapılarak transformatörlerin veri eğitimlerinde başarı yüzdeleri hesaplandı.

Sonuç
Bu projede elde edilen sonuçlar, duygu analizi teknolojilerinin sadece müzik verileriyle bile etkili bir şekilde geliştirilebileceğini gösterdi. Ayrıca, bu tür sistemlerin, gelecekte müşteri ses verileriyle çalışabilecek uygulamalara dönüştürülebileceği potansiyelini ortaya koydu. Müşteri ilişkilerinde duygusal zeka uygulamalarının artması, işletmelere daha empatik ve etkili bir hizmet sunma imkanı sağlayacaktır.

Projenin amacı, müzik verileriyle duygu analizi yapılabileceğini göstermek ve müşteri ilişkileri alanında daha verimli hizmet sunulmasına katkıda bulunmaktır.
