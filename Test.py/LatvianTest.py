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
            ("1", "viens"),
            ("2", "divi"),
            ("3", "tris"),
            ("4", "cetri"),
            ("5", "pieci"),
            ("6", "sesi"),
            ("7", "septini"),
            ("8", "astoni"),
            ("9", "devini"),
            ("10", "desmit")
        ],
        "is_numbers": True
    },
    
    "Lesson 2 - Greetings": {
        "count": 18,
        "words": [
            ("Hello", "sveiki"),
            ("How are you?", "ka jums klajas"),
            ("Nice to meet you", "prieks iepazities"),
            ("See you tomorrow", "tiksimies rit"),
            ("Good morning", "labrit"),
            ("Good afternoon", "labdien"),
            ("Good evening", "labrakar"),
            ("Good night", "ar labu nakti"),
            ("What is your name?", "kads ir jusu vards"),
            ("My name is", "mani sauc"),
            ("Where do you live?", "kur tu dzivo"),
            ("Where are you from?", "no kurienes jus esat"),
            ("Nice to see you", "patikami jus redzet"),
            ("Have a nice day", "novelu jums jauku dienu"),
            ("See you later", "tiksimies velak"),
            ("Goodbye", "uz redzesanos"),
            ("Please", "ludzu"),
            ("Thank you", "paldies")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.1 - Regular -ĀT Verbs": {
        "count": 7,
        "words": [
            ("to speak", "runat"),
            ("to work", "stradat"),
            ("to think", "domat"),
            ("to sing", "dziedat"),
            ("to try", "meginat"),
            ("to reflect", "pardomat"),
            ("to invite", "uzaicinat")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.2 - Regular -ĪT Verbs": {
        "count": 7,
        "words": [
            ("to read", "lasit"),
            ("to smile", "smaidit"),
            ("to teach", "macit"),
            ("to write", "uzrakstit"),
            ("to send", "nosutit"),
            ("to note", "pierakstit"),
            ("to look at", "apskatit")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.3 - Regular -OT Verbs": {
        "count": 7,
        "words": [
            ("to live", "dzivot"),
            ("to cook", "gatavot"),
            ("to travel", "celot"),
            ("to observe", "verot"),
            ("to explain", "izskaidrot"),
            ("to explain", "paskaidrot"),
            ("to monitor", "noverot")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.4 - Regular -TIES Verbs": {
        "count": 4,
        "words": [
            ("to watch", "skatities"),
            ("to learn", "macities"),
            ("to listen", "klausities"),
            ("to sit down", "apsesties")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.5 - Regular -ĒT Verbs": {
        "count": 7,
        "words": [
            ("to swim", "peldet"),
            ("to search", "meklet"),
            ("to wish", "velet"),
            ("to draw", "zimet"),
            ("to sleep", "gulet"),
            ("to attend", "apmeklet"),
            ("to answer", "atbildet")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.6 - Regular -T Verbs": {
        "count": 7,
        "words": [
            ("to ask", "lugt"),
            ("to understand", "saprast"),
            ("to drive/go", "braukt"),
            ("to feel", "sajust"),
            ("to close", "izzvert"),
            ("to assign", "uzdot"),
            ("to interrupt", "partraukt")
        ],
        "is_numbers": False
    },
    
    "Lesson 4 - Adjectives": {
        "count": 35,
        "words": [
            ("Happy", "laimigs"),
            ("Sad", "bedigs"),
            ("Angry", "dusmigs"),
            ("Afraid", "nobijies"),
            ("Joy", "prieks"),
            ("Surprised", "parsteigts"),
            ("Calm", "mierigs"),
            ("Bored", "garlaikots"),
            ("Easy", "viegli"),
            ("Difficult", "gruti"),
            ("Bad", "slikts"),
            ("Good", "labs"),
            ("Noisy", "skals"),
            ("Quiet", "kluss"),
            ("Strong", "specigs"),
            ("Weak", "vajs"),
            ("Hard", "ciets"),
            ("Soft", "miksts"),
            ("More", "vairak"),
            ("Less", "mazak"),
            ("Clean", "tirs"),
            ("Dirty", "netirs"),
            ("New", "jauns"),
            ("Big", "liels"),
            ("Small", "mazs"),
            ("Young", "jauns"),
            ("Old", "vecs"),
            ("Skinny", "tievs"),
            ("Fat", "resns"),
            ("Pretty", "glits"),
            ("Ugly", "neglits"),
            ("Thick", "biezs"),
            ("Thin", "plans"),
            ("Rough", "rupjs"),
            ("Smooth", "gluds")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.1 - Days": {
        "count": 11,
        "words": [
            ("The days of the week", "nedelas dienas"),
            ("Day", "diena"),
            ("Week", "nedela"),
            ("Monday", "pirmdiena"),
            ("Tuesday", "otrdiena"),
            ("Wednesday", "tresdiena"),
            ("Thursday", "ceturtdiena"),
            ("Friday", "piektdiena"),
            ("Saturday", "sestdiena"),
            ("Sunday", "svetdiena"),
            ("Weekend", "nedelas nogale")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.2 - Months": {
        "count": 15,
        "words": [
            ("The months of the year", "gada menesi"),
            ("Month", "menesis"),
            ("Year", "gads"),
            ("January", "janvaris"),
            ("February", "februaris"),
            ("March", "marts"),
            ("April", "aprilis"),
            ("May", "maijs"),
            ("June", "junijs"),
            ("July", "julijs"),
            ("August", "augusts"),
            ("September", "septembris"),
            ("October", "oktobris"),
            ("November", "novembris"),
            ("December", "decembris")
        ],
        "is_numbers": False
    },
    
    "Lesson 6 - Seasons & Weather": {
        "count": 23,
        "words": [
            ("Seasons", "gadalaiki"),
            ("Winter", "ziema"),
            ("Summer", "vasara"),
            ("Spring", "pavasaris"),
            ("Autumn", "rudens"),
            ("Sky", "debesis"),
            ("Cloud", "makonis"),
            ("Rainbow", "varaviksne"),
            ("Cold", "auksts"),
            ("Hot", "karsts"),
            ("It is hot", "ir karsts"),
            ("It is cold", "ir auksts"),
            ("It is sunny", "ir saulains"),
            ("It is cloudy", "ir makonains"),
            ("It is humid", "ir mitrs"),
            ("It is raining", "list"),
            ("It is snowing", "snieg"),
            ("It is windy", "ir vejains"),
            ("How is the weather?", "kads ir laiks"),
            ("Good weather", "labs laiks"),
            ("Bad weather", "slikts laiks"),
            ("What is the temperature?", "kada ir temperatura"),
            ("It is 24 degrees", "ara ir 24 gradi")
        ],
        "is_numbers": False
    },
    
    "Lesson 7 - Colors": {
        "count": 14,
        "words": [
            ("Black", "melns"),
            ("Blue", "zils"),
            ("Brown", "bruns"),
            ("Green", "zals"),
            ("Orange", "oranzs"),
            ("Purple", "purpurs"),
            ("Red", "sarkans"),
            ("White", "balts"),
            ("Yellow", "dzeltens"),
            ("Gray", "peleks"),
            ("Gold", "zelts"),
            ("Silver", "sudrabs"),
            ("What color is it?", "kada krasa tas ir"),
            ("The color is", "krasa ir")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.1 - Family": {
        "count": 35,
        "words": [
            ("Mother", "mate"),
            ("Father", "tevs"),
            ("Brother", "bralis"),
            ("Sister", "masa"),
            ("Son", "dels"),
            ("Daughter", "meita"),
            ("Parents", "vecaki"),
            ("Children", "berni"),
            ("Child", "berns"),
            ("Stepmother", "pamate"),
            ("Stepfather", "patevs"),
            ("Stepsister", "pusmasa"),
            ("Stepbrother", "pusbralis"),
            ("Son-in-law", "znots"),
            ("Daughter-in-law", "vedekla"),
            ("Wife", "sieva"),
            ("Husband", "virs"),
            ("Grandparents", "vecvecaki"),
            ("Grandfather", "vectevs"),
            ("Grandmother", "vecmamina"),
            ("Grandson", "mazdels"),
            ("Granddaughter", "mazmeita"),
            ("Grandchildren", "mazberni"),
            ("Grandchild", "mazberns"),
            ("Aunt", "tante"),
            ("Uncle", "tevocis"),
            ("Cousin (female)", "masica"),
            ("Cousin (male)", "bralens"),
            ("Nephew", "braladels"),
            ("Niece", "bralameita"),
            ("Father-in-law", "viratevs"),
            ("Mother-in-law", "viramate"),
            ("Brother-in-law", "svainis"),
            ("Sister-in-law", "svaine"),
            ("Relative", "radinieks")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.2 - Friends": {
        "count": 14,
        "words": [
            ("Miss", "jaunkundze"),
            ("Boy", "zens"),
            ("Girl", "meitene"),
            ("Baby", "mazulis"),
            ("Woman", "sieviete"),
            ("Man", "virietis"),
            ("Friend (male)", "draugs"),
            ("Friend (female)", "draudzene"),
            ("Boyfriend", "draugs"),
            ("Girlfriend", "draudzene"),
            ("Gentleman", "kungs"),
            ("Lady", "dama"),
            ("Neighbor (male)", "kaimins"),
            ("Neighbor (female)", "kaiminiene")
        ],
        "is_numbers": False
    },
    
    "Lesson 9 - Numbers 11-30": {
        "count": 20,
        "words": [
            ("11", "vienpadsmit"),
            ("12", "divpadsmit"),
            ("13", "trispadsmit"),
            ("14", "cetrpadsmit"),
            ("15", "piecpadsmit"),
            ("16", "sespadsmit"),
            ("17", "septinpadsmit"),
            ("18", "astonpadsmit"),
            ("19", "devinpadsmit"),
            ("20", "divdesmit"),
            ("21", "divdesmit viens"),
            ("22", "divdesmit divi"),
            ("23", "divdesmit tris"),
            ("24", "divdesmit cetri"),
            ("25", "divdesmit pieci"),
            ("26", "divdesmit sesi"),
            ("27", "divdesmit septini"),
            ("28", "divdesmit astoni"),
            ("29", "divdesmit devini"),
            ("30", "trisdesmit")
        ],
        "is_numbers": True
    },
    
    "Lesson 10.1 - Prepositions": {
        "count": 36,
        "words": [
            ("For", "par"),
            ("From", "no"),
            ("In", "ieksa"),
            ("Inside", "ieksa"),
            ("Into", "ieksa"),
            ("Near", "tuvu"),
            ("Of", "no"),
            ("Out", "ara"),
            ("Outside", "arpus"),
            ("To", "uz"),
            ("Under", "zem"),
            ("With", "ar"),
            ("Without", "bez"),
            ("Above", "virs"),
            ("Across", "pari"),
            ("After", "pec"),
            ("Against", "pret"),
            ("Along", "lidzas"),
            ("Around", "apkart"),
            ("At", "pie"),
            ("Behind", "aiz"),
            ("Below", "apaksa"),
            ("Beside", "blakus"),
            ("Between", "starp"),
            ("By", "blakus"),
            ("During", "laika"),
            ("Except", "iznemot"),
            ("And", "un"),
            ("Because", "jo"),
            ("But", "bet"),
            ("Or", "vai"),
            ("Everywhere", "visur"),
            ("Everyone", "ikviens"),
            ("Everything", "viss"),
            ("Few", "maz"),
            ("Some", "dazi"),
            ("Many", "daudz")
        ],
        "is_numbers": False
    },
    
    "Lesson 10.2 - Useful Words": {
        "count": 29,
        "words": [
            ("Question", "jautajums"),
            ("Answer", "atbilde"),
            ("Truth", "patiesiba"),
            ("Lie", "meli"),
            ("Nothing", "nekas"),
            ("Something", "kaut kas"),
            ("Same", "tas pats"),
            ("Different", "atskirigs"),
            ("Pull", "vilkt"),
            ("Push", "stumt"),
            ("Long", "gars"),
            ("Short", "iss"),
            ("Cold", "auksts"),
            ("Hot", "karsts"),
            ("Light", "gaiss"),
            ("Dark", "tumss"),
            ("Wet", "slapjs"),
            ("Dry", "sauss"),
            ("Empty", "tukss"),
            ("Full", "pilns"),
            ("How?", "ka"),
            ("What?", "kas"),
            ("When?", "kad"),
            ("Where?", "kur"),
            ("Which?", "kurs"),
            ("Who?", "kas"),
            ("Why?", "kapec"),
            ("How long?", "cik ilgi"),
            ("How much?", "cik daudz")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.1 - Drinks": {
        "count": 9,
        "words": [
            ("Coffee", "kafija"),
            ("Tea", "teja"),
            ("Soft drink", "gazets dzariens"),
            ("Water", "udens"),
            ("Lemonade", "limonade"),
            ("Juice", "sula"),
            ("Orange juice", "apelsinu sula"),
            ("I would like a glass of water please", "es gribetu glazi udens ludzu"),
            ("With ice", "ar ledu")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.2 - Dairy Products": {
        "count": 19,
        "words": [
            ("Milk", "piens"),
            ("Ice cream", "saldejums"),
            ("Butter", "sviests"),
            ("Cheese", "siers"),
            ("Cottage cheese", "biezpiens"),
            ("Cream", "krems"),
            ("Sour cream", "skabais krejums"),
            ("Yogurt", "jogurts"),
            ("Eggs", "olas"),
            ("Whipping cream", "putukrejums"),
            ("Bakery", "maiznica"),
            ("Baguette", "bagete"),
            ("Doughnut", "virtulis"),
            ("Cookie", "cepums"),
            ("Roll", "rullitis"),
            ("Dessert", "deserts"),
            ("Cake", "kuka"),
            ("Bread", "maize"),
            ("Pie", "pirags")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.3 - Meats": {
        "count": 13,
        "words": [
            ("Beef", "liellopu gala"),
            ("Veal", "tela gala"),
            ("Ham", "skinkis"),
            ("Chicken", "calis"),
            ("Turkey", "titars"),
            ("Duck", "pile"),
            ("Bacon", "bekons"),
            ("Pork", "cukgala"),
            ("Filet mignon", "liellopa galas medaljons"),
            ("Sausage", "desa"),
            ("Lamb chop", "jera karbonade"),
            ("Pork chop", "karbonade"),
            ("Meat", "gala")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.4 - Seafoods": {
        "count": 20,
        "words": [
            ("Fish", "zivs"),
            ("Shellfish", "vezveidigde"),
            ("Bass", "asaris"),
            ("Salmon", "lasis"),
            ("Lobster", "omars"),
            ("Crab", "krabis"),
            ("Mussel", "gliemene"),
            ("Oyster", "austere"),
            ("Cod", "menca"),
            ("Clam", "gliemezis"),
            ("Shrimp", "garnele"),
            ("Tuna", "tuncis"),
            ("Trout", "forele"),
            ("Sole", "zole"),
            ("Shark", "haizivs"),
            ("Carp", "karpa"),
            ("Tilapia", "tilapija"),
            ("Eel", "zutis"),
            ("Catfish", "sams"),
            ("Swordfish", "zobenzivs")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.5 - Herbs & Spices": {
        "count": 17,
        "words": [
            ("Salt", "sals"),
            ("Pepper", "pipari"),
            ("Caraway", "kimenes"),
            ("Garlic", "kiploki"),
            ("Basil", "baziliks"),
            ("Coriander", "koriandrs"),
            ("Fennel", "fenhelis"),
            ("Marjoram", "majorans"),
            ("Oregano", "oregano"),
            ("Parsley", "petersili"),
            ("Rosemary", "rozmarins"),
            ("Sage", "salvija"),
            ("Thyme", "timians"),
            ("Nutmeg", "muskatrieksts"),
            ("Paprika", "paprika"),
            ("Cayenne", "kajenas pipari"),
            ("Ginger", "ingvers")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.6 - Vegetables": {
        "count": 28,
        "words": [
            ("Celery", "selerijas"),
            ("Eggplant", "baklazans"),
            ("Zucchini", "cukini"),
            ("Onion", "sipols"),
            ("Spinach", "spinati"),
            ("Salad", "salati"),
            ("Green beans", "paksu pupinas"),
            ("Cucumber", "gurkis"),
            ("Radish", "rediss"),
            ("Cabbage", "kaposti"),
            ("Mushrooms", "senes"),
            ("Lettuce", "salati"),
            ("Corn", "kukuruza"),
            ("Potatoes", "kartupeli"),
            ("Tomato", "tomats"),
            ("Carrot", "burkans"),
            ("Plantain", "plantans"),
            ("Beans", "pupas"),
            ("Leek", "puravi"),
            ("Lotus root", "lotosa saknes"),
            ("Bamboo shoot", "bambusa atvases"),
            ("Artichoke", "artisoks"),
            ("Asparagus", "spargeli"),
            ("Brussels sprouts", "briseles kaposti"),
            ("Broccoli", "brokoli"),
            ("Peas", "zirni"),
            ("Cauliflower", "ziedkaposti"),
            ("Chili pepper", "cili pipari")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.7 - Fruits": {
        "count": 27,
        "words": [
            ("Cherries", "kirsi"),
            ("Raspberries", "avenes"),
            ("Blueberries", "mellenes"),
            ("Strawberries", "zemenes"),
            ("Lemon", "citrons"),
            ("Lime", "laims"),
            ("Apple", "abols"),
            ("Orange", "apelsins"),
            ("Pear", "bumbieris"),
            ("Banana", "banans"),
            ("Grapes", "vinogas"),
            ("Grapefruit", "greipfruts"),
            ("Watermelon", "arbuzs"),
            ("Pineapple", "ananass"),
            ("Plum", "plume"),
            ("Peach", "persiks"),
            ("Mango", "mango"),
            ("Apricot", "aprikoze"),
            ("Pomegranate", "granatabols"),
            ("Persimmon", "hurma"),
            ("Kiwi", "kivi"),
            ("Litchi", "kiniešu plumes"),
            ("Longan", "longans"),
            ("Balsam pear", "balzambumbieris"),
            ("Passion fruit", "marakuja"),
            ("Avocado", "avokado"),
            ("Coconut", "kokosrieksts")
        ],
        "is_numbers": False
    },
    
    "Lesson 12 - Numbers 31-50": {
        "count": 20,
        "words": [
            ("31", "trisdesmit viens"),
            ("32", "trisdesmit divi"),
            ("33", "trisdesmit tris"),
            ("34", "trisdesmit cetri"),
            ("35", "trisdesmit pieci"),
            ("36", "trisdesmit sesi"),
            ("37", "trisdesmit septini"),
            ("38", "trisdesmit astoni"),
            ("39", "trisdesmit devini"),
            ("40", "cetrdesmit"),
            ("41", "cetrdesmit viens"),
            ("42", "cetrdesmit divi"),
            ("43", "cetrdesmit tris"),
            ("44", "cetrdesmit cetri"),
            ("45", "cetrdesmit pieci"),
            ("46", "cetrdesmit sesi"),
            ("47", "cetrdesmit septini"),
            ("48", "cetrdesmit astoni"),
            ("49", "cetrdesmit devini"),
            ("50", "piecdesmit")
        ],
        "is_numbers": True
    },
    
    "Lesson 13 - Irregular Verbs": {
        "count": 47,
        "words": [
            ("to be", "but"),
            ("to go", "iet"),
            ("can/be able to", "varet"),
            ("to do", "darit"),
            ("to drive/go", "braukt"),
            ("to eat", "est"),
            ("to come", "nakt"),
            ("to give", "dot"),
            ("to want", "gribet"),
            ("to start", "sakt"),
            ("to know", "zinat"),
            ("to say", "teikt"),
            ("to understand", "saprast"),
            ("to put", "likt"),
            ("to find", "atrast"),
            ("to sit", "sedet"),
            ("to call", "zvanit"),
            ("to help", "palidzet"),
            ("to forget", "aizmirst"),
            ("to answer", "atbildet"),
            ("to take", "nemt"),
            ("to run", "skriet"),
            ("to become", "klut"),
            ("to sing", "dziedat"),
            ("to hide", "paslept"),
            ("to continue", "turpinat"),
            ("to explain", "paskaidrot"),
            ("to wait for", "sagaidit"),
            ("to dream", "sapnot"),
            ("to send", "nosutit"),
            ("to stop", "apstaties"),
            ("to climb", "uzkapt"),
            ("to choose", "izveleties"),
            ("to win", "uzvaret"),
            ("to lose", "zaudet"),
            ("to burn", "degt"),
            ("to sit down", "apsesties"),
            ("to take (quickly)", "panemt"),
            ("to assign", "uzdot"),
            ("to solve", "risinat"),
            ("to save (rescue)", "glabt"),
            ("to close", "aizvert"),
            ("to prepare", "pagatavot"),
            ("to build", "uzbuvets"),
            ("to decorate", "izrotat"),
            ("to gather", "sapulcet"),
            ("to compose", "saceret")
        ],
        "is_numbers": False
    },
    
    "Lesson 15 - Physical Appearance": {
        "count": 38,
        "words": [
            ("Tall", "gars"),
            ("Short (height)", "iss"),
            ("Slim", "slaids"),
            ("Fat", "resns"),
            ("Muscular", "muskulots"),
            ("Blonde", "blonds"),
            ("Brown-haired", "bruni mati"),
            ("Black-haired", "melni mati"),
            ("Curly hair", "cirtaini mati"),
            ("Straight hair", "taisni mati"),
            ("Blue eyes", "zilas acis"),
            ("Brown eyes", "brunas acis"),
            ("Green eyes", "zalas acis"),
            ("Beautiful", "skaists"),
            ("Handsome", "izskatigs"),
            ("Ugly", "neglits"),
            ("Young", "jauns"),
            ("Old", "vecs"),
            ("Beard", "barda"),
            ("Light-skinned", "gaisa ada"),
            ("Dark-skinned", "tumsa ada"),
            ("Freckles", "vasaras raibumi"),
            ("Wrinkles", "krunkas"),
            ("Bald", "kails"),
            ("Hairy (body)", "spalvains"),
            ("Straight nose", "taisns deguns"),
            ("Big nose", "liels deguns"),
            ("Small nose", "mazs deguns"),
            ("Thin lips", "planas lupas"),
            ("Full lips", "pilnas lupas"),
            ("Broad shoulders", "plati pleci"),
            ("Narrow shoulders", "sauri pleci"),
            ("Tanned skin", "iedegusi ada"),
            ("Pale skin", "bala ada"),
            ("Wavy hair", "vilnaini mati"),
            ("Ponytail", "zirgaste"),
            ("Braids", "bizites"),
            ("Beard and mustache", "barda un usas")
        ],
        "is_numbers": False
    },
    
    "Lesson 16 - Occupations": {
        "count": 25,
        "words": [
            ("Doctor", "arsts"),
            ("Teacher", "skolotajs"),
            ("Engineer", "inzenieris"),
            ("Lawyer", "jurists"),
            ("Salesperson", "pardevejas"),
            ("Police officer", "policists"),
            ("Firefighter", "ugunsdzesejs"),
            ("Programmer", "programmetajs"),
            ("Cook/Chef", "pavars"),
            ("Journalist", "zurnalists"),
            ("Nurse", "medmasa"),
            ("Architect", "arhitekts"),
            ("Accountant", "gramatvedis"),
            ("Pharmacist", "farmaceits"),
            ("Driver", "vaditajs"),
            ("Mechanic", "mehanikis"),
            ("Scientist", "zinatnieks"),
            ("Dentist", "zobarsts"),
            ("Musician", "muzikis"),
            ("Actor", "aktieris"),
            ("Artist", "maksliniekas"),
            ("Pilot", "pilots"),
            ("Farmer", "zemnieks"),
            ("Photographer", "fotografs"),
            ("Waiter/Waitress", "viesmilis")
        ],
        "is_numbers": False
    },
    
    "Lesson 17 - Sports": {
        "count": 30,
        "words": [
            ("Football/Soccer", "futbols"),
            ("Basketball", "basketbols"),
            ("Volleyball", "volejbols"),
            ("Tennis", "teniss"),
            ("Swimming", "peldesana"),
            ("Running/Athletics", "skrlesana/vieglatletika"),
            ("Ice hockey", "hokejs"),
            ("Skiing", "slepošana"),
            ("Cycling", "ritenbraksana"),
            ("Boxing", "bokss"),
            ("Martial arts", "cinas makslas"),
            ("Golf", "golfs"),
            ("Table tennis", "galda teniss"),
            ("Wrestling", "cina"),
            ("Handball", "handbols"),
            ("Baseball", "beisbols"),
            ("Surfing", "serfosana"),
            ("Skating", "slidošana"),
            ("Horse riding", "jasana"),
            ("Diving", "leksana udeni"),
            ("Cricket", "krikets"),
            ("Rugby", "regbijs"),
            ("Ballet", "balets"),
            ("Bowling", "boulinga"),
            ("Weightlifting", "svarcelsana"),
            ("Windsurfing", "vindserfings"),
            ("Ice skating", "slidošana"),
            ("Rowing", "akademiskais airesana"),
            ("Archery", "loka sausana"),
            ("Climbing", "kapsana")
        ],
        "is_numbers": False
    },
    
    "Lesson 18 - Numbers 51-75": {
        "count": 25,
        "words": [
            ("51", "piecdesmit viens"),
            ("52", "piecdesmit divi"),
            ("53", "piecdesmit tris"),
            ("54", "piecdesmit cetri"),
            ("55", "piecdesmit pieci"),
            ("56", "piecdesmit sesi"),
            ("57", "piecdesmit septini"),
            ("58", "piecdesmit astoni"),
            ("59", "piecdesmit devini"),
            ("60", "sesdesmit"),
            ("61", "sesdesmit viens"),
            ("62", "sesdesmit divi"),
            ("63", "sesdesmit tris"),
            ("64", "sesdesmit cetri"),
            ("65", "sesdesmit pieci"),
            ("66", "sesdesmit sesi"),
            ("67", "sesdesmit septini"),
            ("68", "sesdesmit astoni"),
            ("69", "sesdesmit devini"),
            ("70", "septindesmit"),
            ("71", "septindesmit viens"),
            ("72", "septindesmit divi"),
            ("73", "septindesmit tris"),
            ("74", "septindesmit cetri"),
            ("75", "septindesmit pieci")
        ],
        "is_numbers": True
    },
    
    "Lesson 19 - Clothing": {
        "count": 42,
        "words": [
            ("Shirt", "krekls"),
            ("T-shirt", "t-krekls"),
            ("Blouse", "bluze"),
            ("Sweater", "dzemperis"),
            ("Jacket", "jaka"),
            ("Coat", "metelis"),
            ("Dress", "kleita"),
            ("Skirt", "svarki"),
            ("Pants", "bikses"),
            ("Shorts", "sorti"),
            ("Shoes", "kurpes"),
            ("Boots", "zabaki"),
            ("Sneakers", "kedas"),
            ("Sandals", "sandales"),
            ("Hat/Cap", "cepure"),
            ("Scarf", "salle"),
            ("Gloves", "cimdi"),
            ("Belt", "josta"),
            ("Socks", "zekes"),
            ("Winter coat", "ziemas metelis"),
            ("Wool hat", "vilnas cepure"),
            ("Snow boots", "sniega zabaki"),
            ("Swimsuit", "peldkostims"),
            ("Sunglasses", "saulesbrilles"),
            ("Flip-flops", "ieslucenes"),
            ("Tank top", "tops"),
            ("Suit", "uzvalks"),
            ("Tie", "kaklasaite"),
            ("Blazer", "zakete"),
            ("High heels", "augstpapezu kurpes"),
            ("Evening dress", "vakarkleita"),
            ("Black", "melns"),
            ("White", "balts"),
            ("Red", "sarkans"),
            ("Blue", "zils"),
            ("Green", "zals"),
            ("Cotton", "kokvilna"),
            ("Wool", "vilna"),
            ("Leather", "ada"),
            ("Silk", "zids"),
            ("Linen", "lina")
        ],
        "is_numbers": False
    },
    
    "Lesson 20 - Adverbs": {
        "count": 20,
        "words": [
            ("Quickly", "atri"),
            ("Slowly", "lenam"),
            ("Always", "vienmer"),
            ("Never", "nekad"),
            ("Often", "biezi"),
            ("Sometimes", "dazreiz"),
            ("Rarely", "reti"),
            ("Already", "jau"),
            ("Still", "vel joprojam"),
            ("Yet", "vel"),
            ("Soon", "driz"),
            ("Now", "tagad"),
            ("Later", "velak"),
            ("Today", "sodien"),
            ("Tomorrow", "rit"),
            ("Yesterday", "vakar"),
            ("Clearly", "skaidri"),
            ("Together", "kopa"),
            ("Apart", "skitri"),
            ("Forever", "uz visiem laikiem")
        ],
        "is_numbers": False
    },
    
    "Lesson 21 - Animals": {
        "count": 20,
        "words": [
            ("Dog", "suns"),
            ("Cat", "kakis"),
            ("Horse", "zirgs"),
            ("Cow", "govs"),
            ("Sheep", "aita"),
            ("Pig", "cuka"),
            ("Goat", "kaza"),
            ("Chicken", "vista"),
            ("Duck", "pile"),
            ("Bird", "putns"),
            ("Rabbit", "truss"),
            ("Mouse", "pele"),
            ("Lion", "lauva"),
            ("Tiger", "tigeris"),
            ("Bear", "lacis"),
            ("Elephant", "zilonis"),
            ("Monkey", "pertikis"),
            ("Fox", "lapsa"),
            ("Wolf", "vilks"),
            ("Deer", "briezi")
        ],
        "is_numbers": False
    },
    
    "Lesson 23 - Places in Town": {
        "count": 20,
        "words": [
            ("School", "skola"),
            ("Hospital", "slimnica"),
            ("Bank", "banka"),
            ("Restaurant", "restorans"),
            ("Library", "biblioteka"),
            ("Supermarket", "lielveikals"),
            ("Cinema", "kinoteatris"),
            ("Post office", "pasta nodala"),
            ("Police station", "policijas iecirknis"),
            ("Park", "parks"),
            ("Museum", "muzejs"),
            ("Theatre", "teatris"),
            ("Hotel", "viesnica"),
            ("Stadium", "stadions"),
            ("Church", "baznica"),
            ("Pharmacy", "aptieka"),
            ("Bakery", "maiznica"),
            ("Butcher", "galas veikals"),
            ("Market", "tirgus"),
            ("Hairdresser", "frizieris")
        ],
        "is_numbers": False
    },
    
    "Lesson 24 - School Supplies": {
        "count": 15,
        "words": [
            ("Whiteboard", "balta tafele"),
            ("Compass", "krausts"),
            ("Protractor", "traktaktors"),
            ("Binder", "segmasina"),
            ("Pen holder", "pildspalvu turetajs"),
            ("Sticky notes", "piezimju lapinas"),
            ("Projector", "projektors"),
            ("Chalkboard", "tafele"),
            ("Schoolbag", "skolas soma"),
            ("Clipboard", "platforma"),
            ("Hole punch", "perforators"),
            ("Tape", "lente"),
            ("Stapler", "skavotajs"),
            ("Laptop", "klepjdators"),
            ("Printer", "printeris")
        ],
        "is_numbers": False
    },
    
    "Lesson 25 - Transportation": {
        "count": 20,
        "words": [
            ("Car", "automasina"),
            ("Bus", "autobuss"),
            ("Train", "vilciens"),
            ("Bicycle", "velosipeds"),
            ("Motorcycle", "motocikls"),
            ("Airplane", "lidmasina"),
            ("Boat", "laiva"),
            ("Tram", "tramvajs"),
            ("Taxi", "taksometrs"),
            ("Subway", "metro"),
            ("Ferry", "pramis"),
            ("Yacht", "jahta"),
            ("Hot air balloon", "gaisa balons"),
            ("Spaceship", "kosmosa kugis"),
            ("Rickshaw", "riksa"),
            ("Gondola", "gondola"),
            ("Zeppelin", "cepelins"),
            ("Rollerblades", "skrituslidas"),
            ("Canoe", "kanoe laiva"),
            ("Submarine", "zemudene")
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
        for english, latvian in words:
            questions.append({
                'type': 'num_to_word',
                'question': f"What is '{english}' in Latvian? (Answer with the WORD)",
                'answer': latvian,
                'display_answer': latvian  # Show WORD
            })
        
        # Type 2: Word to number (Answer: NUMBER)
        for english, latvian in words:
            questions.append({
                'type': 'word_to_num',
                'question': f"What number is '{latvian}'? (Answer with the NUMBER)",
                'answer': english,
                'display_answer': english  # Show NUMBER
            })
        
        # Type 3: Mixed (Answer based on type)
        for english, latvian in words:
            if random.choice([True, False]):
                # Number to word
                questions.append({
                    'type': 'mixed',
                    'question': f"Translate '{english}' to Latvian word:",
                    'answer': latvian,
                    'display_answer': latvian  # WORD
                })
            else:
                # Word to number
                questions.append({
                    'type': 'mixed',
                    'question': f"What number is '{latvian}'?",
                    'answer': english,
                    'display_answer': english  # NUMBER
                })
    
    elif count <= 20:
        # 20 or less: 3 different question types
        # Type 1: English -> Latvian
        for english, latvian in words:
            questions.append({
                'type': 'eng_to_lav',
                'question': f"Translate to Latvian: '{english}'",
                'answer': latvian,
                'display_answer': latvian
            })
        
        # Type 2: Latvian -> English
        for english, latvian in words:
            questions.append({
                'type': 'lav_to_eng',
                'question': f"Translate to English: '{latvian}'",
                'answer': english,
                'display_answer': english
            })
        
        # Type 3: First letter hint
        for english, latvian in words:
            first_letter = latvian[0] if latvian else ""
            blanks = "_" * (len(latvian) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}' - Complete the Latvian word",
                'answer': latvian,
                'display_answer': latvian
            })
    
    elif 20 < count <= 40:
        # 20-40: 3 sections, 2 different question types
        third = len(words) // 3
        
        # Section 1: English -> Latvian
        for english, latvian in words[:third]:
            questions.append({
                'type': 'eng_to_lav',
                'question': f"Translate to Latvian: '{english}'",
                'answer': latvian,
                'display_answer': latvian
            })
        
        # Section 2: Latvian -> English
        for english, latvian in words[third:third*2]:
            questions.append({
                'type': 'lav_to_eng',
                'question': f"Translate to English: '{latvian}'",
                'answer': english,
                'display_answer': english
            })
        
        # Section 3: First letter hint
        for english, latvian in words[third*2:]:
            first_letter = latvian[0] if latvian else ""
            blanks = "_" * (len(latvian) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': latvian,
                'display_answer': latvian
            })
    
    else:  # count > 40
        # 40+: 5 sections, 3-4 different question types
        fifth = len(words) // 5
        
        # Section 1: English -> Latvian
        for english, latvian in words[:fifth]:
            questions.append({
                'type': 'eng_to_lav',
                'question': f"Translate to Latvian: '{english}'",
                'answer': latvian,
                'display_answer': latvian
            })
        
        # Section 2: Latvian -> English
        for english, latvian in words[fifth:fifth*2]:
            questions.append({
                'type': 'lav_to_eng',
                'question': f"Translate to English: '{latvian}'",
                'answer': english,
                'display_answer': english
            })
        
        # Section 3: First letter
        for english, latvian in words[fifth*2:fifth*3]:
            first_letter = latvian[0] if latvian else ""
            blanks = "_" * (len(latvian) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': latvian,
                'display_answer': latvian
            })
        
        # Section 4: Last letter
        for english, latvian in words[fifth*3:fifth*4]:
            last_letter = latvian[-1] if latvian else ""
            blanks = "_" * (len(latvian) - 1)
            questions.append({
                'type': 'last_letter',
                'question': f"'{english}' = '{blanks}{last_letter}'",
                'answer': latvian,
                'display_answer': latvian
            })
        
        # Section 5: Letter count hint
        for english, latvian in words[fifth*4:]:
            questions.append({
                'type': 'letter_hint',
                'question': f"'{english}' = ({len(latvian)} letters, starts with {latvian[:2]}...)",
                'answer': latvian,
                'display_answer': latvian
            })
    
    return questions

def create_general_review(lesson_name, words, is_numbers):
    """General review questions after each lesson"""
    review = []
    sample_size = min(20, len(words))
    sampled_words = random.sample(words, sample_size)
    
    for english, latvian in sampled_words:
        if is_numbers:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] '{english}' in Latvian?",
                    'answer': latvian,
                    'display_answer': latvian
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] What number is '{latvian}'?",
                    'answer': english,
                    'display_answer': english
                })
        else:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{english}'",
                    'answer': latvian,
                    'display_answer': latvian
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{latvian}'",
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
║        COMPREHENSIVE LATVIAN TEST SYSTEM                  ║
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
        print(Fore.GREEN + "🎉🎉🎉 EXCELLENT! You're amazing at Latvian! 🎉🎉🎉")
    elif final_percentage >= 70:
        print(Fore.BLUE + "👏👏👏 VERY GOOD! Great performance! 👏👏👏")
    elif final_percentage >= 50:
        print(Fore.YELLOW + "👍👍 GOOD! Keep going and you'll be excellent! 👍👍")
    else:
        print(Fore.RED + "📚📚 Keep studying! You can do it! 📚📚")
    
    print(Fore.GREEN + "\nCongratulations! You completed the entire test! 🎊")

if __name__ == "__main__":
    main()