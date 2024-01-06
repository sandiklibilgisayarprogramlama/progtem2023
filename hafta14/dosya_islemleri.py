# open metodu
# open metodu dosya açmak için kullanılır.

# r -> read - okuma modu
# w -> write - yazma modu
# a -> append - ekleme modu

# write dosyayı siler ve yeniden oluşturur.
#  a modunda ise dosya yoksa oluşturur. varsa dosyanın sonuna ekleme yapar.
"""
dosya = open("dosya.txt", "w")
dosya.write("ahmet\n")  # dosyaya yazma işlemi
dosya.write("nasılsın ?")  # dosyaya yazma işlemi
dosya.close()  # dosyayı kapatma işlemi
"""

"""
# read metodu
dosya = open("dosya.txt", "r")
print(dosya.read())  # dosyayı okuma işlemi
dosya.close()  # dosyayı kapatma işlemi


# satır satır okuma
dosya = open("dosya.txt", "r")
for satir in dosya:
    print(satir, end="")
print()
dosya.close()
"""

# bir dosya içinde saklanan kullanıcı adi ve şifreleri okuyarak eğer klavyeden
# girilen veriler ile dosya içindeki veriler uyuşuyorsa giriş başarılı değilse başarısız
# yazan kodu yazınız.
"""
dosya = open("bilgiler.txt", "r")
satir_sayi = 0
for satir in dosya:
    if satir_sayi == 0:
        kullanici_adi = satir.strip()
    elif satir_sayi == 1:
        sifre = satir.strip()
    elif satir_sayi == 2:
        adi = satir.strip()
    satir_sayi = satir_sayi+1

girilen_kullanici_adi = input("kullanıcı adı giriniz: ").strip()
girilen_sifre = input("şifre giriniz: ").strip()

if kullanici_adi == girilen_kullanici_adi and sifre == girilen_sifre:
    print("giriş başarılı")
    print("hoşgeldin ", adi)
else:
    print("giriş başarısız")

dosya.close()
"""

# bir dosyanın içinde ters bir cümle bulunmaktadır. bu cümleyi okuyarak düz bir cümle
# elde ediniz ve aynı dosyaya baştan yazınız.
dosya = open("ters_metin.txt", "r")
ters_metin = dosya.read()
dosya.close()

duz_metin = ters_metin[::-1]

dosya = open("ters_metin.txt", "w")
dosya.write(duz_metin)
dosya.close()
