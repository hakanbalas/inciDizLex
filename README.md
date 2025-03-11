# inciDizLex
Transkripsiyon İşaretli Metinlerden Otomatik Dizin Oluşturma Yazılımı

Osmanlıca ve Türkçe metinler için geliştirilmiş kapsamlı bir dizin oluşturma aracı. Bu araç, Türkoloji çalışmaları, akademik metinler, sözlükler ve tarihî belgeler için dizin oluşturma işlemini otomatikleştirir.

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

- **Yaprak/Satır Formatı Desteği**: Satır numaralarını standart veya "yaprak/satır" formatında (örn. `1a/02`) işleyebilme.
- **Esnek Girdi Formatı**: Farklı formatlardaki metin dosyalarını işleyebilme (`sayı.`, `sayı:`, yaprak/satır formatları).
- **Sayısal Satır Sıralama**: Satır numaralarını sıralarken sayısal değerleri dikkate alır (`1`, `2`, `10` şeklinde doğru sıralama).

---
## test04.txt Girdi Dosyası (377'nci satırda text04.tx dosya ismi değiştirilerek kullanılır)

```bash
1: ādem ki öz+ün bil.mez ol+ur kör ne yig+i var göz+i gör.se gör
2: yol+da yit.en kisi+den sor+ar+lar akıl az.sa ne fayda bin.se at kör
3: dil+den çık.an söz+ü tut.ar gönül sert ol.an+dan düşman bul+ur bülbül+(1)
.
.
.
.
15: akıl er+se yol+da kal.maz kisi yig ol+ur kim öz+ün bil.e esi 1q 2q
16: tavar+dan yig+i yok ādem+i gör ne ki hayvān+dan, ayır+ır bir kör
17: yol+da yit.me.z ol+an gönül+ü dur az+an kisi+den ne fayda+dur 1 ve 2
```

## Çıktı Dosyaları

- **`...Dizin.txt`**: Ana dizin dosyası. Kelimelerin geçtiği satır numaralarını ve alt maddeleri içerir.
  
