# ROADMAP.md: Python ile DNS Spoofing Özelliklerini Geliştirme ve Test Etme

## 1. Giriş
Bu proje, Counter-Strike: Global Offensive (CS:GO), Valorant ve PlayerUnknown's Battlegrounds (PUBG) gibi popüler çevrimiçi oyunların ağ bağlantılarını derinlemesine incelemeyi hedeflemektedir. Ana amaç, bu oyunlar sırasında kullanılan IP adreslerini, sunucuları, portları ve protokolleri tespit etmektir. Elde edilen veriler, oyun güvenliği araştırmaları, ağ performans analizi ve potansiyel zafiyet tespiti için temel oluşturacaktır.**

Bu rehber, DNS spoofing tekniklerini Python ile yeniden oluşturmayı, etik ve yasal sınırlar içinde kalarak kontrollü bir ortamda test etmeyi amaçlar.

## 2. Proje Vizyonu
** Projenin temel vizyonu, oyun ağ trafiği analizinde kapsamlı ve tekrarlanabilir bir metodoloji sunarak, araştırmacılar, güvenlik uzmanları ve oyun meraklıları için değerli bir kaynak olmaktır. Uzun vadede, bu projenin statik bir raporlama aracından, dinamik ve etkileşimli bir ağ analiz platformuna dönüşmesi hedeflenmektedir. Bu, sadece mevcut oyunları değil, gelecekteki çevrimiçi oyunları da analiz etmeye olanak tanıyan genişletilebilir bir yapıya sahip olacaktır. **

## 3. Tamamlanan Kilometre Taşı: V1.0 - Temel Ağ Analizi ve Raporlama
Bu aşama, projenin başlangıç hedeflerinin başarıyla tamamlandığı ilk temel sürümü temsil etmektedir.
  **Hedefler:**:
   - Seçilen popüler çevrimiçi oyunların (CS:GO, Valorant, PUBG) temel ağ bağlantı detaylarının (IP adresleri, portlar, kullanılan protokoller) tespiti ve belgelenmesi.
   - Bulguların README.md dosyasında açık ve anlaşılır bir şekilde sunulması.

### Tamamlanan Görevler:
  - Her bir hedef oyun için standart oyun senaryolarında (lobi, oyun içi, sunucu bağlantısı) Wireshark ile ağ trafiği yakalama süreçlerinin tanımlanması ve uygulanması.
  - Oyun trafiğini etkili bir şekilde izole etmek ve analiz etmek için özel Wireshark Capture Filters ve Display Filters setlerinin oluşturulması ve test edilmesi.
  - Yakalanan **.pcap** dosyaları üzerinde temel analizlerin yapılması ve kritik IP adresleri, port aralıkları ve ağ protokollerinin (UDP, TCP) belirlenmes
  - Projenin amacını, hedeflerini, kurulum adımlarını ve ilk bulguları içeren kapsamlı bir README.md dosyasının hazırlanması.
  - Tespit edilen IP/port/protokol bilgilerini özetleyen detaylı bir **Oyun Ağ Bağlantıları Analiz Tablosu**nun oluşturulması ve README.md'ye entegrasyonu.
  - İlgili araştırma notları için researchs/ klasörü altında ilk taslak Markdown dosyalarının oluşturulması (örn. csgo_network_analysis.md, wireshark_filters.md).
### Elde Edilen Çıktılar::
```
Temel oyun ağ bağlantı bilgilerini içeren ilk analiz raporu ve dokümantasyon.

Etkili ve çalışır durumda Wireshark yakalama/görüntüleme filtre setleri.

GitHub üzerinde, kolayca klonlanabilir ve anlaşılır bir yapıya sahip proje deposu.

```

## 4. Gelecek Kilometre Taşları
Projenin uzun vadeli potansiyelini gerçekleştirmek için planlanan gelecek aşamalar ve özellikler aşağıda listelenmiştir. 
Her bir aşama, projenin kabiliyetlerini ve değerini artırmayı hedeflemektedir.

### 4.1. V1.1 - Otomatik Veri İşleme ve Görselleştirme (Kısa Vadeli Hedef)
Bu aşama, manuel analiz süreçlerini otomatize etmeyi ve elde edilen ağ verilerini daha anlaşılır, 
görsel formatlarda sunmayı amaçlamaktadır.

### Hedefler:
   - Otomatik Pcap Analizi: Yakalanan .pcap dosyalarını Python kullanarak (örn. scapy, pyshark) otomatik olarak ayrıştıracak ve işleyecek scriptler geliştirmek.
   - Belirli portlardan geçen toplam paket sayısı ve veri hacmi istatistikleri.
   - En sık iletişim kurulan kaynak/hedef IP adresleri ve bunların bant genişliği kullanımları.
   - Paket boyutu dağılımlarının ve akış sürelerinin analizi.

### Veri Görselleştirme Modülü:
Analiz edilen verileri (trafik yoğunluğu, en aktif sunucular, port kullanım dağılımları vb.) dinamik ve statik grafikler (çubuk grafikler, pasta grafikleri, çizgi grafikler, ısı haritaları) aracılığıyla görselleştirmek için Python kütüphaneleri (matplotlib, seaborn, plotly) kullanmak


## 4.2. V1.2 - Derinlemesine Protokol Analizi ve Güvenlik İncelemesi (Orta Vadeli Hedef)
Bu aşama, oyun trafiğinin sadece yüzeysel değil, daha derinlemesine protokol seviyesinde incelenmesini ve potansiyel 
güvenlik anormalliklerinin tespitini içerecektir.

