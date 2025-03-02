# inciDiz
Transkripsiyon İşaretli Metinlerden Otomatik Dizin Oluşturma Yazılımı

# Transkripsiyon İşaretli Metinlerden Otomatik Dizin Oluşturma Yazılımı

Bu araç, metin dosyalarını işleyerek dizin oluşturma, kelime analizi yapma ve çeşitli raporlar üretme amacıyla geliştirilmiştir. Özellikle eski Türkçe metinlerin incelenmesi ve dizinlenmesi için tasarlanmıştır.

## Özellikler

*   **Dizin Oluşturma:** Metin dosyasındaki kelimeleri temel alarak dizin oluşturur.
*   **Kelime Normalizasyonu:** Kelimeleri normalleştirir (küçük harfe çevirme, transkripsiyon işaretlerini dönüştürme).
*   **Hata Kontrolü:** Geçersiz karakterler içeren kelimeleri tespit eder ve raporlar.
*   **Ek ve Birleşik Kelime Analizi:** Kelimelerin kök ve eklerini ayırarak analiz yapar.
*   **Birleşik İfade Tespiti:** Metindeki birleşik ifadeleri (örneğin, "ve", "u", "-ı" bağlaçları ile oluşan) tespit eder.
*   **Çıktı Dosyaları:**
    *   **Dizin Dosyası:** Kelimelerin geçtiği satır numaralarını içeren dizin.
    *   **Madde Başı Sayısı (MBS) Dosyası:** Her madde başının kaç kez geçtiğini gösteren dosya.
    *   **Ek Dosyası:** Kelime eklerini ve geçtiği satırları gösteren dosya.
    *   **Sorunlu Kelimeler Dosyası:** Geçersiz kelimeleri ve hataları içeren dosya.
    *   **Birleşik İfadeler Dosyası:** Tespit edilen birleşik ifadeleri ve geçtiği satırları içeren dosya.
*   **Yaprak/Satır Formatı Desteği:** Satır numaralarını "yaprak/satır" formatında işleyebilme.
*   **Homofon (Eş Sesli) Kelime İşleme:** Eş sesli kelimeleri ve varyasyonlarını doğru şekilde işleyebilme.

## Nasıl Kullanılır

1.  **Gereksinimler:**
    *   Python 3.x
    *   Gerekli kütüphaneler: `re`, `collections`, `os`, `unicodedata` (genellikle Python ile birlikte gelir).

2.  **Kurulum:**

    *   Bu depoyu klonlayın:
        ```bash
        git clone [repo_url]
        cd [repo_dizini]
        ```

3.  **Kullanım:**

    *   Aracı çalıştırmak için:
        ```bash
        python inciDiz.py
        ```

    *   Aracı çalıştırdıktan sonra, aşağıdaki sorulara yanıt vermeniz gerekecektir:
        *   Her madde başından sonra kaç defa geçtiği yazılsın mı? (E/H)
        *   Yaprak/satır formatı kullanılsın mı? (E/H)
        *   Birleşik ifadeler dizini oluşturulsun mu? (E/H)

4.  **Dosya Formatı:**

    *   Giriş dosyası (`.txt`) aşağıdaki formatta olmalıdır:
        ```
        SatırNumarası: Metin içeriği
        ```
        veya
         ```
        YaprakNo/SatirNo Metin içeriği
        ```
        Örneğin:
        ```
        1: Bu bir örnektir.
        2: Başka bir örnek.
        001a/01 Bu bir örnektir.
        001a/02 Başka bir örnek.
        ```

## Örnek

```python
python inciDiz.py

.
├── inciDiz.py          # Ana Python betiği
├── test.txt            # Örnek giriş dosyası
├── test2.txt            # Örnek giriş dosyası
├── README.md           # Bu README dosyası
└── ...


## Lisans

[Lisans Türü] altında lisanslanmıştır.

## İletişim

Sorularınız veya önerileriniz için [e-posta adresiniz] ile iletişime geçebilirsiniz.
