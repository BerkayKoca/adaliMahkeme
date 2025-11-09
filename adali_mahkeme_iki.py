import math


def juriGirdi():

    global juriSayi
    global juriRusvetSayi

    while True:
        try:
            juriSayi = int(input("Jüri Sayısı: "))
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

    while True:
        try:
            juriRusvetSayi = int(input("Jüri Başına Rüşvet (TL): "))
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")


def hakimBirGirdi():

    global hakimBirBeraat
    global hakimBirCekimser

    while True:
        try:
            hakimBirBeraat = int(input("Hakim Bir Beraat Rüşvet (TL): "))
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

    while True:
        try:
            hakimBirCekimser = int(input("Hakim Bir Çekimser Rüşvet (TL): "))
            if hakimBirCekimser >= hakimBirBeraat:
                print("Hakimin çekimser olduğu rüşvet değeri beraat olduğu rüşvet değerinden küçük olmalı.")
                continue
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

            hakimBirSuclu = int(0)

print("     Jüri Parametreleri     ")

juriGirdi()

print("\n")

print("     Hakim Bir     ")

hakimBirGirdi()

print("     Hakim Bir Sonuç     ")

hakim_bir_beraat_sonuc = int(hakimBirBeraat)
hakim_bir_cekimser_sonuc = int(hakimBirCekimser + math.ceil(juriSayi / 2) * juriRusvetSayi)
hakim_bir_suclu_sonuc = int(juriSayi * juriRusvetSayi)

print("Hakim Bir Beraat Değeri (TL): ", hakim_bir_beraat_sonuc)
print("Hakim Bir Çekimser Değeri (TL): ", hakim_bir_cekimser_sonuc)
print("Hakim Bir Suçlu Değeri (TL): ", hakim_bir_suclu_sonuc)

print("Hakim Bir Beraat Kararı İçin En Düşük Maliyet (TL): ",
      min(hakim_bir_beraat_sonuc, hakim_bir_cekimser_sonuc, hakim_bir_suclu_sonuc))

print("\n")


def hakimIkiGirdi():

    global hakimIkiBeraat
    global hakimIkiCekimser

    while True:
        try:
            hakimIkiBeraat = int(input("Hakim İki Beraat Rüşvet (TL): "))
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

    while True:
        try:
            hakimIkiCekimser = int(input("Hakim İki Çekimser Rüşvet (TL): "))
            if hakimIkiCekimser >= hakimIkiBeraat:
                print("Hakimin çekimser olduğu rüşvet değeri beraat olduğu rüşvet değerinden küçük olmalı.")
                continue
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

            hakimIkiSuclu = int(0)

print("     Hakim İki     ")

hakimIkiGirdi()

print("     Hakim İki Sonuç     ")

hakim_iki_beraat_sonuc = int(hakimIkiBeraat)
hakim_iki_cekimser_sonuc = int(hakimIkiCekimser + math.ceil(juriSayi / 2) * juriRusvetSayi)
hakim_iki_suclu_sonuc = int(juriSayi * juriRusvetSayi)

print("Hakim İki Beraat Değeri (TL): ", hakim_iki_beraat_sonuc)
print("Hakim İki Çekimser Değeri (TL): ", hakim_iki_cekimser_sonuc)
print("Hakim İki Suçlu Değeri (TL): ", hakim_iki_suclu_sonuc)

print("Hakim İki Beraat Kararı İçin En Düşük Maliyet (TL): ",
      min(hakim_iki_beraat_sonuc, hakim_iki_cekimser_sonuc, hakim_iki_suclu_sonuc))

print("\n")


def hakimUcGirdi():

    global hakimUcBeraat
    global hakimUcCekimser

    while True:
        try:
            hakimUcBeraat = int(input("Hakim Üç Beraat Rüşvet (TL): "))
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

    while True:
        try:
            hakimUcCekimser = int(input("Hakim Üç Çekimser Rüşvet (TL): "))
            if hakimUcCekimser >= hakimUcBeraat:
                print("Hakimin çekimser olduğu rüşvet değeri beraat olduğu rüşvet değerinden küçük olmalı.")
                continue
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

            hakimUcSuclu = int(0)

print("     Hakim Üç     ")

hakimUcGirdi()

print("     Hakim Üç Sonuç     ")

hakim_uc_beraat_sonuc = int(hakimUcBeraat)
hakim_uc_cekimser_sonuc = int(hakimUcCekimser + math.ceil(juriSayi / 2) * juriRusvetSayi)
hakim_uc_suclu_sonuc = int(juriSayi * juriRusvetSayi)

print("Hakim Üç Beraat Değeri (TL): ", hakim_uc_beraat_sonuc)
print("Hakim Üç Çekimser Değeri (TL): ", hakim_uc_cekimser_sonuc)
print("Hakim Üç Suçlu Değeri (TL): ", hakim_uc_suclu_sonuc)

print("Hakim Üç Beraat Kararı İçin En Düşük Maliyet (TL): ",
      min (hakim_uc_beraat_sonuc, hakim_uc_cekimser_sonuc, hakim_uc_suclu_sonuc))

print("\n")


def hakimDortGirdi():

    global hakimDortBeraat
    global hakimDortCekimser

    while True:
        try:
            hakimDortBeraat = int(input("Hakim Dört Beraat Rüşvet (TL): "))
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

    while True:
        try:
            hakimDortCekimser = int(input("Hakim Dört Çekimser Rüşvet (TL): "))
            if hakimDortCekimser >= hakimDortBeraat:
                print("Hakimin çekimser olduğu rüşvet değeri beraat olduğu rüşvet değerinden küçük olmalı.")
                continue
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

            hakimDortSuclu = int(0)

print("     Hakim Dört     ")

hakimDortGirdi()

print("     Hakim Dört Sonuç     ")

hakim_dort_beraat_sonuc = int(hakimDortBeraat)
hakim_dort_cekimser_sonuc = int(hakimDortCekimser + math.ceil(juriSayi / 2) * juriRusvetSayi)
hakim_dort_suclu_sonuc = int(juriSayi * juriRusvetSayi)

print("Hakim Dört Beraat Değeri (TL): ", hakim_dort_beraat_sonuc)
print("Hakim Dört Çekimser Değeri (TL): ", hakim_dort_cekimser_sonuc)
print("Hakim Dört Suçlu Değeri (TL): ", hakim_dort_suclu_sonuc)

print("Hakim Dört Beraat Kararı İçin En Düşük Maliyet (TL): ",
      min (hakim_dort_beraat_sonuc, hakim_dort_cekimser_sonuc, hakim_dort_suclu_sonuc))

print("\n")


def hakimBesGirdi():

    global hakimBesBeraat
    global hakimBesCekimser

    while True:
        try:
            hakimBesBeraat = int(input("Hakim Beş Beraat Rüşvet (TL): "))
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

    while True:
        try:
            hakimBesCekimser = int(input("Hakim Beş Çekimser Rüşvet (TL): "))
            if hakimBesCekimser >= hakimBesBeraat:
                print("Hakimin çekimser olduğu rüşvet değeri beraat olduğu rüşvet değerinden küçük olmalı.")
                continue
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

            hakimBesSuclu = int(0)

print("     Hakim Beş     ")

hakimBesGirdi()

print("     Hakim Beş Sonuç     ")

hakim_bes_beraat_sonuc = int(hakimBesBeraat)
hakim_bes_cekimser_sonuc = int(hakimBesCekimser + math.ceil(juriSayi / 2) * juriRusvetSayi)
hakim_bes_suclu_sonuc = int(juriSayi * juriRusvetSayi)

print("Hakim Beş Beraat Değeri (TL): ", hakim_bes_beraat_sonuc)
print("Hakim Beş Çekimser Değeri (TL): ", hakim_bes_cekimser_sonuc)
print("Hakim Beş Suçlu Değeri (TL): ", hakim_bes_suclu_sonuc)

print("Hakim Beş Beraat Kararı İçin En Düşük Maliyet (TL): ",
      min (hakim_bes_beraat_sonuc, hakim_bes_cekimser_sonuc, hakim_bes_suclu_sonuc))


input()
