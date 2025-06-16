# Oyun Sunucusu Konumları ve IP Havuzları

Bu doküman, popüler çevrimiçi oyunlar (**CS:GO**, **Valorant**, **PUBG**) tarafından kullanılan sunucu konumlarını, IP havuzlarını ve temel altyapı sağlayıcılarını analiz etmeyi amaçlamaktadır. Oyunların küresel dağıtım stratejileri, düşük gecikme süresi sağlama yöntemleri ve bölgesel sunucu yaklaşımları incelenmektedir.

## 1. Giriş ve Amaç

Çevrimiçi oyunlarda düşük gecikme süresi (ping) ve kararlı bir bağlantı, rekabetçi ve keyifli bir oyun deneyimi için hayati öneme sahiptir. Bu, oyun geliştiricilerinin dünya genelinde stratejik olarak yerleştirilmiş sunucular ve gelişmiş ağ altyapıları kullanmasını gerektirir. Bu analiz, **CS:GO**, **Valorant** ve **PUBG** gibi oyunların sunucularının nerede bulunduğunu, hangi IP aralıklarını kullandığını ve oyun deneyimini optimize etmek için ne tür **CDN** (İçerik Dağıtım Ağı) veya özel ağ çözümlerinden yararlandıklarını araştırmaktadır.

## 2. Genel Oyun Sunucusu Altyapısı Yaklaşımları

Çevrimiçi oyunlar genellikle aşağıdaki yaklaşımları kullanarak sunucularını ve içeriklerini dağıtır:

### Dedicated Servers (Özel Sunucular):
- Oyun geliştiricisi veya üçüncü taraf hosting sağlayıcıları tarafından yönetilen, belirli oyun oturumlarına adanmış sunucular. Bu sunucular genellikle belirli coğrafi bölgelerde bulunur.

### Peer-to-Peer (P2P):
- Oyuncuların doğrudan birbirine bağlandığı, merkezi bir sunucuya daha az bağımlı olan bir model. Daha az yaygın olsa da bazı oyun modlarında veya daha eski oyunlarda görülebilir.

### Content Delivery Networks (CDN'ler):
- Oyun güncellemeleri, yama dosyaları ve oyun içi varlıklar gibi statik içeriği son kullanıcılara daha yakın konumlandırmak için kullanılır. **Akamai**, **Cloudflare** gibi sağlayıcılar popülerdir.

### Anycast IP Adresleri:
- Bir IP adresinin birden fazla coğrafi konumda duyurulmasıyla, kullanıcının en yakın ve en uygun sunucuya yönlendirilmesini sağlayan bir ağ tekniği. Özellikle **Riot Direct** ve **AWS Global Accelerator** gibi servisler tarafından kullanılır.

### Özel Ağ Altyapıları:
- Büyük oyun şirketlerinin (örn. Riot Direct, Steam Datagram Relay) ping sürelerini optimize etmek ve DDoS koruması sağlamak için kendi küresel ağ omurgalarını veya partner ağlarını kullanmaları.

## 3. Oyunlara Özel Sunucu Konumları ve IP Havuzları

### 3.1. **CS:GO Sunucu Konumları ve IP Havuzları**

**CS:GO**, hem Valve'ın resmi sunucularını hem de topluluk tarafından barındırılan sunucuları kullanır. Valve, özellikle **Steam Datagram Relay (SDR)** hizmetiyle trafiği optimize etmeyi ve sunucu IP'lerini gizlemeyi hedefler.

#### Valve Resmi Sunucuları (Steam Datagram Relay - SDR):
- **Küresel Dağıtım**: Valve'ın dünya çapında birçok "Point of Presence" (PoP) noktası bulunur. Bunlar arasında ABD (Sterling, Seattle, California), Avrupa (Stockholm, Frankfurt, Paris, Londra, Viyana, Polonya, İstanbul), Asya Pasifik (Singapur, Tokyo, Hong Kong, Mumbai, Sydney), Orta Doğu (Dubai), Güney Amerika (Sao Paulo) ve Güney Afrika (Cape Town) gibi büyük şehirler yer alır.

