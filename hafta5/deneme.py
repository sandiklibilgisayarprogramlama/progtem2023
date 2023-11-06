
# int , float -> str

print(str(12)) # "12"
print(str(15.3)) # "15.3"

print(type(str(100)))
# klavyeden bilgi alma
# input() -> str
# NOT: input fonksiyonu aracılığıyla klavyeden alınan veriler
# str tipinde olur.
#girilen = input("Bir ifade giriniz:")
#print(girilen)
#print(type(girilen))

# klavyeden girilen iki sayının toplamını ekrana yazdıran program
"""
sayi1 = input("Birinci sayiyi giriniz") 
sayi2 = input("ikinci sayıyı giriniz") 

toplam = int(sayi1)+int(sayi2)
print(toplam)



# klavyeden girilen iki sayının çarpımını ekrana yazdıran program
sayi1 = int(input("birinci sayıyı giriniz"))
sayi2 = int(input("ikinci sayıyı giriniz"))

carpim = sayi1*sayi2
print(carpim)


if şartlar:
    print("şart saglandı")
    print("şart saglandı 2")


print("devam ediyor")    
"""

# klavyeden girilen sayının tek mi çift mi olduğunu ekrana yazdıran program
"""
sayi = int(input("bir sayı giriniz"))
if sayi % 2 == 0: # % mod işareti -> bir sayının bir sayıya bölümünden kalan
    print("çift")
    print("çift")
print("if bitti")
print("program bitti")
"""
# klavyeden girilen bir sayının negatif mi pozitif mi olduğunu ekrana yazdıran program

sayi = int(input("bir sayı giriniz"))
if sayi<0:
    print("negatif")

if sayi>0:
    print("pozitif")