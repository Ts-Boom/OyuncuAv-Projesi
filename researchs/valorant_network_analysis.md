# Valorant Ağ Bağlantıları Analizi

Bu doküman, Riot Games tarafından geliştirilen taktiksel nişancı oyunu **Valorant**'ın ağ trafiğini, temel bağlantı noktalarını, kullanılan protokolleri ve sunucu altyapısını detaylı bir şekilde analiz etmeyi amaçlamaktadır. Elde edilen bulgular, oyunun ağ mimarisini anlamak, potansiyel performans sorunlarını tespit etmek ve güvenlik araştırmaları için temel bilgiler sunmak üzere derlenmiştir.

## 1. Giriş ve Amaç

Valorant, Riot Games'in küresel çapta popüler olan **5v5 taktiksel nişancı oyunudur**. Düşük gecikme süresi ve adil bir rekabet ortamı sunma misyonuyla yola çıkan Valorant, bu hedeflerini gerçekleştirmek için **Riot Direct** gibi özel ağ altyapılarını kullanmaktadır. Bu analiz, Valorant'ın ağ üzerinde nasıl iletişim kurduğunu, hangi portları ve protokolleri kullandığını, Riot Games'in sunucu mimarisini (özellikle Riot Direct ve AWS Global Accelerator kullanımı) ve oyunun anti-hile sistemi **Vanguard**'ın ağ üzerindeki etkileşimlerini incelemeyi hedeflemektedir.

## 2. Metodoloji (Nasıl Yakalandı?)

Ağ trafiği analizi için **Wireshark** kullanılarak farklı oyun senaryoları altında veri yakalama işlemleri gerçekleştirilmiştir.

