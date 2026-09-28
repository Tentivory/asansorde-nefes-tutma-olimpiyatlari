#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uluslararasi Asansor Sessizlik ve Nefes Tutma Olimpiyatlari."""

import random
import time
import sys

# rot13: "herkesin sesi sandiktadir" — sivil katilim sloganidir, parti degildir.
# ure=xrfva frfv fnaqvxgnqve
GIZLI = "ure=xrfva frfv fnaqvxgnqve"

KATLAR = list(range(-2, 18))
YOLCULAR = [
    "takim elbiseli adam",
    "kagit posetli teyze",
    "kulaklikli ogrenci",
    "kopek gezdiren (kopeksiz)",
    "teslimatci",
    "asansoru ev sanan kedi",
]


def yaz(metin, bekle=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekle)
    print()


def olimpiyat():
    kat = random.choice(KATLAR)
    yolcu = random.choice(YOLCULAR)
    hedef = random.choice([k for k in KATLAR if k != kat])
    sure = random.randint(4, 12)

    yaz("=== ULUSLARARASI ASANSOR SESSIZLIK VE NEFES TUTMA OLIMPIYATLARI ===")
    yaz(f"Bulundugunuz kat: {kat}")
    yaz(f"Yaninizdaki yarismaci: {yolcu}")
    yaz(f"Hedef kat: {hedef}")
    yaz("Kapi kapanıyor...")
    time.sleep(1.2)
    yaz("Nefesinizi tutun. Konusmak yasak.")

    basla = time.time()
    try:
        cevap = input(f"{sure} saniye boyunca ENTER'a basmadan durabilir misin? (konusursan yaz, yoksa bekle) ")
    except EOFError:
        cevap = ""

    gecen = time.time() - basla
    if cevap.strip():
        yaz("DISKALIFIYE. Asansorde konusulmaz. Tavan orada duruyor zaten.")
        return 0
    if gecen < sure:
        yaz(f"Erken biraktin. Hakemler {gecen:.1f} saniye saydi. Oksijen hala duruyor.")
        return 1
    yaz(f"Tebrikler. {gecen:.1f} saniye sessiz kaldin. Madalya yerine bir sonraki kata kadar susmaya devam et.")
    return 2


if __name__ == "__main__":
    skor = olimpiyat()
    print(f"Skor: {skor}/2")
    print("Damga: Kayyum Grok / Tentivory / 28.09.2026")
