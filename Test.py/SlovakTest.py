import random
from colorama import Fore, Style, init
import unicodedata

# Initialize Colorama
init(autoreset=True)

def normalize_text(text):
    """Normalize text by removing accents"""
    text = text.lower().strip()
    # Remove accents
    text = unicodedata.normalize('NFD', text)
    text = ''.join(char for char in text if unicodedata.category(char) != 'Mn')
    return text

# ALL ITEMS FROM YOUR CODE - IN ORDER
lessons_data = {
    "Lesson 1 - Numbers 1-10": {
        "count": 10,
        "words": [
            ("1", "jeden"),
            ("2", "dva"),
            ("3", "tri"),
            ("4", "styri"),
            ("5", "pat"),
            ("6", "sest"),
            ("7", "sedem"),
            ("8", "osem"),
            ("9", "devat"),
            ("10", "desat")
        ],
        "is_numbers": True
    },
    
    "Lesson 2 - Greetings": {
        "count": 18,
        "words": [
            ("Hello", "ahoj"),
            ("How are you?", "ako sa mate"),
            ("Nice to meet you", "rad vas spoznavam"),
            ("See you tomorrow", "uvidime sa zajtra"),
            ("Good morning", "dobre rano"),
            ("Good afternoon", "dobre den"),
            ("Good evening", "dobry vecer"),
            ("Good night", "dobru noc"),
            ("What is your name?", "ako sa volate"),
            ("My name is", "moje meno je"),
            ("Where do you live?", "kde byvas"),
            ("Where are you from?", "odkial ste"),
            ("Nice to see you", "rad vas opat'vidim"),
            ("Have a nice day", "pekny den"),
            ("See you later", "uvidime sa neskor"),
            ("Goodbye", "dovidenia"),
            ("Please", "prosim"),
            ("Thank you", "dakujem")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.1 - Regular -AŤ/AŤ SA Verbs": {
        "count": 22,
        "words": [
            ("to ask", "pytat"),
            ("to play", "hrat"),
            ("to read", "citat"),
            ("to listen", "pocuvat"),
            ("to lie down", "lezat"),
            ("to get up", "vstavat"),
            ("to open", "otvarat"),
            ("to close", "zatvarat"),
            ("to call", "zavolat"),
            ("to play (refl)", "hrat sa"),
            ("to write", "napisat"),
            ("to laugh", "smiat sa"),
            ("to cry", "plakat"),
            ("to walk", "kracat"),
            ("to calculate", "pocitavat"),
            ("to try", "skusat"),
            ("to admonish", "napominat"),
            ("to wear", "nosievat"),
            ("to walk", "prech adzat"),
            ("to use", "pouzivat"),
            ("to assume", "predpokladat"),
            ("to dream", "vysnivat")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.2 - Regular -OVAŤ Verbs": {
        "count": 7,
        "words": [
            ("to work", "pracovat"),
            ("to study", "studovat"),
            ("to love", "milovat"),
            ("to dance", "tancovat"),
            ("to paint", "malovat"),
            ("to note down", "zapisovat"),
            ("to build", "budovat")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.3 - Regular -IŤ Verbs": {
        "count": 11,
        "words": [
            ("to cook", "varit"),
            ("to teach", "ucit"),
            ("to draw", "kreslit"),
            ("to feel", "pocitit"),
            ("to clean", "cistit"),
            ("to solve", "riesit"),
            ("to live", "zit"),
            ("to believe", "verit"),
            ("to claim", "tvrdit"),
            ("to own", "vlastnit"),
            ("to evaluate", "hodnotit")
        ],
        "is_numbers": False
    },
    
    "Lesson 4 - Adjectives": {
        "count": 35,
        "words": [
            ("Happy", "stastny"),
            ("Sad", "smutny"),
            ("Angry", "nahnevany"),
            ("Afraid", "vystraseny"),
            ("Joy", "radost"),
            ("Surprised", "prekvapeny"),
            ("Calm", "pokojny"),
            ("Bored", "znudeny"),
            ("Easy", "lahky"),
            ("Difficult", "tazky"),
            ("Bad", "zly"),
            ("Good", "dobry"),
            ("Noisy", "hlucny"),
            ("Quiet", "tichy"),
            ("Strong", "silny"),
            ("Weak", "slaby"),
            ("Hard", "tvrdy"),
            ("Soft", "makky"),
            ("More", "viac"),
            ("Less", "menej"),
            ("Clean", "cisty"),
            ("Dirty", "spinavy"),
            ("Old", "stary"),
            ("New", "novy"),
            ("Big", "velky"),
            ("Small", "maly"),
            ("Young", "mlady"),
            ("Skinny", "vychudnuty"),
            ("Fat", "tucny"),
            ("Pretty", "pekny"),
            ("Ugly", "skaredy"),
            ("Thick", "hruby"),
            ("Thin", "tenky"),
            ("Rough", "drsny"),
            ("Smooth", "hladky")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.1 - Days": {
        "count": 11,
        "words": [
            ("The days of the week", "los dias de la semana"),
            ("Day", "den"),
            ("Week", "tyzden"),
            ("Monday", "pondelok"),
            ("Tuesday", "utorak"),
            ("Wednesday", "streda"),
            ("Thursday", "stvrtok"),
            ("Friday", "piiatok"),
            ("Saturday", "sobota"),
            ("Sunday", "nedela"),
            ("Weekend", "vikend")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.2 - Months": {
        "count": 15,
        "words": [
            ("The months of the year", "mesiace roka"),
            ("Month", "mesiac"),
            ("Year", "rok"),
            ("January", "januar"),
            ("February", "februar"),
            ("March", "marec"),
            ("April", "april"),
            ("May", "maj"),
            ("June", "jun"),
            ("July", "jul"),
            ("August", "august"),
            ("September", "september"),
            ("October", "oktober"),
            ("November", "november"),
            ("December", "december")
        ],
        "is_numbers": False
    },
    
    "Lesson 6 - Seasons & Weather": {
        "count": 23,
        "words": [
            ("Seasons", "rocne obdobia"),
            ("Winter", "zima"),
            ("Summer", "leto"),
            ("Spring", "jar"),
            ("Autumn", "jesen"),
            ("Sky", "obloha"),
            ("Cloud", "mrak"),
            ("Rainbow", "duha"),
            ("Cold", "studeny"),
            ("Hot", "horuci"),
            ("It is hot", "je horuco"),
            ("It is cold", "je zima"),
            ("It is sunny", "je slnecno"),
            ("It is cloudy", "je oblacno"),
            ("It is humid", "je vlhko"),
            ("It is raining", "prsi"),
            ("It is snowing", "snezi"),
            ("It is windy", "fuka"),
            ("How is the weather?", "ake je pocasie"),
            ("Good weather", "dobre pocasie"),
            ("Bad weather", "zle pocasie"),
            ("What is the temperature?", "aka je teplota"),
            ("It is 24 degrees", "je 24 stupnov")
        ],
        "is_numbers": False
    },
    
    "Lesson 7 - Colors": {
        "count": 14,
        "words": [
            ("Black", "clerny"),
            ("Blue", "mordy"),
            ("Brown", "hnedy"),
            ("Green", "zeleny"),
            ("Orange", "oranzovy"),
            ("Purple", "purpurovy"),
            ("Red", "cerveny"),
            ("White", "biely"),
            ("Yellow", "zlty"),
            ("Gray", "sedy"),
            ("Gold", "zlaty"),
            ("Silver", "strieborny"),
            ("What color is it?", "aku to ma farbu"),
            ("The color is", "farbe je")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.1 - Family": {
        "count": 35,
        "words": [
            ("Mother", "matka"),
            ("Father", "otec"),
            ("Brother", "brat"),
            ("Sister", "sestra"),
            ("Son", "syn"),
            ("Daughter", "dcera"),
            ("Parents", "rodicia"),
            ("Children", "deti"),
            ("Child", "dieta"),
            ("Stepmother", "nevlastna matka"),
            ("Stepfather", "nevlastny otec"),
            ("Stepsister", "nevlastna sestra"),
            ("Stepbrother", "nevlastny brat"),
            ("Son-in-law", "zat"),
            ("Daughter-in-law", "nevesta"),
            ("Wife", "manzelka"),
            ("Husband", "manzel"),
            ("Grandparents", "stari rodicia"),
            ("Grandfather", "stary otec"),
            ("Grandmother", "stara mama"),
            ("Grandson", "vnuk"),
            ("Granddaughter", "vnucka"),
            ("Grandchildren", "vnucata"),
            ("Grandchild", "vnuca"),
            ("Aunt", "teta"),
            ("Uncle", "stryko"),
            ("Cousin (female)", "sesternica"),
            ("Cousin (male)", "bratranec"),
            ("Nephew", "synovec"),
            ("Niece", "neter"),
            ("Father-in-law", "svokor"),
            ("Mother-in-law", "svokra"),
            ("Brother-in-law", "svagor"),
            ("Sister-in-law", "svagrina"),
            ("Relative", "pribuzny")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.2 - Friends": {
        "count": 14,
        "words": [
            ("Miss", "pani"),
            ("Boy", "chlapec"),
            ("Girl", "dievca"),
            ("Baby", "dieta"),
            ("Woman", "zena"),
            ("Man", "muz"),
            ("Friend (male)", "kamarat"),
            ("Friend (female)", "kamaratka"),
            ("Boyfriend", "priatel"),
            ("Girlfriend", "priatelka"),
            ("Gentleman", "pan"),
            ("Lady", "dama"),
            ("Neighbor (male)", "sused"),
            ("Neighbor (female)", "suseda")
        ],
        "is_numbers": False
    },
    
    "Lesson 9 - Numbers 11-30": {
        "count": 20,
        "words": [
            ("11", "jedenast"),
            ("12", "dvanast"),
            ("13", "trinast"),
            ("14", "strnast"),
            ("15", "patnast"),
            ("16", "sestnast"),
            ("17", "sedemnast"),
            ("18", "osemnast"),
            ("19", "devatnast"),
            ("20", "dvadsat"),
            ("21", "dvadsatjeden"),
            ("22", "dvadsatdva"),
            ("23", "dvadsattri"),
            ("24", "dvadsatstyri"),
            ("25", "dvadsatpat"),
            ("26", "dvadsatsest"),
            ("27", "dvadsatsedem"),
            ("28", "dvadsatosem"),
            ("29", "dvadsatdevat"),
            ("30", "tridsat")
        ],
        "is_numbers": True
    },
    
    "Lesson 10.1 - Prepositions": {
        "count": 36,
        "words": [
            ("For", "pre"),
            ("From", "z"),
            ("In", "v"),
            ("Inside", "vnutri"),
            ("Into", "do"),
            ("Near", "najblizsie"),
            ("Of", "z"),
            ("Out", "von"),
            ("Outside", "vonku"),
            ("To", "na"),
            ("Under", "pod"),
            ("With", "s"),
            ("Without", "bez"),
            ("Above", "vyssie"),
            ("Across", "napriec"),
            ("After", "po"),
            ("Against", "proti"),
            ("Along", "pozdlz"),
            ("Around", "okolo"),
            ("At", "v/na"),
            ("Behind", "za"),
            ("Below", "nizsie"),
            ("Beside", "vedla"),
            ("Between", "medzi"),
            ("By", "podla"),
            ("During", "pocas"),
            ("Except", "okrem"),
            ("And", "a"),
            ("Because", "pretoze"),
            ("But", "ale"),
            ("Or", "alebo"),
            ("Everywhere", "vsade"),
            ("Everyone", "vsetci"),
            ("Everything", "vsetko"),
            ("Few", "malo"),
            ("Some", "niektori"),
            ("Many", "vela")
        ],
        "is_numbers": False
    },
    
    "Lesson 10.2 - Useful Words": {
        "count": 29,
        "words": [
            ("Question", "otazka"),
            ("Answer", "odpoved"),
            ("Truth", "pravda"),
            ("Lie", "loz"),
            ("Nothing", "nic"),
            ("Something", "nieco"),
            ("Same", "rovnaky"),
            ("Different", "odlisny"),
            ("Pull", "tahat"),
            ("Push", "tlacit"),
            ("Long", "dlhy"),
            ("Short", "kratky"),
            ("Cold", "studeny"),
            ("Hot", "horuci"),
            ("Light", "svetly"),
            ("Dark", "tmavy"),
            ("Wet", "mokry"),
            ("Dry", "suchy"),
            ("Empty", "prazdny"),
            ("Full", "plny"),
            ("How?", "ako"),
            ("What?", "co"),
            ("When?", "kedy"),
            ("Where?", "kde"),
            ("Which?", "ktory"),
            ("Who?", "kto"),
            ("Why?", "preco"),
            ("How long?", "ako dlho"),
            ("How much?", "kolko")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.1 - Drinks": {
        "count": 9,
        "words": [
            ("Coffee", "kava"),
            ("Tea", "caj"),
            ("Soft drink", "nealkoholicky napoj"),
            ("Water", "voda"),
            ("Lemonade", "limonada"),
            ("Juice", "dzus"),
            ("Orange juice", "pomarancovy dzus"),
            ("I would like a glass of water please", "poprosim o pohar vody"),
            ("With ice", "s ladom")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.2 - Dairy Products": {
        "count": 19,
        "words": [
            ("Milk", "mlieko"),
            ("Ice cream", "zmrzlina"),
            ("Butter", "maslo"),
            ("Cheese", "syr"),
            ("Cottage cheese", "tvaroh"),
            ("Cream", "slahacka"),
            ("Sour cream", "kysla smotana"),
            ("Yogurt", "jogurt"),
            ("Eggs", "vajcia"),
            ("Whipping cream", "slahacka"),
            ("Bakery", "pekaren"),
            ("Baguette", "bageta"),
            ("Doughnut", "siska"),
            ("Cookie", "kolacik"),
            ("Roll", "rozok"),
            ("Dessert", "dezert"),
            ("Cake", "kolac"),
            ("Bread", "chlieb"),
            ("Pie", "kolac")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.3 - Meats": {
        "count": 13,
        "words": [
            ("Beef", "hovazie"),
            ("Veal", "telacie"),
            ("Ham", "sunka"),
            ("Chicken", "kuracie"),
            ("Turkey", "morcacie"),
            ("Duck", "kacica"),
            ("Bacon", "slanina"),
            ("Pork", "bravcove"),
            ("Filet mignon", "filet mignon"),
            ("Sausage", "klobasa"),
            ("Lamb chop", "jahnacia kotleta"),
            ("Pork chop", "bravcova kotleta"),
            ("Meat", "maso")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.4 - Seafoods": {
        "count": 20,
        "words": [
            ("Fish", "ryba"),
            ("Shellfish", "musle"),
            ("Bass", "morsky ostries"),
            ("Salmon", "losos"),
            ("Lobster", "homar"),
            ("Crab", "krab"),
            ("Mussel", "slavka jedla"),
            ("Oyster", "ustrica"),
            ("Cod", "treska"),
            ("Clam", "musle"),
            ("Shrimp", "krevety"),
            ("Tuna", "tuniak"),
            ("Trout", "pstruh"),
            ("Sole", "morsky jazyk"),
            ("Shark", "zralok"),
            ("Carp", "kapor"),
            ("Tilapia", "tilapia"),
            ("Eel", "uhor"),
            ("Catfish", "sumec"),
            ("Swordfish", "mecun")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.5 - Herbs & Spices": {
        "count": 17,
        "words": [
            ("Salt", "sol"),
            ("Pepper", "cierne korenie"),
            ("Caraway", "rasca"),
            ("Garlic", "cesnak"),
            ("Basil", "bazalka"),
            ("Coriander", "koriander"),
            ("Fennel", "fenikel"),
            ("Marjoram", "majoranka"),
            ("Oregano", "oregano"),
            ("Parsley", "petrzlen"),
            ("Rosemary", "rozmarin"),
            ("Sage", "salvia"),
            ("Thyme", "tymian"),
            ("Nutmeg", "muskatovy oriesok"),
            ("Paprika", "paprika"),
            ("Cayenne", "kajenske korenie"),
            ("Ginger", "zazvor")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.6 - Vegetables": {
        "count": 28,
        "words": [
            ("Celery", "zeler"),
            ("Eggplant", "baklažan"),
            ("Zucchini", "cuketa"),
            ("Onion", "cibula"),
            ("Spinach", "spenat"),
            ("Salad", "salat"),
            ("Green beans", "zelena fazulka"),
            ("Cucumber", "uhorka"),
            ("Radish", "redkovka"),
            ("Cabbage", "kapusta"),
            ("Mushrooms", "huby"),
            ("Lettuce", "salat"),
            ("Corn", "kukurica"),
            ("Potatoes", "zemiaky"),
            ("Tomato", "paradajka"),
            ("Carrot", "mrkva"),
            ("Plantain", "banan"),
            ("Beans", "fazula"),
            ("Leek", "por"),
            ("Lotus root", "lotosovy koren"),
            ("Bamboo shoot", "bambusove vyhonky"),
            ("Artichoke", "articok"),
            ("Asparagus", "spargla"),
            ("Brussels sprouts", "ruzickovy kel"),
            ("Broccoli", "brokolica"),
            ("Peas", "hrach"),
            ("Cauliflower", "karfiol"),
            ("Chili pepper", "cili papricka")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.7 - Fruits": {
        "count": 27,
        "words": [
            ("Cherries", "ceresne"),
            ("Raspberries", "maliny"),
            ("Blueberries", "cucoriedky"),
            ("Strawberries", "jahody"),
            ("Lemon", "citron"),
            ("Lime", "limetka"),
            ("Apple", "jablko"),
            ("Orange", "pomaranc"),
            ("Pear", "hruska"),
            ("Banana", "banan"),
            ("Grapes", "hrozno"),
            ("Grapefruit", "grapefruit"),
            ("Watermelon", "vodny melon"),
            ("Pineapple", "ananas"),
            ("Plum", "slivka"),
            ("Peach", "broskyna"),
            ("Mango", "mango"),
            ("Apricot", "marhula"),
            ("Pomegranate", "granatove jablko"),
            ("Persimmon", "tomel"),
            ("Kiwi", "kiwi"),
            ("Litchi", "lici"),
            ("Longan", "longan"),
            ("Balsam pear", "balzamova hruska"),
            ("Passion fruit", "mucenky"),
            ("Avocado", "avokado"),
            ("Coconut", "kokos")
        ],
        "is_numbers": False
    },
    
    "Lesson 12 - Irregular Verbs": {
        "count": 50,
        "words": [
            ("to be", "byt"),
            ("to have", "mat"),
            ("to go", "ist"),
            ("to come", "prist"),
            ("to see", "vidiet"),
            ("to give", "dat"),
            ("to eat", "jest"),
            ("to drink", "pit"),
            ("to know", "vediet"),
            ("can", "moct"),
            ("to want", "chciet"),
            ("to stay", "zostat"),
            ("to find", "najst"),
            ("to run", "bezat"),
            ("to sit", "sediet"),
            ("to lie", "lezat"),
            ("to stand", "stat"),
            ("to understand", "rozumiet"),
            ("to say", "povedat"),
            ("to carry", "nosit"),
            ("to take", "zobrat"),
            ("to read", "citat"),
            ("to write", "pisat"),
            ("to play", "hrat"),
            ("to buy", "kupit"),
            ("to lose", "stratit"),
            ("to live", "zit"),
            ("to return", "vratit"),
            ("to know", "poznat"),
            ("to die", "umriet"),
            ("to get", "dostat"),
            ("to get up", "vstat"),
            ("to watch", "pozerat"),
            ("to think", "mysliet"),
            ("to catch", "chytit"),
            ("to order", "objednat"),
            ("to spend (time)", "stravit"),
            ("to finish", "dokoncit"),
            ("to break", "rozbit"),
            ("to explain", "vysvetlit"),
            ("to translate", "prelozit"),
            ("to call", "zavolat"),
            ("to pay", "platit"),
            ("to listen", "pocuvat"),
            ("to entertain", "bavit"),
            ("to forget", "zabudnut"),
            ("to open", "otvorit"),
            ("to close", "zatvorit"),
            ("to dream", "snivat")
        ],
        "is_numbers": False
    },
    
    "Lesson 14 - Numbers 31-50": {
        "count": 20,
        "words": [
            ("31", "tridsatjeden"),
            ("32", "tridsatdva"),
            ("33", "tridsattri"),
            ("34", "tridsatstyri"),
            ("35", "tridsatpat"),
            ("36", "tridsatsest"),
            ("37", "tridsatsedem"),
            ("38", "tridsatosem"),
            ("39", "tridsatdevat"),
            ("40", "styridsat"),
            ("41", "styri dsatjeden"),
            ("42", "styridsatdva"),
            ("43", "styridsattri"),
            ("44", "styridsatstyri"),
            ("45", "styridsatpat"),
            ("46", "styridsatsest"),
            ("47", "styridsatsedem"),
            ("48", "styridsatosem"),
            ("49", "styridsatdevat"),
            ("50", "patdesiat")
        ],
        "is_numbers": True
    },
    
    "Lesson 15 - Physical Appearance": {
        "count": 38,
        "words": [
            ("Tall", "vysoky"),
            ("Short (height)", "nizky"),
            ("Slim", "stihly"),
            ("Fat", "tucny"),
            ("Muscular", "svalnatý"),
            ("Blonde", "blond"),
            ("Brown-haired", "hnedovlasy"),
            ("Black-haired", "ciernovlasy"),
            ("Curly hair", "kucerave vlasy"),
            ("Straight hair", "rovne vlasy"),
            ("Blue eyes", "modre oci"),
            ("Brown eyes", "hnede oci"),
            ("Green eyes", "zelene oci"),
            ("Beautiful", "krasny"),
            ("Handsome", "pekny"),
            ("Ugly", "skaredy"),
            ("Young", "mlady"),
            ("Old", "stary"),
            ("Beard", "brada"),
            ("Light-skinned", "svetla pokozka"),
            ("Dark-skinned", "tmava pokozka"),
            ("Freckles", "pehy"),
            ("Wrinkles", "vrasky"),
            ("Bald", "plesaty"),
            ("Hairy (body)", "chlpaty"),
            ("Straight nose", "rovny nos"),
            ("Big nose", "velky nos"),
            ("Small nose", "maly nos"),
            ("Thin lips", "tenke pery"),
            ("Full lips", "plne pery"),
            ("Broad shoulders", "siroke plecia"),
            ("Narrow shoulders", "uzke plecia"),
            ("Tanned skin", "opalena pokozka"),
            ("Pale skin", "bleda pokozka"),
            ("Wavy hair", "vlnite vlasy"),
            ("Ponytail", "konsky chvost"),
            ("Braids", "vrkoce"),
            ("Beard and mustache", "brada a fuzy")
        ],
        "is_numbers": False
    },
    
    "Lesson 16 - Occupations": {
        "count": 25,
        "words": [
            ("Doctor", "lekar"),
            ("Teacher", "ucitel"),
            ("Engineer", "inzinier"),
            ("Lawyer", "pravnik"),
            ("Salesperson", "predavac"),
            ("Police officer", "policajt"),
            ("Firefighter", "hasic"),
            ("Programmer", "programator"),
            ("Cook/Chef", "kuchar"),
            ("Journalist", "novinar"),
            ("Nurse", "zdravotna sestra"),
            ("Architect", "architekt"),
            ("Accountant", "uctovnik"),
            ("Pharmacist", "lekarnik"),
            ("Driver", "vodic"),
            ("Mechanic", "mechanik"),
            ("Scientist", "vedec"),
            ("Dentist", "zubar"),
            ("Musician", "hudobnik"),
            ("Actor", "herec"),
            ("Artist", "umelec"),
            ("Pilot", "pilot"),
            ("Farmer", "farmar"),
            ("Photographer", "fotograf"),
            ("Waiter/Waitress", "casnik/casnicka")
        ],
        "is_numbers": False
    },
    
    "Lesson 17 - Sports": {
        "count": 30,
        "words": [
            ("Football/Soccer", "futbal"),
            ("Basketball", "basketbal"),
            ("Volleyball", "volejbal"),
            ("Tennis", "tenis"),
            ("Swimming", "plavanie"),
            ("Running/Athletics", "beh/atletika"),
            ("Ice hockey", "hokej"),
            ("Skiing", "lyzovanie"),
            ("Cycling", "cyklistika"),
            ("Boxing", "box"),
            ("Martial arts", "bojove umenia"),
            ("Golf", "golf"),
            ("Table tennis", "stolny tenis"),
            ("Wrestling", "zapasenie"),
            ("Handball", "hadzana"),
            ("Baseball", "baseball"),
            ("Surfing", "surfovanie"),
            ("Skating", "korculovanie"),
            ("Horse riding", "jazdectvo"),
            ("Diving", "potapanie"),
            ("Cricket", "kriket"),
            ("Rugby", "ragby"),
            ("Ballet", "balet"),
            ("Bowling", "bowling"),
            ("Weightlifting", "vzpieranie"),
            ("Windsurfing", "windsurfing"),
            ("Ice skating", "korculovanie"),
            ("Rowing", "veslovanie"),
            ("Archery", "lukostreľba"),
            ("Climbing", "lezenie")
        ],
        "is_numbers": False
    },
    
    "Lesson 18 - Numbers 51-75": {
        "count": 25,
        "words": [
            ("51", "patdesiatjeden"),
            ("52", "patdesiatdva"),
            ("53", "patdesiattri"),
            ("54", "patdesiatstyri"),
            ("55", "patdesiatpat"),
            ("56", "patdesiatsest"),
            ("57", "patdesiatsedem"),
            ("58", "patdesiatosem"),
            ("59", "patdesiatdevat"),
            ("60", "sestdesiat"),
            ("61", "sestdesiatjeden"),
            ("62", "sestdesiatdva"),
            ("63", "sestdesiattri"),
            ("64", "sestdesiatstyri"),
            ("65", "sestdesiatpat"),
            ("66", "sestdesiatsest"),
            ("67", "sestdesiatsedem"),
            ("68", "sestdesiatosem"),
            ("69", "sestdesiatdevat"),
            ("70", "sedemdesiat"),
            ("71", "sedemdesiatjeden"),
            ("72", "sedemdesiatdva"),
            ("73", "sedemdesiattri"),
            ("74", "sedemdesiatstyri"),
            ("75", "sedemdesiatpat")
        ],
        "is_numbers": True
    },
    
    "Lesson 19 - Clothing": {
        "count": 42,
        "words": [
            ("Shirt", "kosela"),
            ("T-shirt", "tricko"),
            ("Blouse", "bluzka"),
            ("Sweater", "sveter"),
            ("Jacket", "bunda"),
            ("Coat", "kabat"),
            ("Dress", "saty"),
            ("Skirt", "sukna"),
            ("Pants", "nohavice"),
            ("Shorts", "kratke nohavice"),
            ("Shoes", "topanky"),
            ("Boots", "cizmy"),
            ("Sneakers", "tenisky"),
            ("Sandals", "sandale"),
            ("Hat/Cap", "ciapka"),
            ("Scarf", "sal"),
            ("Gloves", "rukavice"),
            ("Belt", "opasok"),
            ("Socks", "ponozky"),
            ("Winter coat", "zimny kabat"),
            ("Wool hat", "vlnena ciapka"),
            ("Snow boots", "snehule"),
            ("Swimsuit", "plavky"),
            ("Sunglasses", "slnecne okuliare"),
            ("Flip-flops", "zabky"),
            ("Shorts", "kratke nohavice"),
            ("Tank top", "tielko"),
            ("Suit", "oblek"),
            ("Tie", "kravata"),
            ("Blazer", "sako"),
            ("High heels", "topanky na podpatku"),
            ("Evening dress", "vecerne saty"),
            ("Black", "cierny"),
            ("White", "biely"),
            ("Red", "cerveny"),
            ("Blue", "modry"),
            ("Green", "zeleny"),
            ("Cotton", "bavlna"),
            ("Wool", "vlna"),
            ("Leather", "koza"),
            ("Silk", "hodvab"),
            ("Linen", "lan")
        ],
        "is_numbers": False
    },
    
    "Lesson 20 - Adverbs": {
        "count": 20,
        "words": [
            ("Quickly", "rychlo"),
            ("Slowly", "pomaly"),
            ("Always", "vzdy"),
            ("Never", "nikdy"),
            ("Often", "casto"),
            ("Sometimes", "niekedy"),
            ("Rarely", "zriedka"),
            ("Already", "uz"),
            ("Still", "stale"),
            ("Yet", "este"),
            ("Soon", "coskoro"),
            ("Now", "teraz"),
            ("Later", "neskor"),
            ("Today", "dnes"),
            ("Tomorrow", "zajtra"),
            ("Yesterday", "vcera"),
            ("Clearly", "jasne"),
            ("Together", "spolu"),
            ("Apart", "oddelene"),
            ("Forever", "navzdy")
        ],
        "is_numbers": False
    },
    
    "Lesson 21 - Animals": {
        "count": 20,
        "words": [
            ("Dog", "pes"),
            ("Cat", "macka"),
            ("Horse", "kon"),
            ("Cow", "krava"),
            ("Sheep", "ovca"),
            ("Pig", "prasa"),
            ("Goat", "koza"),
            ("Chicken", "kura"),
            ("Duck", "kacica"),
            ("Bird", "vtak"),
            ("Rabbit", "kralik"),
            ("Mouse", "mys"),
            ("Lion", "lev"),
            ("Tiger", "tiger"),
            ("Bear", "medved"),
            ("Elephant", "slon"),
            ("Monkey", "opica"),
            ("Fox", "liska"),
            ("Wolf", "vlk"),
            ("Deer", "jelen")
        ],
        "is_numbers": False
    },
    
    "Lesson 23 - Places in Town": {
        "count": 20,
        "words": [
            ("School", "skola"),
            ("Hospital", "nemocnica"),
            ("Bank", "banka"),
            ("Restaurant", "restauracia"),
            ("Library", "kniznica"),
            ("Supermarket", "supermarket"),
            ("Cinema", "kino"),
            ("Post office", "posta"),
            ("Police station", "policajna stanica"),
            ("Park", "park"),
            ("Museum", "muzeum"),
            ("Theatre", "divadlo"),
            ("Hotel", "hotel"),
            ("Stadium", "stadion"),
            ("Church", "kostol"),
            ("Pharmacy", "lekaren"),
            ("Bakery", "pekaren"),
            ("Butcher", "masiarstvo"),
            ("Market", "trh"),
            ("Hairdresser", "kadernictvo")
        ],
        "is_numbers": False
    },
    
    "Lesson 24 - School Supplies": {
        "count": 20,
        "words": [
            ("Book", "kniha"),
            ("Pen", "pero"),
            ("Pencil", "ceruzka"),
            ("Eraser", "guma"),
            ("Notebook", "zosit"),
            ("Ruler", "pravitko"),
            ("Scissors", "noznice"),
            ("Backpack", "batoh"),
            ("Folder", "zlozka"),
            ("Calculator", "kalkulacka"),
            ("Marker", "fixka"),
            ("Chalk", "krieda"),
            ("Map", "mapa"),
            ("Highlighter", "zvyraznov ac"),
            ("Projector", "projektor"),
            ("Laptop", "notebook"),
            ("Printer", "tlaciaren"),
            ("USB stick", "usb kluc"),
            ("Schoolbag", "skolska taska"),
            ("Sharpener", "struhadlo")
        ],
        "is_numbers": False
    },
    
    "Lesson 25 - Transportation": {
        "count": 20,
        "words": [
            ("Car", "auto"),
            ("Bus", "autobus"),
            ("Train", "vlak"),
            ("Bicycle", "bicykel"),
            ("Motorcycle", "motorka"),
            ("Airplane", "lietadlo"),
            ("Boat", "lod"),
            ("Tram", "elektricka"),
            ("Taxi", "taxik"),
            ("Subway", "metro"),
            ("Ferry", "trajekt"),
            ("Yacht", "jachta"),
            ("Hot air balloon", "teplovzdusny balon"),
            ("Spaceship", "kozmicka lod"),
            ("Rickshaw", "riksa"),
            ("Gondola", "gondola"),
            ("Zeppelin", "zeppelin"),
            ("Rollerblades", "kolieskove korcule"),
            ("Canoe", "kanoe"),
            ("Submarine", "ponorka")
        ],
        "is_numbers": False
    }
}

def generate_questions(lesson_name, words, count, is_numbers):
    """Generate different question types based on item count"""
    questions = []
    
    if is_numbers:
        # Special question types for number lessons
        # Type 1: Number to word (Answer: WORD)
        for english, slovak in words:
            questions.append({
                'type': 'num_to_word',
                'question': f"What is '{english}' in Slovak? (Answer with the WORD)",
                'answer': slovak,
                'display_answer': slovak  # Show WORD
            })
        
        # Type 2: Word to number (Answer: NUMBER)
        for english, slovak in words:
            questions.append({
                'type': 'word_to_num',
                'question': f"What number is '{slovak}'? (Answer with the NUMBER)",
                'answer': english,
                'display_answer': english  # Show NUMBER
            })
        
        # Type 3: Mixed (Answer based on type)
        for english, slovak in words:
            if random.choice([True, False]):
                # Number to word
                questions.append({
                    'type': 'mixed',
                    'question': f"Translate '{english}' to Slovak word:",
                    'answer': slovak,
                    'display_answer': slovak  # WORD
                })
            else:
                # Word to number
                questions.append({
                    'type': 'mixed',
                    'question': f"What number is '{slovak}'?",
                    'answer': english,
                    'display_answer': english  # NUMBER
                })
    
    elif count <= 20:
        # 20 or less: 3 different question types
        # Type 1: English -> Slovak
        for english, slovak in words:
            questions.append({
                'type': 'eng_to_svk',
                'question': f"Translate to Slovak: '{english}'",
                'answer': slovak,
                'display_answer': slovak
            })
        
        # Type 2: Slovak -> English
        for english, slovak in words:
            questions.append({
                'type': 'svk_to_eng',
                'question': f"Translate to English: '{slovak}'",
                'answer': english,
                'display_answer': english
            })
        
        # Type 3: First letter hint
        for english, slovak in words:
            first_letter = slovak[0] if slovak else ""
            blanks = "_" * (len(slovak) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}' - Complete the Slovak word",
                'answer': slovak,
                'display_answer': slovak
            })
    
    elif 20 < count <= 40:
        # 20-40: 3 sections, 2 different question types
        third = len(words) // 3
        
        # Section 1: English -> Slovak
        for english, slovak in words[:third]:
            questions.append({
                'type': 'eng_to_svk',
                'question': f"Translate to Slovak: '{english}'",
                'answer': slovak,
                'display_answer': slovak
            })
        
        # Section 2: Slovak -> English
        for english, slovak in words[third:third*2]:
            questions.append({
                'type': 'svk_to_eng',
                'question': f"Translate to English: '{slovak}'",
                'answer': english,
                'display_answer': english
            })
        
        # Section 3: First letter hint
        for english, slovak in words[third*2:]:
            first_letter = slovak[0] if slovak else ""
            blanks = "_" * (len(slovak) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': slovak,
                'display_answer': slovak
            })
    
    else:  # count > 40
        # 40+: 5 sections, 3-4 different question types
        fifth = len(words) // 5
        
        # Section 1: English -> Slovak
        for english, slovak in words[:fifth]:
            questions.append({
                'type': 'eng_to_svk',
                'question': f"Translate to Slovak: '{english}'",
                'answer': slovak,
                'display_answer': slovak
            })
        
        # Section 2: Slovak -> English
        for english, slovak in words[fifth:fifth*2]:
            questions.append({
                'type': 'svk_to_eng',
                'question': f"Translate to English: '{slovak}'",
                'answer': english,
                'display_answer': english
            })
        
        # Section 3: First letter
        for english, slovak in words[fifth*2:fifth*3]:
            first_letter = slovak[0] if slovak else ""
            blanks = "_" * (len(slovak) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': slovak,
                'display_answer': slovak
            })
        
        # Section 4: Last letter
        for english, slovak in words[fifth*3:fifth*4]:
            last_letter = slovak[-1] if slovak else ""
            blanks = "_" * (len(slovak) - 1)
            questions.append({
                'type': 'last_letter',
                'question': f"'{english}' = '{blanks}{last_letter}'",
                'answer': slovak,
                'display_answer': slovak
            })
        
        # Section 5: Letter count hint
        for english, slovak in words[fifth*4:]:
            questions.append({
                'type': 'letter_hint',
                'question': f"'{english}' = ({len(slovak)} letters, starts with {slovak[:2]}...)",
                'answer': slovak,
                'display_answer': slovak
            })
    
    return questions

def create_general_review(lesson_name, words, is_numbers):
    """General review questions after each lesson"""
    review = []
    sample_size = min(20, len(words))
    sampled_words = random.sample(words, sample_size)
    
    for english, slovak in sampled_words:
        if is_numbers:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] '{english}' in Slovak?",
                    'answer': slovak,
                    'display_answer': slovak
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] What number is '{slovak}'?",
                    'answer': english,
                    'display_answer': english
                })
        else:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{english}'",
                    'answer': slovak,
                    'display_answer': slovak
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{slovak}'",
                    'answer': english,
                    'display_answer': english
                })
    
    return review

def run_test(lesson_name):
    """Run a lesson's test"""
    lesson_data = lessons_data[lesson_name]
    words = lesson_data['words']
    count = lesson_data['count']
    is_numbers = lesson_data['is_numbers']
    
    print(Fore.CYAN + f"\n{'='*60}")
    print(Fore.YELLOW + f"{lesson_name} - Total {count} Items")
    print(Fore.CYAN + f"{'='*60}\n")
    
    # Generate questions
    questions = generate_questions(lesson_name, words, count, is_numbers)
    
    # Shuffle questions
    random.shuffle(questions)
    
    correct = 0
    total = len(questions)
    
    # Ask questions
    for i, q in enumerate(questions, 1):
        print(Fore.WHITE + f"\nQuestion {i}/{total}:")
        print(Fore.CYAN + q['question'])
        
        user_answer = input(Fore.GREEN + "Your answer: ").strip()
        
        if normalize_text(user_answer) == normalize_text(q['answer']):
            print(Fore.GREEN + "✓ Correct!")
            correct += 1
        else:
            print(Fore.RED + f"✗ Wrong! Correct answer: {q['display_answer']}")
    
    # General Review Section
    print(Fore.MAGENTA + f"\n{'='*60}")
    print(Fore.YELLOW + f"GENERAL REVIEW - {lesson_name}")
    print(Fore.MAGENTA + f"{'='*60}\n")
    
    review_questions = create_general_review(lesson_name, words, is_numbers)
    review_correct = 0
    
    for i, q in enumerate(review_questions, 1):
        print(Fore.WHITE + f"\nReview {i}/{len(review_questions)}:")
        print(Fore.CYAN + q['question'])
        
        user_answer = input(Fore.GREEN + "Your answer: ").strip()
        
        if normalize_text(user_answer) == normalize_text(q['answer']):
            print(Fore.GREEN + "✓ Correct!")
            review_correct += 1
        else:
            print(Fore.RED + f"✗ Wrong! Correct answer: {q['display_answer']}")
    
    # Results
    print(Fore.YELLOW + f"\n{'='*60}")
    print(Fore.CYAN + "RESULTS")
    print(Fore.YELLOW + f"{'='*60}")
    total_all = total + len(review_questions)
    correct_all = correct + review_correct
    percentage = (correct_all / total_all) * 100
    
    print(Fore.WHITE + f"Main Questions: {correct}/{total} ({(correct/total)*100:.1f}%)")
    print(Fore.WHITE + f"General Review: {review_correct}/{len(review_questions)} ({(review_correct/len(review_questions))*100:.1f}%)")
    print(Fore.CYAN + f"TOTAL: {correct_all}/{total_all} ({percentage:.1f}%)")
    
    if percentage >= 90:
        print(Fore.GREEN + "🎉 Excellent!")
    elif percentage >= 70:
        print(Fore.BLUE + "👏 Very Good!")
    elif percentage >= 50:
        print(Fore.YELLOW + "👍 Good!")
    else:
        print(Fore.RED + "📚 Keep studying!")
    
    return correct_all, total_all

def main():
    """Main program - Run all lessons automatically in order"""
    print(Fore.CYAN + """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        COMPREHENSIVE SLOVAK TEST SYSTEM                   ║
║        All Items + Various Question Types                 ║
║        + General Review After Each Lesson                 ║
║                                                           ║
║        AUTOMATIC START-TO-FINISH TEST                     ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    input(Fore.YELLOW + "Press Enter to start the test...")
    
    lessons = list(lessons_data.keys())
    total_correct = 0
    total_questions = 0
    
    # Run all lessons in order
    for lesson_num, lesson in enumerate(lessons, 1):
        print(Fore.MAGENTA + f"\n\n{'#'*60}")
        print(Fore.YELLOW + f"LESSON {lesson_num}/{len(lessons)}")
        print(Fore.MAGENTA + f"{'#'*60}")
        
        correct, total = run_test(lesson)
        total_correct += correct
        total_questions += total
        
        if lesson_num < len(lessons):
            input(Fore.YELLOW + "\n\nPress Enter to continue to the next lesson...")
    
    # Final results
    print(Fore.MAGENTA + f"\n\n{'='*60}")
    print(Fore.YELLOW + "ALL LESSONS COMPLETED!")
    print(Fore.YELLOW + "FINAL RESULTS")
    print(Fore.MAGENTA + f"{'='*60}")
    
    final_percentage = (total_correct / total_questions) * 100
    
    print(Fore.CYAN + f"\nTotal Lessons: {len(lessons)}")
    print(Fore.CYAN + f"Total Score: {total_correct}/{total_questions}")
    print(Fore.CYAN + f"Success Rate: {final_percentage:.1f}%\n")
    
    if final_percentage >= 90:
        print(Fore.GREEN + "🎉🎉🎉 EXCELLENT! You're amazing at Slovak! 🎉🎉🎉")
    elif final_percentage >= 70:
        print(Fore.BLUE + "👏👏👏 VERY GOOD! Great performance! 👏👏👏")
    elif final_percentage >= 50:
        print(Fore.YELLOW + "👍👍 GOOD! Keep going and you'll be excellent! 👍👍")
    else:
        print(Fore.RED + "📚📚 Keep studying! You can do it! 📚📚")
    
    print(Fore.GREEN + "\nCongratulations! You completed the entire test! 🎊")

if __name__ == "__main__":
    main()