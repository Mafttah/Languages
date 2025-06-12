import keyboard

import colorama
from colorama import Fore, init
init()
print(Fore.RED,"1'den 10' a Sayılar")
print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

print(Fore.WHITE,"eins = ?, zwei = ?, drei = ?, vier = ?, fünf = ?, sechs = ?, sieben = ?, acht = ?, neun = ?, zehn = ?")
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")
mesaj = "Karşılık gelen rakamları giriniz:"
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

eins   = input(mesaj)
zwei   = input(mesaj)
drei   = input(mesaj)
vier   = input(mesaj)
fünf   = input(mesaj)
sechs  = input(mesaj)
sieben = input(mesaj)
acht   = input(mesaj)
neun   = input(mesaj)
zehn   = input(mesaj)
print("")

print("Devam etmek için spacebar'a basınız.")
keyboard.wait("space")

print("")

print("eins = 1, zwei = 2, drei  = 3, vier = 4, fünf = 5, sechs = 6, sieben = 7, acht = 8, neun = 9, zehn = 10")
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

print("İşlemler")

print("")
sayi1 = int(input("Birinci sayiyi giriniz:"))
sayi2 = int(input("İkinci sayiyi giriniz:"))
print("")

toplam = sayi1 + sayi2
print("")
print(toplam)