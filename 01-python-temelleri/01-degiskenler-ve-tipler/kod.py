# DERS 01 — Değişkenler ve Veri Tipleri
# Kural: "# TAHMİN:" satırına geldiğinde DUR. Çıktıyı tahmin et, yanına yaz. Sonra çalıştır.

# --- 1) Değişken = bir değere verilen isim ---
yas = 20
isim = "Ali"
boy = 1.78
ogrenci_mi = True

print(type(yas))         # TAHMİN:
print(type(isim))        # TAHMİN:
print(type(boy))         # TAHMİN:
print(type(ogrenci_mi))  # TAHMİN:

# --- 2) Değişkenin değeri değişebilir ---
puan = 10
puan = puan + 5          # sağ taraf önce hesaplanır, sonra sola yazılır
puan += 5                # bu, "puan = puan + 5" ile aynı şey
print(puan)              # TAHMİN:

# --- 3) Bölme türleri (yapay zekada çok kullanılır!) ---
print(7 / 2)             # TAHMİN:   ( / her zaman ondalıklı sonuç verir )
print(7 // 2)            # TAHMİN:   ( // tam sayı bölmesi )
print(7 % 2)             # TAHMİN:   ( % kalanı verir )
print(2 ** 3)            # TAHMİN:   ( ** üs alma )

# --- 4) Tipler karışınca ne olur? ---
a = "5"
b = 5
print(a * 3)             # TAHMİN:   ( metin * sayı = ? )
print(int(a) + b)        # TAHMİN:
# print(a + b)           # Bu satırın yorumunu kaldırırsan HATA verir. Neden? sorular.md'de cevapla.

# --- 5) f-string: değişkenleri metnin içine yerleştirme ---
dogruluk = 0.8734
print(f"{isim} modelinin doğruluğu: {dogruluk}")         # TAHMİN:
print(f"Yuvarlanmış: {dogruluk:.2f}")                    # TAHMİN:
print(f"Yüzde olarak: {dogruluk * 100:.1f}%")            # TAHMİN:
