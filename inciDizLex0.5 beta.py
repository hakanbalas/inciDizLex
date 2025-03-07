# inciDizLex.py
# Copyright (C) 2025 Hakan Balas
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re
from collections import defaultdict
import os
import unicodedata

# Tanımlı karakterler (Transkripsiyon işaretleri dahil)
VALID_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" +
                  "çğıöşüə0123456789+-(/) " +
                  "āḍéḥīūżġḷōåäïɵĀĒĪİ̄ŌȪŪǕÉÍÅÄÏƏƟḳṣṭẓḏs̱ẕḫñŋn͡gňžýⱨⱪţĠŻḌḤḲṢṬẒḎS̱ẔḪÑŊN͡GŇŽÝⱧⱩŢ.,")

# Kelime ayırt ediciler
DELIMITERS = {" ", "\t"}

# Transkripsiyon işaretleri için sıralama dönüşüm tablosu
TRANSLITERATION_MAP = {
    "ġ": "g", "ā": "a", "ż": "z", "ī": "i", "ı̇̄": "ı", "ō": "o", "ȫ": "ö",
    "ū": "u", "ǖ": "ü", "é": "e", "í": "i", "å": "a", "ä": "a", "ï": "i",
    "ə": "e", "ɵ": "o", "Ā": "a", "Ē": "e", "Ī": "i", "İ̄": "i", "Ō": "o",
    "Ȫ": "ö", "Ū": "u", "Ǖ": "ü", "É": "e", "Í": "i", "Å": "a", "Ä": "a",
    "Ï": "i", "Ə": "e", "Ɵ": "o", "ḍ": "d", "ḥ": "h", "ḳ": "k", "ṣ": "s",
    "ṭ": "t", "ẓ": "z", "ḏ": "d", "s̱": "s", "ẕ": "z", "ḫ": "h", "ñ": "n",
    "ŋ": "n", "n͡g": "ng", "ň": "n", "ž": "z", "ý": "y", "ⱨ": "h", "ⱪ": "k",
    "ţ": "t", "Ġ": "g", "Ż": "z", "Ḍ": "d", "Ḥ": "h", "Ḳ": "k", "Ṣ": "s",
    "Ṭ": "t", "Ẓ": "z", "Ḏ": "d", "S̱": "s", "Ẕ": "z", "Ḫ": "h", "Ñ": "n",
    "Ŋ": "n", "N͡G": "ng", "Ň": "n", "Ž": "z", "Ý": "y", "Ⱨ": "h", "Ⱪ": "k",
    "Ţ": "t"
}

def normalize_text(text):
    """Transkripsiyon işaretlerini koru, sadece büyük harfleri küçült."""
    text = unicodedata.normalize("NFKC", text)
    return ''.join(c.lower() if c.isupper() and c not in "DN" else c for c in text)

def normalize_for_sorting(text):
    """Sıralama için transkripsiyon işaretlerini temel harflere çevir."""
    text = unicodedata.normalize("NFKC", text)
    for trans_char, base_char in TRANSLITERATION_MAP.items():
        text = text.replace(trans_char, base_char)
    return text.lower()

def is_valid_word(word):
    """Kelimenin standartlara uygunluğunu kontrol eder."""
    if word.startswith(".") or word.startswith("-"):
        return False
    if "." in word and "-" in word:
        return False
    if "," in word:
        if not word.endswith(",") or not re.match(r".+\+\([0-9]+\),$", word):
            return False
    return all(char in VALID_CHARS for char in word)

def extract_base_and_suffix(word):
    """Kelimeyi taban ve eklerine ayırır, eş sesli işaretleri ek olarak saymaz."""
    if word.endswith(","):
        word = word[:-1]

    homophonic_match = re.match(r"(.+?)(\+\([0-9]+\))$", word)
    if homophonic_match:
        base = homophonic_match.group(1)
        variation = homophonic_match.group(2)
        return base, "", variation

    elif "+" in word:
        parts = word.split("+", 1)
        base = parts[0]
        suffix = "+" + parts[1]
        return base, suffix, None
    elif "." in word:
        parts = word.split(".")
        base = parts[0]
        suffix = "." + ".".join(parts[1:]) if len(parts) > 1 else ""
        return base, suffix, None
    elif "-" in word:
        parts = word.split("-")
        base = parts[0]
        suffix = "-" + "-".join(parts[1:]) if len(parts) > 1 else ""
        return base, suffix, None
    return word, "", None