```bash
1: 17. [=1]
1q: 15. [=1]
2: 17. [=1]
2q: 15. [=1]
adam: 9. [=1]
ādem: 1, 4, 8, 10, 13, 16. [=6]
	ādem+i: 4, 16. [=2]
	ādem-i: 13. [=1]
ādemi: 8, 10. [=2]
	ādemi+den: 10. [=1]
akıl: 2, 5, 9, 15. [=4]
	akıl+ı: 5. [=1]
	akıl+ıdur: 9. [=1]
at: 2, 7, 11. [=3]
ayır: 4, 16. [=2]
	ayır+ır: 4, 16. [=2]
az: 2, 4, 7, 11, 13, 17. [=6]
	az+an: 17. [=1]
	az+maz: 13. [=1]
	az+sa: 7. [=1]
	az.an: 11. [=1]
	az.sa: 2. [=1]
ben: 5. [=1]
	ben.zer: 5. [=1]
bil: 1, 15. [=2]
	bil.e: 15. [=1]
	bil.mez: 1. [=1]
bin: 2, 11. [=2]
	bin.se: 2, 11. [=2]
bin.en: 7. [=1]
	bin.en+den: 7. [=1]
bir: 16. [=1]
bul: 3, 6, 12, 14. [=4]
	bul+an: 6. [=1]
	bul+ur: 3, 6, 12, 14. [=4]
bülbül: [=1]
bülbül+(1): 3. [=1]
can: [=2]
	can+ı: 4. [=1]
can+(1): 12. [=1]
can+(2): 12. [=1]
ci: 8. [=1]
degül: 10. [=1]
dil: 3, 6, 14. [=3]
	dil+den: 3, 6. [=2]
dost: 6, 14. [=2]
dur: 7, 17. [=2]
düşman: 3, 6, 12, 14. [=4]
	düşman+ı: 6, 12. [=2]
er: 13, 15. [=2]
	er+idur: 13. [=1]
	er+se: 15. [=1]
esek: 10. [=1]
esi: 15. [=1]
fayda: 2, 17. [=2]
	fayda+dur: 17. [=1]
gibi: 9. [=1]
gönül: 3, 13, 17. [=3]
	gönül+ü: 17. [=1]
gör: 1, 16. [=2]
	gör.se: 1. [=1]
göz: 1. [=1]
	göz+i: 1. [=1]
hayvān: 4, 8. [=2]
	hayvān+dan: 4. [=1]
her: 10. [=1]
igi: 6, 14. [=2]
it: 5, 9. [=2]
	it+e: 5. [=1]
iç: 4. [=1]
	iç.mek: 4. [=1]
kal: 15. [=1]
	kal.maz: 15. [=1]
ki: 1, 8, 14, 16. [=4]
kim: 5, 9, 11, 15. [=4]
	kim+dir: 5. [=1]
kisi: 2, 9, 11, 15, 17. [=5]
	kisi+den: 2, 11, 17. [=3]
kov: 8. [=1]
kov.ar: 8. [=1]
kov.ar: 4. [=1]
	kov.ar+sa: 4. [=1]
kul: 12. [=1]
	kul+ur: 12. [=1]
kör: 1, 2, 16. [=3]
naz: 4. [=1]
ne: 1, 2, 5, 7, 11, 16, 17. [=7]
ni: 10. [=1]
ofiat: 11. [=1]
ol: 1, 5, 7, 8, 9, 10, 11, 12, 14, 15, 17. [=11]
	ol+an: 17. [=1]
	ol+an+dan: 12. [=1]
	ol+ur: 1, 5, 7, 14, 15. [=5]
	ol.a: 10. [=1]
ol.an: 3. [=1]
	ol.an+dan: 3. [=1]
sek: 10. [=1]
ser: 5. [=1]
sert: 3, 6, 12, 14. [=4]
sol: 8. [=1]
sor: 2. [=1]
	sor+ar+lar: 2. [=1]
söz: 3, 6, 14. [=3]
	söz+den: 6, 14. [=2]
	söz+ü: 3. [=1]
tala: 9. [=1]
	tala.ya: 9. [=1]
tatlı: 6, 14. [=2]
	tatlı+dur: 14. [=1]
	tatlı+dır: 6. [=1]
tavar: 5, 8, 9, 10, 16. [=5]
	tavar+dan: 5, 9, 10, 16. [=4]
tut: 3. [=1]
	tut.ar: 3. [=1]
uyi: 8. [=1]
	uyi.mak: 8. [=1]
var: 1, 5, 11. [=3]
ve: 17. [=1]
vü: 8. [=1]
yavuz: 10. [=1]
yaya: 7, 11. [=2]
	yaya+dan: 7. [=1]
yeg: 10. [=1]
yi: 4, 8. [=2]
	yi.mek: 4, 8. [=2]
yig: 1, 5, 6, 7, 9, 10, 11, 14, 15, 16. [=10]
	yig+i: 1, 5, 6, 9, 14, 16. [=6]
yit: 2, 13, 17. [=3]
	yit.en: 2. [=1]
	yit.me.z: 13, 17. [=2]
yok: 5, 9, 16. [=3]
yol: 2, 7, 11, 13, 15, 17. [=6]
	yol+da: 2, 15, 17. [=3]
	yol+dan: 13. [=1]
yolda: 13. [=1]
yüri: 7, 11. [=2]
	yüri.ye: 11. [=1]
	yüri.yen: 7. [=1]
çare: 7. [=1]
çık: 3. [=1]
	çık.an: 3. [=1]
çık.ar: 13. [=1]
	çık.ar+an: 13. [=1]
öz: 1, 15. [=2]
	öz+ün: 1, 15. [=2]

Toplam kelime: 188
Geçerli kelime: 187
Geçersiz kelime: 1
Alt madde: 93
Madde başı: 83
```

- **`...MBS.txt`**: Her madde başının kaç kez geçtiğini gösteren dosya (Madde Başı Sayısı).
  
```bash
1:	[=1]
1q:	[=1]
2:	[=1]
2q:	[=1]
adam:	[=1]
ādem:	[=6]
ādemi:	[=2]
akıl:	[=4]
at:	[=3]
ayır:	[=2]
az:	[=7]
ben:	[=1]
bil:	[=2]
bin:	[=2]
bin.en:	[=1]
bir:	[=1]
bul:	[=5]
bülbül:	[=1]
bülbül+(1):	[=1]
can:	[=3]
can+(1):	[=1]
can+(2):	[=1]
ci:	[=2]
degül:	[=1]
dil:	[=3]
dost:	[=2]
dur:	[=2]
düşman:	[=4]
er:	[=2]
esek:	[=1]
esi:	[=1]
fayda:	[=2]
gibi:	[=1]
gönül:	[=3]
gör:	[=3]
göz:	[=1]
hayvān:	[=2]
her:	[=1]
igi:	[=2]
it:	[=2]
iç:	[=1]
kal:	[=1]
ki:	[=4]
kim:	[=4]
kisi:	[=5]
kov:	[=1]
kov.ar:	[=1]
kul:	[=1]
kör:	[=3]
naz:	[=1]
ne:	[=7]
ni:	[=1]
ofiat:	[=1]
ol:	[=11]
ol.an:	[=1]
sek:	[=1]
ser:	[=1]
sert:	[=4]
sol:	[=1]
sor:	[=1]
söz:	[=3]
tala:	[=1]
tatlı:	[=2]
tavar:	[=5]
tut:	[=1]
uyi:	[=1]
var:	[=3]
ve:	[=1]
vü:	[=1]
yavuz:	[=1]
yaya:	[=2]
yeg:	[=1]
yi:	[=2]
yig:	[=10]
yit:	[=3]
yok:	[=3]
yol:	[=8]
yolda:	[=1]
yüri:	[=2]
çare:	[=1]
çık:	[=1]
çık.ar:	[=1]
öz:	[=2]
```

