
# yorum satırı 

"""
Çoklu yorum satırı
yorum 2
yorum 3
print("merhaba")
"""

# Tam Sayılar - Integer - int
tam_sayi = 1 # bu bir tam sayı tipinde değişken -> integer
metin = 2 # tam sayı (int)
karakter = 4000 # tam sayı (int)

# type -> amacı içerisine yazılmış verinin tipini döndürür.

print(type(tam_sayi)) # type int 
print(type(30)) # type int

# ondalıklı sayılar - float
sayi = 10.1
ondalikli_sayi = 30.2

print(type(sayi)) # float
print(type(ondalikli_sayi)) # float

print(tam_sayi + ondalikli_sayi) # tip float

# karakter dizisi - string - str
# çift tırnak yada tek tırnaklar arasında yazılan ifadeler

metin = "" 
karakter = ''
cumle = "selam naber"
uzun_cumle = "selam naber napıyon nasılsın iyimisin ?"
deneme = "123123123123"

print(type(metin)) # string str

# mantıksal ifadeler boolean - bool

deneme = True # doğru
asd = False # yanlış

print(type(deneme)) # bool

# Nonetype

sayi = None

print(type(sayi))


# tiplerle çalışma
# str int 
# print("3"+4) -> hata verir

print("se"+"lam") # selam
print("Naber"+" "+"Napıyorsun") #Naber Napıyorsun
print("merhaba "*3) # merhabamerhabamerhaba

# True  -> 1
# False -> 0

print(12+True) # 13
print(23+False) # 23

# Tip Dönüşümü

# 45 + 80 sayılarını toplatıp ekrana
# 45 + 80 sayılarının toplamı : sonuc

sayi1 = 45
sayi2 = 80
toplam = sayi1+sayi2

print(str(sayi1)+" ve "+str(sayi2)+" sayılarının toplamı : "+str(toplam))

# integer,float,bool -> string
# str(içerisine int,float,bool ifadeleri gelebilir)

"""
NOT: print içerisinde sadece tek bir değişken alırsa tip dönüşümünü python 
bizim yerimize yapar. Fakat bir string ile farklı türden bir değişkeni
birleştirmek istiyorsak tip dönüşümü yapmamız gerekir.
"""

print(toplam) # print(str(toplam))
print(12)
print("toplam : "+str(toplam))


# string -> int 
# int(string)

sayi = "45"
sayi1 = "60"

print(sayi+sayi1) #4560

print(int(sayi)+int(sayi1)) # 105


# string -> float
# float

ondalik_sayi = "45.6"
ondalik_sayi1 = "60.9"

print(ondalik_sayi+ondalik_sayi1) #45.660.9

print(float(ondalik_sayi)+float(ondalik_sayi1)) # 105