#### IP Havuzları:
- SDR trafiği belirli IP aralıkları üzerinden geçse de, oyunculara gösterilen IP'ler genellikle "=[A:n:nnnnnnn]" formatında olur ve gerçek sunucu IP'leri doğrudan ifşa edilmez. Bununla birlikte, Valve'ın mülkiyetindeki bilinen IP aralıkları (örneğin: **146.66.152.0/24**, **162.254.192.0/24**, **185.25.180.0/24**, **208.78.164.0/24**, **155.133.240.0/24** vb.) gözlemlenebilir.

#### Portlar:
- SDR röleleri ve oyun sunucuları genellikle **UDP 27015-27200** aralığını kullanır.

#### Topluluk Sunucuları:
- Bağımsız barındırıcılar veya oyuncu grupları tarafından dünya genelinde çeşitli lokasyonlarda barındırılır. Bu sunucuların IP adresleri ve portları genellikle oyun içi sunucu tarayıcılarda veya üçüncü taraf web sitelerinde doğrudan listelenir. Örneğin: `45.136.204.229:27015` (Rusya), `212.12.15.54:27018` (Rusya), `91.211.118.150:27035` (Avrupa).

### 3.2. **Valorant Sunucu Konumları ve IP Havuzları**

**Riot Games**, Valorant için özel ağı **Riot Direct** ve bulut sağlayıcılarını (başta **AWS**) birleştirerek düşük gecikmeli bir deneyim sunar.

#### Riot Direct (POP Noktaları):
- Riot'un kendi fiber optik ağı üzerinden trafiği optimize eden küresel erişim noktalarıdır.
- **Bölgeler**: Kuzey Amerika (US West/East/Central), LATAM (Santiago, Mexico City, Miami), Brezilya, Avrupa (Frankfurt, Paris, Stockholm, İstanbul, Londra, Varşova, Madrid, Bahreyn), Kore, Asya Pasifik (Hong Kong, Tokyo, Singapur, Sydney, Mumbai).

#### AWS Global Accelerator Kullanımı:
- Özellikle Asya Pasifik gibi bölgelerde, Riot sunucuları **AWS Global Accelerator** gibi **Anycast IP** hizmetlerini kullanır. Bu IP'ler, kullanıcıyı otomatik olarak en yakın AWS Edge konumuna yönlendirir.

#### IP Havuzları (Örnekler):
- **13.248.x.x**, **34.120.x.x**, **35.199.x.x**, **43.229.65.1 (AP)**, **75.2.x.x**, **99.83.x.x**, **151.106.x.x** (Singapur: **151.106.248.1**, Mumbai: **151.106.246.1**). Bu IP aralıkları genellikle **Amazon'a (AS16509)** ait olarak görünür.

#### Portlar:
- **UDP 7000-8000**, **8180-8181** (oyun trafiği), **TCP 2099**, **5222-5223**, **8393-8400** (istemci/yama). 
- Sesli sohbet için bölgesel **UDP portları** (örn. NA/EU için **27016-27024**, AP/SE için **54000-54012**).

### 3.3. **PUBG Sunucu Konumları ve IP Havuzları**

**PUBG**, ağırlıklı olarak bulut hizmeti sağlayıcılarını (başta **Amazon Web Services - AWS** ve **Tencent Cloud**) kullanarak küresel sunucu altyapısını yönetir.

#### AWS Bölgeleri:
- **PUBG**, dünya genelindeki çeşitli **AWS** bölgelerinde sunucular barındırır.
- **Bölgeler**: ABD (Doğu, Batı, Ohio, Kuzey Kaliforniya, Oregon), Avrupa (İrlanda, Frankfurt, Londra), Asya Pasifik (Tokyo, Seul, Singapur, Sydney), Güney Amerika (Sao Paulo) gibi AWS bölgeleri yaygın olarak kullanılır.

#### IP Havuzları (Örnekler):
- AWS IP aralıkları çok geniştir ve sürekli değişebilir. Örnek IP'ler: **13.x.x.x**, **18.x.x.x**, **34.x.x.x**, **35.x.x.x**, **52.x.x.x**, **54.x.x.x** ile başlayan geniş havuzlar. Özellikle **52.200.x.x** gibi belirli aralıklar sıkça görülür.

