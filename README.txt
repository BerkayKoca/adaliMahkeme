# Hakim ve Jüri Rüşvet Hesaplama Programı
Bu program, bir davada beraat kararını elde etmek için hakim ve jüri üzerinde uygulanabilecek farklı stratejilerin maliyetlerini Python ile hesaplar ve karşılaştırır.

## Genel İşleyiş
- Kullanıcıdan jüri sayısı ve jüri başına rüşvet miktarı alınır.
- Jüri için alınan değerler tüm değerlendirme için sabit kabul edilir.
- 5 farklı hakim için iki değer girilir:
- Beraat rüşveti
- Çekimser rüşveti

## Kısıtlamalar
- Aynı beraat veya çekimser değeri birden fazla hakime atanamaz.
- Bir hakimin çekimser rüşveti, o hakimin beraat rüşvetinden daha düşük olmak zorundadır.

##Hesaplanan Stratejiler
1. Hakime doğrudan beraat rüşveti verme maliyeti
2. Hakimi çekimser bırakıp jüriden çoğunluk oluşturma maliyeti
3. Jürinin tamamını etkileyerek sonuç alma maliyeti

## Program Çıktısı
Program, her hakim için bu üç stratejiyi karşılaştırır ve en düşük maliyetli seçeneği belirler. Sonuç olarak beraat kararına ulaşmak için en ekonomik strateji ekrana yazdırılır.