- **`...Ek.txt`**: Kelime eklerini ve geçtiği satırları gösteren dosya.

```bash
ādem+i: 4, 16.
ādem-i: 13.
ādemi+den: 10.
akıl+ı: 5.
akıl+ıdur: 9.
ayır+ır: 4, 16.
az+an: 17.
az+maz: 13.
az+sa: 7.
az.an: 11.
az.sa: 2.
ben.zer: 5.
bil.e: 15.
bil.mez: 1.
bin.en+den: 7.
bin.se: 2, 11.
bul+an: 6.
bul+ur: 3, 6, 12, 14.
can+ı: 4.
dil+den: 3, 6.
düşman+ı: 6, 12.
er+idur: 13.
er+se: 15.
fayda+dur: 17.
gönül+ü: 17.
gör.se: 1.
göz+i: 1.
hayvān+dan: 4.
it+e: 5.
iç.mek: 4.
kal.maz: 15.
kim+dir: 5.
kisi+den: 2, 11, 17.
kov.ar: 8.
kov.ar+sa: 4.
kul+ur: 12.
ol+an: 17.
ol+an+dan: 12.
ol+ur: 1, 5, 7, 14, 15.
ol.a: 10.
ol.an+dan: 3.
sor+ar+lar: 2.
söz+den: 6, 14.
söz+ü: 3.
tala.ya: 9.
tatlı+dur: 14.
tatlı+dır: 6.
tavar+dan: 5, 9, 10, 16.
tut.ar: 3.
uyi.mak: 8.
yaya+dan: 7.
yi.mek: 4, 8.
yig+i: 1, 5, 6, 9, 14, 16.
yit.en: 2.
yit.me.z: 13, 17.
yol+da: 2, 15, 17.
yol+dan: 13.
yüri.ye: 11.
yüri.yen: 7.
çık.an: 3.
çık.ar+an: 13.
öz+ün: 1, 15.
```

- **`...Sorun.txt`**: Geçersiz kelimeleri ve hataları içeren dosya.

```bash
16: hayvān+dan, (Geçersiz karakterler: {','})
```

- **`...Birlesik.txt`**: Tespit edilen birleşik ifadeleri ve geçtiği satırları listeleyen dosya.

```bash
1 ve 2: 17.
```

---

## Geçerli Karakterler ve Transkripsiyon Desteği
Program şu karakter gruplarını destekler:

* Latin alfabesi ( `a`-`z`, `A`-`Z`)
* Türkçe karakterler ( `ç`, `ğ`, `ı`, `ö`, `ş`, `ü`, `â`)
* Desteklenen transkripsiyon işaretleri ( `ā`, `ḍ`, `é`, `ḥ`, `ī`, `ū`, `ż`, `ġ`, `ḷ`, `ō`, `å`, `ä`, `ï`, `ɵ`, `ə`, `ḳ`, `ṣ`, `ṭ`, `ẓ`, `ḏ`, `s̱`, `ẕ`, `ḫ`, `ñ`, `ŋ`, `n͡g`, `ň`, `ž`, `ý`, `ⱨ`, `ⱪ`, `ţ`, büyük harf varyasyonları olarak `Ā`, `Ē`, `Ī`, `Ō`, `Ū`, `É`, `Í`, `Å`, `Ä`, `Ï`, `Ə`, `Ɵ`, `Ḍ`, `Ḥ`, `Ḳ`, `Ṣ`, `Ṭ`, `Ẓ`, `Ḏ`, `S̱`, `Ẕ`, `Ḫ`, `Ñ`, `Ŋ`, `N͡G`, `Ň`, `Ž`, `Ý`, `Ⱨ`, `Ⱪ`, `Ţ`  vb.)
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
        python inciDizLex0.5 beta.py
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
python inciDizLex.py

.
├── inciDizLex.py         # Ana Python betiği
├── test01.txt            # Örnek giriş dosyası
├── test02.txt            # Örnek giriş dosyası
├── test03.txt            # Örnek giriş dosyası
├── test04.txt            # Örnek giriş dosyası
├── README.md             # Bu README dosyası
└── ...
```

## Lisans

Bu proje GNU General Public License v3 altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## İletişim

Sorularınız veya önerileriniz için hakanbalas@hotmail.com ile iletişime geçebilirsiniz.
