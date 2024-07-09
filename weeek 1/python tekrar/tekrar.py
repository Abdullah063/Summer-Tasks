# %% Spyder tanıtımı
print("Merhaba Dünya")

# %% Değişkenler

tamsayi_degisken = 10
ondalikli_sayi = 12.3
print(tamsayi_degisken)

# 4 işlem özellikleri
pi_sayisi = 3.14
katsayi = 2

toplam = pi_sayisi + 1
fark = pi_sayisi - 1
carpma = pi_sayisi * katsayi
bolme = pi_sayisi / katsayi

# Print
print("Toplam: ", toplam)
print("Toplam: {} ve fark: {}".format(toplam, fark))
print("Çarpma: %.1f, bölme: %.4f" % (carpma, bolme))

# Değişkenler arası dönüşüm

carpma_int = int(carpma)
print(carpma_int)

tamsayi_float = float(tamsayi_degisken)
print(tamsayi_float)

# String: Karakter dizileri
string = "merhaba dünya"
print(string)

resim_yolu = "veri" + "\\" + "img" + ".png"
print(resim_yolu)

# %% Python temel sözdizimi

# Büyük ve küçük harf
temel = 6
TEMEL = 7

# Yorum
"""
Bu bölümde sözdizimi
    - Büyük küçük harf
    - Yorum
    - Girinti
    - Anahtar kelimeler
"""
# Girinti
if 5 < 10:
    print("Evet")
else:
    print("Hayır")

# Anahtar kelime
de = 4
# def = 4

# Sayılı değişken
sayi1 = 5
sayi2 = 2

# 1sayi = 7

# %% Liste
"""
- Bileşik veri türüdür ve çok yönlüdür
- [ 1, "a", 1.0]
- Farklı veri tiplerini içerisinde barındırabilir
"""

liste = [1, 2, 3, 4, 5, 6]
print(type(liste))

hafta = ["pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"]
# İlk eleman
print(hafta[0])

# Son eleman
print(hafta[6])
print(len(hafta))  # Eleman sayısı
print(hafta[len(hafta) - 1])
print(hafta[-1])

# Liste 2-3-4: 1, 2, 3 indeks
print(hafta[1:4])  # 1'den 4'e kadar 1 dahil - 4 dahil değil

# Sayı listesi
sayi_listesi = [1, 2, 3, 4, 5, 6]
sayi_listesi.append(7)
print(sayi_listesi)

# Listeden eleman çıkarma
sayi_listesi.remove(4)
print(sayi_listesi)

# Listeyi ters çevir
sayi_listesi.reverse()
print(sayi_listesi)

# Listeyi sırala
sayi_listesi = [1, 3, 2, 4, 5, 67, 0]
sayi_listesi.sort()
print(sayi_listesi)

# %% Tuple
"""
Değiştirilemez ve sıralı bir veri tipidir.
(1, 2, 3)
"""
tuple_veritipi = (1, 2, 3, 3, 4, 5, 6)
# İlk eleman
print(tuple_veritipi[0])

# 2. indeksten sonraki elemanları yazdır
print(tuple_veritipi[2:])

# Count eleman
print(tuple_veritipi.count(3))

tuple_xyz = (1, 2, 3)
x, y, z = tuple_xyz
print(x, y, z)

# %% Deque

from collections import deque

dq = deque(maxlen=3)

dq.append(1)  # 1 ekle sonuna [1]
print(dq)

dq.append(2)  # 2 ekle sonuna [1, 2]
print(dq)

dq.append(3)  # 3 ekle sonuna [1, 2, 3]
print(dq)

dq.append(4)  # 4 ekle sonuna [2, 3, 4]
print(dq)

dq = deque(maxlen=3)
dq.append(1)  # 1 ekle sonuna [1]
print(dq)
dq.append(2)  # 2 ekle sonuna [1, 2]
print(dq)

dq.appendleft(3)  # 3 ekle başına [3, 1, 2]
print(dq)

dq.clear()
print(dq)

# %% Sözlük
"""
- Bir çeşit karma tablo türüdür
- Anahtar ve değer çiftlerinden oluşur
- { "anahtar": değer }
"""

dictionary = {"İstanbul": 34,
              "İzmir": 35,
              "Konya": 42}
print(dictionary)

# İstanbul anahtarının değeri
print(dictionary["İstanbul"])

# Anahtarlar
print(dictionary.keys())

