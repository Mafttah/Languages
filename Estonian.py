import keyboard

import colorama
from colorama import Fore, init
init()

print("1'den 10' a Sayılar")
print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

print("üks =?, kaks =?, kolm =?, neil =?, viis =?, kuus =?, seitse =?, kaheksa =?, üheksa =?, kümme =?")
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

mesaj = "Karşılık gelen rakamları giriniz:"

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

üks     = input(mesaj)
kaks    = input(mesaj)
kolm    = input(mesaj)
neil    = input(mesaj)
viis    = input(mesaj)
kuus    = input(mesaj)
seitse  = input(mesaj)
kaheksa = input(mesaj)
üheksa  = input(mesaj)
kümme   = input(mesaj)

print("Devam etmek için spacebar'a basınız.")
keyboard.wait("space")
print("")

print("üks = 1, kaks = 2, kolm = 3, neil = 4, viis = 5, kuus = 6, seitse = 7, kaheksa = 8, üheksa = 9, kümme = 10")
print("")
print("Devam etmek için spacebar'a basınız.")
keyboard.wait("space")
print("")

print("İşlemler")

sayi1 = int(input("Birinci sayiyi giriniz:"))
sayi2 = int(input("İkinci sayiyi giriniz:"))

toplam = sayi1 + sayi2

print(toplam)