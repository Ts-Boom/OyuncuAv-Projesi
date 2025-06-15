m<div align="center">
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
| CS:GO Ağ Trafiği Analizi	      | [researchs/deepsearch.01.md](deepsearch.01.md) | Counter-Strike: Global Offensive oyununun ağ bağlantılarının, kullanılan IP adreslerinin, portların ve sunucuların detaylı analizi.* |
| Valorant Ağ Trafiği Analizi	  | [researchs/your-research-file.md](researchs/your-research-file.md) | Valorant oyununun ağ bağlantılarının, kullanılan IP adreslerinin, portların ve sunucuların detaylı analizi.* |
| Wireshark Filtre Kılavuzu       | *Link to your other research files*     | *Oyun trafiği yakalama ve analizi için özel olarak hazırlanmış Wireshark yakalama ve görüntüleme filtrelerinin detaylı kılavuzu.*                  |
| Oyun Sunucusu Konumları ve IP Havuzları      | *Link to your other research files*     | *Analiz edilen oyunların kullandığı sunucu konumları, IP havuzları ve olası CDN (İçerik Dağıtım Ağı) kullanımları hakkında araştırma.*                  |



---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python main.py --input your_file.pcap --output results.txt
```

**Steps**:  
1. Prepare input data (*explain data needed*).  
2. Run the script with arguments (*explain key arguments*).  
3. Check output (*explain where to find results*).  

*Adımlar*:  
1. Giriş verilerini hazırlayın (*ne tür verilere ihtiyaç duyulduğunu açıklayın*).  
2. Betiği argümanlarla çalıştırın (*önemli argümanları açıklayın*).  
3. Çıktıyı kontrol edin (*sonuçları nerede bulacağınızı açıklayın*).

---

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).  

*Topluluk katkilerini memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.*

---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Awesome Library: For enabling X.  
- Inspiration Source.  
- Special thanks to...  

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [Your Name/Org Name] - [your.email@example.com]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [Adınız/Kuruluş Adınız] - [e-posta.adresiniz@ornek.com]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*

# bilgilerinizi doldurmaniz gerekiyor. 🚫🚫🚫