### Hedefler:
1. **Oyun Protokolü İmzaları ve Deseni Tespiti**: Bilinen veya tespit edilen oyunlara özgü uygulama katmanı protokol imzalarını veya veri desenlerini belirlemek ve bunları otomatik olarak filtreleyebilme/tanımlayabilme yeteneği. Bu, belirli oyun içi eylemlerin (örn. vuruş kaydı, beceri kullanımı) ağ trafiğindeki karşılığını bulmaya yardımcı olabilir.
2. **Ağ Performansı Metrikleri:** Paket yakalama verilerinden gecikme (Latency), titreme (Jitter) ve paket kaybı gibi kritik ağ performans metriklerini çıkararak oyun deneyimi üzerindeki etkilerini analiz etmek.
3. **Anormal Trafik Desenleri Tespiti:** DDoS saldırıları, hile (cheat) motorlarının aktivitesi veya diğer kötü niyetli ağ davranışlarını işaret edebilecek anormal trafik desenlerini (örn. belirli bir IP'den gelen aşırı trafik, olağandışı port taramaları, anormal büyüklükte paketler) otomatik olarak algılama mekanizmaları geliştirmek.
4. **Coğrafi Konum Haritalaması:** Tespit edilen sunucu IP adreslerinin coğrafi konumlarını (ülke, şehir) belirlemek için açık kaynak veya ticari coğrafi konum veri tabanları (örn. MaxMind GeoLite2) ile entegrasyon. Bu veriyi interaktif dünya haritaları üzerinde görselleştirerek sunucu dağılımlarını gösterme.
5. **DNS Spoofing Zafiyet İncelemesi:**  Oyunların DNS çözümleme süreçlerini ve potansiyel DNS spoofing zafiyetlerini (örn. oyun istemcisinin veya sunucusunun DNS kayıtlarına güvenip güvenmediği) araştırmak. Bu alanda, Python ile basit DNS spoofing senaryolarının simülasyonu ve olası etkilerinin analizi.
6. **Potansiyel Teknolojiler:** Python, Coğrafi Konum API'leri/Veritabanları, Trafik Analizi Algoritmaları, Makine Öğrenimi (Anormal Tespit için temel düzeyde).

## 4.3. V2.0 - Etkileşimli Araç ve Genişletilebilir Platform (Uzun Vadeli Hedef):
Bu uzun vadeli hedef, projenin sadece bir araştırma çıktıları koleksiyonu olmaktan öteye geçerek, 
kullanıcıların kendi analizlerini yapabileceği etkileşimli bir araç veya modüler bir analiz platformuna dönüşmesini kapsamaktadır.

### Hedefler:
  - **Basit Web Arayüzü (Web UI)**: Kullanıcıların .pcap dosyalarını yükleyebileceği, temel analiz sonuçlarını ve görselleştirmeleri doğrudan tarayıcı üzerinden görüntüleyebileceği, kullanıcı dostu basit bir web arayüzü geliştirmek (örn. Flask veya Django frameworkleri ile).
  - **Dinamik Oyun ve Kural Ekleme:** Kullanıcıların veya geliştiricilerin, yeni oyunları veya özel analiz kurallarını kolayca platforma ekleyebileceği modüler ve genişletilebilir bir mimari oluşturmak.
  - **Otomatik Raporlama ve Dışa Aktarma:** Analiz sonuçlarını otomatik olarak PDF, HTML veya CSV gibi okunabilir ve paylaşılabilir rapor formatlarına dönüştürme ve dışa aktarma yeteneği eklemek.
  - **Kapsamlı Dokümantasyon ve Katkı Rehberleri:** Projeye dışarıdan katkıda bulunmak isteyen geliştiriciler için daha detaylı dokümantasyon (API referansları, mimari dokümanları) ve katkı rehberleri (CONTRIBUTING.md) hazırlamak.
  - **Docker Entegrasyonu (Kolay Dağıtım):** Projeyi Dockerize ederek, bağımlılık sorunları yaşamadan farklı ortamlarda kolayca kurulup çalıştırılabilmesini sağlamak.
  - **Potansiyel Teknolojiler:** Python web frameworkleri (Flask, Django), JavaScript/HTML/CSS (ön yüz için), Docker, Sphinx (dokümantasyon için).
    
## 5. Anahtar Sonraki Adımlar (Mevcut Odak)
```
 1. CS:GO, Valorant ve PUBG için kapsamlı ve detaylı pcap yakalama senaryolarının tamamlanması.
 2. Wireshark yakalama ve görüntüleme filtrelerinin her oyun için optimize edilmesi ve nihai hale getirilmesi.
 3. researchs klasörü altındaki her bir oyunun ağ analizi (örn. csgo_network_analysis.md, valorant_network_analysis.md)
 ve Wireshark filtreleri (wireshark_filters.md) hakkındaki Markdown dosyalarının içeriğinin detaylıca doldurulması.
 4. Projenin Python ile ilgili tüm bağımlılıklarını (eğer varsa) doğru bir şekilde listeleyen requirements.txt dosyasının oluşturulması ve güncel tutulması.
```

## 6. Katkıda Bulunma
Bu proje açık kaynaklıdır ve katkılara açıktır. Eğer projenin gelişimine yardımcı olmak isterseniz, lütfen CONTRIBUTING.md 
dosyasını inceleyin veya bir sorun (Issue) oluşturarak bizimle iletişime geçin. Her türlü katkı (kod, dokümantasyon, hata raporu, fikir) değerlidir.
