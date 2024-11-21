# YouTube Videosundan Sınav Notları Oluşturucu

Bu proje, bir YouTube videosunun metin transkriptini alarak üniversite öğrencilerinin sınav çalışmaları için önemli noktaları vurgulayan kısa ve odaklı özetler oluşturur. Özellikle sınavlarda çıkabilecek anahtar bilgilerin belirlenmesine yardımcı olur. 

## Özellikler
- YouTube videosundan otomatik transkript alma (Türkçe destekli).
- Öğrencilerin sınav çalışmaları için önemli noktaları 250 kelime içinde özetleme.
- Kolay ve kullanıcı dostu bir arayüz.

## Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki gereksinimlere ihtiyacınız var:
- **Python 3.8 veya üzeri**
- Gerekli kütüphaneler (kurulum talimatları aşağıda verilmiştir).

## Kurulum

1. **Projeyi klonlayın:**
   ```bash
   git clone https://github.com/canbingol/youtube_video_summarizer
2.Gerekli bağımlılıkları yükleyin: Sanal bir ortam oluşturup bağımlılıkları yüklemek için:
 ```bash
  python -m venv venv
  source venv/bin/activate  # Windows kullanıyorsanız: venv\Scripts\activate
  pip install -r requirements.txt
```
3. Google AI Studio API Key'i oluşturun:
- [Google AI Studio](https://aistudio.google.com/app/apikey) adresine gidin
- API erişimi için bir API Key oluşturun.

  4. .env dosyasını oluşturun ve API anahtarını ekleyin: Proje dizininde bir .env dosyası oluşturun:
  -Dosyanın içine şu satırı ekleyin:
 ```bash
GOOGLE_API_KEY="BURAYA_API_KEYİNİZİ_YAZIN"
```

Kullanım
Projeyi başlatmak için aşağıdaki komutu çalıştırın:
 ```bash
streamlit run app.py
```
Tarayıcınızda açılan arayüzde, YouTube Video Bağlantısını girin ve "Notları Al" butonuna tıklayın.
Sistem, videodan transkripti alır ve sınav çalışmaları için odaklı bir özet oluşturur.
## Uyarılar

⚠️ **Prompt Özelleştirilebilir:**  
Prompt, ihtiyaçlarınıza uygun şekilde değiştirilerek farklı türde özetler oluşturulabilir.

⚠️ **Türkçe Altyazı Gerekliliği:**  
Bu uygulama, sadece Türkçe altyazı içeren YouTube videoları için çalışmaktadır. Altyazı desteği olmayan videolarda özetleme yapılamaz.

aşağıdaki kod satırında 'tr' bölümünü istediğiniz dil ile değiştirerek istediğini video için özet oluşturabilirsiniz
 ```bash
transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['video_diliniz'])
```
