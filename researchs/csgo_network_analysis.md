# CS:GO Ağ Bağlantıları Analiziü

Bu doküman, Counter-Strike: Global Offensive (CS:GO) oyununun ağ trafiğini, temel bağlantı noktalarını, kullanılan protokolleri ve sunucu tiplerini detaylı bir şekilde analiz etmeyi amaçlamaktadır. Elde edilen bulgular, oyunun ağ mimarisini anlamak, potansiyel performans sorunlarını tespit etmek ve güvenlik araştırmaları için temel bilgiler sunmak üzere derlenmiştir.

## 1. Giriş ve Amaç

Counter-Strike: Global Offensive (CS:GO), Valve tarafından geliştirilen ve milyonlarca oyuncuyu çevrimiçi olarak bir araya getiren popüler bir birinci şahıs nişancı oyunudur. Oyunun akıcı ve rekabetçi bir deneyim sunabilmesi için kararlı ve optimize edilmiş bir ağ altyapısı kritik öneme sahiptir. Bu analiz, CS:GO'nun ağ üzerinde nasıl iletişim kurduğunu, hangi portları ve protokolleri kullandığını, farklı sunucu tiplerinin (oyun sunucuları, Steam sunucuları, sesli sohbet sunucuları vb.) rollerini ve veri akışlarını incelemeyi hedeflemektedir.

## 2. Metodoloji (Nasıl Yakalandı?)

Ağ trafiği analizi için Wireshark kullanılarak farklı oyun senaryoları altında veri yakalama işlemleri gerçekleştirilmiştir.

