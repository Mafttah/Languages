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
            ("2", "dwa"),
            ("3", "trzy"),
            ("4", "cztery"),
            ("5", "piec"),
            ("6", "szesc"),
            ("7", "siedem"),
            ("8", "osiem"),
            ("9", "dziewiec"),
            ("10", "dziesiec")
        ],
        "is_numbers": True
    },
    
    "Lesson 2 - Greetings": {
        "count": 18,
        "words": [
            ("Hello", "czesc"),
            ("How are you?", "jak sie masz"),
            ("Nice to meet you", "milo cie poznac"),
            ("See you tomorrow", "do zobaczenia jutro"),
            ("Good morning", "dzien dobry"),
            ("Good afternoon", "dzien dobry"),
            ("Good evening", "dobry wieczor"),
            ("Good night", "dobranoc"),
            ("What is your name?", "kaj masz na imic"),
            ("My name is", "nazywam sie"),
            ("Where do you live?", "gdzie mieszkasz"),
            ("Where are you from?", "skad pochodzisz"),
            ("Nice to see you", "milo cie widziec"),
            ("Have a nice day", "milego dnia"),
            ("See you later", "do zobaczenia"),
            ("Goodbye", "do widzenia"),
            ("Please", "prosze"),
            ("Thank you", "dziekuje")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.1 - Regular -AĆ Verbs": {
        "count": 15,
        "words": [
            ("to read", "czytac"),
            ("to love", "kochac"),
            ("to watch", "ogladac"),
            ("to play", "grac"),
            ("to dance", "tanczyc"),
            ("to live", "mieszkac"),
            ("to listen", "sluchac"),
            ("to cry", "plakac"),
            ("to wait", "czekac"),
            ("to ask", "pytac"),
            ("to go/ride", "jechac"),
            ("to push", "pchac"),
            ("to drag", "ciagac"),
            ("to catch", "lapac"),
            ("to blow", "dmuchac")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.2 - Regular -YĆ SIĘ Verbs": {
        "count": 10,
        "words": [
            ("to learn", "uczyc sie"),
            ("to be happy", "cieszyc sie"),
            ("to worry", "martwic sie"),
            ("to laugh", "smiac sie"),
            ("to be bored", "nudzic sie"),
            ("to shave", "golic sie"),
            ("to bathe", "kapac sie"),
            ("to comb", "czesac sie"),
            ("to dress", "ubierac sie"),
            ("to hurry", "spieszyc sie")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.3 - Regular -EĆ Verbs": {
        "count": 10,
        "words": [
            ("to think", "myslec"),
            ("to count", "liczyc"),
            ("to sit", "siedziec"),
            ("to see", "widziec"),
            ("to judge", "sadzic"),
            ("to hurt", "bolec"),
            ("to fail", "zawodzic"),
            ("to shout", "krzyczec"),
            ("to fade", "plowiec"),
            ("to tremble", "drzec")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.4 - Regular -IĆ Verbs": {
        "count": 10,
        "words": [
            ("to speak", "mowic"),
            ("to do", "robic"),
            ("to walk", "chodzic"),
            ("to wear", "nosic"),
            ("to finish", "konczyc"),
            ("to request", "prosic"),
            ("to feed", "karmic"),
            ("to wake up", "obudzic"),
            ("to let in", "wpuscic"),
            ("to announce", "glosic")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.5 - Regular -OWAĆ Verbs": {
        "count": 10,
        "words": [
            ("to work", "pracowac"),
            ("to cook", "gotowac"),
            ("to phone", "telefonowac"),
            ("to thank", "dziekowac"),
            ("to study", "studiowac"),
            ("to rescue", "ratowac"),
            ("to paint", "malowac"),
            ("to buy", "kupowac"),
            ("to plan", "planowac"),
            ("to organize", "organizowac")
        ],
        "is_numbers": False
    },
    
    "Lesson 4 - Adjectives": {
        "count": 35,
        "words": [
            ("Happy", "szczesliwy"),
            ("Sad", "smutny"),
            ("Angry", "zly"),
            ("Afraid", "przestraszony"),
            ("Joy", "radosc"),
            ("Surprised", "zaskoczony"),
            ("Calm", "spokojny"),
            ("Bored", "znudzony"),
            ("Easy", "latwy"),
            ("Difficult", "trudny"),
            ("Bad", "zly"),
            ("Good", "dobry"),
            ("Noisy", "halasliwy"),
            ("Quiet", "cichy"),
            ("Strong", "silny"),
            ("Weak", "slaby"),
            ("Hard", "twardy"),
            ("Soft", "miekki"),
            ("More", "wiecej"),
            ("Less", "mniej"),
            ("Clean", "czysty"),
            ("Dirty", "brudny"),
            ("Old", "stary"),
            ("New", "nowy"),
            ("Big", "duzy"),
            ("Small", "maly"),
            ("Young", "mlody"),
            ("Skinny", "chudy"),
            ("Fat", "gruby"),
            ("Pretty", "ladny"),
            ("Ugly", "brzydki"),
            ("Thick", "gruby"),
            ("Thin", "cienki"),
            ("Rough", "szorstki"),
            ("Smooth", "gladki")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.1 - Days": {
        "count": 11,
        "words": [
            ("The days of the week", "dni tygodnia"),
            ("Day", "dzien"),
            ("Week", "tydzien"),
            ("Monday", "poniedzialek"),
            ("Tuesday", "wtorek"),
            ("Wednesday", "sroda"),
            ("Thursday", "czwartek"),
            ("Friday", "piatek"),
            ("Saturday", "sobota"),
            ("Sunday", "niedziela"),
            ("Weekend", "weekend")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.2 - Months": {
        "count": 15,
        "words": [
            ("The months of the year", "miesiace w roku"),
            ("Month", "miesiac"),
            ("Year", "rok"),
            ("January", "styczen"),
            ("February", "luty"),
            ("March", "marzec"),
            ("April", "kwiecien"),
            ("May", "maj"),
            ("June", "czerwiec"),
            ("July", "lipiec"),
            ("August", "sierpien"),
            ("September", "wrzesien"),
            ("October", "pazdziernik"),
            ("November", "listopad"),
            ("December", "grudzien")
        ],
        "is_numbers": False
    },
    
    "Lesson 6 - Seasons & Weather": {
        "count": 23,
        "words": [
            ("Seasons", "pory roku"),
            ("Winter", "zima"),
            ("Summer", "lato"),
            ("Spring", "wiosna"),
            ("Autumn", "jesien"),
            ("Sky", "niebo"),
            ("Cloud", "chmura"),
            ("Rainbow", "tecza"),
            ("Cold", "zimno"),
            ("Hot", "goraco"),
            ("It is hot", "jest goraco"),
            ("It is cold", "jest zimno"),
            ("It is sunny", "jest slonecznie"),
            ("It is cloudy", "jest pochmurnie"),
            ("It is humid", "jest wilgotnie"),
            ("It is raining", "pada deszcz"),
            ("It is snowing", "pada snieg"),
            ("It is windy", "jest wietrznie"),
            ("How is the weather?", "jaka jest pogoda"),
            ("Good weather", "dobra pogoda"),
            ("Bad weather", "zla pogoda"),
            ("What is the temperature?", "jaka jest temperatura"),
            ("It is 24 degrees", "mamy 24 stopnie")
        ],
        "is_numbers": False
    },
    
    "Lesson 7 - Colors": {
        "count": 14,
        "words": [
            ("Black", "czarny"),
            ("Blue", "niebieski"),
            ("Brown", "brazowy"),
            ("Green", "zielony"),
            ("Orange", "pomaranczowy"),
            ("Purple", "fioletowy"),
            ("Red", "czerwony"),
            ("White", "bialy"),
            ("Yellow", "zolty"),
            ("Gray", "szary"),
            ("Gold", "zloty"),
            ("Silver", "srebrny"),
            ("What color is it?", "jaki to kolor"),
            ("The color is", "ten kolor to")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.1 - Family": {
        "count": 35,
        "words": [
            ("Mother", "matka"),
            ("Father", "ojciec"),
            ("Brother", "brat"),
            ("Sister", "siostra"),
            ("Son", "syn"),
            ("Daughter", "corka"),
            ("Parents", "rodzice"),
            ("Children", "dzieci"),
            ("Child", "dziecko"),
            ("Stepmother", "macocha"),
            ("Stepfather", "ojczym"),
            ("Stepsister", "siostra przyrodnia"),
            ("Stepbrother", "brat przyrodni"),
            ("Son-in-law", "ziec"),
            ("Daughter-in-law", "synowa"),
            ("Wife", "zona"),
            ("Husband", "maz"),
            ("Grandparents", "dziadkowie"),
            ("Grandfather", "dziadek"),
            ("Grandmother", "babcia"),
            ("Grandson", "wnuczek"),
            ("Granddaughter", "wnuczka"),
            ("Grandchildren", "wnuki"),
            ("Grandchild", "wnuk"),
            ("Aunt", "ciotka"),
            ("Uncle", "wujek"),
            ("Cousin (female)", "kuzynka"),
            ("Cousin (male)", "kuzyn"),
            ("Nephew", "siostrzeniec"),
            ("Niece", "siostrzenica"),
            ("Father-in-law", "tesc"),
            ("Mother-in-law", "tesciowa"),
            ("Brother-in-law", "szwagier"),
            ("Sister-in-law", "szwagierka"),
            ("Relative", "krewny")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.2 - Friends": {
        "count": 16,
        "words": [
            ("Mr", "pan"),
            ("Mrs", "pani"),
            ("Miss", "panna"),
            ("Boy", "chlopak"),
            ("Girl", "dziewczyna"),
            ("Baby", "niemowle"),
            ("Woman", "kobieta"),
            ("Man", "mezczyzna"),
            ("Friend (male)", "przyjaciel"),
            ("Friend (female)", "przyjaciolka"),
            ("Boyfriend", "chlopak"),
            ("Girlfriend", "dziewczyna"),
            ("Gentleman", "dzentelmen"),
            ("Lady", "dama"),
            ("Neighbor (male)", "sasiad"),
            ("Neighbor (female)", "sasiadka")
        ],
        "is_numbers": False
    },
    
    "Lesson 9 - Numbers 11-30": {
        "count": 20,
        "words": [
            ("11", "jedenascie"),
            ("12", "dwanascie"),
            ("13", "trzynascie"),
            ("14", "czternascie"),
            ("15", "pietnascie"),
            ("16", "szesnascie"),
            ("17", "siedemnascie"),
            ("18", "osiemnascie"),
            ("19", "dziewietnascie"),
            ("20", "dwadziescia"),
            ("21", "dwadziescia jeden"),
            ("22", "dwadziescia dwa"),
            ("23", "dwadziescia trzy"),
            ("24", "dwadziescia cztery"),
            ("25", "dwadziescia piec"),
            ("26", "dwadziescia szesc"),
            ("27", "dwadziescia siedem"),
            ("28", "dwadziescia osiem"),
            ("29", "dwadziescia dziewiec"),
            ("30", "trzydziesci")
        ],
        "is_numbers": True
    },
    
    "Lesson 10.1 - Prepositions": {
        "count": 36,
        "words": [
            ("For", "dla"),
            ("From", "od"),
            ("In", "w"),
            ("Inside", "wewnatrz"),
            ("Into", "w"),
            ("Near", "blisko"),
            ("Of", "z"),
            ("Out", "z"),
            ("Outside", "na zewnatrz"),
            ("To", "do"),
            ("Under", "pod"),
            ("With", "z"),
            ("Without", "bez"),
            ("Above", "nad"),
            ("Across", "po drugiej stronie"),
            ("After", "po"),
            ("Against", "pod"),
            ("Along", "wzdluz"),
            ("Around", "wokol"),
            ("At", "w"),
            ("Behind", "za"),
            ("Below", "pod"),
            ("Beside", "obok"),
            ("Between", "miedzy"),
            ("By", "przy"),
            ("During", "podczas"),
            ("Except", "oprocz"),
            ("And", "i"),
            ("Because", "poniewaz"),
            ("But", "ale"),
            ("Or", "lub"),
            ("Everywhere", "wszedzie"),
            ("Everyone", "wszyscy"),
            ("Everything", "wszystko"),
            ("Few", "malo"),
            ("Some", "niektore"),
            ("Many", "wiele")
        ],
        "is_numbers": False
    },
    
    "Lesson 10.2 - Useful Words": {
        "count": 29,
        "words": [
            ("Question", "pytanie"),
            ("Answer", "odpowiedz"),
            ("Truth", "prawda"),
            ("Lie", "klamstwo"),
            ("Nothing", "nic"),
            ("Something", "cos"),
            ("Same", "tak samo"),
            ("Different", "inny"),
            ("Pull", "ciagnac"),
            ("Push", "pchac"),
            ("Long", "dlugi"),
            ("Short", "krotki"),
            ("Cold", "zimno"),
            ("Hot", "goraco"),
            ("Light", "jasny"),
            ("Dark", "ciemny"),
            ("Wet", "mokro"),
            ("Dry", "sucho"),
            ("Empty", "pusty"),
            ("Full", "pelny"),
            ("How?", "jak"),
            ("What?", "co"),
            ("When?", "kiedy"),
            ("Where?", "gdzie"),
            ("Which?", "ktora"),
            ("Who?", "kto"),
            ("Why?", "dlaczego"),
            ("How long?", "jak dlugo"),
            ("How much?", "ile")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.1 - Drinks": {
        "count": 9,
        "words": [
            ("Coffee", "kawa"),
            ("Tea", "herbata"),
            ("Soft drink", "napoj gazowany"),
            ("Water", "woda"),
            ("Lemonade", "lemoniada"),
            ("Juice", "sok"),
            ("Orange juice", "sok pomaranczowy"),
            ("I would like a glass of water please", "poprosze o szklank e wody"),
            ("With ice", "z lodem")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.2 - Dairy Products": {
        "count": 19,
        "words": [
            ("Milk", "mleko"),
            ("Ice cream", "lody"),
            ("Butter", "maslo"),
            ("Cheese", "ser"),
            ("Cottage cheese", "twarozek"),
            ("Cream", "smietana"),
            ("Sour cream", "kwasna smietana"),
            ("Yogurt", "jogurt"),
            ("Eggs", "jajka"),
            ("Whipping cream", "bita smietana"),
            ("Bakery", "piekarnia"),
            ("Baguette", "bagietka"),
            ("Doughnut", "paczek"),
            ("Cookie", "ciastko"),
            ("Roll", "bulka"),
            ("Dessert", "deser"),
            ("Cake", "ciasto"),
            ("Bread", "chleb"),
            ("Pie", "placek")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.3 - Meats": {
        "count": 13,
        "words": [
            ("Beef", "wolowina"),
            ("Veal", "cielecina"),
            ("Ham", "szynka"),
            ("Chicken", "kurczak"),
            ("Turkey", "indyk"),
            ("Duck", "kaczka"),
            ("Bacon", "boczek"),
            ("Pork", "wieprzowina"),
            ("Filet mignon", "filet z poledwicy"),
            ("Sausage", "kielbasa"),
            ("Lamb chop", "kotlet z jagnieciny"),
            ("Pork chop", "kotlet schabowy"),
            ("Meat", "mieso")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.4 - Seafoods": {
        "count": 20,
        "words": [
            ("Fish", "ryba"),
            ("Shellfish", "skorupiak"),
            ("Bass", "okon"),
            ("Salmon", "losos"),
            ("Lobster", "homar"),
            ("Crab", "krab"),
            ("Mussel", "malze"),
            ("Oyster", "ostryga"),
            ("Cod", "dorsz"),
            ("Clam", "malz"),
            ("Shrimp", "krewetka"),
            ("Tuna", "tunczyk"),
            ("Trout", "pstrag"),
            ("Sole", "sola"),
            ("Shark", "rekin"),
            ("Carp", "karp"),
            ("Tilapia", "tilapia"),
            ("Eel", "wegorz"),
            ("Catfish", "sum"),
            ("Swordfish", "miecznik")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.5 - Herbs & Spices": {
        "count": 17,
        "words": [
            ("Salt", "sol"),
            ("Pepper", "pieprz"),
            ("Caraway", "kminek"),
            ("Garlic", "czosnek"),
            ("Basil", "bazylia"),
            ("Coriander", "kolendra"),
            ("Fennel", "fenkul"),
            ("Marjoram", "majeranek"),
            ("Oregano", "oregano"),
            ("Parsley", "pietruszka"),
            ("Rosemary", "rozmaryn"),
            ("Sage", "szalwia"),
            ("Thyme", "tymianek"),
            ("Nutmeg", "galka muszkatolowa"),
            ("Paprika", "papryka"),
            ("Cayenne", "pieprz cayenne"),
            ("Ginger", "imbir")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.6 - Vegetables": {
        "count": 28,
        "words": [
            ("Celery", "seler"),
            ("Eggplant", "baklazan"),
            ("Zucchini", "cukinia"),
            ("Onion", "cebula"),
            ("Spinach", "szpinak"),
            ("Salad", "salatka"),
            ("Green beans", "zielona fasola"),
            ("Cucumber", "ogorek"),
            ("Radish", "rzodkiewka"),
            ("Cabbage", "kapusta"),
            ("Mushrooms", "grzyby"),
            ("Lettuce", "salata"),
            ("Corn", "kukurydza"),
            ("Potatoes", "ziemniaki"),
            ("Tomato", "pomidor"),
            ("Carrot", "marchew"),
            ("Plantain", "banan"),
            ("Beans", "fasola"),
            ("Leek", "por"),
            ("Lotus root", "korzen lotosu"),
            ("Bamboo shoot", "pedy bambusa"),
            ("Artichoke", "karczoch"),
            ("Asparagus", "szparag"),
            ("Brussels sprouts", "brukselka"),
            ("Broccoli", "brokuly"),
            ("Peas", "groszek"),
            ("Cauliflower", "kalafior"),
            ("Chili pepper", "papryka chili")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.7 - Fruits": {
        "count": 27,
        "words": [
            ("Cherries", "wisnie"),
            ("Raspberries", "maliny"),
            ("Blueberries", "jagody"),
            ("Strawberries", "truskawki"),
            ("Lemon", "cytryna"),
            ("Lime", "limonka"),
            ("Apple", "jablko"),
            ("Orange", "pomarancza"),
            ("Pear", "gruszka"),
            ("Banana", "banan"),
            ("Grapes", "winogrona"),
            ("Grapefruit", "grejpfrut"),
            ("Watermelon", "arbuz"),
            ("Pineapple", "ananas"),
            ("Plum", "sliwka"),
            ("Peach", "brzoskwinia"),
            ("Mango", "mango"),
            ("Apricot", "morela"),
            ("Pomegranate", "granat"),
            ("Persimmon", "persymona"),
            ("Kiwi", "kiwi"),
            ("Litchi", "liczi"),
            ("Longan", "longan"),
            ("Balsam pear", "przepekla ogurkowata"),
            ("Passion fruit", "marakuja"),
            ("Avocado", "awokado"),
            ("Coconut", "orzech kokosowy")
        ],
        "is_numbers": False
    },
    
    "Lesson 12 - Irregular Verbs": {
        "count": 50,
        "words": [
            ("to be", "byc"),
            ("to have", "miec"),
            ("to go", "isc"),
            ("to come", "przyjsc"),
            ("to see", "widziec"),
            ("to give", "dac"),
            ("to eat", "jesc"),
            ("to drink", "pic"),
            ("to know (fact)", "wiedziec"),
            ("to want", "chciec"),
            ("to find", "znalezc"),
            ("to run", "biec"),
            ("to sit", "siedziec"),
            ("to lie down", "lezec"),
            ("to stand", "stac"),
            ("to understand", "rozumiec"),
            ("to say", "powiedziec"),
            ("to take", "wziac"),
            ("to write", "pisac"),
            ("to fall", "upasc"),
            ("to begin", "zaczac"),
            ("to break", "zlamac"),
            ("to build", "zbudowac"),
            ("to choose", "wybrac"),
            ("to do/make", "robic"),
            ("to drive", "prowadzic"),
            ("to forget", "zapomniec"),
            ("to get", "dostac"),
            ("to hear", "slyszec"),
            ("to hold", "trzymac"),
            ("to leave", "opuscic"),
            ("to meet", "spotkac"),
            ("to pay", "placic"),
            ("to put", "polozyc"),
            ("to read", "czytac"),
            ("to send", "wyslac"),
            ("to sleep", "spac"),
            ("to speak", "mowic"),
            ("to spend (time)", "spedzac"),
            ("to swim", "plywac"),
            ("to teach", "uczyc"),
            ("to tell", "opowiedziec"),
            ("to think", "myslec"),
            ("to throw", "rzucic"),
            ("to win", "wygrac"),
            ("to bring", "przyniesc")
        ],
        "is_numbers": False
    },
    
    "Lesson 14 - Numbers 31-50": {
        "count": 20,
        "words": [
            ("31", "trzydziesci jeden"),
            ("32", "trzydziesci dwa"),
            ("33", "trzydziesci trzy"),
            ("34", "trzydziesci cztery"),
            ("35", "trzydziesci piec"),
            ("36", "trzydziesci szesc"),
            ("37", "trzydziesci siedem"),
            ("38", "trzydziesci osiem"),
            ("39", "trzydziesci dziewiec"),
            ("40", "czterdziesci"),
            ("41", "czterdziesci jeden"),
            ("42", "czterdziesci dwa"),
            ("43", "czterdziesci trzy"),
            ("44", "czterdziesci cztery"),
            ("45", "czterdziesci piec"),
            ("46", "czterdziesci szesc"),
            ("47", "czterdziesci siedem"),
            ("48", "czterdziesci osiem"),
            ("49", "czterdziesci dziewiec"),
            ("50", "piecdziesiat")
        ],
        "is_numbers": True
    },
    
    "Lesson 15 - Physical Appearance": {
        "count": 38,
        "words": [
            ("Tall", "wysoki"),
            ("Short (height)", "niski"),
            ("Slim", "szczuply"),
            ("Fat", "gruby"),
            ("Muscular", "umiesniony"),
            ("Blonde", "blond"),
            ("Brown-haired", "brazowe wlosy"),
            ("Black-haired", "czarne wlosy"),
            ("Curly hair", "krecone wlosy"),
            ("Straight hair", "proste wlosy"),
            ("Blue eyes", "niebieskie oczy"),
            ("Brown eyes", "brazowe oczy"),
            ("Green eyes", "zielone oczy"),
            ("Beautiful", "piekny"),
            ("Handsome", "przystojny"),
            ("Ugly", "brzydki"),
            ("Young", "mlody"),
            ("Old", "stary"),
            ("Beard", "broda"),
            ("Light-skinned", "jasna skora"),
            ("Dark-skinned", "ciemna skora"),
            ("Freckles", "piegi"),
            ("Wrinkles", "zmarszczki"),
            ("Bald", "lysy"),
            ("Hairy (body)", "owlosiony"),
            ("Straight nose", "prosty nos"),
            ("Big nose", "duzy nos"),
            ("Small nose", "maly nos"),
            ("Thin lips", "cienkie usta"),
            ("Full lips", "pelne usta"),
            ("Broad shoulders", "szerokie ramiona"),
            ("Narrow shoulders", "waskie ramiona"),
            ("Tanned skin", "opalona skora"),
            ("Pale skin", "blada skora"),
            ("Wavy hair", "falowane wlosy"),
            ("Ponytail", "konski ogon"),
            ("Braids", "warkocze"),
            ("Beard and mustache", "broda i wasy")
        ],
        "is_numbers": False
    },
    
    "Lesson 16 - Occupations": {
        "count": 25,
        "words": [
            ("Doctor", "lekarz"),
            ("Teacher", "nauczyciel"),
            ("Engineer", "inzynier"),
            ("Lawyer", "prawnik"),
            ("Salesperson", "sprzedawca"),
            ("Police officer", "policjant"),
            ("Firefighter", "strazak"),
            ("Programmer", "programista"),
            ("Cook/Chef", "kucharz"),
            ("Journalist", "dziennikarz"),
            ("Nurse", "pielgniarka"),
            ("Architect", "architekt"),
            ("Accountant", "ksigowy"),
            ("Pharmacist", "farmaceuta"),
            ("Driver", "kierowca"),
            ("Mechanic", "mechanik"),
            ("Scientist", "naukowiec"),
            ("Dentist", "dentysta"),
            ("Musician", "muzyk"),
            ("Actor", "aktor"),
            ("Artist", "artysta"),
            ("Pilot", "pilot"),
            ("Farmer", "rolnik"),
            ("Photographer", "fotograf"),
            ("Waiter/Waitress", "kelner/kelnerka")
        ],
        "is_numbers": False
    },
    
    "Lesson 17 - Sports": {
        "count": 30,
        "words": [
            ("Football/Soccer", "pilka nozna"),
            ("Basketball", "koszykowka"),
            ("Volleyball", "siatkowka"),
            ("Tennis", "tenis"),
            ("Swimming", "plywanie"),
            ("Running/Athletics", "bieganie/lekkoatletyka"),
            ("Ice hockey", "hokej"),
            ("Skiing", "narciarstwo"),
            ("Cycling", "kolarstwo"),
            ("Boxing", "boks"),
            ("Martial arts", "sztuki walki"),
            ("Golf", "golf"),
            ("Table tennis", "tenis stolowy"),
            ("Wrestling", "zapasy"),
            ("Handball", "pilka reczna"),
            ("Baseball", "baseball"),
            ("Surfing", "surfowanie"),
            ("Skating", "jazda na lyzwach"),
            ("Horse riding", "jazda konna"),
            ("Diving", "nurkowanie"),
            ("Cricket", "krykiet"),
            ("Rugby", "rugby"),
            ("Ballet", "balet"),
            ("Bowling", "kregle"),
            ("Weightlifting", "podnoszenie ciezarow"),
            ("Windsurfing", "windsurfing"),
            ("Ice skating", "jazda na lyzwach"),
            ("Rowing", "wioslarstwo"),
            ("Archery", "lucznictwo"),
            ("Climbing", "wspinaczka")
        ],
        "is_numbers": False
    },
    
    "Lesson 18 - Numbers 51-75": {
        "count": 25,
        "words": [
            ("51", "piecdziesiat jeden"),
            ("52", "piecdziesiat dwa"),
            ("53", "piecdziesiat trzy"),
            ("54", "piecdziesiat cztery"),
            ("55", "piecdziesiat piec"),
            ("56", "piecdziesiat szesc"),
            ("57", "piecdziesiat siedem"),
            ("58", "piecdziesiat osiem"),
            ("59", "piecdziesiat dziewiec"),
            ("60", "szescdziesiat"),
            ("61", "szescdziesiat jeden"),
            ("62", "szescdziesiat dwa"),
            ("63", "szescdziesiat trzy"),
            ("64", "szescdziesiat cztery"),
            ("65", "szescdziesiat piec"),
            ("66", "szescdziesiat szesc"),
            ("67", "szescdziesiat siedem"),
            ("68", "szescdziesiat osiem"),
            ("69", "szescdziesiat dziewiec"),
            ("70", "siedemdziesiat"),
            ("71", "siedemdziesiat jeden"),
            ("72", "siedemdziesiat dwa"),
            ("73", "siedemdziesiat trzy"),
            ("74", "siedemdziesiat cztery"),
            ("75", "siedemdziesiat piec")
        ],
        "is_numbers": True
    },
    
    "Lesson 19 - Clothing": {
        "count": 42,
        "words": [
            ("Shirt", "koszula"),
            ("T-shirt", "koszulka"),
            ("Blouse", "bluzka"),
            ("Sweater", "sweter"),
            ("Jacket", "kurtka"),
            ("Coat", "plaszcz"),
            ("Dress", "sukienka"),
            ("Skirt", "spodnica"),
            ("Pants", "spodnie"),
            ("Shorts", "krotkie spodenki"),
            ("Shoes", "buty"),
            ("Boots", "kozaki"),
            ("Sneakers", "trampki"),
            ("Sandals", "sandaly"),
            ("Hat/Cap", "czapka"),
            ("Scarf", "szalik"),
            ("Gloves", "rekawiczki"),
            ("Belt", "pasek"),
            ("Socks", "skarpetki"),
            ("Winter coat", "zimowy plaszcz"),
            ("Wool hat", "welniana czapka"),
            ("Snow boots", "buty sniegowe"),
            ("Swimsuit", "kostium kapielowy"),
            ("Sunglasses", "okulary przeciwsloneczne"),
            ("Flip-flops", "klapki"),
            ("Tank top", "top"),
            ("Suit", "garnitur"),
            ("Tie", "krawat"),
            ("Blazer", "marynarka"),
            ("High heels", "buty na obcasie"),
            ("Evening dress", "suknia wieczorowa"),
            ("Black", "czarny"),
            ("White", "bialy"),
            ("Red", "czerwony"),
            ("Blue", "niebieski"),
            ("Green", "zielony"),
            ("Cotton", "bawelna"),
            ("Wool", "welna"),
            ("Leather", "skora"),
            ("Silk", "jedwab"),
            ("Linen", "len")
        ],
        "is_numbers": False
    },
    
    "Lesson 20 - Adverbs": {
        "count": 20,
        "words": [
            ("Quickly", "szybko"),
            ("Slowly", "powoli"),
            ("Always", "zawsze"),
            ("Never", "nigdy"),
            ("Often", "czesto"),
            ("Sometimes", "czasami"),
            ("Rarely", "rzadko"),
            ("Already", "juz"),
            ("Still", "nadal"),
            ("Yet", "jeszcze"),
            ("Soon", "wkrotce"),
            ("Now", "teraz"),
            ("Later", "pozniej"),
            ("Today", "dzisiaj"),
            ("Tomorrow", "jutro"),
            ("Yesterday", "wczoraj"),
            ("Clearly", "wyraznie"),
            ("Together", "razem"),
            ("Apart", "osobno"),
            ("Forever", "na zawsze")
        ],
        "is_numbers": False
    },
    
    "Lesson 21 - Animals": {
        "count": 20,
        "words": [
            ("Dog", "pies"),
            ("Cat", "kot"),
            ("Horse", "kon"),
            ("Cow", "krowa"),
            ("Sheep", "owca"),
            ("Pig", "swinia"),
            ("Goat", "koza"),
            ("Chicken", "kurczak"),
            ("Duck", "kaczka"),
            ("Bird", "ptak"),
            ("Rabbit", "krolik"),
            ("Mouse", "mysz"),
            ("Lion", "lew"),
            ("Tiger", "tygrys"),
            ("Bear", "niedzwiedz"),
            ("Elephant", "slon"),
            ("Monkey", "malpa"),
            ("Fox", "lis"),
            ("Wolf", "wilk"),
            ("Deer", "jelen")
        ],
        "is_numbers": False
    },
    
    "Lesson 23 - Places in Town": {
        "count": 20,
        "words": [
            ("School", "szkola"),
            ("Hospital", "szpital"),
            ("Bank", "bank"),
            ("Restaurant", "restauracja"),
            ("Library", "biblioteka"),
            ("Supermarket", "supermarket"),
            ("Cinema", "kino"),
            ("Post office", "poczta"),
            ("Police station", "posterunek policji"),
            ("Park", "park"),
            ("Museum", "muzeum"),
            ("Theatre", "teatr"),
            ("Hotel", "hotel"),
            ("Stadium", "stadion"),
            ("Church", "kosciol"),
            ("Pharmacy", "apteka"),
            ("Bakery", "piekarnia"),
            ("Butcher", "rzeznik"),
            ("Market", "targ"),
            ("Hairdresser", "fryzjer")
        ],
        "is_numbers": False
    },
    
    "Lesson 24 - School Supplies": {
        "count": 15,
        "words": [
            ("Whiteboard", "tablica"),
            ("Compass", "cyrkiel"),
            ("Protractor", "katomierz"),
            ("Binder", "segregator"),
            ("Pen holder", "przybornik"),
            ("Sticky notes", "karteczki samoprzylepne"),
            ("Projector", "rzutnik"),
            ("Chalkboard", "tablica kredowa"),
            ("Schoolbag", "torba szkolna"),
            ("Clipboard", "podkladka"),
            ("Hole punch", "dziurkacz"),
            ("Tape", "tasma"),
            ("Stapler", "zszywacz"),
            ("Laptop", "laptop"),
            ("Printer", "drukarka")
        ],
        "is_numbers": False
    },
    
    "Lesson 25 - Transportation": {
        "count": 20,
        "words": [
            ("Car", "samochod"),
            ("Bus", "autobus"),
            ("Train", "pociag"),
            ("Bicycle", "rower"),
            ("Motorcycle", "motocykl"),
            ("Airplane", "samolot"),
            ("Boat", "lodz"),
            ("Tram", "tramwaj"),
            ("Taxi", "taksowka"),
            ("Subway", "metro"),
            ("Ferry", "prom"),
            ("Yacht", "jacht"),
            ("Hot air balloon", "balon"),
            ("Spaceship", "statek kosmiczny"),
            ("Rickshaw", "riksza"),
            ("Gondola", "gondola"),
            ("Zeppelin", "sterowiec"),
            ("Rollerblades", "rolki"),
            ("Canoe", "kajak"),
            ("Submarine", "lodz podwodna")
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
        for english, polish in words:
            questions.append({
                'type': 'num_to_word',
                'question': f"What is '{english}' in Polish? (Answer with the WORD)",
                'answer': polish,
                'display_answer': polish  # Show WORD
            })
        
        # Type 2: Word to number (Answer: NUMBER)
        for english, polish in words:
            questions.append({
                'type': 'word_to_num',
                'question': f"What number is '{polish}'? (Answer with the NUMBER)",
                'answer': english,
                'display_answer': english  # Show NUMBER
            })
        
        # Type 3: Mixed (Answer based on type)
        for english, polish in words:
            if random.choice([True, False]):
                # Number to word
                questions.append({
                    'type': 'mixed',
                    'question': f"Translate '{english}' to Polish word:",
                    'answer': polish,
                    'display_answer': polish  # WORD
                })
            else:
                # Word to number
                questions.append({
                    'type': 'mixed',
                    'question': f"What number is '{polish}'?",
                    'answer': english,
                    'display_answer': english  # NUMBER
                })
    
    elif count <= 20:
        # 20 or less: 3 different question types
        # Type 1: English -> Polish
        for english, polish in words:
            questions.append({
                'type': 'eng_to_pol',
                'question': f"Translate to Polish: '{english}'",
                'answer': polish,
                'display_answer': polish
            })
        
        # Type 2: Polish -> English
        for english, polish in words:
            questions.append({
                'type': 'pol_to_eng',
                'question': f"Translate to English: '{polish}'",
                'answer': english,
                'display_answer': english
            })
        
        # Type 3: First letter hint
        for english, polish in words:
            first_letter = polish[0] if polish else ""
            blanks = "_" * (len(polish) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}' - Complete the Polish word",
                'answer': polish,
                'display_answer': polish
            })
    
    elif 20 < count <= 40:
        # 20-40: 3 sections, 2 different question types
        third = len(words) // 3
        
        # Section 1: English -> Polish
        for english, polish in words[:third]:
            questions.append({
                'type': 'eng_to_pol',
                'question': f"Translate to Polish: '{english}'",
                'answer': polish,
                'display_answer': polish
            })
        
        # Section 2: Polish -> English
        for english, polish in words[third:third*2]:
            questions.append({
                'type': 'pol_to_eng',
                'question': f"Translate to English: '{polish}'",
                'answer': english,
                'display_answer': english
            })
        
        # Section 3: First letter hint
        for english, polish in words[third*2:]:
            first_letter = polish[0] if polish else ""
            blanks = "_" * (len(polish) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': polish,
                'display_answer': polish
            })
    
    else:  # count > 40
        # 40+: 5 sections, 3-4 different question types
        fifth = len(words) // 5
        
        # Section 1: English -> Polish
        for english, polish in words[:fifth]:
            questions.append({
                'type': 'eng_to_pol',
                'question': f"Translate to Polish: '{english}'",
                'answer': polish,
                'display_answer': polish
            })
        
        # Section 2: Polish -> English
        for english, polish in words[fifth:fifth*2]:
            questions.append({
                'type': 'pol_to_eng',
                'question': f"Translate to English: '{polish}'",
                'answer': english,
                'display_answer': english
            })
        
        # Section 3: First letter
        for english, polish in words[fifth*2:fifth*3]:
            first_letter = polish[0] if polish else ""
            blanks = "_" * (len(polish) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': polish,
                'display_answer': polish
            })
        
        # Section 4: Last letter
        for english, polish in words[fifth*3:fifth*4]:
            last_letter = polish[-1] if polish else ""
            blanks = "_" * (len(polish) - 1)
            questions.append({
                'type': 'last_letter',
                'question': f"'{english}' = '{blanks}{last_letter}'",
                'answer': polish,
                'display_answer': polish
            })
        
        # Section 5: Letter count hint
        for english, polish in words[fifth*4:]:
            questions.append({
                'type': 'letter_hint',
                'question': f"'{english}' = ({len(polish)} letters, starts with {polish[:2]}...)",
                'answer': polish,
                'display_answer': polish
            })
    
    return questions

def create_general_review(lesson_name, words, is_numbers):
    """General review questions after each lesson"""
    review = []
    sample_size = min(20, len(words))
    sampled_words = random.sample(words, sample_size)
    
    for english, polish in sampled_words:
        if is_numbers:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] '{english}' in Polish?",
                    'answer': polish,
                    'display_answer': polish
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] What number is '{polish}'?",
                    'answer': english,
                    'display_answer': english
                })
        else:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{english}'",
                    'answer': polish,
                    'display_answer': polish
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{polish}'",
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
║        COMPREHENSIVE POLISH TEST SYSTEM                   ║
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
        print(Fore.GREEN + "🎉🎉🎉 EXCELLENT! You're amazing at Polish! 🎉🎉🎉")
    elif final_percentage >= 70:
        print(Fore.BLUE + "👏👏👏 VERY GOOD! Great performance! 👏👏👏")
    elif final_percentage >= 50:
        print(Fore.YELLOW + "👍👍 GOOD! Keep going and you'll be excellent! 👍👍")
    else:
        print(Fore.RED + "📚📚 Keep studying! You can do it! 📚📚")
    
    print(Fore.GREEN + "\nCongratulations! You completed the entire test! 🎊")

if __name__ == "__main__":
    main()