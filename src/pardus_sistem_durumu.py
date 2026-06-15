#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Sistem Durumu Bilgilendirme Aracı
ÇalıPardusLab2 / Pardus Hata Yakalama ve Öneri Yarışması 2026
"""

import shutil


def sistem_durumu():
    toplam, kullanilan, bos = shutil.disk_usage("/")

    disk_yuzde = (kullanilan / toplam) * 100

    print("=" * 60)
    print("PARDUS SİSTEM DURUMU")
    print("=" * 60)

    print("\nDisk Durumu:")
    print(f"Kullanım: %{disk_yuzde:.1f}")

    if disk_yuzde < 70:
        print("Durum: İyi ✅")
    elif disk_yuzde < 85:
        print("Durum: Dikkat ⚠")
    else:
        print("Durum: Kritik ❌")

    print("\nRAM Durumu:")
    print("Örnek değer: Normal ✅")

    print("\nCPU Durumu:")
    print("Örnek değer: Normal ✅")


def main():
    sistem_durumu()


if __name__ == "__main__":
    main()
