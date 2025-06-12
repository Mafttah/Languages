import keyboard

print("1'den 10' a Sayılar")
print("jeden =?, dva =?, tri =?, styri =?, pat =?, sest =?, sedem =?, osem =?, devat =?, desat =?")
print("")
print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")

mesaj = "Karşılık gelen rakamları giriniz:"

print("Devam etmek için enter'a basınız.")
keyboard.wait("enter")

jeden = input(mesaj)
dva   = input(mesaj)
tri   = input(mesaj)
styri = input(mesaj)
pat   = input(mesaj)
sest  = input(mesaj)
sedem = input(mesaj)
osem  = input(mesaj)
devat = input(mesaj)
desat = input(mesaj)

print("Devam etmek için spacebar'a basınız.")
keyboard.wait("space")
print("")

print("jeden = 1, dva = 2, tri = 3, styri = 4, pat = 5, sest = 6, sedem = 7, osem = 8, devat = 9, desat = 10")

sayi1 = int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("İkinci sayiyi giriniz: "))
sayi3 = int(input("Ucuncu sayiyi giriniz: "))
sayi4 = int(input("Dorduncu sayiyi giriniz: "))

toplam = sayi1 + sayi2 + sayi3 + sayi4

print(toplam)