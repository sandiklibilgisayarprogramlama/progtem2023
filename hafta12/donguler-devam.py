# klavyeden girilen bir sayıya göre içi boş kare oluşturan programı kodlayınız.


"""
***
* *
***

****
*  *
*  *
****


sayi = int(input("Bir sayı giriniz: "))

for sayac in range(sayi):
    if sayac == 0 or sayac == sayi - 1:
        print("*" * sayi)
    else:
        print("*"+" "*(sayi-2)+"*")
"""
"""
# while dongusu
while kosul:
    # koşul sağlandıkça döngü çalışır.

for sayac in range(10):
    print(sayac)

sayac=0
while sayac < 10:
    print(sayac)
    sayac += 1


# Örnekler
# klavyeden -1 girilince kadar girilen sayıların toplamını ekrana yazdıran programı kodlayınız.
#1. yol
toplam = 0
girilen = 0

while girilen != -1:
    girilen = int(input("bir sayı giriniz: "))
    toplam = toplam + girilen

print("toplam: ", toplam)

# 2. yol
toplam = 0
while True:
    girilen = int(input("bir sayı giriniz: "))
    if girilen == -1:
        break
    toplam = toplam + girilen

print("toplam: ", toplam)


# toplam değeri 100 u gecinceye kadar sadece cift sayıları toplayan programı kodlayınız.
toplam = 0
while toplam < 100:
    girilen = int(input("bir sayı giriniz: "))
    if girilen % 2 == 1:
        continue
    toplam = toplam + girilen

print("toplam: ", toplam)
---------------------------------

999999999
88888888
7777777
666666
55555
4444
333
22
1

yukarıdaki şekil while dongusu kullanarak oluşturunuz

sayac = 9
while sayac > 0:
    print(str(sayac) * sayac)
    sayac = sayac - 1


Ödev 1: 1 den 100 e kadar olan fibonacci sayılarını ekrana yazdıran programı kodlayınız.
1 1 2 3 5 8 13 21 34 55 89


# iç içe döngüler

for sayac in range(10):
    print("disaridaki ")
    for sayac2 in range(10):
        print("icteki ")

# iç içe döndülerden yararlanılarak çarpım tablosu oluşturunuz.
for birinci in range(1, 11):
    for ikinci in range(1, 11):
        print(str(birinci)+" x "+str(ikinci)+" = "+str(birinci*ikinci))
    print("--------------------------")


# 1 den 100 e kadar olan asal sayıları ekrana yazdıran programı kodlayınız.
"""
for sayi in range(2, 101):
    asal_kontrol = True
    for yeni in range(2, sayi):
        if sayi % yeni == 0:
            asal_kontrol = False
            break
    if asal_kontrol:
        print(sayi)