### 2.1. Test Ortamı
- **İşletim Sistemi**: Windows (Valorant ve Wireshark'ın çalıştığı ortam)
- **Ağ Bağlantısı**: Kablolu / Kablosuz (Stabil kablolu bağlantı tercih edilir)
- **Yazılımlar**: Valorant İstemcisi, Riot İstemcisi, Wireshark

### 2.2. Wireshark Yapılandırması
Valorant trafiğini diğer ağ etkinliklerinden izole etmek için belirli **Wireshark filtreleri** kullanılmıştır.

#### Capture Filtreleri (Veri Yakalama Öncesi):
- **Hedef Portlar Üzerinden Filtreleme**: udp portrange 7000-8000 or udp portrange 8180-8181 or tcp port 2099 or tcp port 5222 or tcp port 5223 or tcp port 8393-8400 or tcp port 80 or tcp port 443
(Bu portlar Valorant ve Riot istemcisi için yaygın olarak kullanılır.)

- **IP Adresi Filtreleme** (isteğe bağlı): host [IP_ADRESİ]
Eğer belirli bir Riot veya AWS IP aralığının bilindiği durumlarda trafiği daha da daraltmak için kullanılabilir.

#### Senaryolar (Trafik Yakalama Esnasında):
- **Oyun Başlatma ve Riot İstemcisi Girişi**: İstemcinin Riot sunucularıyla ilk bağlantısı.
- **Lobi ve Parti Kurma**: Arkadaşlarla lobi oluşturma ve parti içi iletişim.
- **Matchmaking (Eşleştirme)**: Oyun arama ve sunucuya bağlanma süreci.
- **Maç İçi Oyun**: Aktif bir oyun sırasında (hareket, atış, yetenek kullanımı) gerçekleşen trafik.
- **Sesli Sohbet**: Oyun içi takım ve parti sesli iletişimi.
- **Maç Sonu/İstatistikler**: Maç bittikten sonra sonuçların gönderilmesi ve istatistiklerin alınması.

## 3. Bulgular (Tespit Edilen IP'ler, Portlar, Protokoller)

Valorant'ın ağ trafiği, gerçek zamanlı oyun verileri için ağırlıklı olarak **UDP (User Datagram Protocol)** kullanırken, istemci bağlantıları, güncellemeler, sohbet ve diğer kontrol mekanizmaları için **TCP (Transmission Control Protocol)** kullanır.

### 3.1. Ana Kullanılan Portlar ve Protokoller

Valorant ve Riot istemcisi için gözlemlenen veya gerekli olan temel portlar şunlardır:

#### Valorant Oyun İstemcisi Trafiği:
- **UDP**: 7000-8000 (Oyun içi genel trafik)
- **UDP**: 8180-8181 (Oyun içi ek trafik)

#### Riot Games İstemcisi (Giriş, Eşleştirme, Yama):
- **TCP**: 5223 (Riot Games İstemcisi, giriş, eşleştirme)
- **TCP**: 8393-8400 (Patcher ve Maestro - Güncellemeler)

#### Parti ve Oyun İçi Sohbet:
- **TCP**: 2099 (Parti ve oyun içi metin sohbeti)

#### HTTP/HTTPS Bağlantıları:
- **TCP**: 80 (HTTP bağlantıları)
- **TCP**: 443 (HTTPS bağlantıları)

#### Gözlemci Modu (Spectator Mode):
- **TCP/UDP**: 8088

#### Sesli Sohbet Port Aralıkları:
- **UDP**: 27016-27024 (Kuzey Amerika ve Avrupa bölgeleri için)
- **UDP**: 54000-54012 (Asya Pasifik ve Güneydoğu Asya bölgeleri için)
- **TCP**: 1024-65000 aralığından seçilen 50 port (Genel sesli sohbet için, yönlendirme tavsiye edilir)

### 3.2. Riot Direct ve Sunucu Altyapısı

Riot Games, düşük gecikme süresi ve stabil bağlantılar sağlamak amacıyla kendi ağ altyapısı **Riot Direct**'i kullanmaktadır. Bu, oyuncuların Riot'un dünya çapındaki **PoP (Point of Presence)** noktalarına bağlanarak, trafiğin en optimize rota üzerinden Riot'un kendi ağına iletilmesini sağlar.

- **Riot Direct'in Rolü**: Oyuncular ve Riot sunucuları arasındaki yolu optimize ederek ping sürelerini düşürür ve paket kaybını azaltır.
- **AWS Global Accelerator Kullanımı**: Valorant'ın bazı sunucuları (özellikle Asya Pasifik bölgesinde gözlemlenenler), **AWS Global Accelerator** gibi **Anycast IP** adreslerini kullanan hizmetlerden yararlanmaktadır. Bu, oyuncuların coğrafi olarak kendilerine en yakın sunucuya otomatik olarak yönlendirilmesini sağlar. Bu IP'ler, genellikle standart AWS/Amazon trafiğinden ayırt edilemez.

#### Tespit Edilen IP Adresi Örnekleri (AWS/Riot):
- **13.248.x.x**, **34.120.x.x**, **35.199.x.x**, **43.229.x.x**, **75.2.x.x**, **99.83.x.x**, **151.106.x.x** gibi IP aralıkları gözlemlenmiştir. Bu IP'ler Riot'un çeşitli bölgelerdeki sunucularına veya AWS altyapısına aittir.

### 3.3. Anti-Hile (Vanguard) Trafiği

**Riot Vanguard**, Valorant'ın kapsamlı anti-hile sistemidir. Oyunun çekirdeğiyle derinlemesine entegre olan bir kernel-mode sürücü ve bir istemci bileşeninden oluşur. Vanguard, hileleri aktif olarak tarar ve oyuncuların sistemlerindeki şüpheli davranışları izler.

- **Ağ Etkileşimleri**: Vanguard, oyun sunucularıyla ve Riot'un anti-hile altyapısıyla sürekli iletişim halinde olabilir. Bu iletişim, hile tespit verilerini göndermek, güncellemeleri almak veya sistem bütünlüğünü doğrulamak için kullanılır.
- **Tespit Mekanizmaları**: Vanguard'ın ağ trafiği üzerindeki varlığı, anormal trafik kalıplarını (örn. beklenmeyen port kullanımları, yüksek frekansta veri gönderimi) analiz ederek hile tespitine dair ipuçları sağlayabilir. Ancak, Vanguard'ın kendisi de trafiği gizleyebilir veya şifreleyebilir.
- **HWID Yasaklamaları**: Valorant, **IP yasaklarından** ziyade daha çok **donanım kimliği (HWID) yasaklamaları** kullanır, bu da IP adreslerinin tek başına bir oyuncuyu durdurmada yeterli olmadığını gösterir.

### 3.4. Sesli İletişim Trafiği

Valorant içi sesli sohbet, ayrı sunucular üzerinden gerçekleşir ve belirli port aralıklarını kullanır.

- **Protokol**: Genellikle **UDP** üzerinden yüksek performans ve düşük gecikme süresi için kullanılır.
- **Portlar**: Yukarıda 3.1. bölümde belirtilen **UDP** port aralıkları (27016-27024 veya 54000-54012) bölgesel olarak farklılık gösterebilir. Ek olarak, **TCP 1024-65000** aralığından 50 portluk bir aralık da önerilmektedir.

### 3.5. Diğer Bağlantılar (Telemetri, Oyun Hizmetleri)

#### Telemetri Verileri:
Valorant, oyun performansını, oyuncu hareketlerini, oyun içi kararları, yetenek kullanımlarını ve diğer metrikleri içeren kapsamlı telemetri verileri toplar. Bu veriler, oyun geliştirme, hata ayıklama ve performans iyileştirme için kullanılır. Bu trafik genellikle **HTTP/HTTPS (TCP 80/443)** veya özel portlar üzerinden Riot'un arka uç sistemlerine gönderilir.

#### Oyun Hizmetleri:
Maç oluşturma, arkadaş listesi, envanter yönetimi, mağaza erişimi gibi hizmetler **Riot Games** sunucularıyla **TCP** üzerinden (özellikle **2099**, **5222**, **5223** portları) iletişim kurar.

## 4. Wireshark Analiz Detayları ve İpuçları

Yakalanan pcap dosyalarının **Wireshark**'ta daha etkin incelenmesi için:

### Display Filtreleri:
- **Sadece Valorant trafiği**: udp.portrange 7000-8000 || udp.portrange 8180-8181 || tcp.port == 2099 || tcp.port == 5222 || tcp.port == 5223 || tcp.port >= 8393 && tcp.port <= 8400 || tcp.port == 80 || tcp.port == 443 || udp.portrange 27016-27024 || udp.portrange 54000-54012
- **Sadece UDP trafiği**: `udp`
- **Sadece TCP trafiği**: `tcp`
- **Belirli bir IP'ye giden/gelen trafik**: `ip.addr == [IP_ADRESİ]`
- **Belirli bir porttan geçen UDP trafiği**: `udp.port == [PORT_NUMARASI]`

### Protokol Hiyerarşisi (Protocol Hierarchy):
Trafikteki protokol dağılımlarını görselleştirir.

### Konuşmalar (Conversations):
Belirli IP-port çiftleri arasındaki trafik hacmini ve süresini gösterir. Özellikle **Riot Direct IP**'leri ile olan yoğun iletişimi gözlemlemek için faydalıdır.

### Akış Grafiği (Flow Graph):
**TCP/UDP akışlarının** zaman içindeki paket akışını görselleştirir.

### Paket Boyutları:
**len filtresi** (örn. `udp.length > 500`) anormal derecede büyük veya küçük paketleri tespit etmek için kullanılabilir.

## 5. Sonuç ve Değerlendirme

Valorant'ın ağ bağlantıları, düşük gecikme süreli oyun deneyimi için **UDP**'ye büyük ölçüde güvenmektedir. **Riot Direct** ve **AWS Global Accelerator** gibi gelişmiş ağ teknolojilerinin kullanımı, Riot Games'in küresel oyuncu kitlesine optimize edilmiş bağlantı sağlamaya verdiği önemi vurgulamaktadır. **Vanguard** gibi anti-hile sistemlerinin ağ etkileşimleri, güvenlik araştırmaları için karmaşık ancak ilgi çekici bir alan sunmaktadır.

Bu analiz, Valorant'ın ağ mimarisine dair temel bir anlayış sağlamakta ve daha derinlemesine güvenlik, performans veya zafiyet analizi çalışmaları için bir başlangıç noktası teşkil etmektedir. Özellikle **Riot Direct**'in rolü ve **Anycast IP** kullanımları, geleneksel IP tabanlı analiz yöntemlerinin ötesine geçmeyi gerektirebilir ve trafik analizini daha çok protokol içeriği ve davranışsal anormallikler üzerine odaklamayı teşvik eder.


