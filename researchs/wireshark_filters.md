# Wireshark Filtre Kılavuzu

Bu doküman, popüler çevrimiçi oyunların (**CS:GO**, **Valorant**, **PUBG**) ağ trafiğini yakalamak ve analiz etmek için kullanılan **Wireshark** filtrelerini detaylandırmaktadır. Hem yakalama (capture) hem de görüntüleme (display) filtrelerinin nasıl oluşturulacağı ve uygulanacağı hakkında pratik bilgiler sunulmaktadır. Doğru filtreleme, büyük miktardaki ağ verisi içinde hedeflenen trafiği hızla bulmak ve analizi kolaylaştırmak için kritik öneme sahiptir.

## 1. Giriş ve Amaç

**Wireshark**, ağ trafiği analizi için vazgeçilmez bir araçtır. Ancak, yoğun ağ ortamlarında yalnızca ilgili trafiği yakalamak ve görüntülemek zorlayıcı olabilir. Bu kılavuz, özellikle çevrimiçi oyunların karmaşık ve hızlı değişen ağ iletişimlerini izlemek için özel olarak tasarlanmış **Capture** ve **Display** filtrelerini sunmaktadır. Bu filtreler, analiz sürecini verimli hale getirmeyi ve istenmeyen gürültüyü eleyerek odaklanmayı amaçlar.

## 2. Wireshark Capture Filtreleri

**Capture filtreleri** (Yakalama Filtreleri), ağ arayüzünden veri yakalamaya başlamadan önce uygulanır. Bu filtreler, sadece belirli kriterlere uyan paketlerin kaydedilmesini sağlayarak **.pcap** dosyasının boyutunu küçültür ve disk alanı/işlem gücü tasarrufu sağlar. Bu filtreler, **BPF (Berkeley Packet Filter)** sözdizimini kullanır.

### 2.1. Genel Oyun Trafiği İçin Capture Filtreleri

Oyunlar genellikle **UDP** protokolünü kullandığından, başlangıç noktası olarak **UDP trafiğine** odaklanmak mantıklıdır.

- **Tüm UDP Trafiği**: udp
**Açıklama**: Ağdaki tüm **UDP** paketlerini yakalar. Çok fazla trafik olabilir.

- **Belirli Yaygın Oyun Portlarını Hedefleme**: udp portrange 27000-27200 or udp port 2099 or udp portrange 7000-8000 or udp portrange 8180-8181 or udp port 8080
**Açıklama**: Bu filtre, **CS:GO**, **Valorant** ve **PUBG** gibi oyunlar tarafından sıkça kullanılan yaygın **UDP** port aralıklarını kapsar.
- **27000-27200**: Çoğunlukla Steam (CS:GO) ve diğer Valve oyunları
- **2099, 7000-8000, 8180-8181**: Özellikle **Valorant** için
- **8080**: Çeşitli oyunlar (PUBG dahil) için genel bir oyun portu olabilir.

- **Belirli TCP Portlarını Dahil Etme (Oturum Açma, Güncellemeler vb.)**: tcp port 80 or tcp port 443 or tcp port 27015 or tcp port 27036 or tcp port 5222 or tcp port 5223 or tcp portrange 8393-8400
**Açıklama**: **HTTP/HTTPS** (**80, 443**), **Steam** (**27015, 27036**) ve **Riot Games** istemci/yama portlarını (**5222, 5223, 8393-8400**) dahil eder.

- **Yerel IP Adresinizi Hariç Tutma (Dışarıya Giden/Gelen Trafik İçin)**: ip and not host [YEREL_IP_ADRESİNİZ]
**Açıklama**: Kendi bilgisayarınızın yerel ağdaki **IP adresini** (192.168.1.X veya 10.0.0.X gibi) hariç tutarak sadece dış ağ ile olan trafiği yakalar. Bu, yerel ağ içi gürültüyü azaltır.

### 2.2. Oyunlara Özel Capture Filtreleri Örnekleri

#### **CS:GO için Optimize Edilmiş Capture Filtresi**: (udp port 27015 or udp port 27020 or udp portrange 27031-27036 or udp port 4380 or tcp port 27015 or tcp port 27036) and not host 192.168.1.X
**Açıklama**: **CS:GO**'nun temel **UDP** ve **TCP** portlarını hedeflerken, yerel ağ trafiğini dışarıda bırakır.

#### **Valorant için Optimize Edilmiş Capture Filtresi**: (udp portrange 7000-8000 or udp portrange 8180-8181 or tcp port 2099 or tcp port 5222 or tcp port 5223 or tcp portrange 8393-8400 or tcp port 80 or tcp port 443) and not host 192.168.1.X
**Açıklama**: **Valorant**'ın genel ve spesifik portlarını hedefler ve yerel ağdan gelen/giden trafiği filtreler.

#### **PUBG için Optimize Edilmiş Capture Filtresi**: (udp port 8080 or udp portrange 7000-7999 or tcp port 80 or tcp port 443) and not host 192.168.1.X
**Açıklama**: **PUBG**'nin bilinen portlarını ve **HTTP/HTTPS** trafiğini hedefler.

## 3. Wireshark Display Filtreleri

**Display filtreleri** (Görüntüleme Filtreleri), yakalama işlemi tamamlandıktan sonra veya canlı yakalama sırasında, yakalanan tüm paketler arasından belirli kriterlere uyanları "görüntülemek" için kullanılır. Bu filtreler, **Capture** filtrelerinden daha güçlü ve esnektir. **Wireshark**'ın kendi **Display Filter** sözdizimini kullanır.