# Değerler
print(dictionary.values())

# %% Koşullu İfadeler (if-else statements)
"""
Bir bool ifadesine göre doğru ya da yanlış olarak değerlendirilmesine
bağlı olarak farklı hesaplamalar veya eylemler gerçekleştiren 
bir ifadedir.
"""

# Büyük küçük sayı karşılaştırması
sayi1 = 12.0
sayi2 = 20.0

if sayi1 < sayi2:
    print("Sayı 1 küçüktür sayı 2")
elif sayi1 > sayi2:
    print("Sayı 1 büyüktür sayı 2")
else:
    print("Sayı 1 eşittir sayı 2")

liste = [1, 2, 3, 4, 5]
deger = 1

if deger in liste:
    print("{} değeri listenin içerisindedir".format(deger))
else:
    print("{} değeri listenin içerisinde değildir".format(deger))

dictionary = {"Türkiye": "Ankara", "İngiltere": "Londra", "İspanya": "Madrid"}

keys = dictionary.keys()
deger = "Türkiye"
if deger in keys:
    print("Evet")
else:
    print("Hayır")

bool1 = True
bool2 = True

if bool1 and bool2:
    print("Doğru")
else:
    print("Yanlış")

# %% Döngüler
"""
- Bir dizi üzerinde yineleme yapmak için kullanılan yapılardır.
- Diziler: Liste, tuple, string, sözlük, numpy pandas veri tipleri
"""

# For
for i in range(1, 11):
    print(i)

liste = [1, 4, 5, 6, 8, 3, 3, 4, 67]
print(sum(liste))

toplam = 0
for c in liste:
    toplam = toplam + c

print(toplam)
"""
0 = 0 + 1
1 = 1 + 4
5 = 5 + 6
11 = 11 + 8
toplam = 19 ...
"""

tup1 = ((1, 2, 3), (3, 4, 5))
for x, y, z in tup1:
    print(x, y, z)

# While
i = 0
while i < 4:
    print(i)
    i = i + 1

liste = [1, 4, 5, 6, 8, 3, 3, 4, 67]
sinir = len(liste)

her = 0
hesapla = 0
while her < sinir:
    hesapla = hesapla + liste[her]
    her = her + 1
print(hesapla)

# %% Fonksiyonlar
"""
 - Karmaşık işlemleri toplar ve tek adımda yapmamızı sağlar
 - Şablon
 - Düzenleme
"""


# Kullanıcı tarafından tanımlanan fonksiyonlar

def daireAlan(r):
    """
    Parameters
    ----------
    r : int - Daire yarıçapı.

    Returns
    -------
    daire_alani : float - Daire alanı
    """
    pi = 3.14
    daire_alani = pi * (r ** 2)
    return daire_alani


daireAlanıDegiskeni = daireAlan(3)
print(daireAlanıDegiskeni)


def daireCevre(r, pi=3.14):
    """
    Parameters
    ----------
    r : int - Daire yarıçapı.
    pi: float - Pi sayısı

    Returns
    -------
    daire_cevre : float - Daire çevresi
    """
    daire_cevre = 2 * pi * r
    return daire_cevre


daireCevreDegiskeni = daireCevre(3)
print(daireCevreDegiskeni)

katsayi = 5


def katsayiCarpma():
    global katsayi
    print(katsayi * katsayi)


katsayiCarpma()
print(katsayi)


# Boş fonksiyon
def bos():
    pass


# Built-in fonksiyonlar
liste = [1, 2, 3, 4]
print(len(liste))
print(str(liste))
kopya_liste = liste.copy()
print(kopya_liste)
print(max(kopya_liste))
print(min(liste))

# Lambda fonksiyonları
"""
- İleri seviyeli
- Küçük ve anonim bir işlemdir
"""


def carpma(x, y, z):
    return x * y * z


sonuc = carpma(2, 3, 4)
print(sonuc)

# Aynı işlem lambda ile
lambda_fonksiyon = lambda x, y, z: x * y * z
sonuc2 = lambda_fonksiyon(2, 3, 4)
print(sonuc2)

# %% Yield
"""
- İterasyon - yineleme
- Generator
- Yield
"""

liste = [1, 2, 3]
for i in liste:
    print(i)

"""
Generator yineleyicileri
"""


def myGenerator():
    yield 1
    yield 2
    yield 3


for value in myGenerator():
    print(value)
