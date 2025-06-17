import keyboard

import colorama
from colorama import Fore, init
init()
print(Fore.RED,"1'den 10' a Sayılar")
print(Fore.WHITE,"jeden =?, dva =?, tri =?, styri =?, pat =?, sest =?, sedem =?, osem =?, devat =?, desat =?")
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

print(Fore.RED, "Lesson 2 - Greeting")
print("")
print(Fore.WHITE,"Ahoj = Hello")
print("Ako sa mate = How are you?")
print("Rad vas spoznavam = Nice to meet you")
print("Uvidime sa zajtra = See you tomorrow")
print("Dobre rano = Good morning")
print("Dobre den = Good afternoon")
print("Dobry vecer = Good evening")
print("Dobru noc = Good night")
print("Ako sa volate ? = What is your name ?")
print("Moje meno je ____ = My name is ___")
print("kde byvas ? = Where do you live?")
print("Odkial ste ? = Where are you from?")
print("Rad vas opat'vidim = Nice to see you")
print("Pekny den = Have a nice day")
print("Uvidime sa neskor = See you later")
print("Dovidenia = Goodbye")
print("Prosim = Please")
print("Dakujem = Thank you")

print(Fore.RED, "Lesson_3 = Regular Verbs,")

print(Fore.WHITE,"Regular verbs are divided into 3 categories")

print(Fore.BLUE, "1. -AŤ/AŤ sa Verbs")

print(Fore.WHITE, "pýtať = to ask")
print("hrať = to play")
print("čítať = to read")
print("počúvať = to listen")
print("ležať = to lie down")
print("vstávať = to get up")
print("otvárať = to open")
print("zatvárať = to close")
print("zavolať	= to call")
print("hrať sa = to play (refl.)")
print("napísať = to write")
print("smiať sa = to laugh")
print("plakať = to cry")
print("kráčať =to walk")
print("počítavať = to calculate")
print("skúšať = to try")
print("napomínať = to admonish")
print("nosievať = to wear")
print("prechádzať = to walk")
print("používať = to use")
print("predpokladať = to assume")
print("vysnívať = to dream")

print(Fore.BLUE, "2. -OVAŤ Verbs")

print(Fore.WHITE, "pracovať = to work")
print("študovať = to study")
print("milovať = to love")
print("tancovať = to dance")
print("maľovať = to paint")
print("zapisovať = to note down")
print("budovať = to build")

print(Fore.BLUE, "3. -IŤ Verbs")

print(Fore.WHITE,"variť = to cook")
print("učiť = to teach")
print("kresliť = to draw")
print("pocítiť = to feel")
print("čistiť = to clean")
print("riešiť = to solve")
print("žiť = to live")
print("veriť = to believe")
print("tvrdiť = to claim")
print("vlastniť = to own")
print("hodnotiť = to evaluate")