import keyboard

import colorama
from colorama import Fore, init
init()
print(Fore.RED,"1'den 10' a Sayılar")
print(Fore.WHITE,"uno = ?, due = ?, tre = ?, quattro = ?, cinque = ?, sei = ?, sette = ?, otto = ?, nove = ?, dieci = ?")
print("")

mesaj = "uno: "
uno     = input(mesaj)
mesaj = "dos: "
due     = input(mesaj)
mesaj = "tre: "
tre     = input(mesaj)
mesaj = "quattro:"
quattro = input(mesaj)
mesaj = "cinque:"
cinque  = input(mesaj)
mesaj = "sei: "
sei     = input(mesaj)
mesaj = "sette: "
sette   = input(mesaj)
mesaj = "otto: "
otto    = input(mesaj)
mesaj = "nove: "
nove    = input(mesaj)
mesaj = "dieci: "
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

print(Fore.RED, "Lesson 2 - Greeting")
print("")
print(Fore.WHITE,"Cioa = Hello")
print("Come stai = How are you?")
print("Felice di vederti = Nice to see you")
print("Piacere di conoscerti = Nice to meet you")
print("A domani = See you tomorrow")
print("Buon giorno  = Good morning")
print("Buon pomeriggio = Good afternoon")
print("Buona srea = Godd evening")
print("Buona notte = Good night")
print("Come ti chiami ?  = What is your name ?")
print("Mi chiamo____ = My name is ___")
print("Dóve vive ? = Where do you live?")
print("Di dove sei ? = Where are you from?")
print("Buona giornata = Have a nice day")
print("A dopo = See you later")
print("Arrivederci = Goodbye")
print("Per favore = Please")
print("Grazie = Thank you")

print(Fore.RED, "Lesson_3 = Regular Verbs,")

print(Fore.WHITE,"Regular verbs are divided into 3 categories")

print(Fore.BLUE, "1. -Are Verbs")

print(Fore.WHITE, "abitare to live, inhabit")
print("aiutare = to help")
print("amare = to love")
print("arrivare	= to arrive")
print("ascoltare = to listen to")
print("aspettare = to wait for")
print("baciare*	= to kiss")
print("conservare = to conserve, keep")
print("considerare = to consider")
print("consigliare*	= to advise")
print("costare = to cost")
print("causare = to cause")
print("cenare = to have dinner")
print("chiamare = to call")
print("cominciare* = to begin, start")
print("comprare	= to buy")
print("insegnare = to teach")
print("lamentare = to complain")
print("lasciare* = to leave")
print("lavare = to wash")
print("lavorare	= to work")
print("mangiare* = to eat")
print("nuotare = to swim")
print("cucinare	= to cook")
print("curare = to take care of, treat")
print("disegnare = to draw")
print("incontrare = to meet, encounter")
print("indossare = to wear, put on")
print("diventare = to become")
print("dubitare	= to doubt")
print("entrare = to enter")
print("evitare = to avoid")
print("fumare = to smoke")
print("guardare	= to watch, look")
print("guidare = to drive")
print("imparare	= to learn")
print("bastare = to suffice, be enough")
print("camminare = to walk")
print("cantare = to sing")
print("ordinare	= to organize, sort, put in order")
print("parlare = to speak")
print("passare = to pass, go by; to drop in; to spend time")
print("pensare = to think")
print("portare = to take, bring")
print("pranzare	= to have lunch")
print("prenotare = to book, reserve")
print("provare = to try")
print("restare = to stay, remain")
print("ricordare = to remember")
print("salutare	= to greet, say hello")
print("salvare = to save")
print("sbagliare* = to make a mistake, be wrong")
print("sperare = to hope")
print("studiare* = to study")
print("tagliare* = to cut")
print("tornare = to return, go back")
print("trovare = to find")
print("viaggiare* = to travel")
print("visitare	= to visit")

print(Fore.BLUE, "2. -Ere Verbs")

print(Fore.WHITE, "accedere to access")
print("accendere = to turn on")
print("apprendere = to learn")
print("assumere = to assume; to hire, employ")
print("attendere = to wait for")
print("battere = to beat")
print("chiedere = to ask")
print("chiudere = to close")
print("comprendere = to understand, to include")
print("conoscere = to know")
print("correre	= to run, hurry")
print("credere	= to believe")
print("decedere = to die")
print("decidere = to decide")
print("descrivere = to describe")
print("dibattere = to debate")
print("discutere = to discuss")
print("mettere	= to put")
print("perdere	= to lose")
print("precedere = to precede")
print("premere	= to press")
print("prendere = to take")
print("pretendere = to claim")
print("promettere = to promise")
print("rendere	= to give back, return")
print("ricevere = to receive")
print("ridere = to laugh")
print("ripetere = to repeat")
print("rispondere = to answer")
print("rompere = to break")
print("scendere = to descend, go down")
print("scrivere = to write")
print("sorridere = to smile")
print("spendere = to spend")
print("temere = to fear")
print("tessere	= to weave")
print("vedere = to see")
print("vendere	= to sell")
print("vivere = to live")

