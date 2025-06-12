import keyboard

import colorama
from colorama import Fore

print(Fore.RED,"1'den 10' a Sayılar")
print(Fore.WHITE,"uno =?, dos =?, tres =?, cuatro =?, cinco =?, seis =?, siete =?, ocho =?, nueve =?, diez =?")
print("")


mesaj = "uno: "
uno    = input(mesaj)
mesaj = "dos: "
dos    = input(mesaj)
mesaj = "tres: "
tres   = input(mesaj)
mesaj = "cuatro: "
cuatro = input(mesaj)
mesaj = "cinco: "
cinco  = input(mesaj)
mesaj = "seis: "
seis   = input(mesaj)
mesaj = "siete: "
siete  = input(mesaj)
mesaj = "ocho: "
ocho   = input(mesaj)
mesaj = "nueve: "
nueve  = input(mesaj)
mesaj = "diez: "
diez   = input(mesaj)

print("Devam etmek için spacebar'a basınız.")
keyboard.wait("space")

print(f"\nGirilen Değerler: \nuno = {uno}, dos = {dos}, tres = {tres}, cuatro = {cuatro}, cinco = {cinco}, seis = {seis}, siete = {siete}, ocho = {ocho}, nueve = {nueve}, diez = {diez}")

print("\nCevap Anahtarı:\n")
print("uno = 1\n, dos = 2\n, tres = 3\n, cuatro = 4\n, cinco = 5\n, seis = 6\n, siete = 7\n, ocho = 8\n, nueve = 9\n, diez = 10\n")
print("İşlemler")

sayi1 = int(input("Birinci sayiyi giriniz:"))
sayi2 = int(input("İkinci sayiyi giriniz:"))

toplam = sayi1 + sayi2

print(toplam)