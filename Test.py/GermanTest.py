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
            ("1", "eins"),
            ("2", "zwei"),
            ("3", "drei"),
            ("4", "vier"),
            ("5", "fünf"),
            ("6", "sechs"),
            ("7", "sieben"),
            ("8", "acht"),
            ("9", "neun"),
            ("10", "zehn")
        ],
        "is_numbers": True
    },
    
    "Lesson 2 - Greetings": {
        "count": 18,
        "words": [
            ("Hello", "hallo"),
            ("How are you?", "wie geht es ihnen"),
            ("Nice to meet you", "freut mich sie kennen zu lernen"),
            ("See you tomorrow", "bis morgen"),
            ("Good morning", "guten morgen"),
            ("Good afternoon", "guten nachmittag"),
            ("Good evening", "guten abend"),
            ("Good night", "gute nacht"),
            ("What is your name?", "wie heissen sie"),
            ("My name is", "mein name ist"),
            ("Where do you live?", "wo wohnst du"),
            ("Where are you from?", "woher kommen sie"),
            ("Nice to see you", "freut mich sie zu sehen"),
            ("Have a nice day", "ich wunsche ihnen einen schonen tag"),
            ("See you later", "bis spater"),
            ("Goodbye", "auf wiedersehen"),
            ("Please", "bitte"),
            ("Thank you", "danke")
        ],
        "is_numbers": False
    },
    
    "Lesson 3 - Regular Verbs": {
        "count": 21,
        "words": [
            ("to work", "arbeiten"),
            ("to learn", "lernen"),
            ("to live", "leben"),
            ("to play", "spielen"),
            ("to ask", "fragen"),
            ("to do/make", "machen"),
            ("to say", "sagen"),
            ("to buy", "kaufen"),
            ("to hear/listen", "horen"),
            ("to live (reside)", "wohnen"),
            ("to love", "lieben"),
            ("to talk", "reden"),
            ("to open", "offnen"),
            ("to wait", "warten"),
            ("to show", "zeigen"),
            ("to need", "brauchen"),
            ("to dance", "tanzen"),
            ("to believe", "glauben"),
            ("to travel", "reisen")
        ],
        "is_numbers": False
    },
    
    "Lesson 4 - Adjectives": {
        "count": 35,
        "words": [
            ("Happy", "glucklich"),
            ("Sad", "traurig"),
            ("Angry", "wutend"),
            ("Afraid", "angst"),
            ("Joy", "freude"),
            ("Surprised", "uberrascht"),
            ("Calm", "ruhig"),
            ("Bored", "gelangweilt"),
            ("Easy", "leicht"),
            ("Difficult", "schwer"),
            ("Bad", "schlecht"),
            ("Good", "gut"),
            ("Noisy", "laut"),
            ("Quiet", "leise"),
            ("Strong", "stark"),
            ("Weak", "schwach"),
            ("Hard", "hart"),
            ("Soft", "weich"),
            ("More", "mehr"),
            ("Less", "weniger"),
            ("Clean", "sauber"),
            ("Dirty", "schmutzig"),
            ("Old", "alt"),
            ("New", "neu"),
            ("Big", "groß"),
            ("Small", "klein"),
            ("Young", "jung"),
            ("Skinny", "dunn"),
            ("Fat", "dick"),
            ("Pretty", "hubsch"),
            ("Ugly", "hasslich"),
            ("Thick", "dick"),
            ("Thin", "dunn"),
            ("Rough", "rau"),
            ("Smooth", "glatt")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.1 - Days": {
        "count": 10,
        "words": [
            ("The days of the week", "die wochentage"),
            ("Day", "tag"),
            ("Week", "woche"),
            ("Monday", "montag"),
            ("Tuesday", "dienstag"),
            ("Wednesday", "mittwoch"),
            ("Thursday", "donnerstag"),
            ("Friday", "freitag"),
            ("Saturday", "samstag"),
            ("Sunday", "sonntag"),
            ("Weekend", "wochenende")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.2 - Months": {
        "count": 15,
        "words": [
            ("The months of the year", "die monate des jahres"),
            ("Month", "monat"),
            ("Year", "jahr"),
            ("January", "januar"),
            ("February", "februar"),
            ("March", "marz"),
            ("April", "april"),
            ("May", "mai"),
            ("June", "juni"),
            ("July", "juli"),
            ("August", "august"),
            ("September", "september"),
            ("October", "oktober"),
            ("November", "november"),
            ("December", "dezember")
        ],
        "is_numbers": False
    },
    
    "Lesson 6 - Seasons & Weather": {
        "count": 23,
        "words": [
            ("Seasons", "jahreszeiten"),
            ("Winter", "winter"),
            ("Summer", "sommer"),
            ("Spring", "fruhling"),
            ("Autumn", "herbst"),
            ("Sky", "himmel"),
            ("Cloud", "wolke"),
            ("Rainbow", "regenbogen"),
            ("Cold", "kalt"),
            ("Hot", "heiß"),
            ("It is hot", "es ist heiß"),
            ("It is cold", "es ist kalt"),
            ("It is sunny", "es ist sonnig"),
            ("It is cloudy", "es ist bewolkt"),
            ("It is humid", "es ist schwul"),
            ("It is raining", "es regnet"),
            ("It is snowing", "es schneit"),
            ("It is windy", "es ist windig"),
            ("How is the weather?", "wie ist das wetter"),
            ("Good weather", "gutes wetter"),
            ("Bad weather", "schlechtes wetter"),
            ("What is the temperature?", "wie viel grad ist es"),
            ("It is 24 degrees", "es ist vierundzwanzig grad")
        ],
        "is_numbers": False
    },
    
    "Lesson 7 - Colors": {
        "count": 14,
        "words": [
            ("Black", "schwarz"),
            ("Blue", "blau"),
            ("Brown", "braun"),
            ("Green", "grun"),
            ("Orange", "orange"),
            ("Purple", "lila"),
            ("Red", "rot"),
            ("White", "weiß"),
            ("Yellow", "gelb"),
            ("Gray", "grau"),
            ("Gold", "gold"),
            ("Silver", "silber"),
            ("What color is it?", "welche farbe ist das"),
            ("The color is", "das ist")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.1 - Family": {
        "count": 35,
        "words": [
            ("Mother", "mutter"),
            ("Father", "vater"),
            ("Brother", "bruder"),
            ("Sister", "schwester"),
            ("Son", "sohn"),
            ("Daughter", "tochter"),
            ("Parents", "eltern"),
            ("Children", "kinder"),
            ("Child", "kind"),
            ("Stepmother", "stiefmutter"),
            ("Stepfather", "stiefvater"),
            ("Stepsister", "stiefschwester"),
            ("Stepbrother", "stiefbruder"),
            ("Son-in-law", "schwiegersohn"),
            ("Daughter-in-law", "schwiegertochter"),
            ("Wife", "ehefrau"),
            ("Husband", "ehemann"),
            ("Grandparents", "großeltern"),
            ("Grandfather", "opa"),
            ("Grandmother", "oma"),
            ("Grandson", "enkel"),
            ("Granddaughter", "enkelin"),
            ("Grandchildren", "enkelkinder"),
            ("Grandchild", "enkelkind"),
            ("Aunt", "tante"),
            ("Uncle", "onkel"),
            ("Cousin (female)", "cousine"),
            ("Cousin (male)", "cousin"),
            ("Nephew", "neffe"),
            ("Niece", "nichte"),
            ("Father-in-law", "schwiegervater"),
            ("Mother-in-law", "schwiegermutter"),
            ("Brother-in-law", "schwager"),
            ("Sister-in-law", "schwagerin"),
            ("Relative", "verwandter")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.2 - Friends": {
        "count": 14,
        "words": [
            ("Miss", "fraulein"),
            ("Boy", "junge"),
            ("Girl", "madchen"),
            ("Baby", "baby"),
            ("Woman", "frau"),
            ("Man", "mann"),
            ("Friend (male)", "freund"),
            ("Friend (female)", "freundin"),
            ("Boyfriend", "freund"),
            ("Girlfriend", "freundin"),
            ("Gentleman", "gentleman"),
            ("Lady", "dame"),
            ("Neighbor (male)", "nachbar"),
            ("Neighbor (female)", "nachbarin")
        ],
        "is_numbers": False
    },
    
    "Lesson 9 - Numbers 11-30": {
        "count": 20,
        "words": [
            ("11", "elf"),
            ("12", "zwolf"),
            ("13", "dreizehn"),
            ("14", "vierzehn"),
            ("15", "funfzehn"),
            ("16", "sechzehn"),
            ("17", "siebzehn"),
            ("18", "achtzehn"),
            ("19", "neunzehn"),
            ("20", "zwanzig"),
            ("21", "einundzwanzig"),
            ("22", "zweiundzwanzig"),
            ("23", "dreiundzwanzig"),
            ("24", "vierundzwanzig"),
            ("25", "funfundzwanzig"),
            ("26", "sechsundzwanzig"),
            ("27", "siebenundzwanzig"),
            ("28", "achtundzwanzig"),
            ("29", "neunundzwanzig"),
            ("30", "dreißig")
        ],
        "is_numbers": True
    },
    
    "Lesson 10.1 - Prepositions": {
        "count": 35,
        "words": [
            ("For", "fur"),
            ("From", "von"),
            ("In", "in"),
            ("Inside", "drinnen"),
            ("Into", "in"),
            ("Near", "nah"),
            ("Of", "von"),
            ("Out", "aus"),
            ("Outside", "draußen"),
            ("To", "zu"),
            ("Under", "unter"),
            ("With", "mit"),
            ("Without", "ohne"),
            ("Above", "uber"),
            ("Across", "uber"),
            ("After", "nach"),
            ("Against", "gegen"),
            ("Along", "entlang"),
            ("Around", "um"),
            ("At", "am"),
            ("Behind", "hinter"),
            ("Below", "unten"),
            ("Beside", "neben"),
            ("Between", "zwischen"),
            ("By", "an"),
            ("During", "wahrend"),
            ("Except", "außer"),
            ("And", "und"),
            ("Because", "weil"),
            ("But", "aber"),
            ("Or", "oder"),
            ("Everywhere", "uberall"),
            ("Everyone", "jeder"),
            ("Everything", "alles"),
            ("Few", "wenige"),
            ("Some", "einige"),
            ("Many", "viele")
        ],
        "is_numbers": False
    },
    
    "Lesson 10.2 - Useful Words": {
        "count": 29,
        "words": [
            ("Question", "frage"),
            ("Answer", "antwort"),
            ("Truth", "wahrheit"),
            ("Lie", "luge"),
            ("Nothing", "nichts"),
            ("Something", "etwas"),
            ("Same", "gleich"),
            ("Different", "unterschiedlich"),
            ("Pull", "ziehen"),
            ("Push", "drucken"),
            ("Long", "lang"),
            ("Short", "kurz"),
            ("Cold", "kalt"),
            ("Hot", "heiß"),
            ("Light", "hell"),
            ("Dark", "dunkel"),
            ("Wet", "nass"),
            ("Dry", "trocken"),
            ("Empty", "leer"),
            ("Full", "voll"),
            ("How?", "wie"),
            ("What?", "was"),
            ("When?", "wann"),
            ("Where?", "wo"),
            ("Which?", "welche"),
            ("Who?", "wer"),
            ("Why?", "warum"),
            ("How long?", "wie lange"),
            ("How much?", "wie viel")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.1 - Drinks": {
        "count": 9,
        "words": [
            ("Coffee", "kaffee"),
            ("Tea", "tee"),
            ("Soft drink", "erfrischungsgetrank"),
            ("Water", "wasser"),
            ("Lemonade", "zitronenlimonade"),
            ("Juice", "saft"),
            ("Orange juice", "orangensaft"),
            ("I would like a glass of water please", "ich hatte gerne ein glas wasser bitte"),
            ("With ice", "mit eis")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.2 - Dairy Products": {
        "count": 19,
        "words": [
            ("Milk", "milch"),
            ("Ice cream", "eis"),
            ("Butter", "butter"),
            ("Cheese", "kase"),
            ("Cottage cheese", "huttenkase"),
            ("Cream", "sahne"),
            ("Sour cream", "saure sahne"),
            ("Yogurt", "joghurt"),
            ("Eggs", "eier"),
            ("Whipping cream", "schlagsahne"),
            ("Bakery", "backerei"),
            ("Baguette", "baguette"),
            ("Doughnut", "krapfen"),
            ("Cookie", "platzchen"),
            ("Roll", "brotchen"),
            ("Dessert", "nachtisch"),
            ("Cake", "kuchen"),
            ("Bread", "brot"),
            ("Pie", "torte")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.3 - Meats": {
        "count": 13,
        "words": [
            ("Beef", "rindfleisch"),
            ("Veal", "kalbfleisch"),
            ("Ham", "schinken"),
            ("Chicken", "huhn"),
            ("Turkey", "pute"),
            ("Duck", "ente"),
            ("Bacon", "speck"),
            ("Pork", "schweinefleisch"),
            ("Filet mignon", "filet mignon"),
            ("Sausage", "wurst"),
            ("Lamb chop", "lammkotelett"),
            ("Pork chop", "schweinekotelett"),
            ("Meat", "fleisch")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.4 - Seafoods": {
        "count": 20,
        "words": [
            ("Fish", "fisch"),
            ("Shellfish", "schalentier"),
            ("Bass", "barsch"),
            ("Salmon", "lachs"),
            ("Lobster", "hummer"),
            ("Crab", "krabbe"),
            ("Mussel", "muscheln"),
            ("Oyster", "austern"),
            ("Cod", "kabeljau"),
            ("Clam", "venusmuscheln"),
            ("Shrimp", "garnelen"),
            ("Tuna", "thunfisch"),
            ("Trout", "forelle"),
            ("Sole", "seezunge"),
            ("Shark", "hai"),
            ("Carp", "karpfen"),
            ("Tilapia", "tilapia"),
            ("Eel", "aal"),
            ("Catfish", "wels"),
            ("Swordfish", "schwertfisch")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.5 - Herbs & Spices": {
        "count": 17,
        "words": [
            ("Salt", "salz"),
            ("Pepper", "pfeffer"),
            ("Caraway", "kummel"),
            ("Garlic", "knoblauch"),
            ("Basil", "basilikum"),
            ("Coriander", "koriander"),
            ("Fennel", "fenchel"),
            ("Marjoram", "majoran"),
            ("Oregano", "oregano"),
            ("Parsley", "petersilie"),
            ("Rosemary", "rosmarin"),
            ("Sage", "salbei"),
            ("Thyme", "thymian"),
            ("Nutmeg", "muskatnuss"),
            ("Paprika", "paprika"),
            ("Cayenne", "cayenne-pfeffer"),
            ("Ginger", "ingwer")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.6 - Vegetables": {
        "count": 28,
        "words": [
            ("Celery", "sellerie"),
            ("Eggplant", "aubergine"),
            ("Zucchini", "zucchini"),
            ("Onion", "zwiebel"),
            ("Spinach", "spinat"),
            ("Salad", "salat"),
            ("Green beans", "grune bohnen"),
            ("Cucumber", "gurke"),
            ("Radish", "radieschen"),
            ("Cabbage", "kohl"),
            ("Mushrooms", "pilze"),
            ("Lettuce", "salat"),
            ("Corn", "mais"),
            ("Potatoes", "kartoffeln"),
            ("Tomato", "tomate"),
            ("Carrot", "mohre"),
            ("Plantain", "kochbanane"),
            ("Beans", "bohnen"),
            ("Leek", "lauch"),
            ("Lotus root", "lotuswurzel"),
            ("Bamboo shoot", "bambussprosse"),
            ("Artichoke", "artischocke"),
            ("Asparagus", "spargel"),
            ("Brussels sprouts", "rosenkohl"),
            ("Broccoli", "brokkoli"),
            ("Peas", "erbsen"),
            ("Cauliflower", "blumenkohl"),
            ("Chili pepper", "chili-pfeffer")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.7 - Fruits": {
        "count": 27,
        "words": [
            ("Cherries", "kirschen"),
            ("Raspberries", "himbeeren"),
            ("Blueberries", "heidelbeeren"),
            ("Strawberries", "erdbeeren"),
            ("Lemon", "zitrone"),
            ("Lime", "limette"),
            ("Apple", "apfel"),
            ("Orange", "orange"),
            ("Pear", "birne"),
            ("Banana", "banane"),
            ("Grapes", "trauben"),
            ("Grapefruit", "grapefruit"),
            ("Watermelon", "wassermelone"),
            ("Pineapple", "ananas"),
            ("Plum", "pflaume"),
            ("Peach", "pfirsich"),
            ("Mango", "mango"),
            ("Apricot", "aprikose"),
            ("Pomegranate", "granatapfel"),
            ("Persimmon", "kaki"),
            ("Kiwi", "kiwi-frucht"),
            ("Litchi", "litschi"),
            ("Longan", "longan-frucht"),
            ("Balsam pear", "balsam-birne"),
            ("Passion fruit", "passionsfrucht"),
            ("Avocado", "avocado"),
            ("Coconut", "kokosnuss")
        ],
        "is_numbers": False
    },
    
    "Lesson 12 - Numbers 31-50": {
        "count": 20,
        "words": [
            ("31", "einunddreißig"),
            ("32", "zweiunddreißig"),
            ("33", "dreiunddreißig"),
            ("34", "vierunddreißig"),
            ("35", "funfunddreißig"),
            ("36", "sechsunddreißig"),
            ("37", "siebenunddreißig"),
            ("38", "achtunddreißig"),
            ("39", "neununddreißig"),
            ("40", "vierzig"),
            ("41", "einundvierzig"),
            ("42", "zweiundvierzig"),
            ("43", "dreiundvierzig"),
            ("44", "vierundvierzig"),
            ("45", "funfundvierzig"),
            ("46", "sechsundvierzig"),
            ("47", "siebenundvierzig"),
            ("48", "achtundvierzig"),
            ("49", "neunundvierzig"),
            ("50", "funfzig")
        ],
        "is_numbers": True
    },
    
    "Lesson 13 - Irregular Verbs": {
        "count": 50,
        "words": [
            ("to be", "sein"),
            ("to have", "haben"),
            ("to go", "gehen"),
            ("to come", "kommen"),
            ("to see", "sehen"),
            ("to give", "geben"),
            ("to eat", "essen"),
            ("to drink", "trinken"),
            ("to know (fact)", "wissen"),
            ("to want", "wollen"),
            ("to find", "finden"),
            ("to run", "laufen"),
            ("to sit", "sitzen"),
            ("to lie down", "liegen"),
            ("to stand", "stehen"),
            ("to understand", "verstehen"),
            ("to say", "sagen"),
            ("to take", "nehmen"),
            ("to write", "schreiben"),
            ("to fall", "fallen"),
            ("to begin", "beginnen"),
            ("to break", "brechen"),
            ("to build", "bauen"),
            ("to choose", "wahlen"),
            ("to do/make", "machen"),
            ("to drive", "fahren"),
            ("to forget", "vergessen"),
            ("to get", "bekommen"),
            ("to hear", "horen"),
            ("to hold", "halten"),
            ("to leave", "verlassen"),
            ("to meet", "treffen"),
            ("to pay", "bezahlen"),
            ("to put", "legen/stellen"),
            ("to read", "lesen"),
            ("to send", "senden"),
            ("to sleep", "schlafen"),
            ("to speak", "sprechen"),
            ("to spend (time)", "verbringen"),
            ("to swim", "schwimmen"),
            ("to teach", "lehren"),
            ("to tell", "erzahlen"),
            ("to think", "denken"),
            ("to throw", "werfen"),
            ("to win", "gewinnen"),
            ("to bring", "bringen")
        ],
        "is_numbers": False
    },
    
    "Lesson 15 - Physical Appearance": {
        "count": 38,
        "words": [
            ("Tall", "groß"),
            ("Short (height)", "klein"),
            ("Slim", "schlank"),
            ("Fat", "dick"),
            ("Muscular", "muskulos"),
            ("Blonde", "blond"),
            ("Brown-haired", "braunhaarig"),
            ("Black-haired", "schwarzhaarig"),
            ("Curly hair", "lockiges haar"),
            ("Straight hair", "glattes haar"),
            ("Blue eyes", "blaue augen"),
            ("Brown eyes", "braune augen"),
            ("Green eyes", "grune augen"),
            ("Beautiful", "schon"),
            ("Handsome", "gutaussehend"),
            ("Ugly", "hasslich"),
            ("Young", "jung"),
            ("Old", "alt"),
            ("Beard", "bart"),
            ("Light-skinned", "helle haut"),
            ("Dark-skinned", "dunkle haut"),
            ("Freckles", "sommersprossen"),
            ("Wrinkles", "falten"),
            ("Bald", "kahl"),
            ("Hairy (body)", "behaart"),
            ("Straight nose", "gerade nase"),
            ("Big nose", "große nase"),
            ("Small nose", "kleine nase"),
            ("Thin lips", "schmale lippen"),
            ("Full lips", "volle lippen"),
            ("Broad shoulders", "breite schultern"),
            ("Narrow shoulders", "schmale schultern"),
            ("Tanned skin", "gebraunte haut"),
            ("Pale skin", "blasse haut"),
            ("Wavy hair", "welliges haar"),
            ("Ponytail", "pferdeschwanz"),
            ("Braids", "zopfe"),
            ("Beard and mustache", "bart und schnurrbart")
        ],
        "is_numbers": False
    },
    
    "Lesson 16 - Occupations": {
        "count": 25,
        "words": [
            ("Doctor", "arzt/arztin"),
            ("Teacher", "lehrer/lehrerin"),
            ("Engineer", "ingenieur/ingenieurin"),
            ("Lawyer", "anwalt/anwaltin"),
            ("Salesperson", "verkaufer/verkauferin"),
            ("Police officer", "polizist/polizistin"),
            ("Firefighter", "feuerwehrmann/feuerwehrfrau"),
            ("Programmer", "programmierer/programmiererin"),
            ("Cook/Chef", "koch/kochin"),
            ("Journalist", "journalist/journalistin"),
            ("Nurse", "krankenpfleger/krankenschwester"),
            ("Architect", "architekt/architektin"),
            ("Accountant", "buchhalter/buchhalterin"),
            ("Pharmacist", "apotheker/apothekerin"),
            ("Driver", "fahrer/fahrerin"),
            ("Mechanic", "mechaniker/mechanikerin"),
            ("Scientist", "wissenschaftler/wissenschaftlerin"),
            ("Dentist", "zahnarzt/zahnarztin"),
            ("Musician", "musiker/musikerin"),
            ("Actor", "schauspieler/schauspielerin"),
            ("Artist", "kunstler/kunstlerin"),
            ("Pilot", "pilot/pilotin"),
            ("Farmer", "landwirt/landwirtin"),
            ("Photographer", "fotograf/fotografin"),
            ("Waiter/Waitress", "kellner/kellnerin")
        ],
        "is_numbers": False
    },
    
    "Lesson 17 - Sports": {
        "count": 30,
        "words": [
            ("Football/Soccer", "fußball"),
            ("Basketball", "basketball"),
            ("Volleyball", "volleyball"),
            ("Tennis", "tennis"),
            ("Swimming", "schwimmen"),
            ("Running/Athletics", "laufen/leichtathletik"),
            ("Ice hockey", "eishockey"),
            ("Skiing", "skifahren"),
            ("Cycling", "radfahren"),
            ("Boxing", "boxen"),
            ("Martial arts", "kampfsport"),
            ("Golf", "golf"),
            ("Table tennis", "tischtennis"),
            ("Wrestling", "ringen"),
            ("Handball", "handball"),
            ("Baseball", "baseball"),
            ("Surfing", "surfen"),
            ("Skating", "eislaufen"),
            ("Horse riding", "reiten"),
            ("Diving", "tauchen"),
            ("Cricket", "kricket"),
            ("Rugby", "rugby"),
            ("Ballet", "ballett"),
            ("Bowling", "bowling"),
            ("Weightlifting", "gewichtheben"),
            ("Windsurfing", "windsurfen"),
            ("Ice skating", "eislaufen"),
            ("Rowing", "rudern"),
            ("Archery", "bogenschießen"),
            ("Climbing", "klettern")
        ],
        "is_numbers": False
    },
    
    "Lesson 18 - Numbers 51-75": {
        "count": 25,
        "words": [
            ("51", "einundfunfzig"),
            ("52", "zweiundfunfzig"),
            ("53", "dreiundfunfzig"),
            ("54", "vierundfunfzig"),
            ("55", "funfundfunfzig"),
            ("56", "sechsundfunfzig"),
            ("57", "siebenundfunfzig"),
            ("58", "achtundfunfzig"),
            ("59", "neunundfunfzig"),
            ("60", "sechzig"),
            ("61", "einundsechzig"),
            ("62", "zweiundsechzig"),
            ("63", "dreiundsechzig"),
            ("64", "vierundsechzig"),
            ("65", "funfundsechzig"),
            ("66", "sechsundsechzig"),
            ("67", "siebenundsechzig"),
            ("68", "achtundsechzig"),
            ("69", "neunundsechzig"),
            ("70", "siebzig"),
            ("71", "einundsiebzig"),
            ("72", "zweiundsiebzig"),
            ("73", "dreiundsiebzig"),
            ("74", "vierundsiebzig"),
            ("75", "funfundsiebzig")
        ],
        "is_numbers": True
    },
    
    "Lesson 19 - Clothing": {
        "count": 44,
        "words": [
            ("Shirt", "hemd"),
            ("T-shirt", "t-shirt"),
            ("Blouse", "bluse"),
            ("Sweater", "pullover"),
            ("Jacket", "jacke"),
            ("Coat", "mantel"),
            ("Dress", "kleid"),
            ("Skirt", "rock"),
            ("Pants", "hose"),
            ("Shorts", "shorts"),
            ("Shoes", "schuhe"),
            ("Boots", "stiefel"),
            ("Sneakers", "turnschuhe"),
            ("Sandals", "sandalen"),
            ("Hat/Cap", "mutze/hut"),
            ("Scarf", "schal"),
            ("Gloves", "handschuhe"),
            ("Belt", "gurtel"),
            ("Socks", "socken"),
            ("Winter coat", "wintermantel"),
            ("Wool hat", "wollmutze"),
            ("Snow boots", "schneestiefel"),
            ("Swimsuit", "badeanzug"),
            ("Sunglasses", "sonnenbrille"),
            ("Flip-flops", "flip-flops"),
            ("Tank top", "top"),
            ("Suit", "anzug"),
            ("Tie", "krawatte"),
            ("Blazer", "blazer"),
            ("High heels", "high heels"),
            ("Evening dress", "abendkleid"),
            ("Black", "schwarz"),
            ("White", "weiß"),
            ("Red", "rot"),
            ("Blue", "blau"),
            ("Green", "grun"),
            ("Cotton", "baumwolle"),
            ("Wool", "wolle"),
            ("Leather", "leder"),
            ("Silk", "seide"),
            ("Linen", "leinen")
        ],
        "is_numbers": False
    },
    
    "Lesson 20 - Adverbs": {
        "count": 20,
        "words": [
            ("Quickly", "schnell"),
            ("Slowly", "langsam"),
            ("Always", "immer"),
            ("Never", "nie"),
            ("Often", "oft"),
            ("Sometimes", "manchmal"),
            ("Rarely", "selten"),
            ("Already", "schon"),
            ("Still", "noch"),
            ("Yet", "noch"),
            ("Soon", "bald"),
            ("Now", "jetzt"),
            ("Later", "spater"),
            ("Today", "heute"),
            ("Tomorrow", "morgen"),
            ("Yesterday", "gestern"),
            ("Clearly", "klar"),
            ("Together", "zusammen"),
            ("Apart", "getrennt"),
            ("Forever", "fur immer")
        ],
        "is_numbers": False
    },
    
    "Lesson 21 - Animals": {
        "count": 20,
        "words": [
            ("Dog", "hund"),
            ("Cat", "katze"),
            ("Horse", "pferd"),
            ("Cow", "kuh"),
            ("Sheep", "schaf"),
            ("Pig", "schwein"),
            ("Goat", "ziege"),
            ("Chicken", "huhn"),
            ("Duck", "ente"),
            ("Bird", "vogel"),
            ("Rabbit", "kaninchen"),
            ("Mouse", "maus"),
            ("Lion", "lowe"),
            ("Tiger", "tiger"),
            ("Bear", "bar"),
            ("Elephant", "elefant"),
            ("Monkey", "affe"),
            ("Fox", "fuchs"),
            ("Wolf", "wolf"),
            ("Deer", "reh")
        ],
        "is_numbers": False
    },
    
    "Lesson 22 - Places in Town": {
        "count": 20,
        "words": [
            ("School", "schule"),
            ("Hospital", "krankenhaus"),
            ("Bank", "bank"),
            ("Restaurant", "restaurant"),
            ("Library", "bibliothek"),
            ("Supermarket", "supermarkt"),
            ("Cinema", "kino"),
            ("Post office", "post"),
            ("Police station", "polizeistation"),
            ("Park", "park"),
            ("Museum", "museum"),
            ("Theatre", "theater"),
            ("Hotel", "hotel"),
            ("Stadium", "stadion"),
            ("Church", "kirche"),
            ("Pharmacy", "apotheke"),
            ("Bakery", "backerei"),
            ("Butcher", "metzgerei"),
            ("Market", "markt"),
            ("Hairdresser", "friseur")
        ],
        "is_numbers": False
    },
    
    "Lesson 23 - School Supplies": {
        "count": 20,
        "words": [
            ("Book", "buch"),
            ("Pen", "stift"),
            ("Pencil", "bleistift"),
            ("Eraser", "radiergummi"),
            ("Notebook", "heft"),
            ("Ruler", "lineal"),
            ("Scissors", "schere"),
            ("Backpack", "rucksack"),
            ("Folder", "ordner"),
            ("Calculator", "taschenrechner"),
            ("Marker", "marker"),
            ("Chalk", "kreide"),
            ("Map", "karte"),
            ("Highlighter", "textmarker"),
            ("Projector", "projektor"),
            ("Laptop", "laptop"),
            ("Printer", "drucker"),
            ("USB stick", "usb-stick"),
            ("Schoolbag", "schultasche"),
            ("Sharpener", "spitzer")
        ],
        "is_numbers": False
    },
    
    "Lesson 24 - Transportation": {
        "count": 20,
        "words": [
            ("Car", "auto"),
            ("Bus", "bus"),
            ("Train", "zug"),
            ("Bicycle", "fahrrad"),
            ("Motorcycle", "motorrad"),
            ("Airplane", "flugzeug"),
            ("Boat", "boot"),
            ("Tram", "straßenbahn"),
            ("Taxi", "taxi"),
            ("Subway", "u-bahn"),
            ("Ferry", "fahre"),
            ("Yacht", "yacht"),
            ("Hot air balloon", "heißluftballon"),
            ("Spaceship", "raumschiff"),
            ("Rickshaw", "rikscha"),
            ("Gondola", "gondel"),
            ("Zeppelin", "zeppelin"),
            ("Rollerblades", "inlineskates"),
            ("Canoe", "kanu"),
            ("Submarine", "u-boot")
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
        for english, german in words:
            questions.append({
                'type': 'num_to_word',
                'question': f"What is '{english}' in German? (Answer with the WORD)",
                'answer': german,
                'display_answer': german  # KELIME göster
            })
        
        # Tarz 2: Kelimeden sayıya (Cevap: SAYI)
        for english, german in words:
            questions.append({
                'type': 'word_to_num',
                'question': f"What number is '{german}'? (Answer with the NUMBER)",
                'answer': english,
                'display_answer': english  # SAYI göster
            })
        
        # Tarz 3: Karışık (Cevap türüne göre)
        for english, german in words:
            if random.choice([True, False]):
                # Sayıdan kelimeye
                questions.append({
                    'type': 'mixed',
                    'question': f"Translate '{english}' to German word:",
                    'answer': german,
                    'display_answer': german  # KELIME
                })
            else:
                # Kelimeden sayıya
                questions.append({
                    'type': 'mixed',
                    'question': f"What number is '{german}'?",
                    'answer': english,
                    'display_answer': english  # SAYI
                })
    
    elif count <= 20:
        # 20 ve altı: 3 farklı soru tarzı
        # Tarz 1: English -> German
        for english, german in words:
            questions.append({
                'type': 'eng_to_ger',
                'question': f"Translate to German: '{english}'",
                'answer': german,
                'display_answer': german
            })
        
        # Tarz 2: German -> English
        for english, german in words:
            questions.append({
                'type': 'ger_to_eng',
                'question': f"Translate to English: '{german}'",
                'answer': english,
                'display_answer': english
            })
        
        # Tarz 3: İlk harf ipucu
        for english, german in words:
            first_letter = german[0] if german else ""
            blanks = "_" * (len(german) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}' - Complete the German word",
                'answer': german,
                'display_answer': german
            })
    
    elif 20 < count <= 40:
        # 20-40 arası: 3 bölüm, 2 farklı soru tarzı
        third = len(words) // 3
        
        # Bölüm 1: English -> German
        for english, german in words[:third]:
            questions.append({
                'type': 'eng_to_ger',
                'question': f"Translate to German: '{english}'",
                'answer': german,
                'display_answer': german
            })
        
        # Bölüm 2: German -> English
        for english, german in words[third:third*2]:
            questions.append({
                'type': 'ger_to_eng',
                'question': f"Translate to English: '{german}'",
                'answer': english,
                'display_answer': english
            })
        
        # Bölüm 3: İlk harf ipucu
        for english, german in words[third*2:]:
            first_letter = german[0] if german else ""
            blanks = "_" * (len(german) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': german,
                'display_answer': german
            })
    
    else:  # count > 40
        # 40+ : 5 bölüm, 3-4 farklı soru tarzı
        fifth = len(words) // 5
        
        # Bölüm 1: English -> German
        for english, german in words[:fifth]:
            questions.append({
                'type': 'eng_to_ger',
                'question': f"Translate to German: '{english}'",
                'answer': german,
                'display_answer': german
            })
        
        # Bölüm 2: German -> English
        for english, german in words[fifth:fifth*2]:
            questions.append({
                'type': 'ger_to_eng',
                'question': f"Translate to English: '{german}'",
                'answer': english,
                'display_answer': english
            })
        
        # Bölüm 3: İlk harf
        for english, german in words[fifth*2:fifth*3]:
            first_letter = german[0] if german else ""
            blanks = "_" * (len(german) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': german,
                'display_answer': german
            })
        
        # Bölüm 4: Son harf
        for english, german in words[fifth*3:fifth*4]:
            last_letter = german[-1] if german else ""
            blanks = "_" * (len(german) - 1)
            questions.append({
                'type': 'last_letter',
                'question': f"'{english}' = '{blanks}{last_letter}'",
                'answer': german,
                'display_answer': german
            })
        
        # Bölüm 5: Harf sayısı ipucu
        for english, german in words[fifth*4:]:
            questions.append({
                'type': 'letter_hint',
                'question': f"'{english}' = ({len(german)} letters, starts with {german[:2]}...)",
                'answer': german,
                'display_answer': german
            })
    
    return questions

def create_general_review(lesson_name, words, is_numbers):
    """Her bölümün sonunda genel tekrar soruları"""
    review = []
    sample_size = min(20, len(words))
    sampled_words = random.sample(words, sample_size)
    
    for english, german in sampled_words:
        if is_numbers:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] '{english}' in German?",
                    'answer': german,
                    'display_answer': german
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] What number is '{german}'?",
                    'answer': english,
                    'display_answer': english
                })
        else:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{english}'",
                    'answer': german,
                    'display_answer': german
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{german}'",
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
║        COMPREHENSIVE GERMAN TEST SYSTEM                   ║
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
        print(Fore.GREEN + "🎉🎉🎉 EXCELLENT! You're amazing at German! 🎉🎉🎉")
    elif final_percentage >= 70:
        print(Fore.BLUE + "👏👏👏 VERY GOOD! Great performance! 👏👏👏")
    elif final_percentage >= 50:
        print(Fore.YELLOW + "👍👍 GOOD! Keep going and you'll be excellent! 👍👍")
    else:
        print(Fore.RED + "📚📚 Keep studying! You can do it! 📚📚")
    
    print(Fore.GREEN + "\nCongratulations! You completed the entire test! 🎊")

if __name__ == "__main__":
    main()