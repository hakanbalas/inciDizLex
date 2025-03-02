# inciDiz
Transkripsiyon İşaretli Metinlerden Otomatik Dizin Oluşturma Yazılımı

Osmanlıca ve Türkçe metinler için geliştirilmiş kapsamlı bir dizin oluşturma aracı. Bu araç, akademik metinler, sözlükler ve tarihî belgeler için dizin oluşturma işlemini otomatikleştirir.

## Özellikler

## Temel İşlevler

- **Dizin Oluşturma**: Metin dosyasındaki kelimeleri temel alarak alfabetik sıralı dizin oluşturur.
- **Kelime Normalizasyonu**: Kelimeleri normalleştirir (küçük harfe çevirme, transkripsiyon işaretlerini dönüştürme).
- **Akıllı Sıralama**: Transkripsiyon işaretlerini dikkate alarak doğru alfabetik sıralama yapar.
- **Hata Kontrolü**: Geçersiz karakterler içeren kelimeleri tespit eder ve ayrıntılı şekilde raporlar.
- **Madde Başı İstatistikleri**: Her kelimenin metinde kaç kez geçtiğini hesaplar ve raporlar.

---

## Dilbilimsel Özellikler

- **Ek ve Birleşik Kelime Analizi**: Kelimelerin kök ve eklerini ayırarak ayrıntılı analiz yapar.
- **Eş Sesli Kelime İşleme**: Aynı yazılışa sahip farklı anlamlı kelimeleri (`kelime+(1)`, `kelime+(2)` formunda) doğru şekilde işleyebilme.
- **Birleşik İfade Tespiti**: Metindeki bağlaçlarla (`ve`, `u`, `-ı` gibi) birleşik ifadeleri tespit eder.
- **Unicode Desteği**: Özel transkripsiyon işaretleri ve çeşitli alfabeler için tam Unicode desteği.

---

## Format Özellikleri

- **Yaprak/Satır Formatı Desteği**: Satır numaralarını standart veya "yaprak/satır" formatında (örn. `001a/02`) işleyebilme.
- **Esnek Girdi Formatı**: Farklı formatlardaki metin dosyalarını işleyebilme (`sayı.`, `sayı:`, yaprak/satır formatları).
- **Sayısal Satır Sıralama**: Satır numaralarını sıralarken sayısal değerleri dikkate alır (`1`, `2`, `10` şeklinde doğru sıralama).

---

## Çıktı Dosyaları

- **`...Dizin.txt`**: Ana dizin dosyası. Kelimelerin geçtiği satır numaralarını ve alt maddeleri içerir.
  
```bash
aldım: 1. [=1]
bahsediyorum: 2. [=1]
burada: 3. [=1]
kalem: 1. [=1]
kitāb: 1. [=1]
kitāb+dan: 2. [=1]
kitāb+(2): 3. [=1]
ve: 1. [=1]
```

- **`...MBS.txt`**: Her madde başının kaç kez geçtiğini gösteren dosya (Madde Başı Sayısı).
  
```bash
aldım: 1. [=1]
bahsediyorum: 2. [=1]
burada: 3. [=1]
kalem: 1. [=1]
kitāb: 1. [=1]
kitāb+dan: 2. [=1]
kitāb+(2): 3. [=1]
ve: 1. [=1]
```

- **`...Ek.txt`**: Kelime eklerini ve geçtiği satırları gösteren dosya.

```bash
aldım: 1. [=1]
bahsediyorum: 2. [=1]
burada: 3. [=1]
kalem: 1. [=1]
kitāb: 1. [=1]
kitāb+dan: 2. [=1]
kitāb+(2): 3. [=1]
ve: 1. [=1]
```

- **`...Sorun.txt`**: Geçersiz kelimeleri ve hataları içeren dosya.

```bash
aldım: 1. [=1]
bahsediyorum: 2. [=1]
burada: 3. [=1]
kalem: 1. [=1]
kitāb: 1. [=1]
kitāb+dan: 2. [=1]
kitāb+(2): 3. [=1]
ve: 1. [=1]
```

- **`...Birlesik.txt`**: Tespit edilen birleşik ifadeleri ve geçtiği satırları listeleyen dosya.

```bash
aldım: 1. [=1]
bahsediyorum: 2. [=1]
burada: 3. [=1]
kalem: 1. [=1]
kitāb: 1. [=1]
kitāb+dan: 2. [=1]
kitāb+(2): 3. [=1]
ve: 1. [=1]
```

---

## Geçerli Karakterler ve Transkripsiyon Desteği
Program şu karakter gruplarını destekler:

* Latin alfabesi (a-z, A-Z)
* Türkçe karakterler (ç, ğ, ı, ö, ş, ü, â)
* Transkripsiyon işaretleri (ā, ḍ, é, ḥ, vb.)
* Rakamlar ve bazı noktalama işaretleri


## Kurulum ve Kullanım

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
        1a/01 Bu bir örnektir.
        1a/02 Başka bir örnek.
        01 Bu bir örnektir.
        02 Başka bir örnek.
        ```

## Proje Yapısı

```python
python inciDiz.py

.
├── inciDiz.py            # Ana Python betiği
├── test01.txt            # Örnek giriş dosyası
├── test02.txt            # Örnek giriş dosyası
├── test03.txt            # Örnek giriş dosyası
├── README.md             # Bu README dosyası
└── ...
```

## Lisans

Bu proje GNU General Public License v3 altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## İletişim

Sorularınız veya önerileriniz için hakanbalas@hotmail.com ile iletişime geçebilirsiniz.
