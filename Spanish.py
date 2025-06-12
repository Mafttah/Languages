import keyboard

print("1'den 10' a Sayılar")
print("uno =?, dos =?, tres =?, cuatro =?, cinco =?, seis =?, siete =?, ocho =?, nueve =?, diez =?")
print("")
print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")

mesaj = "Karşılık gelen rakamları giriniz:"

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")

uno    = input(mesaj)
dos    = input(mesaj)
tres   = input(mesaj)
cuatro = input(mesaj)
cinco  = input(mesaj)
seis   = input(mesaj)
siete  = input(mesaj)
ocho   = input(mesaj)
nueve  = input(mesaj)
diez   = input(mesaj)

print("Devam etmek için spacebar'a basınız.")
keyboard.wait("space")
print("")

print("uno = 1, dos = 2, tres = 3, cuatro = 4, cinco = 5, seis = 6, siete = 7, ocho = 8, nueve = 9, diez = 10")

print("İşlemler")

sayi1 = int(input("Birinci sayiyi giriniz:"))
sayi2 = int(input("İkinci sayiyi giriniz:"))

toplam = sayi1 + sayi2

print(toplam)