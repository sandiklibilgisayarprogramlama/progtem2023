import random  # random modülünü içe aktar

# print(random.randint(1, 100))  # 1 ile 100 arasında rastgele bir sayı üretir

tahmin_edilecek_sayi = random.randint(1, 100)

for hak in range(10):
    print("kalan hak sayısı: ", 10 - hak)
    tahmin_sayi = int(input("bir sayı giriniz: "))
    if tahmin_sayi > tahmin_edilecek_sayi:
        print("daha küçük bir sayı giriniz")
    elif tahmin_edilecek_sayi > tahmin_sayi:
        print("daha büyük bir sayı giriniz")
    else:
        print("tebrikler")
        print("kalan hak sayısı: ", 10 - hak)
        break

    if hak == 9:
        print("hakkınız bitti")
        print("tahmin edilmesi gereken sayı: ", tahmin_edilecek_sayi)
