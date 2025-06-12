import keyboard

print("1'den 10' a Sayılar")
print("uno = ?, due = ?, tre = ?, quattro = ?, cinque = ?, sei = ?, sette = ?, otto = ?, nove = ?, dieci = ?")
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")

mesaj = "Karşılık gelen rakamları giriniz:"
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

uno     = input(mesaj)
due     = input(mesaj)
tre     = input(mesaj)
quattro = input(mesaj)
cinque  = input(mesaj)
sei     = input(mesaj)
sette   = input(mesaj)
otto    = input(mesaj)
nove    = input(mesaj)
dieci   = input(mesaj)
print("")

print("Devam etmek için spacebar'a basınız.")
keyboard.wait("space")

print("")

print("uno = 1, dos = 2, tres = 3, cuatro = 4, cinco = 5, seis = 6, siete = 7, ocho = 8, nueve = 9, diez = 10")
print("")

print("İşlemler")

print("")
sayi1 = int(input("Birinci sayiyi giriniz:"))
sayi2 = int(input("İkinci sayiyi giriniz:"))
print("")

toplam = sayi1 + sayi2
print("")
print(toplam)
