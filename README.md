<div align="center">
  <img src="https://img.shields.io/github/languages/count/keyvanarasteh/Project?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/keyvanarasteh/Project?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/keyvanarasteh/Project?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/keyvanarasteh/Project?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# Oyuncu Avı Projesi
Bu proje, çevrimiçi oyunların ağ trafiğini analiz etmeyi ve oyunlara bağlanırken kullanılan IP adreslerini, sunucuları ve portları tespit etmeyi amaçlamaktadır. Popüler oyunlar olan CS:GO, Valorant, PUBG gibi oyunlar örnek alınarak, bu oyunların sunucularıyla iletişim kurarken hangi IP adreslerine ve portlara bağlandığı araştırılacaktır. Wireshark kullanılarak oyun trafiği yakalanacak ve bu trafiği analiz etmek için gerekli filtreler oluşturulacaktır.

Proje, oyuncu ve oyun sunucusu arasındaki ağ bağlantılarını detaylı bir şekilde inceleyerek, ağ güvenliği ve olası sızma testlerine yönelik önemli bilgiler sağlamayı hedefler.

---

## Features / *Özellikler*

- **Ağ Trafiği Analizi:** Bu proje, popüler çevrimiçi oyunların ağ trafiğini detaylı bir şekilde analiz etmenizi sağlar. Wireshark kullanarak, oyunlara bağlanırken kullanılan IP adreslerini, sunucuları ve portları tespit edebilirsiniz.
- **Gerçek Zamanlı İzleme:** Oyun oynarken gerçek zamanlı olarak ağ trafiğini izleyebilir, oyun sunucusuyla bağlantı kurulan IP'leri ve portları anında tespit edebilirsiniz.
- **Özelleştirilmiş Filtreleme:** Wireshark’ta oyun trafiğini izlemek için özel Capture Filters ve Display Filters oluşturma yeteneği sunar. Bu sayede yalnızca oyun trafiğine odaklanabilir, gereksiz verilerden arındırabilirsiniz.
- **Ağ Güvenliği İçin Uygulama:** Bu proje, çevrimiçi oyunlardaki ağ güvenliğini test etmenizi sağlar. Oyun sunucusuna ve IP bağlantılarına dair derinlemesine analiz yaparak potansiyel güvenlik açıklarını belirleyebilirsiniz.
  
---

## Team / *Ekip*

- **2420191020** - Taha SAYIN: Proje Yöneticisi

  
---


## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*        | Link                                    | Description / *Açıklama*                        |
|-------------------------|-----------------------------------------|------------------------------------------------|
| CS:GO Ağ Trafiği Analizi	      | [researchs/csgo_network_analysis.md](researchs/csgo_network_analysis.md) | Counter-Strike: Global Offensive oyununun ağ bağlantılarının, kullanılan IP adreslerinin, portların ve sunucuların detaylı analizi.* |
| Valorant Ağ Trafiği Analizi	  | [researchs/valorant_network_analysis.md](researchs/valorant_network_analysis.md) | Valorant oyununun ağ bağlantılarının, kullanılan IP adreslerinin, portların ve sunucuların detaylı analizi.* |
| Wireshark Filtre Kılavuzu       | [researchs/wireshark_filters.md](researchs/wireshark_filters.md)     | *Oyun trafiği yakalama ve analizi için özel olarak hazırlanmış Wireshark yakalama ve görüntüleme filtrelerinin detaylı kılavuzu.*                  |
| Oyun Sunucusu Konumları ve IP Havuzları      | [researchs/game_server_locations.md](researchs/game_server_locations.md)     | *Analiz edilen oyunların kullandığı sunucu konumları, IP havuzları ve olası CDN (İçerik Dağıtım Ağı) kullanımları hakkında araştırma.*                  |



---

## Installation / *Kurulum*

# Kurulum

Bu proje, popüler çevrimiçi oyunların ağ bağlantılarını analiz etmek için tasarlanmıştır. Projeyi kendi sisteminizde kurmak ve çalıştırmak için aşağıdaki adımları takip ediniz.

## Ön Gereksinimler

Projeyi başarıyla kurup çalıştırabilmeniz için sisteminizde aşağıdaki yazılımların yüklü olması gerekmektedir:

- **Python 3.x** (Tercihen 3.8 ve üzeri)  
  [Python.org](https://www.python.org) adresinden indirilebilir.  
  Kurulum esnasında **"Add Python to PATH"** seçeneğini işaretlemeyi unutmayın.

- **pip**: Python paket yöneticisi. Python 3.x ile birlikte gelir.

- **Git**: Proje deposunu klonlamak için.  
  [Git'i buradan indirin](https://git-scm.com)

- **Wireshark**: Ağ trafiği yakalama ve manuel analiz için.  
  [Wireshark'ı buradan indirin](https://www.wireshark.org)  
  Kurulum esnasında **Npcap sürücüsünü kurmayı onayladığınızdan** emin olun.

- **Hedef Oyunlar**: Analiz etmek istediğiniz oyunlar sisteminizde kurulu ve çalışır durumda olmalıdır:
  - **CS:GO** – Steam üzerinden
  - **Valorant** – Riot Games istemcisi üzerinden
  - **PUBG** – Steam üzerinden

---

## Adım Adım Kurulum

Projeyi kurmak ve çalıştırmak için aşağıdaki komutları terminalinizde veya komut istemcinizde sırasıyla uygulayın:

### 1. Proje Deposunu Klonlayın

```
git clone https://github.com/Ts-Boom/OyuncuAv-Projesi.git
```
### 2. Proje Dizinine Girin

```
cd OyuncuAv-Projesi
```

### 3. Python Sanal Ortamı Oluşturun (Önerilir)
```
python -m venv venv
```

### 4. Sanal Ortamı Etkinleştirin

**Windows**
```
.\venv\Scripts\activate
```

**Linux/macOS:**

```
source venv/bin/activate
```

## 5. Gerekli Python Kütüphanelerini Yükleyin

```
pip install -r requirements.txt
```

# Çalıştırma

Proje kurulumu tamamlandıktan sonra, analizleri başlatmak için aşağıdaki genel adımları izleyebilirsiniz. Projenin spesifik scriptleri ve kullanım detayları için `scripts/` klasöründeki ilgili dosyalara ve onların kendi dökümantasyonlarına başvurunuz.

---

## 1. Wireshark ile Ağ Trafiğini Yakalayın

1. **Wireshark** uygulamasını açın.
2. `Capture > Options` menüsünden uygun ağ adaptörünüzü seçin (genellikle internete bağlandığınız adaptör).
3. **Capture Filtreleri** alanına, analiz etmek istediğiniz oyunun trafik filtrelerini girin (bkz. `researchs/wireshark_filters.md`).
4. Yakalamayı başlatın ve analiz etmek istediğiniz oyunu çalıştırarak ilgili senaryoları (lobi, maç içi vb.) gerçekleştirin.
5. Yakalama bittikten sonra `File > Save As` ile `.pcapng` veya `.pcap` uzantılı olarak kaydedin.  
   Örn: `captures/csgo_match_1.pcapng`

---

## 2. Otomatik Analiz Scriptlerini Çalıştırın  
*(Eğer varsa ve ilgili kilometre taşlarına ulaşıldıysa)*

1. Sanal ortamınızın etkin olduğundan emin olun.
2. Proje dizininde (örneğin `Project/`) aşağıdaki komutları kullanarak Python analiz scriptlerini çalıştırabilirsiniz:

   ```
   python scripts/analyze_csgo_pcap.py captures/csgo_match_1.pcapng
   # Veya:
   python scripts/analyze_valorant_pcap.py captures/valorant_match_2.pcapng
   ```
3. Not: scripts/ klasöründeki dosyaların adları ve kullanım şekilleri projenizin ilerleyişine göre farklılık gösterebilir. Lütfen ilgili script dosyasının içindeki veya yanındaki açıklamalara bakın.

**Bu adımları takip ederek projenizi sorunsuz bir şekilde kurabilir ve analizlere başlayabilirsiniz. Herhangi bir sorunla karşılaşırsanız, lütfen projenin Issues bölümünde bir sorun (issue) oluşturmaktan çekinmeyin.**
    
## Lisans

Bu proje, **MIT Lisansı** kapsamında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.