#### Tencent Cloud:
- Özellikle **PUBG Mobile** gibi versiyonlar için **Tencent Cloud** altyapısı da kullanılır. Çin ve bazı Asya bölgelerindeki sunucular bu sağlayıcıya ait olabilir.
- **IP Örnekleri**: **162.62.115.42** (Almanya'da gözlemlenen Tencent Cloud IP'si).

#### Portlar:
- **PUBG** için yaygın olarak **UDP 8080** (oyun içi), **UDP 7000-7999** (oyun içi ve diğer hizmetler), **TCP 80/443** (güncellemeler ve web tabanlı iletişim) gibi portlar kullanılır.

## 4. Tespit Metodolojisi ve İpuçları

Oyun sunucularının ve IP havuzlarının tespiti için çeşitli araçlar ve teknikler kullanılabilir:

- **Wireshark ile Trafik Yakalama**: Oyun oynarken veya lobi/eşleştirme ekranlarında Wireshark ile ağ trafiği yakalamak, doğrudan bağlantı kurulan IP adreslerini ve kullanılan portları gözlemlemek için en temel yöntemdir.
- **Statistics > Conversations**: En çok trafik alışverişi yapılan IP adreslerini ve portları hızlıca tespit etmenizi sağlar.
- **Statistics > Endpoints**: Bağlantı kurulan tüm uç noktaları listeler.
- **netstat Komutu (Windows/Linux)**: Oyun çalışırken komut istemcisinde `netstat -n -o` (Windows) veya `netstat -tulnp` (Linux) komutlarını kullanarak aktif TCP/UDP bağlantılarını ve ilgili işlem ID'lerini görebilirsiniz. Oyunun PID'ini (Process ID) Task Manager/Kaynak İzleyici üzerinden bulup, netstat çıktısında bu PID'e sahip harici IP'leri filtreleyebilirsiniz.
- **tracert / traceroute Komutu**: Oyun sunucusunun IP adresini öğrendikten sonra, bu IP adresine `tracert` (Windows) veya `traceroute` (Linux/macOS) komutunu kullanarak paketin hedefe ulaşana kadar geçtiği tüm yönlendiricileri ve coğrafi konumları (her hop için) izleyebilirsiniz. Bu, sunucunun fiziksel konumuna dair ipuçları verebilir.
- **IP Sorgulama Araçları (Online IP Lookup)**: Tespit edilen IP adreslerini **whois.arin.net** (Kuzey Amerika), **whois.ripe.net** (Avrupa), **whois.apnic.net** (Asya Pasifik) gibi WHOIS servislerinde veya **ipinfo.io**, **whatismyipaddress.com/ip-lookup** gibi online IP sorgulama sitelerinde aratarak ilgili IP adresinin ait olduğu kuruluş (AWS, Google Cloud, Riot Games vb.), ASN (Autonomous System Number) ve genellikle coğrafi konumu hakkında bilgi edinebilirsiniz.
- **Oyun İçi Konsol Komutları**: Bazı oyunlar (örn. **CS:GO**'da **status** veya **net_graph** benzeri komutlar) bağlı olduğunuz sunucunun IP adresini veya ağ istatistiklerini gösterebilir.

## 5. Sonuç ve Değerlendirme

Oyunların sunucu konumları ve IP havuzları analizi, modern çevrimiçi oyunların karmaşık ağ altyapılarını ortaya koymaktadır. **Valve**'ın **SDR**'si ve **Riot Games**'in **Riot Direct**'i gibi özel ağ çözümleri, gecikmeyi azaltma ve güvenliği artırma konusunda önemli adımlar atmıştır. **PUBG** gibi oyunların bulut sağlayıcılarına (**AWS**, **Tencent Cloud**) bağımlılığı, dinamik ve ölçeklenebilir bir altyapı sunarken, aynı zamanda IP havuzlarının geniş ve değişken olmasına neden olmaktadır.

Bu bulgular, oyunlardaki ağ sorunlarını teşhis etmek, potansiyel güvenlik zafiyetlerini (örn. **DDoS hedefleri**) belirlemek ve genel ağ performansı hakkında bilgi edinmek için kritik öneme sahiptir. Analizler, IP adreslerinin coğrafi dağılımının yanı sıra, her oyunun kendine özgü ağ mimarisi yaklaşımının da anlaşılması gerektiğini göstermektedir.

