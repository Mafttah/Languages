import keyboard

import colorama
from colorama import Fore, init
init()
print(Fore.RED,"1'den 10' a Sayılar")
print(Fore.WHITE,"jeden =?, dwa =?, trzy =?, cztery =?, piec =?, szesc =?, siedem =?, osiem =?, dziewiec =?, dziesiec =?")
print("")
print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")
mesaj = "Karşılık gelen rakamları giriniz:"

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")
jeden     = input(mesaj)
dwa       = input(mesaj)
trzy      = input(mesaj)
cztery    = input(mesaj)
piec      = input(mesaj)
szesc     = input(mesaj)
siedem    = input(mesaj)
osiem     = input(mesaj)
dziewiec  = input(mesaj)
deziesiec = input(mesaj)
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")
print("jeden = 1, dwa = 2, trzy = 3, cztery = 4, pięć = 5, sześć = 6, siedem = 7, osiem = 8, dziewięć = 9, dziesięć = 10")
