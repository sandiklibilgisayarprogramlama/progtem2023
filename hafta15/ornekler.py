# klavyeden girilen bir sayının tek mi çift mi olduğunu bulan program
"""
girilen = int(input("bir sayı giriniz: "))
if girilen % 2 == 0:
    print("çift")
else:
    print("tek")
"""
# klavyeden girilen bir metindeki sesli harf sayısını bulan program
"""
sayac = 0
girilen = input("bir metin giriniz: ")
for harf in girilen:
    if "a" == harf or "e" == harf or "ı" == harf or "i" == harf or "o" == harf or "ö" == harf or "u" == harf or "ü" == harf:
        sayac += 1  # sayac = sayac + 1

# harf in "aeiıoöuü"

print("sesli harf sayısı: ", sayac)
"""
# bir dosyadan veri okuyup okunan veri içindeki rakamların
# toplamını bulan program
"""
dosya = open("ornek3.txt", "r")
icerik = dosya.read()
dosya.close()

toplam = 0
for karakter in icerik:
    if karakter in "0123456789":
        toplam = toplam + int(karakter)

print(toplam)
"""
# 1 den 100 e kadar olan sayılardan 3 veya 5 in katı olanları
# ekrana yazdıran program
"""
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
"""
# klavyeden girilen N sayısına göre +N ve -N arasındaki sayıları ekrana yazdıran program

# N = 10  # 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
# N = 1  # 1 0 -1
"""
N = int(input("bir sayı giriniz: "))

for i in range(N, -1*N-1, -1):
    print(i, end=" ")
print()
"""

# klavyeden girilen 10 sayının toplamını bulan program
toplam = 0
for _ in range(10):  # 0 1 2 3 4 5 6 7 8 9
    sayi = int(input("bir sayı giriniz: "))
    toplam = toplam + sayi

print("toplam: ", toplam)

# klavyeden -1 girilinceye kadar girilen sayıların toplamını bulan program

while True:
    sayi = int(input("bir sayı giriniz: "))
    if sayi == -1:
        break
    toplam = toplam + sayi

print("toplam: ", toplam)
