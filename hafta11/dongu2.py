"""

# odev
# 0 ile 100 arasındaki sayıların toplamını ekrana yazdıran programı kodlayınız.

# 0 ile 100 arasındaki 3 e ve 5 e bölünen sayıların toplamını ekrana yazdıran
# programı kodlayınız.

# aşağıdaki simgeyi ekrana yazdıran programı kodlayınız.

***
 *
***
 *
***
"""

toplam = 0

for i in range(101):
    toplam = toplam + i

print("0 ile 100 arasındaki sayıların toplamı:")
print(toplam)


# 0 ile 100 arasındaki 3 e ve 5 e bölünen sayıların toplamını ekrana yazdıran
# programı kodlayınız.
toplam = 0
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:  # if i%15==0:
        toplam = toplam + i

print("0 ile 100 arasındaki 3 e ve 5 e bölünen sayıların toplamı:")
print(toplam)


# aşağıdaki simgeyi ekrana yazdıran programı kodlayınız.


"""
***        0
 *         1
***        2
 *         3
***        4
"""

for i in range(5):
    if i % 2 == 0:
        print("***")
    else:
        print(" * ")


# ör:

# *0 ile 1000 arasındaki 60 a bölünen sayıları ekrana yazdıran programı kodlayınız.

for sayac in range(1000):
    if sayac % 60 == 0:
        print(sayac)

# --------------------------------------------

# *300 den geriye doğru 3 e bölünen sayıları ekrana yazdıran programı kodlayınız.
# 1. yol
for s in range(300, 0, -1):
    if s % 3 == 0:
        print(s)

# 2.yol
for s in range(300, 0, -3):
    print(s)

# --------------------------------------------

# *girilen bir sayının faktoriyelini alma
"""
girilen = int(input("faktoiyelini almak istediğiniz sayıyı giriniz:"))
faktoriyel = 1
for s in range(girilen, 1, -1): # for s in range(1,girilen+1):
    faktoriyel = faktoriyel * s

print(faktoriyel)
"""
# --------------------------------------------
# * 1 den baslayarak klavyeden girilen bir sayıya kadar olan sayılarının karelerini ekrana
# yazdıran programı kodlayınız.
"""
sayi = int(input("karesini almak istediğiniz son sayıyı giriniz:"))
for s in range(1, sayi + 1):
    print(s * s)  # print(s**2)
"""
# --------------------------------------------

# break ve continue

# break: belirli bir koşulda döngüyü sonlandırmak için kullanılır.
"""

for s in range(10):
    if s==5:
        break
    print(s)
"""

# ör: klavyden negatif bir sayı girilen sayıyı ekrana yazan programı kodlayınız.

"""
for k in range(1000):
    girilen = int(input("bir sayı giriniz (Çıkma için -1):"))
    if girilen >= 0:
        print(girilen)
    else:
        break
"""
# continue: belirli bir koşulda döngüyü sonlandırmak için kullanılır.

"""
for s in range(10):
    if s==5:
        continue
    print(s)

# 0,1,2,3,4,6,7,8,9
"""

# -10 ile 10 arasındaki pozitif sayıları ekrana
# yazdıran programı kodlayınız.
print("---------------------")
for i in range(-10, 10):
    if i <= 0:
        continue
    print(i)

# --------------------------------------------
"""
*       1
        2
***     3
        4
*****   5
*****   5
        4
***     3
        2
*       1
"""
# Yukarıdaki şekli ekrana yazdıran programı kodlayınız.

for i in range(1, 6):
    if i % 2 == 0:
        print("")
    else:
        print("*"*i)

for i in range(5, 0, -1):
    if i % 2 == 0:
        print("")
    else:
        print("*"*i)


"""
klavyeden girilen sayı kadar satır ve
sütundan oluşan bir kare oluşturan programı kodlayınız.
"""
sayi = int(input("sayi giriniz:"))
for i in range(sayi):
    print("*"*sayi)


"""
* klavyden girilen bir sayının asal olup olmadığını bulan programı kodlayınız.

* klavyeden girilen bir sayıya göre içi boş kare oluşturan programı kodlayınız.

"""
