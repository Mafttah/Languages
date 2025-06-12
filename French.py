import keyboard

print("1'den 10' a Sayılar")
print("")

print("une =?, deux =?, trois =?, quatre =?, cinq =?, six =?, sept =?, huit =?, neuf =?, dix =?")
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

mesaj = "Karşılık gelen rakamları giriniz:"
print("")

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")
print("")

une    = input(mesaj)
deux   = input(mesaj)
trois  = input(mesaj)
quatre = input(mesaj)
cincq  = input(mesaj)
six    = input(mesaj)
sept   = input(mesaj)
huit   = input(mesaj)
neuf   = input(mesaj)
dix    = input(mesaj)
print("")

print("Devam etmek için spacebar'a basınız.")
keyboard.wait("space")
print("")

print("une = 1, deux = 2, trois = 3, quatre = 4, cincq = 5, six = 6, sept = 7, huit = 8, neuf = 9, dix = 10")
print("")

print("İşlemler")
print("")

sayi1 = int(input("Birinci sayiyi giriniz:"))
sayi2 = int(input("İkinci sayiyi giriniz:"))

toplam = sayi1 + sayi2

print(toplam)