### 3.1. Temel Görüntüleme Filtreleri

- **Belirli Bir Protokoldeki Tüm Paketler**:udp
tcp
dns
icmp


- **Kaynak veya Hedef IP Adresine Göre Filtreleme**:
ip.src == 1.2.3.4 # Kaynak IP 1.2.3.4 olan paketler
ip.dst == 5.6.7.8 # Hedef IP 5.6.7.8 olan paketler
ip.addr == 1.2.3.4 # Kaynak veya hedef IP 1.2.3.4 olan paketler

- **Belirli Bir Porta Göre Filtreleme**:
udp.port == 27015 # UDP 27015 portunu kullanan paketler
tcp.port == 443 # TCP 443 portunu kullanan paketler

- **Port Aralıkları ve Mantıksal Operatörler (AND/OR/NOT)**:
udp.port >= 27015 and udp.port <= 27030 # Belirli bir UDP port aralığı
tcp.port == 80 or tcp.port == 443 # TCP 80 veya 443 portu
not ip.addr == 192.168.1.1 # Belirli bir IP adresini hariç tutma


- **Paket Uzunluğuna Göre Filtreleme**:
frame.len > 1000 # 1000 byte'tan büyük paketler
udp.length < 50 # UDP veri bölümü 50 byte'tan küçük paketler (örn. kalp atışı)


- **Bayraklara Göre TCP Filtreleme**:
tcp.flags.syn == 1 and tcp.flags.ack == 0 # SYN paketleri (bağlantı kurma)
tcp.flags.push == 1 # PUSH bayraklı paketler (uygulama verisi)


### 3.2. Oyunlara Özel Görüntüleme Filtreleri Örnekleri

Bu filtreler, oyun trafiği analizi sırasında sıkça kullanılan kombinasyonlardır.

#### **CS:GO Trafiğini Ayrıştırma**:
(udp.port == 27015 || udp.port == 27020 || udp.port >= 27031 && udp.port <= 27036 || udp.port == 4380) || (tcp.port == 27015 || tcp.port == 27036)

**Açıklama**: **CS:GO**'ya özgü oyun, eşleştirme ve sesli sohbet portlarını bir araya getirir.

#### **Valorant Trafiğini Ayrıştırma**:
(udp.portrange 7000-8000 || udp.portrange 8180-8181 || udp.portrange 27016-27024 || udp.portrange 54000-54012) || (tcp.port == 2099 || tcp.port == 5222 || tcp.port == 5223 || tcp.portrange 8393-8400)

**Açıklama**: **Valorant**'ın oyun içi ve istemci portlarını kapsar. Sesli sohbetin bölgeye göre portlarının ayarlanması önemlidir.

#### **PUBG Trafiğini Ayrıştırma**: udp.port == 8080 || udp.portrange 7000-7999 || tcp.port == 8088

**Açıklama**: **PUBG**'nin genellikle kullandığı portları hedefler.

#### **Belirli Bir Oyun Sunucusu ile İletişimi Takip Etme**: ip.addr == [OYUN_SUNUCUSU_IP_ADRESİ] and (udp.port == [OYUN_PORTU] or tcp.port == [OYUN_PORTU])

**Açıklama**: Yakaladığınız spesifik bir oyun sunucusu IP'si ile olan iletişimi izlemek için kullanılır.

#### **DNS Sorgularını ve Yanıtlarını Görüntüleme (Sunucu Adı Çözümlemesi İçin)**: dns

**Açıklama**: Oyun istemcisinin sunucu adreslerini nasıl çözümlediğini görmek için önemlidir.

#### **Oyun İçi Sesli Sohbet Trafiği (Örnek)**: udp.port == 3478 || udp.port == 4379 || udp.port == 4380

**Açıklama**: **Steam** veya **Riot P2P/sesli sohbet** portları üzerinden geçen ses trafiğini gözlemlemek için kullanılabilir.

## 4. Filtreleri Uygulama İpuçları

- **Wireshark Arayüzü**: **Capture** filtreleri "Capture Options" penceresinde, **Display** filtreleri ise Wireshark'ın ana penceresindeki "Display Filter" çubuğuna yazılır.
- **Kaydetme ve Yükleme**: Sık kullanılan filtreleri kaydetmek için Wireshark'ın filtre kaydetme özelliğini kullanabilirsiniz. Bu, her seferinde tekrar yazmaktan kurtarır.
- **Kombinasyon**: Karmaşık senaryolar için birden fazla filtreyi **and**, **or**, **not** operatörleri ile birleştirmekten çekinmeyin. Parantez **()** kullanarak mantıksal gruplamalar yapın.
- **Deneme ve Yanılma**: Doğru filtreleri bulmak, biraz deneme ve yanılma gerektirebilir. Küçük bir trafik örneği yakalayarak filtrelerinizi test edin.

## 5. Sonuç

Etkili **Wireshark** filtreleri, ağ trafiği analizinin temelidir ve çevrimiçi oyunların karmaşık ağ yapısını anlamak için vazgeçilmezdir. Bu kılavuzda sunulan filtreler ve ipuçları, oyun trafiğini daha verimli bir şekilde yakalamanıza, ayrıştırmanıza ve analiz etmenize yardımcı olacaktır. Projenizin ilerleyen aşamalarında, **Python** gibi araçlarla bu filtrelerin otomatikleştirilmesi veya dinamik olarak oluşturulması da mümkündür.





  