def convert_to_leaf_line(satır_no):
    """Satır numarasını yaprak/satır formatına çevirir."""
    try:
        # Satır numarasını temizle (başındaki sıfırları at)
        satır_no = re.sub(r"^0+", "", satır_no)
        num = int(satır_no)
        yaprak = num // 10
        satir = num % 10
        if satir == 0:
            yaprak -= 1
            satir = 10
        return f"{yaprak:03d}a/{satir:02d}"
    except ValueError:
        return satır_no

def detect_compound_expressions(content, bağlaçlar=["ve", "u", "-ı"]):
    """Bağlaçlarla birleşik ifadeleri tespit et."""
    birlesik_ifadeler = defaultdict(list)
    words = content.split()
    for i in range(len(words) - 2):
        if words[i+1] in bağlaçlar:
            birlesik_ifade = f"{words[i]} {words[i+1]} {words[i+2]}"
            birlesik_ifadeler[birlesik_ifade].append((i, content))
    return birlesik_ifadeler

def process_file(input_file, output_dir, include_count=True, use_leaf_line=False, create_compound_report=False):
    """Giriş dosyasını işler ve dizin dosyalarını oluşturur."""
    dizin = defaultdict(list)
    ekler = defaultdict(list)
    sorunlu_kelimeler = []
    birlesik_ifadeler = defaultdict(list)
    homophonic_entries = defaultdict(set)

    toplam_kelime = 0
    gecerli_kelime = 0
    gecersiz_kelime = 0
    alt_madde = 0
    madde_basi_sayisi = 0

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"Dosyadan {len(lines)} satır okundu.")
    except FileNotFoundError:
        print(f"Hata: {input_file} dosyası bulunamadı!")
        return
    except UnicodeDecodeError:
        print(f"Hata: {input_file} dosyası UTF-8 kodlamasıyla okunamadı!")
        return
    except Exception as e:
        print(f"Dosya okuma hatası: {e}")
        return

    if not lines:
        print("Dosya boş veya satırlar okunamadı!")
        return

    satır_kelimeler = defaultdict(list)
    use_leaf_format = False

    for line in lines[:1]:
        line = line.strip()
        if line and "/" in line.split(" ", 1)[0]:
            use_leaf_format = True
            break

    for line in lines:
        line = line.strip()
        if line:
            try:
                if use_leaf_format and " " in line:
                    parts = line.split(" ", 1)
                elif ":" in line:
                    parts = line.split(":", 1)
                elif "." in line:
                    parts = line.split(".", 1)
                else:
                    print(f"Geçersiz satır formatı: {line}")
                    continue

                if len(parts) < 2:
                    print(f"Geçersiz satır formatı: {line}")
                    continue

                satır_no, içerik = parts[0].strip(), parts[1].strip()

                # Satır numarasını temizleme (başındaki sıfırları atma)
                satır_no = re.sub(r"^0+", "", satır_no)

                kelimeler = içerik.split()

                if not use_leaf_format and use_leaf_line:
                    satır_no = convert_to_leaf_line(satır_no)
                satır_kelimeler[satır_no].extend(kelimeler)

                if create_compound_report:
                    birlesikler = detect_compound_expressions(içerik)
                    for ifade, pozisyonlar in birlesikler.items():
                        birlesik_ifadeler[ifade].append(satır_no)
            except Exception as e:
                print(f"Satır işleme hatası: {line} - {e}")
                continue

    if not satır_kelimeler:
        print("Hiçbir kelime işlenemedi!")
        return

    for satır_no, kelimeler in satır_kelimeler.items():
        toplam_kelime += len(kelimeler)
        for kelime in kelimeler:
            normalized_kelime = normalize_text(kelime)
            if is_valid_word(normalized_kelime):
                gecerli_kelime += 1
                base, suffix, variation = extract_base_and_suffix(normalized_kelime)

                if variation:
                    dizin[base].append(satır_no)
                    full_homophonic = base + variation
                    dizin[full_homophonic].append(satır_no)
                    homophonic_entries[base].add((full_homophonic, satır_no))
                    alt_madde += 1
                else:
                    dizin[base].append(satır_no)
                    if suffix:
                        ekler[base + suffix].append(satır_no)
                        alt_madde += 1
            else:
                gecersiz_kelime += 1
                sorunlu_kelimeler.append(f"{satır_no}: {kelime} (Geçersiz karakterler: {set(normalized_kelime) - VALID_CHARS})")

    madde_basi_sayisi = len(dizin)
    homophonic_groups = defaultdict(list)
    for kelime in dizin.keys():
        base, _, variation = extract_base_and_suffix(kelime)
        if variation:
            homophonic_groups[base].append(kelime)

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    dizin_file = os.path.join(output_dir, f"{base_name}Dizin.txt")
    mbs_file = os.path.join(output_dir, f"{base_name}MBS.txt")
    ek_file = os.path.join(output_dir, f"{base_name}Ek.txt")
    sorun_file = os.path.join(output_dir, f"{base_name}Sorun.txt")
    birlesik_file = os.path.join(output_dir, f"{base_name}Birlesik.txt")

    # MBS.txt dosyasını önce yazalım ki karşılaştırma yapabilelim
    mbs_entries = set()
    with open(mbs_file, "w", encoding="utf-8") as f:
        all_entries = sorted(dizin.keys(), key=normalize_for_sorting)
        for madde_basi in all_entries:
            satırlar = dizin[madde_basi]
            f.write(f"{madde_basi}:\t[={len(satırlar)}]\n")
            mbs_entries.add(madde_basi)

    # DİZİN DOSYASI YAZMA - YENİ FORMAT İLE
    with open(dizin_file, "w", encoding="utf-8") as f:
        base_entries = [entry for entry in dizin.keys() if not re.match(r".+\+\([0-9]+\)$", entry)]
        sorted_base_entries = sorted(base_entries, key=normalize_for_sorting)

        processed_homophonics = set()

        for madde_basi in sorted_base_entries:
            # Düzeltme: Satır numaralarını sayısal olarak sırala
            try:
                base_satırlar = sorted(set(dizin[madde_basi]), key=int)
            except ValueError:
                # Eğer int dönüşümü başarısız olursa (örn. yaprak format "001a/02" kullanıyorsa), metin sıralamasına geri dön
                base_satırlar = sorted(set(dizin[madde_basi]))
                
            ana_madde_kullanim = len(base_satırlar)
            es_sesli_varyasyonlar = homophonic_groups[madde_basi]

            line = f"{madde_basi}:"
            if base_satırlar and not es_sesli_varyasyonlar:
                line += f" {', '.join(base_satırlar)}."
            if include_count:
                line += f" [={ana_madde_kullanim}]"
            f.write(line + "\n")

            alt_maddeler = defaultdict(list)
            for satır in dizin[madde_basi]:
                for kelime in satır_kelimeler[satır]:
                    normalized_kelime = normalize_text(kelime)
                    if is_valid_word(normalized_kelime):
                        base, suffix, variation = extract_base_and_suffix(normalized_kelime)
                        if base == madde_basi and suffix and not variation:
                            alt_maddeler[madde_basi + suffix].append(satır)

            for entry in base_entries[:]:
                if (entry != madde_basi and
                    entry.startswith(madde_basi) and
                    ("-" in entry or "+" in entry) and
                    not re.match(r".+\+\([0-9]+\)$", entry)):
                    alt_maddeler[entry].extend(dizin[entry])

            for alt_madde_key, satır_listesi in sorted(alt_maddeler.items(), key=lambda x: normalize_for_sorting(x[0])):
                # Düzeltme: Alt madde satırlarını sayısal olarak sırala
                if satır_listesi:
                    try:
                        unique_lines = sorted(set(satır_listesi), key=int)
                    except ValueError:
                        # int dönüşümü başarısız olursa metin sıralamasına geri dön
                        unique_lines = sorted(set(satır_listesi))
                        
                    line_count = len(unique_lines)
                    line = f"{alt_madde_key}: {', '.join(unique_lines)}."
                    if include_count:
                        line += f" [={line_count}]"
                    if alt_madde_key not in mbs_entries:
                        line = f"\t{line}"
                    f.write(line + "\n")
                    if alt_madde_key in base_entries:
                        base_entries.remove(alt_madde_key)

            for varyasyon in sorted(es_sesli_varyasyonlar, key=lambda x: int(re.search(r"\+\(([0-9]+)\)$", x).group(1))):
                processed_homophonics.add(varyasyon)
                # Düzeltme: Varyasyon satırlarını sayısal olarak sırala
                try:
                    var_satırlar = sorted(set(dizin[varyasyon]), key=int)
                except ValueError:
                    # int dönüşümü başarısız olursa metin sıralamasına geri dön
                    var_satırlar = sorted(set(dizin[varyasyon]))
                    
                var_count = len(var_satırlar)
                line = f"{varyasyon}: {', '.join(var_satırlar)}."
                if include_count:
                    line += f" [={var_count}]"
                f.write(line + "\n")

        remaining_homophonics = [entry for entry in dizin.keys()
                               if re.match(r".+\+\([0-9]+\)$", entry) and entry not in processed_homophonics]
        for entry in sorted(remaining_homophonics, key=normalize_for_sorting):
            # Düzeltme: Kalan homofon satırlarını sayısal olarak sırala
            try:
                satırlar = sorted(set(dizin[entry]), key=int)
            except ValueError:
                # int dönüşümü başarısız olursa metin sıralamasına geri dön
                satırlar = sorted(set(dizin[entry]))
                
            line = f"{entry}: {', '.join(satırlar)}."
            if include_count:
                line += f" [={len(satırlar)}]"
            f.write(line + "\n")

        f.write(f"\nToplam kelime: {toplam_kelime}\n")
        f.write(f"Geçerli kelime: {gecerli_kelime}\n")
        f.write(f"Geçersiz kelime: {gecersiz_kelime}\n")
        f.write(f"Alt madde: {alt_madde}\n")
        f.write(f"Madde başı: {madde_basi_sayisi}\n")

    # EKLER DOSYASI YAZMA
    with open(ek_file, "w", encoding="utf-8") as f:
        for ek in sorted(ekler.keys(), key=normalize_for_sorting):
            satırlar = ekler[ek]
            # Düzeltme: Satır numaralarını sayısal olarak sırala
            try:
                sorted_satırlar = sorted(set(satırlar), key=int)
            except ValueError:
                # int dönüşümü başarısız olursa metin sıralamasına geri dön
                sorted_satırlar = sorted(set(satırlar))
                
            f.write(f"{ek}: {', '.join(sorted_satırlar)}.\n")

    # SORUNLU KELİMELER DOSYASI YAZMA
    if sorunlu_kelimeler:
        with open(sorun_file, "w", encoding="utf-8") as f:
            f.write("\n".join(sorunlu_kelimeler))

    # BİRLEŞİK İFADELER DOSYASI YAZMA
    if create_compound_report and birlesik_ifadeler:
        with open(birlesik_file, "w", encoding="utf-8") as f:
            for ifade, satırlar in sorted(birlesik_ifadeler.items(), key=lambda x: normalize_for_sorting(x[0])):
                # Düzeltme: Birleşik ifadelerin satır numaralarını sayısal olarak sırala
                try:
                    sorted_satırlar = sorted(set(satırlar), key=int)
                except ValueError:
                    # int dönüşümü başarısız olursa metin sıralamasına geri dön
                    sorted_satırlar = sorted(set(satırlar))
                    
                f.write(f"{ifade}: {', '.join(sorted_satırlar)}.\n")

def main():
    input_file = "test04.txt"
    output_dir = os.getcwd()

    if not os.path.exists(input_file):
        print(f"Hata: {input_file} dosyası bulunamadı!")
        return

    sıklık = input("Her madde başından sonra kaç defa geçtiği yazılsın mı? (E/H): ").strip().upper()
    if sıklık not in ["E", "H"]:
        print("Lütfen E veya H girin!")
        return
    include_count = sıklık == "E"

    leaf_line = input("Yaprak/satır formatı kullanılsın mı? (E/H): ").strip().upper()
    use_leaf_line = leaf_line == "E"

    birlesik = input("Birleşik ifadeler dizini oluşturulsun mu? (E/H): ").strip().upper()
    create_compound_report = birlesik == "E"

    print("Dosya işleniyor...")
    process_file(input_file, output_dir, include_count, use_leaf_line, create_compound_report)
    print("İşlem tamamlandı. Çıkış dosyaları oluşturuldu.")

if __name__ == "__main__":
    main()
