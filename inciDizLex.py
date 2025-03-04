# Copyright (C) 2025 Hakan Balas
# Bu proje GNU General Public License v3 altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

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
