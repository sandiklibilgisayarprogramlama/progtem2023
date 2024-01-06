metin = "Deneme"

# string metotları
str.upper(metin)
str.lower(metin)
str.replace(metin, "e", "a")
str.title(metin)
str.capitalize(metin)

# len - range for döngüsü

print(range(len(metin)))
# pythonda string index 0 dan başlar

for i in range(len(metin)):  # 0,1,2,3,4,5
    print(metin[i])

print("-------------------")
# for döngüsü ile string elemanlarına erişmek
for eleman in metin:
    print(eleman)

"""
# klavyeden girilen bir kelimenin birinci ve üçüncü harflerini büyük yapınız.
girilen = input("kelime giriniz: ")
for i in range(len(girilen)):
    if i == 0 or i == 2:
        print(girilen[i].upper(), end="")
    else:
        print(girilen[i], end="")
print()

# ahmet upper fonksiyonunu bilmiyor ve klavyeden girilen bir kelimeyi büyük yazmak istiyor.
# ahmet bunu nasıl yapabilir?

girilen = input("kelime giriniz: ")
for harf in girilen:
    print(harf.title(), end="")
print()
"""

# strip metodu
# strip metodu stringin başındaki ve sonundaki boşlukları siler.
metin = "    Deneme    "
print("orjinal metin: ", metin)
print(metin.strip())
# left strip metodu
print(metin.lstrip())  # başındaki boşlukları siler
# right strip metodu
print(metin.rstrip())  # sonundaki boşlukları siler

print(metin.replace(" ", ""))  # boşlukları siler

# verilen bir kelimenin sadece başındaki boşlukları kaldıran kodu yazınız.
kelime = "    Örnek"
for harf in kelime:
    if harf == " ":
        print("", end="")
    else:
        print(harf, end="")
print()

# Ödev
kelime = "     Örnekler      "
# yukarda verilen kelimenin sonundaki boşlukları rstip metodu kullanmadan siliniz.

# ascii tablosu
# 0-127 arası ascii karakterler
# klavyede basılan her karakterin bir ascii kodu vardır.
# a -> 97
# A -> 65 01000001

# ord fonksiyonu
print(ord("a"))
print(ord("A"))

if "a" == "A":
    print("eşit")


# merhaba kelimesi ascii kod kullanarak büyük yazan kodu yazınız.
# chr fonksiyonu
# print(chr(97))
# print(chr(65))

# print(chr(98))
# print(chr(66))

for karakter in "merhaba":
    print(chr(ord(karakter)-32), end="")

print()
