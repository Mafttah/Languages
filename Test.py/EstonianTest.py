import random
from colorama import Fore, Style, init
import unicodedata

# Colorama'yı başlat
init(autoreset=True)

def normalize_text(text):
    """Türkçe karakterleri ve aksanları normalize et"""
    text = text.lower().strip()
    # Aksanları kaldır
    text = unicodedata.normalize('NFD', text)
    text = ''.join(char for char in text if unicodedata.category(char) != 'Mn')
    return text

# KODUNUZDAN ALINAN TÜM MADDELER - SIRAYLA
lessons_data = {
    "Lesson 1 - Numbers 1-10": {
        "count": 10,
        "words": [
            ("1", "uks"),
            ("2", "kaks"),
            ("3", "kolm"),
            ("4", "neli"),
            ("5", "viis"),
            ("6", "kuus"),
            ("7", "seitse"),
            ("8", "kaheksa"),
            ("9", "uheksa"),
            ("10", "kumme")
        ],
        "is_numbers": True
    },
    
    "Lesson 2 - Greetings": {
        "count": 18,
        "words": [
            ("Hello", "tere"),
            ("How are you?", "kuidas sul laheb"),
            ("Nice to see you", "tore sind naha"),
            ("Nice to meet you", "meeldiv tutvuda"),
            ("See you tomorrow", "naeme homme"),
            ("Good morning", "tere hommikust"),
            ("Good afternoon", "tere paevast"),
            ("Good evening", "tere ohtust"),
            ("Good night", "head ood"),
            ("What is your name?", "mis si nimi on"),
            ("My name is", "minu nimi on"),
            ("Where do you live?", "kus sa elad"),
            ("Where are you from?", "kust sa parit oled"),
            ("Have a nice day", "kena paeva"),
            ("See you later", "naeme hiljem"),
            ("Goodbye", "head aega"),
            ("Please", "palun"),
            ("Thank you", "aitah")
        ],
        "is_numbers": False
    },
    
    "Lesson 3 - Regular Verbs": {
        "count": 45,
        "words": [
            ("to withdraw/shrink", "tombuma"),
            ("to say/tell", "utlema"),
            ("to do/make", "tegema"),
            ("to think", "motlema"),
            ("to present", "esitlema"),
            ("to call (on phone)", "helistama"),
            ("to ask", "kusima"),
            ("to seem", "tunduma"),
            ("to leave (behind)", "jatma"),
            ("to begin/start", "alustama"),
            ("to hallucinate", "viirastuma"),
            ("to help", "aitama"),
            ("to let play", "mangitama"),
            ("to run", "jooksma"),
            ("to move (house)", "kolima"),
            ("to believe", "uskuma"),
            ("to write", "kirjutama"),
            ("to pose", "poseerima"),
            ("to rumble", "porama"),
            ("to continue", "jatkuma"),
            ("to set/place", "seadma"),
            ("to study/learn", "oppima"),
            ("to exchange", "vahetama"),
            ("to tolerate", "talutama"),
            ("to observe", "jalgima"),
            ("to stand (cause)", "seisatama"),
            ("to speak/talk", "raakima"),
            ("to spend (time)", "veetma"),
            ("to teach", "opetama"),
            ("to weigh/consider", "kaalutlema"),
            ("to appear", "ilmuma"),
            ("to buy", "ostma"),
            ("to serve", "servima"),
            ("to send (official)", "lakitama"),
            ("to build", "ehitama"),
            ("to fumble", "pusima"),
            ("to cut", "loikama"),
            ("to sell", "muuma"),
            ("to return", "tagastama"),
            ("to explain", "seletama"),
            ("to develop", "arenema"),
            ("to keep/hold", "hoidma"),
            ("to produce", "tootma"),
            ("to use/consume", "tarvitama"),
            ("to bind/cover", "kaanetama")
        ],
        "is_numbers": False
    },
    
    "Lesson 4 - Adjectives": {
        "count": 35,
        "words": [
            ("Happy", "onnelik"),
            ("Sad", "kurb"),
            ("Angry", "vihane"),
            ("Afraid", "kartlik"),
            ("Joy", "roomus"),
            ("Surprised", "ullatunud"),
            ("Calm", "rahulik"),
            ("Bored", "igav"),
            ("Easy", "lihtne"),
            ("Difficult", "raske"),
            ("Bad", "halb"),
            ("Good", "hea"),
            ("Noisy", "larmakas"),
            ("Quiet", "vaikne"),
            ("Strong", "tugev"),
            ("Weak", "nork"),
            ("Hard", "kova"),
            ("Soft", "pehme"),
            ("More", "rohkem"),
            ("Less", "vahem"),
            ("Clean", "puhas"),
            ("Dirty", "must"),
            ("Old", "vana"),
            ("New", "uus"),
            ("Big", "suur"),
            ("Small", "vaike"),
            ("Young", "noor"),
            ("Skinny", "kohn"),
            ("Fat", "paks"),
            ("Pretty", "ilus"),
            ("Ugly", "inetu"),
            ("Thick", "paks"),
            ("Thin", "ohuke"),
            ("Rough", "kare"),
            ("Smooth", "sile")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.1 - Days": {
        "count": 11,
        "words": [
            ("The days of the week", "nadalapaevad"),
            ("Day", "paev"),
            ("Week", "nadal"),
            ("Monday", "esmispaev"),
            ("Tuesday", "teisipaev"),
            ("Wednesday", "kolmapaev"),
            ("Thursday", "neljapaev"),
            ("Friday", "reede"),
            ("Saturday", "laupaev"),
            ("Sunday", "puhapaev"),
            ("Weekend", "nadalavahetus")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.2 - Months": {
        "count": 15,
        "words": [
            ("The months of the year", "kalendrikuud"),
            ("Month", "kuu"),
            ("Year", "aasta"),
            ("January", "jaanuar"),
            ("February", "veebruar"),
            ("March", "marts"),
            ("April", "aprill"),
            ("May", "mai"),
            ("June", "juuni"),
            ("July", "juuli"),
            ("August", "august"),
            ("September", "september"),
            ("October", "oktoober"),
            ("November", "november"),
            ("December", "detsember")
        ],
        "is_numbers": False
    },
    
    "Lesson 6 - Seasons & Weather": {
        "count": 23,
        "words": [
            ("Seasons", "aastaajad"),
            ("Winter", "talv"),
            ("Summer", "suvi"),
            ("Spring", "kevad"),
            ("Autumn", "sugis"),
            ("Sky", "taevas"),
            ("Cloud", "pilv"),
            ("Rainbow", "vikerkaar"),
            ("Cold", "kulm"),
            ("Hot", "palav"),
            ("It is hot", "on palav"),
            ("It is cold", "on kulm"),
            ("It is sunny", "on paikesepaisteline"),
            ("It is cloudy", "on pilvine"),
            ("It is humid", "on niiske"),
            ("It is raining", "vihma sajab"),
            ("It is snowing", "lund sajab"),
            ("It is windy", "on tuuline"),
            ("How is the weather?", "mis ilm on"),
            ("Good weather", "hea ilm"),
            ("Bad weather", "halb ilm"),
            ("What is the temperature?", "milline temperatuur valjas on"),
            ("It is 24 degrees", "on 24 kraadi")
        ],
        "is_numbers": False
    },
    
    "Lesson 7 - Colors": {
        "count": 14,
        "words": [
            ("Black", "must"),
            ("Blue", "sinine"),
            ("Brown", "pruun"),
            ("Green", "roheline"),
            ("Orange", "oranz"),
            ("Purple", "lilla"),
            ("Red", "punane"),
            ("White", "valge"),
            ("Yellow", "kollane"),
            ("Gray", "hall"),
            ("Gold", "kuldne"),
            ("Silver", "hobedane"),
            ("What color is it?", "mis varvi see on"),
            ("The color is", "varv on")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.1 - Family": {
        "count": 35,
        "words": [
            ("Mother", "ema"),
            ("Father", "isa"),
            ("Brother", "vend"),
            ("Sister", "ode"),
            ("Son", "poeg"),
            ("Daughter", "tutar"),
            ("Parents", "vanemad"),
            ("Children", "lapsed"),
            ("Child", "laps"),
            ("Stepmother", "kasuema"),
            ("Stepfather", "kasuisa"),
            ("Stepsister", "poolode"),
            ("Stepbrother", "poolvend"),
            ("Son-in-law", "vaimees"),
            ("Daughter-in-law", "minia"),
            ("Wife", "naine"),
            ("Husband", "mees"),
            ("Grandparents", "vanavanemad"),
            ("Grandfather", "vanaisa"),
            ("Grandmother", "vanaema"),
            ("Grandson", "lapselaps"),
            ("Granddaughter", "lapselaps"),
            ("Grandchildren", "lapselapsed"),
            ("Grandchild", "lapselaps"),
            ("Aunt", "tadi"),
            ("Uncle", "onu"),
            ("Cousin (female)", "onututar/taditutar"),
            ("Cousin (male)", "onupoeg/tadipoeg"),
            ("Nephew", "vennapoeg"),
            ("Niece", "vennatutar"),
            ("Father-in-law", "ai"),
            ("Mother-in-law", "amm"),
            ("Brother-in-law", "mehevend/naisevend"),
            ("Sister-in-law", "meheode/naiseode"),
            ("Relative", "sugulane")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.2 - Friends": {
        "count": 14,
        "words": [
            ("Miss", "prl"),
            ("Boy", "poiss"),
            ("Girl", "tudruk"),
            ("Baby", "beebi"),
            ("Woman", "naine"),
            ("Man", "mees"),
            ("Friend (male)", "sober"),
            ("Friend (female)", "sobranna"),
            ("Boyfriend", "poiss-sober"),
            ("Girlfriend", "tudruksober"),
            ("Gentleman", "harrasmees"),
            ("Lady", "daam"),
            ("Neighbor (male)", "naaber"),
            ("Neighbor (female)", "naaber")
        ],
        "is_numbers": False
    },
    
    "Lesson 9 - Numbers 11-30": {
        "count": 20,
        "words": [
            ("11", "uksteist"),
            ("12", "kaksteist"),
            ("13", "kolmteist"),
            ("14", "neliteist"),
            ("15", "viisteist"),
            ("16", "kuusteist"),
            ("17", "seitseteist"),
            ("18", "kaheksateist"),
            ("19", "uheksateist"),
            ("20", "kakskümmend"),
            ("21", "kakskümmend uks"),
            ("22", "kakskümmend kaks"),
            ("23", "kakskümmend kolm"),
            ("24", "kakskümmend neli"),
            ("25", "kakskümmend viis"),
            ("26", "kakskümmend kuus"),
            ("27", "kakskümmend seitse"),
            ("28", "kakskümmend kaheksa"),
            ("29", "kakskümmend uheksa"),
            ("30", "kolmkümmend")
        ],
        "is_numbers": True
    },
    
    "Lesson 10.1 - Prepositions": {
        "count": 36,
        "words": [
            ("For", "jaoks"),
            ("From", "alates"),
            ("In", "sisse/sees"),
            ("Inside", "sees"),
            ("Into", "sisse"),
            ("Near", "lahedal"),
            ("Of", "millest"),
            ("Out", "valja"),
            ("Outside", "valjas"),
            ("Under", "all"),
            ("With", "koos"),
            ("Without", "ilma"),
            ("Above", "ulalpool"),
            ("Across", "ule"),
            ("After", "parast"),
            ("Against", "vastu"),
            ("Along", "mooda"),
            ("Around", "umber"),
            ("At", "juures"),
            ("Behind", "taga"),
            ("Below", "allpool"),
            ("Beside", "korval"),
            ("Between", "vahel"),
            ("By", "korval"),
            ("During", "ajal"),
            ("Except", "valja arvatud"),
            ("And", "ja"),
            ("Because", "sest"),
            ("But", "aga"),
            ("Or", "voi"),
            ("Everywhere", "igal pool"),
            ("Everyone", "igauks"),
            ("Everything", "koik"),
            ("Few", "vahe"),
            ("Some", "moni"),
            ("Many", "palju")
        ],
        "is_numbers": False
    },
    
    "Lesson 10.2 - Useful Words": {
        "count": 29,
        "words": [
            ("Question", "kusimus"),
            ("Answer", "vastus"),
            ("Truth", "tode"),
            ("Lie", "vale"),
            ("Nothing", "mitte midagi"),
            ("Something", "midagi"),
            ("Same", "sama"),
            ("Different", "erinev"),
            ("Pull", "tomba"),
            ("Push", "lukka"),
            ("Long", "pikk"),
            ("Short", "luhike"),
            ("Cold", "kulm"),
            ("Hot", "kuum"),
            ("Light", "hele"),
            ("Dark", "tume"),
            ("Wet", "marg"),
            ("Dry", "kuiv"),
            ("Empty", "tuhi"),
            ("Full", "tais"),
            ("How?", "kuidas"),
            ("What?", "mida"),
            ("When?", "millal"),
            ("Where?", "kuhu"),
            ("Which?", "milline"),
            ("Who?", "kes"),
            ("Why?", "miks"),
            ("How long?", "kui kaua"),
            ("How much?", "kui palju")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.1 - Drinks": {
        "count": 9,
        "words": [
            ("Coffee", "kohv"),
            ("Tea", "tee"),
            ("Soft drink", "karastusjook"),
            ("Water", "vesi"),
            ("Lemonade", "limonaad"),
            ("Juice", "mahl"),
            ("Orange juice", "apelsinimahl"),
            ("I would like a glass of water please", "palun mulle klaas vett"),
            ("With ice", "jaaga")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.2 - Dairy Products": {
        "count": 19,
        "words": [
            ("Milk", "piim"),
            ("Ice cream", "jaatis"),
            ("Butter", "voi"),
            ("Cheese", "juust"),
            ("Cottage cheese", "kodujuust"),
            ("Cream", "koor"),
            ("Sour cream", "hapukoor"),
            ("Yogurt", "jogurt"),
            ("Eggs", "munad"),
            ("Whipping cream", "vahukoor"),
            ("Bakery", "pagaritooted"),
            ("Baguette", "pikk sai"),
            ("Doughnut", "soorik"),
            ("Cookie", "kupsis"),
            ("Roll", "kukkel"),
            ("Dessert", "magustoit"),
            ("Cake", "kook"),
            ("Bread", "leib"),
            ("Pie", "pirukas")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.3 - Meats": {
        "count": 13,
        "words": [
            ("Beef", "veiseliha"),
            ("Veal", "vasikaliha"),
            ("Ham", "sink"),
            ("Chicken", "kanaliha"),
            ("Turkey", "kalkun"),
            ("Duck", "part"),
            ("Bacon", "peekon"),
            ("Pork", "sealiha"),
            ("Filet mignon", "sisefilee"),
            ("Sausage", "vorst"),
            ("Lamb chop", "tallekarree"),
            ("Pork chop", "seakarbonaad"),
            ("Meat", "liha")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.4 - Seafoods": {
        "count": 20,
        "words": [
            ("Fish", "kala"),
            ("Shellfish", "koorikloomad"),
            ("Bass", "ahven"),
            ("Salmon", "lohe"),
            ("Lobster", "vahk"),
            ("Crab", "krabi"),
            ("Mussel", "rannakarp"),
            ("Oyster", "auster"),
            ("Cod", "tursk"),
            ("Clam", "merikarp"),
            ("Shrimp", "krevett"),
            ("Tuna", "tuun"),
            ("Trout", "forell"),
            ("Sole", "lest"),
            ("Shark", "hai"),
            ("Carp", "karpkala"),
            ("Tilapia", "tilapia"),
            ("Eel", "angerjas"),
            ("Catfish", "saga"),
            ("Swordfish", "mookkala")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.5 - Herbs & Spices": {
        "count": 17,
        "words": [
            ("Salt", "sool"),
            ("Pepper", "pipar"),
            ("Caraway", "koomen"),
            ("Garlic", "kuuslauk"),
            ("Basil", "basiilik"),
            ("Coriander", "koriander"),
            ("Fennel", "apteegitill"),
            ("Marjoram", "majoraan"),
            ("Oregano", "oregano"),
            ("Parsley", "petersell"),
            ("Rosemary", "rosmariin"),
            ("Sage", "salvei"),
            ("Thyme", "tuumian"),
            ("Nutmeg", "muskaatpahkel"),
            ("Paprika", "paprika"),
            ("Cayenne", "cayenne"),
            ("Ginger", "ingver")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.6 - Vegetables": {
        "count": 28,
        "words": [
            ("Celery", "seller"),
            ("Eggplant", "baklažaan"),
            ("Zucchini", "suvikorvits"),
            ("Onion", "sibul"),
            ("Spinach", "spinat"),
            ("Salad", "salat"),
            ("Green beans", "rohelised oad"),
            ("Cucumber", "kurk"),
            ("Radish", "redis"),
            ("Cabbage", "kapsas"),
            ("Mushrooms", "seened"),
            ("Lettuce", "lehtsalat"),
            ("Corn", "mais"),
            ("Potatoes", "kartul"),
            ("Tomato", "tomat"),
            ("Carrot", "porgand"),
            ("Plantain", "jahubanaanid"),
            ("Beans", "oad"),
            ("Leek", "porrulauk"),
            ("Lotus root", "lootosejuur"),
            ("Bamboo shoot", "bambusevorsed"),
            ("Artichoke", "artisokk"),
            ("Asparagus", "spargel"),
            ("Brussels sprouts", "rooskapsas"),
            ("Broccoli", "brokkoli"),
            ("Peas", "herned"),
            ("Cauliflower", "lillkapsas"),
            ("Chili pepper", "tsillipipar")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.7 - Fruits": {
        "count": 27,
        "words": [
            ("Cherries", "kirsid"),
            ("Raspberries", "vaarikad"),
            ("Blueberries", "mustikad"),
            ("Strawberries", "maasikad"),
            ("Lemon", "sidrun"),
            ("Lime", "laim"),
            ("Apple", "oun"),
            ("Orange", "apelsin"),
            ("Pear", "pirn"),
            ("Banana", "banaan"),
            ("Grapes", "viinamarjad"),
            ("Grapefruit", "greip"),
            ("Watermelon", "arbuus"),
            ("Pineapple", "ananass"),
            ("Plum", "ploom"),
            ("Peach", "virsik"),
            ("Mango", "mango"),
            ("Apricot", "aprikoos"),
            ("Pomegranate", "granaatoün"),
            ("Persimmon", "hurmaa"),
            ("Kiwi", "kiivi"),
            ("Litchi", "litsi"),
            ("Longan", "longan"),
            ("Balsam pear", "karella-kibekurk"),
            ("Passion fruit", "granadill"),
            ("Avocado", "avokaado"),
            ("Coconut", "kookospahkel")
        ],
        "is_numbers": False
    },
    
    "Lesson 12 - Irregular Verbs": {
        "count": 52,
        "words": [
            ("to be", "olema"),
            ("to have", "omama"),
            ("to go", "minema"),
            ("to come", "tulema"),
            ("to do/make", "tegema"),
            ("to put", "panema"),
            ("to take", "votma"),
            ("to drive", "soitma"),
            ("to stay", "jaama"),
            ("to see", "nagema"),
            ("to eat", "sooma"),
            ("to drink", "jooma"),
            ("to say", "utlema"),
            ("to give", "andma"),
            ("to get/become", "saama"),
            ("to bring", "tooma"),
            ("to carry", "viima"),
            ("to find", "leidma"),
            ("to wash", "pesema"),
            ("to read", "lugema"),
            ("to sleep", "magama"),
            ("to close", "sulgema"),
            ("to wear/carry", "kandma"),
            ("to stand", "seisma"),
            ("to sit", "istuma"),
            ("to run", "jooksma"),
            ("to die", "surema"),
            ("to wake up", "arkama"),
            ("to learn", "oppima"),
            ("to live", "elama"),
            ("to love", "armastama"),
            ("to believe", "uskuma"),
            ("to hear", "kuulma"),
            ("to feel/know", "tundma"),
            ("to melt", "sulatama"),
            ("to rise", "tousma"),
            ("to lose", "kaotama"),
            ("to fight", "voitlema"),
            ("to search", "otsima"),
            ("to start", "alustama"),
            ("to cover", "katma"),
            ("to sing", "laulma"),
            ("to forget", "unustama"),
            ("to forgive", "andeks andma"),
            ("to create", "looma"),
            ("can/may", "voima"),
            ("to escape", "pogenema"),
            ("to send", "saatma"),
            ("to fall", "langema"),
            ("to decide", "otsustama"),
            ("to open", "avama"),
            ("to play", "mangima")
        ],
        "is_numbers": False
    },
    
    "Lesson 14 - Numbers 31-50": {
        "count": 20,
        "words": [
            ("31", "kolmkümmend uks"),
            ("32", "kolmkümmend kaks"),
            ("33", "kolmkümmend kolm"),
            ("34", "kolmkümmend neli"),
            ("35", "kolmkümmend viis"),
            ("36", "kolmkümmend kuus"),
            ("37", "kolmkümmend seitse"),
            ("38", "kolmkümmend kaheksa"),
            ("39", "kolmkümmend uheksa"),
            ("40", "nelikümmend"),
            ("41", "nelikümmend uks"),
            ("42", "nelikümmend kaks"),
            ("43", "nelikümmend kolm"),
            ("44", "nelikümmend neli"),
            ("45", "nelikümmend viis"),
            ("46", "nelikümmend kuus"),
            ("47", "nelikümmend seitse"),
            ("48", "nelikümmend kaheksa"),
            ("49", "nelikümmend uheksa"),
            ("50", "viiskümmend")
        ],
        "is_numbers": True
    },
    
    "Lesson 15 - Physical Appearance": {
        "count": 38,
        "words": [
            ("Tall", "pikk"),
            ("Short (height)", "luhike"),
            ("Slim", "sale"),
            ("Fat", "paks"),
            ("Muscular", "lihaseline"),
            ("Blonde", "blond"),
            ("Brown-haired", "pruunide juustega"),
            ("Black-haired", "mustade juustega"),
            ("Curly hair", "lokkis juuksed"),
            ("Straight hair", "sirged juuksed"),
            ("Blue eyes", "sinised silmad"),
            ("Brown eyes", "pruunid silmad"),
            ("Green eyes", "rohelised silmad"),
            ("Beautiful", "ilus"),
            ("Handsome", "nagus"),
            ("Ugly", "kole"),
            ("Young", "noor"),
            ("Old", "vana"),
            ("Beard", "habe"),
            ("Light-skinned", "hele nahk"),
            ("Dark-skinned", "tume nahk"),
            ("Freckles", "tedretahnid"),
            ("Wrinkles", "kortsud"),
            ("Bald", "kiilakas"),
            ("Hairy (body)", "karvane"),
            ("Straight nose", "sirge nina"),
            ("Big nose", "suur nina"),
            ("Small nose", "vaike nina"),
            ("Thin lips", "ohukesed huuled"),
            ("Full lips", "taidlased huuled"),
            ("Broad shoulders", "laiad olad"),
            ("Narrow shoulders", "kitsad olad"),
            ("Tanned skin", "paevitunud nahk"),
            ("Pale skin", "kahvatu nahk"),
            ("Wavy hair", "lainelised juuksed"),
            ("Ponytail", "hobusesaba"),
            ("Braids", "patsid"),
            ("Beard and mustache", "habe ja vuntsid")
        ],
        "is_numbers": False
    },
    
    "Lesson 16 - Occupations": {
        "count": 25,
        "words": [
            ("Doctor", "arst"),
            ("Teacher", "opetaja"),
            ("Engineer", "insener"),
            ("Lawyer", "jurist"),
            ("Salesperson", "muuja"),
            ("Police officer", "politseinik"),
            ("Firefighter", "tuletorjuja"),
            ("Programmer", "programmeerija"),
            ("Cook/Chef", "kokk"),
            ("Journalist", "ajakirjanik"),
            ("Nurse", "ode"),
            ("Architect", "arhitekt"),
            ("Accountant", "raamatupidaja"),
            ("Pharmacist", "apteeker"),
            ("Driver", "autojuht"),
            ("Mechanic", "mehaanik"),
            ("Scientist", "teadlane"),
            ("Dentist", "hambaarst"),
            ("Musician", "muusik"),
            ("Actor", "naitleja"),
            ("Artist", "kunstnik"),
            ("Pilot", "piloot"),
            ("Farmer", "talunik"),
            ("Photographer", "fotograaf"),
            ("Waiter/Waitress", "ettekandja")
        ],
        "is_numbers": False
    },
    
    "Lesson 17 - Sports": {
        "count": 30,
        "words": [
            ("Football/Soccer", "jalgpall"),
            ("Basketball", "korvpall"),
            ("Volleyball", "vorkpall"),
            ("Tennis", "tennis"),
            ("Swimming", "ujumine"),
            ("Running/Athletics", "jooksmine/kergejoustik"),
            ("Ice hockey", "jaahoki"),
            ("Skiing", "suusatamine"),
            ("Cycling", "jalgrattasoit"),
            ("Boxing", "poks"),
            ("Martial arts", "voitluskunst"),
            ("Golf", "golf"),
            ("Table tennis", "lauatennis"),
            ("Wrestling", "maadlus"),
            ("Handball", "kasipall"),
            ("Baseball", "pesapall"),
            ("Surfing", "lainelauasoit"),
            ("Skating", "uisutamine"),
            ("Horse riding", "ratsutamine"),
            ("Diving", "sukeldumine"),
            ("Cricket", "kriket"),
            ("Rugby", "ragbi"),
            ("Ballet", "ballett"),
            ("Bowling", "keegel"),
            ("Weightlifting", "tostmine"),
            ("Windsurfing", "purjelauasoit"),
            ("Ice skating", "uisutamine"),
            ("Rowing", "soudmine"),
            ("Archery", "vibulaskmine"),
            ("Climbing", "ronimine")
        ],
        "is_numbers": False
    },
    
    "Lesson 18 - Numbers 51-75": {
        "count": 25,
        "words": [
            ("51", "viiskümmend uks"),
            ("52", "viiskümmend kaks"),
            ("53", "viiskümmend kolm"),
            ("54", "viiskümmend neli"),
            ("55", "viiskümmend viis"),
            ("56", "viiskümmend kuus"),
            ("57", "viiskümmend seitse"),
            ("58", "viiskümmend kaheksa"),
            ("59", "viiskümmend uheksa"),
            ("60", "kuuskümmend"),
            ("61", "kuuskümmend uks"),
            ("62", "kuuskümmend kaks"),
            ("63", "kuuskümmend kolm"),
            ("64", "kuuskümmend neli"),
            ("65", "kuuskümmend viis"),
            ("66", "kuuskümmend kuus"),
            ("67", "kuuskümmend seitse"),
            ("68", "kuuskümmend kaheksa"),
            ("69", "kuuskümmend uheksa"),
            ("70", "seitsekümmend"),
            ("71", "seitsekümmend uks"),
            ("72", "seitsekümmend kaks"),
            ("73", "seitsekümmend kolm"),
            ("74", "seitsekümmend neli"),
            ("75", "seitsekümmend viis")
        ],
        "is_numbers": True
    },
    
    "Lesson 19 - Clothing": {
        "count": 42,
        "words": [
            ("Shirt", "sark"),
            ("T-shirt", "t-sark"),
            ("Blouse", "pluus"),
            ("Sweater", "kampsun"),
            ("Jacket", "jakk"),
            ("Coat", "mantel"),
            ("Dress", "kleit"),
            ("Skirt", "seelik"),
            ("Pants", "puksid"),
            ("Shorts", "luhikesed puksid"),
            ("Shoes", "kingad"),
            ("Boots", "saapad"),
            ("Sneakers", "tossud"),
            ("Sandals", "sandaalid"),
            ("Hat/Cap", "muts"),
            ("Scarf", "sall"),
            ("Gloves", "kindad"),
            ("Belt", "voo"),
            ("Socks", "sokid"),
            ("Winter coat", "talvemantel"),
            ("Wool hat", "villane muts"),
            ("Snow boots", "lumesaapad"),
            ("Swimsuit", "ujumisriided"),
            ("Sunglasses", "paikeseprillid"),
            ("Flip-flops", "platud"),
            ("Tank top", "top"),
            ("Suit", "ulikond"),
            ("Tie", "lips"),
            ("Blazer", "bleiser"),
            ("High heels", "kontsaga kingad"),
            ("Evening dress", "ohtukleit"),
            ("Black", "must"),
            ("White", "valge"),
            ("Red", "punane"),
            ("Blue", "sinine"),
            ("Green", "roheline"),
            ("Cotton", "puuvill"),
            ("Wool", "vill"),
            ("Leather", "nahk"),
            ("Silk", "siid"),
            ("Linen", "linane")
        ],
        "is_numbers": False
    },
    
    "Lesson 20 - Adverbs": {
        "count": 20,
        "words": [
            ("Quickly", "kiiresti"),
            ("Slowly", "aeglaselt"),
            ("Always", "alati"),
            ("Never", "mitte kunagi"),
            ("Often", "sageli"),
            ("Sometimes", "monikord"),
            ("Rarely", "harva"),
            ("Already", "juba"),
            ("Still", "ikka"),
            ("Yet", "veel"),
            ("Soon", "varsti"),
            ("Now", "nuud"),
            ("Later", "hiljem"),
            ("Today", "tana"),
            ("Tomorrow", "homme"),
            ("Yesterday", "eile"),
            ("Clearly", "selgelt"),
            ("Together", "koos"),
            ("Apart", "lahku"),
            ("Forever", "igavesti")
        ],
        "is_numbers": False
    },
    
    "Lesson 21 - Animals": {
        "count": 20,
        "words": [
            ("Dog", "koer"),
            ("Cat", "kass"),
            ("Horse", "hobune"),
            ("Cow", "lehm"),
            ("Sheep", "lammas"),
            ("Pig", "siga"),
            ("Goat", "kits"),
            ("Chicken", "kana"),
            ("Duck", "part"),
            ("Bird", "lind"),
            ("Rabbit", "janes"),
            ("Mouse", "hiir"),
            ("Lion", "lovi"),
            ("Tiger", "tiiger"),
            ("Bear", "karu"),
            ("Elephant", "elevant"),
            ("Monkey", "ahv"),
            ("Fox", "rebane"),
            ("Wolf", "hunt"),
            ("Deer", "hirv")
        ],
        "is_numbers": False
    },
    
    "Lesson 23 - Places in Town": {
        "count": 20,
        "words": [
            ("School", "kool"),
            ("Hospital", "haigla"),
            ("Bank", "pank"),
            ("Restaurant", "restoran"),
            ("Library", "raamatukogu"),
            ("Supermarket", "supermarket"),
            ("Cinema", "kino"),
            ("Post office", "postkontor"),
            ("Police station", "politseijaoskond"),
            ("Park", "park"),
            ("Museum", "muuseum"),
            ("Theatre", "teater"),
            ("Hotel", "hotell"),
            ("Stadium", "staadion"),
            ("Church", "kirik"),
            ("Pharmacy", "apteek"),
            ("Bakery", "pagariäri"),
            ("Butcher", "lihunik"),
            ("Market", "turg"),
            ("Hairdresser", "juuksur")
        ],
        "is_numbers": False
    },
    
    "Lesson 24 - School Supplies": {
        "count": 20,
        "words": [
            ("Book", "raamat"),
            ("Pen", "pliiats"),
            ("Pencil", "harilik pliiats"),
            ("Eraser", "kustutuskumm"),
            ("Notebook", "markmik"),
            ("Ruler", "joonlaud"),
            ("Scissors", "kaarid"),
            ("Backpack", "seljakott"),
            ("Folder", "kaust"),
            ("Calculator", "kalkulaator"),
            ("Marker", "marker"),
            ("Chalk", "kriit"),
            ("Map", "kaart"),
            ("Highlighter", "marker"),
            ("Projector", "projektor"),
            ("Laptop", "sulearvuti"),
            ("Printer", "printer"),
            ("USB stick", "usb-malupulk"),
            ("Schoolbag", "koolikott"),
            ("Sharpener", "teritaja")
        ],
        "is_numbers": False
    },
    
    "Lesson 25 - Transportation": {
        "count": 20,
        "words": [
            ("Car", "auto"),
            ("Bus", "buss"),
            ("Train", "rong"),
            ("Bicycle", "jalgratas"),
            ("Motorcycle", "mootorratas"),
            ("Airplane", "lennuk"),
            ("Boat", "paat"),
            ("Tram", "tramm"),
            ("Taxi", "takso"),
            ("Subway", "metroo"),
            ("Ferry", "parvlaev"),
            ("Yacht", "jaht"),
            ("Hot air balloon", "kuumaohupall"),
            ("Spaceship", "kosmoselaev"),
            ("Rickshaw", "riksa"),
            ("Gondola", "gondel"),
            ("Zeppelin", "tsepeliin"),
            ("Rollerblades", "rulluisud"),
            ("Canoe", "kanuu"),
            ("Submarine", "allveelaev")
        ],
        "is_numbers": False
    }
}

def generate_questions(lesson_name, words, count, is_numbers):
    """Madde sayısına göre farklı soru tarzları oluştur"""
    questions = []
    
    if is_numbers:
        # Sayı dersleri için özel soru tarzları
        # Tarz 1: Sayıdan kelimeye (Cevap: KELIME)
        for english, estonian in words:
            questions.append({
                'type': 'num_to_word',
                'question': f"What is '{english}' in Estonian? (Answer with the WORD)",
                'answer': estonian,
                'display_answer': estonian  # KELIME göster
            })
        
        # Tarz 2: Kelimeden sayıya (Cevap: SAYI)
        for english, estonian in words:
            questions.append({
                'type': 'word_to_num',
                'question': f"What number is '{estonian}'? (Answer with the NUMBER)",
                'answer': english,
                'display_answer': english  # SAYI göster
            })
        
        # Tarz 3: Karışık (Cevap türüne göre)
        for english, estonian in words:
            if random.choice([True, False]):
                # Sayıdan kelimeye
                questions.append({
                    'type': 'mixed',
                    'question': f"Translate '{english}' to Estonian word:",
                    'answer': estonian,
                    'display_answer': estonian  # KELIME
                })
            else:
                # Kelimeden sayıya
                questions.append({
                    'type': 'mixed',
                    'question': f"What number is '{estonian}'?",
                    'answer': english,
                    'display_answer': english  # SAYI
                })
    
    elif count <= 20:
        # 20 ve altı: 3 farklı soru tarzı
        # Tarz 1: English -> Estonian
        for english, estonian in words:
            questions.append({
                'type': 'eng_to_est',
                'question': f"Translate to Estonian: '{english}'",
                'answer': estonian,
                'display_answer': estonian
            })
        
        # Tarz 2: Estonian -> English
        for english, estonian in words:
            questions.append({
                'type': 'est_to_eng',
                'question': f"Translate to English: '{estonian}'",
                'answer': english,
                'display_answer': english
            })
        
        # Tarz 3: İlk harf ipucu
        for english, estonian in words:
            first_letter = estonian[0] if estonian else ""
            blanks = "_" * (len(estonian) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}' - Complete the Estonian word",
                'answer': estonian,
                'display_answer': estonian
            })
    
    elif 20 < count <= 40:
        # 20-40 arası: 3 bölüm, 2 farklı soru tarzı
        third = len(words) // 3
        
        # Bölüm 1: English -> Estonian
        for english, estonian in words[:third]:
            questions.append({
                'type': 'eng_to_est',
                'question': f"Translate to Estonian: '{english}'",
                'answer': estonian,
                'display_answer': estonian
            })
        
        # Bölüm 2: Estonian -> English
        for english, estonian in words[third:third*2]:
            questions.append({
                'type': 'est_to_eng',
                'question': f"Translate to English: '{estonian}'",
                'answer': english,
                'display_answer': english
            })
        
        # Bölüm 3: İlk harf ipucu
        for english, estonian in words[third*2:]:
            first_letter = estonian[0] if estonian else ""
            blanks = "_" * (len(estonian) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': estonian,
                'display_answer': estonian
            })
    
    else:  # count > 40
        # 40+ : 5 bölüm, 3-4 farklı soru tarzı
        fifth = len(words) // 5
        
        # Bölüm 1: English -> Estonian
        for english, estonian in words[:fifth]:
            questions.append({
                'type': 'eng_to_est',
                'question': f"Translate to Estonian: '{english}'",
                'answer': estonian,
                'display_answer': estonian
            })
        
        # Bölüm 2: Estonian -> English
        for english, estonian in words[fifth:fifth*2]:
            questions.append({
                'type': 'est_to_eng',
                'question': f"Translate to English: '{estonian}'",
                'answer': english,
                'display_answer': english
            })
        
        # Bölüm 3: İlk harf
        for english, estonian in words[fifth*2:fifth*3]:
            first_letter = estonian[0] if estonian else ""
            blanks = "_" * (len(estonian) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': estonian,
                'display_answer': estonian
            })
        
        # Bölüm 4: Son harf
        for english, estonian in words[fifth*3:fifth*4]:
            last_letter = estonian[-1] if estonian else ""
            blanks = "_" * (len(estonian) - 1)
            questions.append({
                'type': 'last_letter',
                'question': f"'{english}' = '{blanks}{last_letter}'",
                'answer': estonian,
                'display_answer': estonian
            })
        
        # Bölüm 5: Harf sayısı ipucu
        for english, estonian in words[fifth*4:]:
            questions.append({
                'type': 'letter_hint',
                'question': f"'{english}' = ({len(estonian)} letters, starts with {estonian[:2]}...)",
                'answer': estonian,
                'display_answer': estonian
            })
    
    return questions

def create_general_review(lesson_name, words, is_numbers):
    """Her bölümün sonunda genel tekrar soruları"""
    review = []
    sample_size = min(20, len(words))
    sampled_words = random.sample(words, sample_size)
    
    for english, estonian in sampled_words:
        if is_numbers:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] '{english}' in Estonian?",
                    'answer': estonian,
                    'display_answer': estonian
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] What number is '{estonian}'?",
                    'answer': english,
                    'display_answer': english
                })
        else:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{english}'",
                    'answer': estonian,
                    'display_answer': estonian
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{estonian}'",
                    'answer': english,
                    'display_answer': english
                })
    
    return review

def run_test(lesson_name):
    """Bir dersin testini çalıştır"""
    lesson_data = lessons_data[lesson_name]
    words = lesson_data['words']
    count = lesson_data['count']
    is_numbers = lesson_data['is_numbers']
    
    print(Fore.CYAN + f"\n{'='*60}")
    print(Fore.YELLOW + f"{lesson_name} - Total {count} Items")
    print(Fore.CYAN + f"{'='*60}\n")
    
    # Soruları oluştur
    questions = generate_questions(lesson_name, words, count, is_numbers)
    
    # Soruları karıştır
    random.shuffle(questions)
    
    correct = 0
    total = len(questions)
    
    # Soruları sor
    for i, q in enumerate(questions, 1):
        print(Fore.WHITE + f"\nQuestion {i}/{total}:")
        print(Fore.CYAN + q['question'])
        
        user_answer = input(Fore.GREEN + "Your answer: ").strip()
        
        if normalize_text(user_answer) == normalize_text(q['answer']):
            print(Fore.GREEN + "✓ Correct!")
            correct += 1
        else:
            print(Fore.RED + f"✗ Wrong! Correct answer: {q['display_answer']}")
    
    # Genel Tekrar Bölümü
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
    
    # Sonuçlar
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
    """Ana program - Tüm dersleri otomatik olarak sırayla çalıştır"""
    print(Fore.CYAN + """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        COMPREHENSIVE ESTONIAN TEST SYSTEM                 ║
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
    
    # Tüm dersleri sırayla çalıştır
    for lesson_num, lesson in enumerate(lessons, 1):
        print(Fore.MAGENTA + f"\n\n{'#'*60}")
        print(Fore.YELLOW + f"LESSON {lesson_num}/{len(lessons)}")
        print(Fore.MAGENTA + f"{'#'*60}")
        
        correct, total = run_test(lesson)
        total_correct += correct
        total_questions += total
        
        if lesson_num < len(lessons):
            input(Fore.YELLOW + "\n\nPress Enter to continue to the next lesson...")
    
    # Genel final sonuçları
    print(Fore.MAGENTA + f"\n\n{'='*60}")
    print(Fore.YELLOW + "ALL LESSONS COMPLETED!")
    print(Fore.YELLOW + "FINAL RESULTS")
    print(Fore.MAGENTA + f"{'='*60}")
    
    final_percentage = (total_correct / total_questions) * 100
    
    print(Fore.CYAN + f"\nTotal Lessons: {len(lessons)}")
    print(Fore.CYAN + f"Total Score: {total_correct}/{total_questions}")
    print(Fore.CYAN + f"Success Rate: {final_percentage:.1f}%\n")
    
    if final_percentage >= 90:
        print(Fore.GREEN + "🎉🎉🎉 EXCELLENT! You're amazing at Estonian! 🎉🎉🎉")
    elif final_percentage >= 70:
        print(Fore.BLUE + "👏👏👏 VERY GOOD! Great performance! 👏👏👏")
    elif final_percentage >= 50:
        print(Fore.YELLOW + "👍👍 GOOD! Keep going and you'll be excellent! 👍👍")
    else:
        print(Fore.RED + "📚📚 Keep studying! You can do it! 📚📚")
    
    print(Fore.GREEN + "\nCongratulations! You completed the entire test! 🎊")

if __name__ == "__main__":
    main()