### 2.1. Test Ortamı
  - **İşletim Sistemi:** Windows / Linux (Oyunun ve Wireshark'ın çalıştığı ortam)
  - **Ağ Bağlantısı:** Kablolu / Kablosuz (Tercihen stabil kablolu bağlantı)
  - **Yazılımlar:** CS:GO, Steam İstemcisi, Wireshark
    
### 2.2. Wireshark Yapılandırması

CS:GO trafiğini diğer ağ etkinliklerinden izole etmek için belirli Wireshark filtreleri kullanılmıştır.

### Capture Filtreleri (Veri Yakalama Öncesi):
  - ***Hedef Portlar Üzerinden Filtreleme:*** udp port 27015 or udp port 27020 or udp portrange 27031-27036 or udp port 4380 or tcp port 27015 or tcp port 27036 (Bu portlar genellikle CS:GO ve Steam için kullanılır.)
  - ***IP Adresi Filtreleme (isteğe bağlı):** Eğer belirli bir oyun sunucusunun veya Steam IP aralığının bilindiği durumlarda trafiği daha da daraltmak için kullanılabilir: host [IP_ADRESİ]

### Senaryolar (Trafik Yakalama Esnasında):
  - ***Oyun Başlatma ve Lobi:*** Steam ve oyunun başlangıçta yaptığı bağlantılar.
  - ***Matchmaking (Eşleştirme):*** Oyun arama ve sunucuya bağlanma süreci.
  - ***Maç İçi Oyun:*** Aktif bir oyun sırasında (hareket, atış, yetenek kullanımı) gerçekleşen trafik.
  - ***Sesli Sohbet:*** Oyun içi sesli iletişim (mikrofon kullanımı) sırasındaki trafik.
  - ***Maç Sonu/Skor Tablosu:*** Maç bittikten sonra sonuçların gönderilmesi ve istatistiklerin alınması.

# 3. Bulgular (Tespit Edilen IP'ler, Portlar, Protokoller)

CS:GO'nun ağ trafiği genellikle **UDP (User Datagram Protocol)** ağırlıklıdır, zira UDP, gerçek zamanlı uygulamalar için düşük gecikme süresi sunar. Ancak, Steam bağlantıları, indirmeler ve bazı kontrol mesajları için **TCP (Transmission Control Protocol)** de kullanılır.

## 3.1. Ana Kullanılan Portlar ve Protokoller

Genel olarak CS:GO ve Steam için açılması gereken veya gözlemlenen temel portlar şunlardır:

### Steam İstemcisi ve Oyun Trafiği (Genel):
- **UDP**: 27000-27100 (Oyun trafiği)
- **UDP**: 27015-27050 (Eşleştirme ve HLTV - Yayın sunucuları)
- **TCP**: 27015, 27036 (Oyun sunucuları, Steam indirmeleri)
- **TCP**: 80, 443 (HTTP/HTTPS - Genel Steam ve web tabanlı iletişim)

### Özel veya Dinleme Sunucuları (Dedicated/Listen Servers):
- **TCP**: 27015 (SRCDS Rcon portu - uzaktan kontrol)
- **UDP**: 27015 (Varsayılan oyun trafiği)

### Steamworks P2P (Peer-to-Peer) Ağı ve Steam Sesli Sohbet:
- **UDP**: 3478, 4379, 4380 (Giden trafik)
- **UDP**: 27014-27030 (Sesli sohbet ve P2P)

## 3.2. Steam Datagram Relay (SDR)

CS:GO, özellikle son zamanlarda, doğrudan oyun sunucularıyla iletişim kurmak yerine **Steam Datagram Relay (SDR)** protokolünü kullanmaktadır. SDR, Valve'ın özel sanal oyun ağıdır ve trafik istemci ile oyun sunucusu arasında bir Valve rölesi üzerinden yönlendirilir.

### Özellikleri:
- **DoS Koruması**: IP adresleri doğrudan açığa çıkmadığı için sunucuları ve oyuncuları DoS saldırılarından korur.
- **Geliştirilmiş Yönlendirme**: Çoğu durumda, Valve'ın omurgası üzerinden daha hızlı bir rota bularak oyuncu ping sürelerini iyileştirebilir.
- **Otomatik Röle Değişimi**: Bir röle saldırı altındaysa veya çevrimdışı olursa, istemci otomatik olarak başka bir röleye geçiş yapabilir.
- **Trafik Gözlemi**: SDR kullanılırken, bağlantı adresi doğrudan bir IP adresi yerine "=[A:n:nnnnnnn]" gibi bir formatta görünür. SDR röleleri genellikle oyun sunucuları ile aynı port aralığını (27015-27200) dinler.

## 3.3. Anti-Hile (VAC) Trafiği

**Valve Anti-Cheat (VAC)** sistemi, oyuncu bilgisayarlarında kurulu hileleri tespit etmek için tasarlanmış otomatik bir sistemdir. VAC, istemci ile sunucu arasında sürekli bir iletişim ("kalp atışı" paketi gibi) kurarak, VAC'ın istemcide düzgün çalıştığından emin olur.

### Gözlemlenecekler:
- VAC'ın belirli aralıklarla sunucuya gönderdiği doğrulama paketleri (Genellikle bu trafik, oyun trafiğiyle aynı portlar üzerinden şifreli bir şekilde akabilir).
- Hile yazılımlarının veya üçüncü parti müdahalelerin bu iletişimi kesintiye uğratması veya taklit etmeye çalışması durumunda ortaya çıkabilecek anormal desenler.
- VAC, hile imzalarını (cheat signatures) tespit etmek için çalışır ve oyunun çekirdek yürütülebilir dosyalarındaki veya dinamik bağlantı kütüphanelerindeki değişiklikleri izler.

## 3.4. Sesli İletişim Trafiği

CS:GO içi sesli sohbet, **Steamworks P2P Ağı** üzerinden işlenir.

### Gözlemlenecekler:
- Sesli sohbet trafiği genellikle **UDP protokolü** üzerinden, Steamworks P2P için belirtilen port aralıklarında (örn. UDP 27014-27030) gerçekleşir.
- WebRTC standart protokollerini kullanır ve giden UDP trafiği için 27014 ila 27020 portlarını kullanır.
- Trafik, genellikle şifrelidir.

## 3.5. Diğer Bağlantılar (Telemetry, Cloud Services)

### Telemetri Verileri:
Oyun, performans verilerini (FPS, ping, paket kaybı) ve diğer istatistikleri sunuculara veya Valve'ın telemetri hizmetlerine gönderebilir. Bu veriler, oyun deneyimini iyileştirm


