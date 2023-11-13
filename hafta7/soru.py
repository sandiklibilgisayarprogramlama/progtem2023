# Klavyeden girilen boy ve kiloya göre obez olup olmadığını ekrana
# yazdıran uygulama

# 30 üstünde çıkarsa
# formul = kilo / boy * boy
"""
kilo = float(input("kilonuzu giriniz: "))
boy = float(input("boyunuzu giriniz: "))/100

vki = kilo / boy**2
print(vki)
if vki > 30:
    print("Kilonuza dikkat ediniz")
else:
    print("Kilonuz normaldir")

Örn:

Bir kullanıcının Kullanıcı adı ahmet şifresi 1234 ise
Klavyeden kullanıcı adı ve şifre isteyen 
ve girilen değerlerin doğruluğunu kontrol eden
değerler doğru ise "Giriş Başarılı" değilse "Giriş Başarısız" yazan
programı yazınız




kullanici_adi = "ahmet"
sifre = "1234"

kullanici_adi_girilen = input("Kullanıcı adını giriniz: ")
sifre_girilen = input("Şifrenizi giriniz: ")

if kullanici_adi == kullanici_adi_girilen and sifre == sifre_girilen:
    print("Giriş Başarılı")
else:
    print("Giriş Başarısız")

# klavyeden girilen ay numarasına göre ayın kaç gün çektiğini ekrana yazdıran program

ay_numarasi = int(input("Bir ay numarası giriniz: "))
if ay_numarasi <= 7:
    if ay_numarasi % 2 == 1:
        print("31 gün bulunur")
    else:
        print("30 veya altı gün bulunur")
else:
    if ay_numarasi % 2 == 0:
        print("31 gün bulunur")
    else:
        print("30 gün bulunur")

"""
# klavyeden girilen ay numarasına göre hangi mevsimde olduğunu ekrana yazdıran program

ay_numarasi = int(input("Bir ay numarası giriniz: "))

if ay_numarasi == 12 or ay_numarasi == 1 or ay_numarasi == 2:
    print("Kış mevsimindeyiz")
elif ay_numarasi == 3 or ay_numarasi == 4 or ay_numarasi == 5:
    print("İlkbahar mevsimindeyiz")
elif ay_numarasi == 6 or ay_numarasi == 7 or ay_numarasi == 8:
    print("Yaz mevsimindeyiz")
else:
    print("Sonbahar mevsimindeyiz")

# klavyeden girilen park süresine göre ücreti hesaplayan program
# 0-2 saat arası 5 tl
# 2-5 saat arası 10 tl
# 5 saatten fazla 15 tl

park_suresi = int(input("Park süresini giriniz: "))
if park_suresi > 0 and park_suresi < 2:
    print("5 tl")
elif park_suresi >= 2 and park_suresi < 5:
    print("10 tl")
elif park_suresi >= 5:
    print("15 tl")
else:
    print("Hatalı giriş yaptınız")
