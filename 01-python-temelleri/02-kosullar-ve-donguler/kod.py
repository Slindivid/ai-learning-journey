# DERS 02 — Koşullar ve Döngüler
# Kural: "# TAHMİN:" satırına gelince DUR, tahmin et, sonra çalıştır.

# --- 1) if / elif / else ---
# Bir modelin tahmin olasılığına göre karar verelim
olasilik = 0.65

if olasilik >= 0.9:
    print("Kesin kedi")
elif olasilik >= 0.5:
    print("Muhtemelen kedi")
else:
    print("Kedi değil")
# TAHMİN: Hangi satır yazdırılır?

# --- 2) for döngüsü ---
for i in range(3):       # range(3) -> 0, 1, 2
    print("adım", i)
# TAHMİN: Kaç satır, ne yazdırır?

# --- 3) Döngü ile toplam (ML'de "loss toplamak" böyle başlar) ---
hatalar = [0.5, 0.2, 0.3]
toplam = 0
for h in hatalar:
    toplam += h
    print("şu anki toplam:", toplam)
ortalama = toplam / len(hatalar)
print("ortalama hata:", ortalama)
# TAHMİN: Her adımda toplam ne olur? Ortalama kaç?
# İPUCU: Bilgisayarda 0.5+0.2+0.3 tam 1.0 çıkmayabilir! Neden? (float hassasiyeti)

# --- 4) while döngüsü ---
# Bir değeri her adımda yarıya indir (öğrenme oranı azaltma gibi)
ogrenme_orani = 1.0
adim = 0
while ogrenme_orani > 0.1:
    ogrenme_orani = ogrenme_orani / 2
    adim += 1
print(adim, ogrenme_orani)
# TAHMİN: Döngü kaç kez döner? Son değer kaç?

# --- 5) break ve continue ---
for sayi in range(10):
    if sayi % 2 == 0:
        continue         # çiftleri atla, döngünün başına dön
    if sayi > 6:
        break            # döngüden tamamen çık
    print(sayi)
# TAHMİN: Hangi sayılar yazdırılır?
