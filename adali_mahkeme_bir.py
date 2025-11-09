import math


def juriGirdi():
    while True:
        try:
            juriSayi = int(input("     Jüri Parametreleri     ""\n""Jüri Sayısı: "))
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

    while True:
        try:
            juriRusvetSayi = int(input("Jüri Başına Rüşvet (TL): "))
            break
        except ValueError:
            print("Lütfen sayıları rakamsal değerlerle yazınız.")

    return juriSayi, juriRusvetSayi


girilen_beraatlar = set()
girilen_cekimserler = set()

def hakimGirdi(hakim_adi):
    while True:
        try:
            hakimBeraat = int(input("\n"f"     {hakim_adi} Rüşvet Değerleri     ""\n"f"{hakim_adi} Beraat Rüşvet (TL): "))
            if hakimBeraat in girilen_beraatlar:
                print(
                    "Girilen beraat rüşvet değeri daha önce girildi. Lütfen farklı bir değer giriniz.")
                continue
            girilen_beraatlar.add(hakimBeraat)
            break
        except ValueError:
                print("Lütfen sayıları rakamsal değerlerle yazınız.")

    while True:
        try:
            hakimCekimser = int(input(f"{hakim_adi} Çekimser Rüşvet (TL): "))
            if hakimCekimser >= hakimBeraat:
                print("Hakimin çekimser olduğu rüşvet değeri beraat olduğu rüşvet değerinden küçük olmalı.")
                continue
            if hakimCekimser in girilen_cekimserler:
                print(
                    "Girilen çekimser rüşvet değeri daha önce girildi. Lütfen farklı bir değer giriniz.")
                continue
            girilen_cekimserler.add(hakimCekimser)
            break
        except ValueError:
                print("Lütfen sayıları rakamsal değerlerle yazınız.")

    return hakimBeraat, hakimCekimser


hakimler = ["Hakim Bir", "Hakim İki", "Hakim Üç", "Hakim Dört", "Hakim Beş"]

juriSayi, juriRusvetSayi = juriGirdi()

for hakim in hakimler:
    hakimBeraat, hakimCekimser = hakimGirdi(hakim)

    hakim_beraat_sonuc = int(hakimBeraat)
    hakim_cekimser_sonuc = int(hakimCekimser + math.ceil(juriSayi / 2) * juriRusvetSayi)
    hakim_suclu_sonuc = int(juriSayi * juriRusvetSayi)

    print("\n     ", hakim, "     ")
    print(hakim, "Beraat Rüşvet Değeri (TL): ", hakim_beraat_sonuc)
    print(hakim, "Çekimser (Hakim+Jüri Rüşvet Değeri TL): ", hakim_cekimser_sonuc)
    print(hakim, "Suçlu (Jüri Rüşvet Değeri TL): ", hakim_suclu_sonuc)
    print("Beraat Kararı İçin En Düşük Maliyet (TL): ",
          min(hakim_beraat_sonuc, hakim_cekimser_sonuc, hakim_suclu_sonuc))
    print("\n")


input()
