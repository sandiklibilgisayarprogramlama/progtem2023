"""
#0 ile 100 arasındaki 3 e bölünün sayıları ekrana yazdıran
#uygulama

Adım 1: Başla
Adım 2: i=0
Adım 3: Eğer i%3==0 ise ekrana i yaz
Adım 4: i=i+1
Adım 5: Eğer i<100 ise 3. adıma git
Adım 6: Dur

pythonda döngü yapısı

for döngüsü
for sayac in aralik:
   -dongu icerisinde yapilacak islemler- 

range(bitis) # 0 dan baslar bitis-1 e kadar gider
print(range(10)) # 0-10(dahil değil) arasındaki sayıları getirir
-----------------
range(baslangic,bitis) # baslangic dan baslar bitis-1 e kadar gider
print(range(5,13)) # 5-13(dahil değil) arasındaki sayıları getirir

print(range(5, 13)) # 5,6,7,8,9,10,11,12
-------------------------
range(baslangic,bitis,artis) # baslangic dan baslar bitis-1 e 
kadar artış miktarınca gider

range(1,9,2) # 1,3,5,7

range(3,19,7) # 3,10,17

# artış miktarı negatif olabilir
range(30,3,-9) # 30,21,12
"""
# 0 ile 10 (dahil) arasındaki sayıları ekrana yazan programı kodlayınız.
for sayac in range(11):
    print(sayac)

# 5 ile 10 (hariç) arasındaki sayıları ekrana yazan programı kodlayınız.
for sayac in range(5, 10):  # [5,10)
    print(sayac)
print("*---------------")
# 5 ile 10 (dahil) arasındaki çift sayıları ekrana yazan programı kodlayınız.
for sayac in range(6, 11, 2):
    print(sayac)

for i in range(5, 11):
    if i % 2 == 0:
        print(i)

# 0 ile 100 arasında 3 e bölünen sayıları ekrana yazan programı kodlayınız.
# iki yollada yapınız.

# 1. yol
for sayac in range(0, 100, 3):
    print(sayac)

# 2. yol
for sayac in range(100):
    if sayac % 3 == 0:
        print(sayac)


# ekrana 100 kez finale daha çok çalışmalıyım yazdıran programı kodlayınız.

for dshfgsdhfıushflılas in range(100):  # 0, 1,....99
    print("Finale daha çok çalışmalıyım")


# ekrana aşağıdaki simgeyi çıkartan programı kodlayınız.
"""
*
**
***
****
*****
"""
for i in range(1, 6):
    print("*"*i)

# ekrana aşağıdaki simgeyi çıkartan programı kodlayınız.
"""
*****
****
***
**
*
"""

# odev
# 0 ile 100 arasındaki sayıların toplamını ekrana yazdıran programı kodlayınız.

# 0 ile 100 arasındaki 3 e ve 5 e bölünen sayıların toplamını ekrana yazdıran
# programı kodlayınız.

# aşağıdaki simgeyi ekrana yazdıran programı kodlayınız.
"""
***
 *
***
 *
***
"""
