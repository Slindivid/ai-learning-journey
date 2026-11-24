# DERS 03 — Fonksiyonlar
# Fonksiyon = tekrar kullanılabilen, isimli kod bloğu. Girdi alır, çıktı (return) verir.

# --- 1) Basit fonksiyon ---
def kare(x):
    return x * x

print(kare(4))           # TAHMİN:
print(kare(kare(2)))     # TAHMİN:  (içten dışa doğru oku!)

# --- 2) print ile return farkı (en sık yapılan hata) ---
def yazdir_topla(a, b):
    print(a + b)         # sadece ekrana yazar, değer GERİ VERMEZ

def dondur_topla(a, b):
    return a + b         # değeri geri verir

x = yazdir_topla(2, 3)   # TAHMİN: ekrana ne çıkar?
print(x)                 # TAHMİN: x'in değeri ne?
y = dondur_topla(2, 3)
print(y)                 # TAHMİN:

# --- 3) Varsayılan parametre ---
def tahmin_et(olasilik, esik=0.5):
    if olasilik >= esik:
        return 1
    return 0             # else yazmaya gerek yok, return fonksiyonu bitirir

print(tahmin_et(0.7))            # TAHMİN:
print(tahmin_et(0.7, esik=0.8))  # TAHMİN:

# --- 4) Gerçek bir ML parçası: ortalama karesel hata (MSE) ---
# MSE = her (gerçek - tahmin) farkının karesinin ortalaması
def mse(gercekler, tahminler):
    toplam = 0
    for g, t in zip(gercekler, tahminler):   # zip: iki listeyi eş eş gezer
        toplam += (g - t) ** 2
    return toplam / len(gercekler)

gercek = [3, 5, 2]
tahmin = [2, 5, 4]
print(mse(gercek, tahmin))       # TAHMİN: Önce farkları, sonra kareleri, sonra ortalamayı hesapla.

# --- 5) Kapsam (scope) ---
sayac = 0
def artir():
    sayac = 100          # bu, fonksiyonun İÇİNDE yeni bir değişken
    return sayac

print(artir())           # TAHMİN:
print(sayac)             # TAHMİN: Dışarıdaki sayac değişti mi?
