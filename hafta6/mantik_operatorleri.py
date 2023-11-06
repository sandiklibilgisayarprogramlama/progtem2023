"""
<
>
<=
>=
!=
==

if koşul:
    # koşul doğruysa
    # bu blok çalışır
"""

print(10 == 10)  # True

print(10 <= 10)  # küçük yada eşit

print(10 != 10)  # eşit değil

print(10 > 40)  # false

print(10 < 60)  # true

print(10 >= 100)  # false

print(10 % 2 == 0)  # true

print(10+20 < 0)  # false

print(90/3 == 10)  # false

print(40 % 3 == 0)  # false


"""
koşul sonucu true olursa if bloğu çalışır

"""

# klavyeden girilen bir sayının 6 ya tam bölünüyorsa
# ekrana 6 tam bölünüyor yazan programı kodlayınız.abs
"""
sayi = int(input("sayı giriniz: "))

if sayi % 6 == 0:
    print("6 ya tam bölünüyor")

if - else ifadesi

if koşul :
    # koşul doğruysa
    # bu blok çalışır
else:
    # koşul yanlışsa
    # bu blok çalışır
"""

# bir sayının tek mi çift mi olduğunu ekrana yazdıran programı kodlayınız.
"""
girilen = int(input("Sayi giriniz: "))
if girilen % 2 == 0:
    print("sayi çift")
else:
    print("sayi tek")
"""
# koşul birleştime

# and operatörü
# koşulların hepsi doğruysa true döner

"""

if koşul1 and koşul2 and koşul3 :
    # koşulların hepsi doğruysa
    # bu blok çalışır
else:
    # koşullardan en az biri yanlışsa
    # bu blok çalışır

"""

# klavyeden girilen bir sayının 0 ile 100 arasında olup olmadığını ekrana yazan program
"""
x = int(input("sayi giriniz: "))
if x > 0 and x < 100:
    print("x 0 ve 100 arasındadır")
else:
    print("x belirtilen aralıkta değil")
"""
# print(True and True) # True
# print(True and False) # False

# or operatörü
# koşulların en az biri doğruysa true döner

# klavyeden girilen bir sayının 2 ye veya 3 e
# bölünmesi durumunda ekrana bölünüyor
# bölünmemesi durumunda ise bölünmüyor yazan uygulamayı kodlayınız.
"""
x = int(input("sayi giriniz: "))

if x % 2 == 0 or x % 3 == 0:
    print("sayı 2 ye veya 3 e bölünür")
else:
    print("sayı 2 ye veya 3 e bölünmez")
"""
# print(True or True) # True
# print(True or False) # True
# print(False or False) # False

# ör:
# if (10>0 and 0<100) and (True and False):
#    print("şart saglandı")

#  print(True and (False or True)) # true

# not operatörü

print(not True)  # false
print(not False)  # true

# if elif else ifadesi

# if koşul1:
#    # koşul1 doğruysa
#    # bu blok çalışır
# elif koşul2:
#    # koşul2 doğruysa
#    # bu blok çalışır
# elif koşul3:
#    # koşul3 doğruysa
#    # bu blok çalışır
# else:
#    # koşulların hepsi yanlışsa

# klavyden girilen bir sayının pozitif mi negatif mi yoksa 0 mı oldugunu ekrana yazan programı
# kodlayınız

"""
x = int(input("sayi giriniz: "))

if x > 0:
    print("pozitif")
elif x < 0:
    print("negatif")
elif x == 0:
    print("sıfır")
"""
"""
ÖDEVLER:
1- klavyeden girilen yaşa göre ehliyet alıp alamayacağını ekrana yazdıran programı kodlayınız.
ehliyet yaşı 18 dir.
2- klavyeden girilen boy ve kiloya göre kullanıcının obez olup 
olmadığını ekrana yazdıran programı kodlayınız.
3- klavyeden girilen gün numarasına göre hangi gün oldugunu yazınız.
4- klavyden girilen vize ve final notuna göre öğrencinin geçip geçmediğini ekrana yazdıran programı kodlayınız.
geçme notu 50 dir.


"""
# bir öğrencinin notuna göre harf notunu ekrana yazdıran programı kodlayınız.
# 0-30 dahil ff
# 31-50 dahil dd
# 51-70 dahil cc
# 71-90 dahil bb
# 91-100 dahil aa

_not = int(input("not giriniz: "))
if _not >= 0 and _not <= 30:
    print("ff")
elif _not > 30 and _not <= 50:
    print("dd")
elif _not > 50 and _not <= 70:
    print("cc")
elif _not > 70 and _not <= 90:
    print("bb")
elif _not > 90 and _not <= 100:
    print("aa")
else:
    print("hatalı not girdiniz")