print(Fore.BLUE, "3. -Ire Verbs")

print(Fore.WHITE, "aborrire** = to abhor")
print("acconsentire = to agree, consent")
print("applaudire** = to applaud, clap")
print("aprire = to open")
print("assentire = to assent")
print("assorbire** =  to absorb")
print("avvertire = to warn")
print("bollire = to boil")
print("compartire** = to share, to divide")
print("convertire = to convert")
print("coprire = to cover")
print("cucire*** = to sew")
print("divertire = to enjoy, amuse")
print("dormire = to sleep")
print("fuggire = to escape, flee")
print("inghiottire** = to swallow")
print("mentire** = to lie")
print("nutrire** = to feed")
print("offrire = to offer")
print("partire = to leave, to start")
print("riaprire = to reopen")
print("riempire = to fill")
print("scoprire = to discover, to uncover")
print("seguire = to follow")
print("sentire = to feel, hear, smell, taste, sense")
print("servire = to serve")
print("soffrire = to suffer")
print("tossire** = to cough")
print("vestire to dress, to wear")

print(Fore.RED,"Lesson 3.1 - Present Tense")           

print(Fore.WHITE,"I = io")
print("you = tu")
print("he/she/it = lui/lei")
print("we = noi")
print("you = voi")
print("they = loro")

print("Example for parlare = to speak, credere = to believe and dormire = to sleep")

print("yo parlo - yo credo - yo dormo")
print("tu parli - tu credi dormi")
print("lui/lei parla - lui/lei corede - lui/lei dorme")
print("noi parliamo - nosotros crediamo, noi dormiamo")
print("voi parlatr - vosotros credete - voi dormite")
print("loro parlano - loro credono - loro dormono")

print(Fore.BLUE, "Lesson 4 = Adjectives")

print(Fore.WHITE, "Felice = Happy")
print("Triste = Sad")
print("Arrabbiato = Angry")
print("Spaventato = Afraid")
print("Gioia = Joy")
print("Sorpreso = Surprised")
print("Calmo = Calm")
print("Annoiato = Bored")
print("Facile = Easy")
print("Difficile = Difficult")
print("Cattivo = Bad")
print("Buono = Good")
print("Rumoroso = Noisy")
print("Silenzioso = Quiet")
print("Forte = Strong")
print("Debole = Weak")
print("Duro = Hard")
print("Morbido = Soft")
print("Più = More")
print("Meno = Less")
print("Pulito = Clean")
print("Sporco = Dirty")
print("Vecchio = Old")
print("Nuovo = New")
print("Grande = Big")
print("Piccolo = Small")
print("Giovane = Young")
print("Magro = Skinny")
print("Grasso = Fat")
print("Bello = Pretty") 
print("Brutto = Ugly")
print("Spesso = Thick")
print("Sottile = Thin")
print("Ruvido = Rough")
print("Liscio = Smooth")

print(Fore.RED,"Lesson 5 - Days and Months")
print("")

print(Fore.BLUE,"Lesson 5.1 - Days of the week")
print("")

print(Fore.WHITE,"I giorni della settimana = The days of the week")
print("Giorno = Day")
print("Settimana = Week")
print("Lunedì = Monday")
print("Martedì = Tuesday")
print("Mercoledì = Wednesday")
print("Giovedì = Thursday")
print("Venerdì = Friday")
print("Sabato = Saturday")
print("Domenica = Sunday")
print("Fine settimana = Weekend")

print(Fore.RED,"Lesson 5.2 - Months of the year")
print("")

print(Fore.WHITE,"I mesi dell’anno = The months of the year")
print("Mese = Month")
print("Anno = Year")
print("Gennaio = January")
print("Febbraio = February")
print("Marzo = March")
print("Aprile = April")
print("Maggio = May")
print("Giugno = June")
print("Luglio = July")
print("Agosto = August")
print("Settembre = September")
print("Ottobre = October")
print("Novembre = November")
print("Dicembre = December")