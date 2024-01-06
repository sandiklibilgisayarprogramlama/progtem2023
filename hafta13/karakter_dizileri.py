
# karakter dizileri
karakter_dizisi = "merhaba dünya"

karakter_dizi2 = 'A'

print(type(karakter_dizisi))
print(type(karakter_dizi2))

# karakter dizileri üctırnak (""") kullanılarak çoklu satırda yazılabilir.

ornek_dizi = """
selam
merhaba 
lorem ipsum dolor sit amet consectetur adipisicing elit.

"""
print(ornek_dizi)

# bazı özel karakterler özel anlamlara sahiptir.
# bu karakterleri yazdırmak için kaçış dizileri \\) kullanılır.

# \n: yeni satır
ornek = "merhaba\n dünya"
print(ornek)
ornek2 = "merhaba\\n dünya"
print(ornek2)

# \t: tab
print("merhaba\tdünya")

# \": çift tırnak

print("ahmet: 'merhaba dünya' dedi ")
print("ahmet: \"merhaba dünya\" dedi ")
print("\\")
print('ahmet\'in doğum yeri erzurum\'dur.')

# karakter dizileri indekslenebilir ve parçalanabilir.
# ornek_metin = "merhaba d ü  n  y  a"
#               123456789 10 11 12 13
#               012345678  9 10 11 12

ornek_metin = "merhaba dünya"
print(ornek_metin[0])  # m
print(ornek_metin[2])  # r
print(ornek_metin[7])  # boşluk

# indisler 0 dan başlar.
# Aynı zamanda negatif değer alarak sondan başlayabilir.

print(ornek_metin[12])  # a
print(ornek_metin[-1])  # a

# ornek_metin = "merhab a       d   ü  n   y   a"
#                       -7  -6 -5  -4 -3 -2 -1


# karakter dizileri belirli aralıklarda parçalanabilir.

metin = "merhaba dünya"

print(metin[0:3])  # 0 m, 1 e, 2 r
# 0:3 aralığında 3 dahil değildir.

print(metin[8:13])
print(metin[-5:])

# len fonksiyonu -  lenght -> uzunluk
# karakter dizisinin uzunluğunu verir.

print(len(metin))

for i in range(len(metin)):
    print(metin[i])


# karakter dizileri birleştirilebilir.
ad = "Ahmet"
soyad = "Yılmaz"
print(ad, " ", soyad)  # print(ad+" "+soyad)

# karakter dizileri çarpılabilir.
print(ad*3)

# karakter dizileri değiştirilemez. (immutable)
print(metin[0])  # m
# metin[0] = "M"  # hata verir.

# karakter dizileri üzerinde bazı işlemler yapılabilir.
# upper -> büyük harfe çevirir.

kelime = "Merhaba"
print(kelime.upper())

# lower -> küçük harfe çevirir.
print(kelime.lower())

# replace -> karakter dizisi içindeki bir karakteri
# başka bir karakter ile değiştirir.
print(kelime.replace("a", "e"))

print(kelime.replace("Mer", "A"))

# title -> karakter dizisi içindeki kelimelerin
# baş harflerini büyük yapar.

print("ahmet yılmaz".title())

# print fonksiyonu end parametresi ile satır sonu karakterini
# değiştirebilir.

print("merhaba", "dünya")
print("ahmet"+" "+"uzun")


print("merhaba", end="\n")  # print("merhaba")
print("merhaba", end=".")
print("dünya")


# Örnek:Klavyeden alınan bir kelimenin ilk harfini büyütüp ekrana yazan
# programı kodlayınız.

# girilen = input("kelime giriniz: ")
# print(girilen.title())
# print(girilen[0].upper()+girilen[1:len(girilen)])

# capitalize -> karakter dizisinin ilk harfini büyük yapar.
# print("merhaba".capitalize())

# klavyeden alınan bir kelimenin son harfini büyütüp ekrana yazan
# programı kodlayınız.

# girilen = input("kelime giriniz: ")

# print(girilen[0:-1] + girilen[-1].upper())


"""
lorem ipsum dolor sit amet consectetur adipisicing elit.
1- yukarıdaki cümlede kaç tane a harfi vardır?
2- Yukarıdaki cümleyi tersten yazdırınız.
3- Yukarıdaki cümledeki kelimelerin ilk harflerini büyük harf yapınız.
4- yukarıdaki cümlede herbir kelime arasına . koyunuz.
"""

# 1
cumle = "lorem ipsum dolor sit amet consectetur adipisicing elit."
sayac = 0

for i in range(len(cumle)):
    if cumle[i] == "a":
        sayac = sayac+1

print(sayac)

#
print(cumle.count("a"))

# 2
cumle = "lorem ipsum dolor sit amet consectetur adipisicing elit."
for i in range(len(cumle)-1, -1, -1):
    print(cumle[i], end="")

# 3
cumle = "lorem ipsum dolor sit amet consectetur adipisicing elit."
print(cumle.title())

# 4
cumle = "lorem ipsum dolor sit amet consectetur adipisicing elit."
print(cumle.replace(" ", "."))
