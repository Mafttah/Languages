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
            ("1", "uno"),
            ("2", "dos"),
            ("3", "tres"),
            ("4", "cuatro"),
            ("5", "cinco"),
            ("6", "seis"),
            ("7", "siete"),
            ("8", "ocho"),
            ("9", "nueve"),
            ("10", "diez")
        ],
        "is_numbers": True
    },
    
    "Lesson 2 - Greetings": {
        "count": 18,
        "words": [
            ("Hello", "ciao"),
            ("How are you?", "come stai"),
            ("Nice to see you", "felice di vederti"),
            ("Nice to meet you", "piacere di conoscerti"),
            ("See you tomorrow", "a domani"),
            ("Good morning", "buon giorno"),
            ("Good afternoon", "buon pomeriggio"),
            ("Good evening", "buona sera"),
            ("Good night", "buona notte"),
            ("What is your name?", "come ti chiami"),
            ("My name is", "mi chiamo"),
            ("Where do you live?", "dove vive"),
            ("Where are you from?", "di dove sei"),
            ("Have a nice day", "buona giornata"),
            ("See you later", "a dopo"),
            ("Goodbye", "arrivederci"),
            ("Please", "per favore"),
            ("Thank you", "grazie")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.1 - Regular -ARE Verbs": {
        "count": 60,
        "words": [
            ("to live/inhabit", "abitare"),
            ("to help", "aiutare"),
            ("to love", "amare"),
            ("to arrive", "arrivare"),
            ("to listen to", "ascoltare"),
            ("to wait for", "aspettare"),
            ("to kiss", "baciare"),
            ("to conserve", "conservare"),
            ("to consider", "considerare"),
            ("to advise", "consigliare"),
            ("to cost", "costare"),
            ("to cause", "causare"),
            ("to have dinner", "cenare"),
            ("to call", "chiamare"),
            ("to begin", "cominciare"),
            ("to buy", "comprare"),
            ("to teach", "insegnare"),
            ("to complain", "lamentare"),
            ("to leave", "lasciare"),
            ("to wash", "lavare"),
            ("to work", "lavorare"),
            ("to eat", "mangiare"),
            ("to swim", "nuotare"),
            ("to cook", "cucinare"),
            ("to take care of", "curare"),
            ("to draw", "disegnare"),
            ("to meet", "incontrare"),
            ("to wear", "indossare"),
            ("to become", "diventare"),
            ("to doubt", "dubitare"),
            ("to enter", "entrare"),
            ("to avoid", "evitare"),
            ("to smoke", "fumare"),
            ("to watch", "guardare"),
            ("to drive", "guidare"),
            ("to learn", "imparare"),
            ("to suffice", "bastare"),
            ("to walk", "camminare"),
            ("to sing", "cantare"),
            ("to organize", "ordinare"),
            ("to speak", "parlare"),
            ("to pass", "passare"),
            ("to think", "pensare"),
            ("to bring", "portare"),
            ("to have lunch", "pranzare"),
            ("to book", "prenotare"),
            ("to try", "provare"),
            ("to stay", "restare"),
            ("to remember", "ricordare"),
            ("to greet", "salutare"),
            ("to save", "salvare"),
            ("to make mistake", "sbagliare"),
            ("to hope", "sperare"),
            ("to study", "studiare"),
            ("to cut", "tagliare"),
            ("to return", "tornare"),
            ("to find", "trovare"),
            ("to travel", "viaggiare"),
            ("to visit", "visitare")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.2 - Regular -ERE Verbs": {
        "count": 39,
        "words": [
            ("to access", "accedere"),
            ("to turn on", "accendere"),
            ("to learn", "apprendere"),
            ("to assume", "assumere"),
            ("to wait for", "attendere"),
            ("to beat", "battere"),
            ("to ask", "chiedere"),
            ("to close", "chiudere"),
            ("to understand", "comprendere"),
            ("to know", "conoscere"),
            ("to run", "correre"),
            ("to believe", "credere"),
            ("to die", "decedere"),
            ("to decide", "decidere"),
            ("to describe", "descrivere"),
            ("to debate", "dibattere"),
            ("to discuss", "discutere"),
            ("to put", "mettere"),
            ("to lose", "perdere"),
            ("to precede", "precedere"),
            ("to press", "premere"),
            ("to take", "prendere"),
            ("to claim", "pretendere"),
            ("to promise", "promettere"),
            ("to give back", "rendere"),
            ("to receive", "ricevere"),
            ("to laugh", "ridere"),
            ("to repeat", "ripetere"),
            ("to answer", "rispondere"),
            ("to break", "rompere"),
            ("to descend", "scendere"),
            ("to write", "scrivere"),
            ("to smile", "sorridere"),
            ("to spend", "spendere"),
            ("to fear", "temere"),
            ("to weave", "tessere"),
            ("to see", "vedere"),
            ("to sell", "vendere"),
            ("to live", "vivere")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.3 - Regular -IRE Verbs": {
        "count": 28,
        "words": [
            ("to abhor", "aborrire"),
            ("to agree", "acconsentire"),
            ("to applaud", "applaudire"),
            ("to open", "aprire"),
            ("to assent", "assentire"),
            ("to absorb", "assorbire"),
            ("to warn", "avvertire"),
            ("to boil", "bollire"),
            ("to share", "compartire"),
            ("to convert", "convertire"),
            ("to cover", "coprire"),
            ("to sew", "cucire"),
            ("to enjoy", "divertire"),
            ("to sleep", "dormire"),
            ("to escape", "fuggire"),
            ("to swallow", "inghiottire"),
            ("to lie", "mentire"),
            ("to feed", "nutrire"),
            ("to offer", "offrire"),
            ("to leave", "partire"),
            ("to reopen", "riaprire"),
            ("to fill", "riempire"),
            ("to discover", "scoprire"),
            ("to follow", "seguire"),
            ("to feel", "sentire"),
            ("to serve", "servire"),
            ("to suffer", "soffrire"),
            ("to cough", "tossire"),
            ("to dress", "vestire")
        ],
        "is_numbers": False
    },
    
    "Lesson 4 - Adjectives": {
        "count": 35,
        "words": [
            ("Happy", "felice"),
            ("Sad", "triste"),
            ("Angry", "arrabbiato"),
            ("Afraid", "spaventato"),
            ("Joy", "gioia"),
            ("Surprised", "sorpreso"),
            ("Calm", "calmo"),
            ("Bored", "annoiato"),
            ("Easy", "facile"),
            ("Difficult", "difficile"),
            ("Bad", "cattivo"),
            ("Good", "buono"),
            ("Noisy", "rumoroso"),
            ("Quiet", "silenzioso"),
            ("Strong", "forte"),
            ("Weak", "debole"),
            ("Hard", "duro"),
            ("Soft", "morbido"),
            ("More", "piu"),
            ("Less", "meno"),
            ("Clean", "pulito"),
            ("Dirty", "sporco"),
            ("Old", "vecchio"),
            ("New", "nuovo"),
            ("Big", "grande"),
            ("Small", "piccolo"),
            ("Young", "giovane"),
            ("Skinny", "magro"),
            ("Fat", "grasso"),
            ("Pretty", "bello"),
            ("Ugly", "brutto"),
            ("Thick", "spesso"),
            ("Thin", "sottile"),
            ("Rough", "ruvido"),
            ("Smooth", "liscio")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.1 - Days": {
        "count": 11,
        "words": [
            ("The days of the week", "i giorni della settimana"),
            ("Day", "giorno"),
            ("Week", "settimana"),
            ("Monday", "lunedi"),
            ("Tuesday", "martedi"),
            ("Wednesday", "mercoledi"),
            ("Thursday", "giovedi"),
            ("Friday", "venerdi"),
            ("Saturday", "sabato"),
            ("Sunday", "domenica"),
            ("Weekend", "fine settimana")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.2 - Months": {
        "count": 15,
        "words": [
            ("The months of the year", "i mesi dell'anno"),
            ("Month", "mese"),
            ("Year", "anno"),
            ("January", "gennaio"),
            ("February", "febbraio"),
            ("March", "marzo"),
            ("April", "aprile"),
            ("May", "maggio"),
            ("June", "giugno"),
            ("July", "luglio"),
            ("August", "agosto"),
            ("September", "settembre"),
            ("October", "ottobre"),
            ("November", "novembre"),
            ("December", "dicembre")
        ],
        "is_numbers": False
    },
    
    "Lesson 6 - Seasons & Weather": {
        "count": 23,
        "words": [
            ("Seasons", "stagioni"),
            ("Winter", "inverno"),
            ("Summer", "estate"),
            ("Spring", "primavera"),
            ("Autumn", "autunno"),
            ("Sky", "cielo"),
            ("Cloud", "nuvola"),
            ("Rainbow", "arcobaleno"),
            ("Cold", "freddo"),
            ("Hot", "caldo"),
            ("It is hot", "fa caldo"),
            ("It is cold", "fa freddo"),
            ("It is sunny", "c'e il sole"),
            ("It is cloudy", "e nuvoloso"),
            ("It is humid", "e umido"),
            ("It is raining", "piove"),
            ("It is snowing", "nevica"),
            ("It is windy", "c'e vento"),
            ("How is the weather?", "com'e il tempo"),
            ("Good weather", "bel tempo"),
            ("Bad weather", "maltempo"),
            ("What is the temperature?", "che temperatura c'e"),
            ("It is 24 degrees", "ci sono ventiquattro gradi")
        ],
        "is_numbers": False
    },
    
    "Lesson 7 - Colors": {
        "count": 14,
        "words": [
            ("Black", "nero"),
            ("Blue", "blu"),
            ("Brown", "marrone"),
            ("Green", "verde"),
            ("Orange", "arancione"),
            ("Purple", "viola"),
            ("Red", "rosso"),
            ("White", "bianco"),
            ("Yellow", "giallo"),
            ("Gray", "grigio"),
            ("Gold", "oro"),
            ("Silver", "argento"),
            ("What color is it?", "che colore e"),
            ("The color is", "il colore e")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.1 - Family": {
        "count": 35,
        "words": [
            ("Mother", "madre"),
            ("Father", "padre"),
            ("Brother", "fratello"),
            ("Sister", "sorella"),
            ("Son", "figlio"),
            ("Daughter", "figlia"),
            ("Parents", "genitori"),
            ("Children", "bambini"),
            ("Child", "bambino"),
            ("Stepmother", "madre acquisita"),
            ("Stepfather", "padre acquisito"),
            ("Stepsister", "sorella acquisita"),
            ("Stepbrother", "fratello acquisito"),
            ("Son-in-law", "genero"),
            ("Daughter-in-law", "nuora"),
            ("Wife", "moglie"),
            ("Husband", "marito"),
            ("Grandparents", "nonni"),
            ("Grandfather", "nonno"),
            ("Grandmother", "nonna"),
            ("Grandson", "nipotino"),
            ("Granddaughter", "nipotina"),
            ("Grandchildren", "nipotini"),
            ("Grandchild", "nipotino"),
            ("Aunt", "zia"),
            ("Uncle", "zio"),
            ("Cousin (female)", "cugina"),
            ("Cousin (male)", "cugino"),
            ("Nephew", "nipote"),
            ("Niece", "nipote"),
            ("Father-in-law", "suocero"),
            ("Mother-in-law", "suocera"),
            ("Brother-in-law", "cognato"),
            ("Sister-in-law", "cognata"),
            ("Relative", "parente")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.2 - Friends": {
        "count": 14,
        "words": [
            ("Miss", "signorina"),
            ("Boy", "ragazzo"),
            ("Girl", "ragazza"),
            ("Baby", "bebe"),
            ("Woman", "donna"),
            ("Man", "uomo"),
            ("Friend (male)", "amico"),
            ("Friend (female)", "amica"),
            ("Boyfriend", "fidanzato"),
            ("Girlfriend", "fidanzata"),
            ("Gentleman", "signore"),
            ("Lady", "signora"),
            ("Neighbor (male)", "vicino"),
            ("Neighbor (female)", "vicina di casa")
        ],
        "is_numbers": False
    },
    
    "Lesson 9 - Numbers 11-30": {
        "count": 20,
        "words": [
            ("11", "undici"),
            ("12", "dodici"),
            ("13", "tredici"),
            ("14", "quattordici"),
            ("15", "quindici"),
            ("16", "sedici"),
            ("17", "diciassette"),
            ("18", "diciotto"),
            ("19", "diciannove"),
            ("20", "venti"),
            ("21", "ventuno"),
            ("22", "ventidue"),
            ("23", "ventitre"),
            ("24", "ventiquattro"),
            ("25", "venticinque"),
            ("26", "ventisei"),
            ("27", "ventisette"),
            ("28", "ventotto"),
            ("29", "ventinove"),
            ("30", "trenta")
        ],
        "is_numbers": True
    },
    
    "Lesson 10.1 - Prepositions": {
        "count": 36,
        "words": [
            ("For", "per"),
            ("From", "da"),
            ("In", "in"),
            ("Inside", "dentro"),
            ("Into", "in"),
            ("Near", "vicino"),
            ("Of", "di"),
            ("Out", "fuori"),
            ("Outside", "fuori"),
            ("To", "a"),
            ("Under", "sotto"),
            ("With", "con"),
            ("Without", "senza"),
            ("Above", "sopra"),
            ("Across", "attraverso"),
            ("After", "dopo"),
            ("Against", "contro"),
            ("Along", "lungo"),
            ("Around", "intorno"),
            ("At", "a"),
            ("Behind", "dietro"),
            ("Below", "in basso"),
            ("Beside", "accanto a"),
            ("Between", "fra"),
            ("By", "da"),
            ("During", "durante"),
            ("Except", "tranne"),
            ("And", "e"),
            ("Because", "perche"),
            ("But", "ma"),
            ("Or", "o"),
            ("Everywhere", "dappertutto"),
            ("Everyone", "tutti"),
            ("Everything", "tutto"),
            ("Few", "pochi"),
            ("Some", "alcuni"),
            ("Many", "molti")
        ],
        "is_numbers": False
    },
    
    "Lesson 10.2 - Useful Words": {
        "count": 29,
        "words": [
            ("Question", "domanda"),
            ("Answer", "risposta"),
            ("Truth", "verita"),
            ("Lie", "bugia"),
            ("Nothing", "niente"),
            ("Something", "qualcosa"),
            ("Same", "identico"),
            ("Different", "diverso"),
            ("Pull", "tirare"),
            ("Push", "spingere"),
            ("Long", "lungo"),
            ("Short", "corto"),
            ("Cold", "freddo"),
            ("Hot", "caldo"),
            ("Light", "chiaro"),
            ("Dark", "scuro"),
            ("Wet", "bagnato"),
            ("Dry", "asciutto"),
            ("Empty", "vuoto"),
            ("Full", "pieno"),
            ("How?", "come"),
            ("What?", "cosa"),
            ("When?", "quando"),
            ("Where?", "dove"),
            ("Which?", "quale"),
            ("Who?", "chi"),
            ("Why?", "perche"),
            ("How long?", "quanto tempo"),
            ("How much?", "quanto")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.1 - Drinks": {
        "count": 9,
        "words": [
            ("Coffee", "caffe"),
            ("Tea", "te"),
            ("Soft drink", "bibita"),
            ("Water", "acqua"),
            ("Lemonade", "limonata"),
            ("Juice", "succo di frutta"),
            ("Orange juice", "aranciata"),
            ("I would like a glass of water please", "un bicchiere d'acqua per favore"),
            ("With ice", "con ghiaccio")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.2 - Dairy Products": {
        "count": 19,
        "words": [
            ("Milk", "latte"),
            ("Ice cream", "gelato"),
            ("Butter", "burro"),
            ("Cheese", "formaggio"),
            ("Cottage cheese", "fiocchi di latte"),
            ("Cream", "panna"),
            ("Sour cream", "panna acida"),
            ("Yogurt", "yogurt"),
            ("Eggs", "uova"),
            ("Whipping cream", "panna da montare"),
            ("Bakery", "panificio"),
            ("Baguette", "filoncino"),
            ("Doughnut", "ciambella"),
            ("Cookie", "biscotto"),
            ("Roll", "rosetta di pane"),
            ("Dessert", "dolci"),
            ("Cake", "torta"),
            ("Bread", "pane"),
            ("Pie", "crostata")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.3 - Meats": {
        "count": 13,
        "words": [
            ("Beef", "manzo"),
            ("Veal", "vitello"),
            ("Ham", "prosciutto"),
            ("Chicken", "pollo"),
            ("Turkey", "tacchino"),
            ("Duck", "anatra"),
            ("Bacon", "pancetta"),
            ("Pork", "maiale"),
            ("Filet mignon", "filetto"),
            ("Sausage", "salsiccia"),
            ("Lamb chop", "braciola di agnello"),
            ("Pork chop", "braciola di maiale"),
            ("Meat", "carne")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.4 - Seafoods": {
        "count": 20,
        "words": [
            ("Fish", "pesce"),
            ("Shellfish", "crostacei"),
            ("Bass", "branzino"),
            ("Salmon", "salmone"),
            ("Lobster", "aragosta"),
            ("Crab", "granchio"),
            ("Mussel", "cozza"),
            ("Oyster", "ostrica"),
            ("Cod", "merluzzo"),
            ("Clam", "vongola"),
            ("Shrimp", "gambero"),
            ("Tuna", "tonno"),
            ("Trout", "trota"),
            ("Sole", "sogliola"),
            ("Shark", "squalo"),
            ("Carp", "carpa"),
            ("Tilapia", "tilapia"),
            ("Eel", "anguilla"),
            ("Catfish", "pesce gatto"),
            ("Swordfish", "pesce spada")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.5 - Herbs & Spices": {
        "count": 17,
        "words": [
            ("Salt", "sale"),
            ("Pepper", "pepe"),
            ("Caraway", "cumino"),
            ("Garlic", "aglio"),
            ("Basil", "basilico"),
            ("Coriander", "coriandolo"),
            ("Fennel", "finocchio"),
            ("Marjoram", "maggiorana"),
            ("Oregano", "origano"),
            ("Parsley", "prezzemolo"),
            ("Rosemary", "rosmarino"),
            ("Sage", "salvia"),
            ("Thyme", "timo"),
            ("Nutmeg", "noce moscata"),
            ("Paprika", "paprika"),
            ("Cayenne", "pepe di caienna"),
            ("Ginger", "zenzero")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.6 - Vegetables": {
        "count": 28,
        "words": [
            ("Celery", "sedano"),
            ("Eggplant", "melanzana"),
            ("Zucchini", "zucchine"),
            ("Onion", "cipolla"),
            ("Spinach", "spinaci"),
            ("Salad", "insalata"),
            ("Green beans", "fagiolini"),
            ("Cucumber", "cetriolo"),
            ("Radish", "ravanello"),
            ("Cabbage", "cavolo"),
            ("Mushrooms", "funghi"),
            ("Lettuce", "lattuga"),
            ("Corn", "mais"),
            ("Potatoes", "patate"),
            ("Tomato", "pomodoro"),
            ("Carrot", "carota"),
            ("Plantain", "banana platano"),
            ("Beans", "fagioli"),
            ("Leek", "porro"),
            ("Lotus root", "radice di loto"),
            ("Bamboo shoot", "germoglio di bambu"),
            ("Artichoke", "carciofo"),
            ("Asparagus", "asparagi"),
            ("Brussels sprouts", "cavolini di bruxelles"),
            ("Broccoli", "broccoli"),
            ("Peas", "piselli"),
            ("Cauliflower", "cavolfiore"),
            ("Chili pepper", "peperoncino")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.7 - Fruits": {
        "count": 27,
        "words": [
            ("Cherries", "ciliegie"),
            ("Raspberries", "lamponi"),
            ("Blueberries", "mirtilli"),
            ("Strawberries", "fragole"),
            ("Lemon", "limone"),
            ("Lime", "lime"),
            ("Apple", "mela"),
            ("Orange", "arancia"),
            ("Pear", "pera"),
            ("Banana", "banana"),
            ("Grapes", "uva"),
            ("Grapefruit", "pompelmo"),
            ("Watermelon", "anguria"),
            ("Pineapple", "ananas"),
            ("Plum", "prugna"),
            ("Peach", "pesca"),
            ("Mango", "mango"),
            ("Apricot", "albicocca"),
            ("Pomegranate", "melograno"),
            ("Persimmon", "caco"),
            ("Kiwi", "kiwi"),
            ("Litchi", "litchi"),
            ("Longan", "longan"),
            ("Balsam pear", "zucca amara"),
            ("Passion fruit", "frutto della passione"),
            ("Avocado", "avocado"),
            ("Coconut", "cocco")
        ],
        "is_numbers": False
    },
    
    "Lesson 12 - Numbers 31-50": {
        "count": 20,
        "words": [
            ("31", "trentuno"),
            ("32", "trentadue"),
            ("33", "trentatre"),
            ("34", "trentaquattro"),
            ("35", "trentacinque"),
            ("36", "trentasei"),
            ("37", "trentasette"),
            ("38", "trentotto"),
            ("39", "trentanove"),
            ("40", "quaranta"),
            ("41", "quarantuno"),
            ("42", "quarantadue"),
            ("43", "quarantatre"),
            ("44", "quarantaquattro"),
            ("45", "quarantacinque"),
            ("46", "quarantasei"),
            ("47", "quarantasette"),
            ("48", "quarantotto"),
            ("49", "quarantanove"),
            ("50", "cinquanta")
        ],
        "is_numbers": True
    },
    
    "Lesson 13.1 - Irregular -ARE Verbs": {
        "count": 19,
        "words": [
            ("to go", "andare"),
            ("to give", "dare"),
            ("to find", "trovare"),
            ("to stand", "stare"),
            ("to begin", "cominciare"),
            ("to do/make", "fare"),
            ("to drive", "guidare"),
            ("to forget", "dimenticare"),
            ("to meet", "incontrare"),
            ("to pay", "pagare"),
            ("to speak", "parlare"),
            ("to spend (time)", "passare"),
            ("to swim", "nuotare"),
            ("to teach", "insegnare"),
            ("to tell", "raccontare"),
            ("to think", "pensare"),
            ("to throw", "lanciare"),
            ("to bring", "portare"),
            ("to send", "inviare")
        ],
        "is_numbers": False
    },
    
    "Lesson 13.2 - Irregular -ERE Verbs": {
        "count": 22,
        "words": [
            ("to be", "essere"),
            ("to have", "avere"),
            ("to see", "vedere"),
            ("to drink", "bere"),
            ("to know (fact)", "sapere"),
            ("to want", "volere"),
            ("to run", "correre"),
            ("to sit", "sedere"),
            ("to lie down", "giacere"),
            ("to take", "prendere"),
            ("to write", "scrivere"),
            ("to fall", "cadere"),
            ("to break", "rompere"),
            ("to put", "mettere"),
            ("to read", "leggere"),
            ("to get", "ottenere"),
            ("to hold", "tenere"),
            ("to win", "vincere"),
            ("to choose", "scegliere")
        ],
        "is_numbers": False
    },
    
    "Lesson 13.3 - Irregular -IRE Verbs": {
        "count": 9,
        "words": [
            ("to come", "venire"),
            ("to eat", "mangiare"),
            ("to understand", "capire"),
            ("to say", "dire"),
            ("to sleep", "dormire"),
            ("to build", "costruire"),
            ("to hear", "sentire"),
            ("to leave", "partire")
        ],
        "is_numbers": False
    },
    
    "Lesson 15 - Physical Appearance": {
        "count": 38,
        "words": [
            ("Tall", "alto"),
            ("Short (height)", "basso"),
            ("Slim", "snello"),
            ("Fat", "grasso"),
            ("Muscular", "muscoloso"),
            ("Blonde", "biondo"),
            ("Brown-haired", "castano"),
            ("Black-haired", "moro"),
            ("Curly hair", "ricci"),
            ("Straight hair", "lisci"),
            ("Blue eyes", "occhi azzurri"),
            ("Brown eyes", "occhi castani"),
            ("Green eyes", "occhi verdi"),
            ("Beautiful", "bello/bella"),
            ("Handsome", "bello"),
            ("Ugly", "brutto"),
            ("Young", "giovane"),
            ("Old", "vecchio"),
            ("Beard", "barba"),
            ("Light-skinned", "pelle chiara"),
            ("Dark-skinned", "pelle scura"),
            ("Freckles", "lentiggini"),
            ("Wrinkles", "rughe"),
            ("Bald", "calvo"),
            ("Hairy (body)", "peloso"),
            ("Straight nose", "naso dritto"),
            ("Big nose", "naso grande"),
            ("Small nose", "naso piccolo"),
            ("Thin lips", "labbra sottili"),
            ("Full lips", "labbra carnose"),
            ("Broad shoulders", "spalle larghe"),
            ("Narrow shoulders", "spalle strette"),
            ("Tanned skin", "pelle abbronzata"),
            ("Pale skin", "pelle pallida"),
            ("Wavy hair", "capelli mossi"),
            ("Ponytail", "coda di cavallo"),
            ("Braids", "trecce"),
            ("Beard and mustache", "barba e baffi")
        ],
        "is_numbers": False
    },
    
    "Lesson 16 - Occupations": {
        "count": 25,
        "words": [
            ("Doctor", "dottore/medico"),
            ("Teacher", "insegnante"),
            ("Engineer", "ingegnere"),
            ("Lawyer", "avvocato"),
            ("Salesperson", "commesso"),
            ("Police officer", "poliziotto"),
            ("Firefighter", "pompiere"),
            ("Programmer", "programmatore"),
            ("Cook/Chef", "cuoco"),
            ("Journalist", "giornalista"),
            ("Nurse", "infermiere/infermiera"),
            ("Architect", "architetto"),
            ("Accountant", "contabile"),
            ("Pharmacist", "farmacista"),
            ("Driver", "autista"),
            ("Mechanic", "meccanico"),
            ("Scientist", "scienziato"),
            ("Dentist", "dentista"),
            ("Musician", "musicista"),
            ("Actor", "attore/attrice"),
            ("Artist", "artista"),
            ("Pilot", "pilota"),
            ("Farmer", "contadino"),
            ("Photographer", "fotografo"),
            ("Waiter/Waitress", "cameriere/cameriera")
        ],
        "is_numbers": False
    },
    
    "Lesson 17 - Sports": {
        "count": 30,
        "words": [
            ("Football/Soccer", "calcio"),
            ("Basketball", "pallacanestro"),
            ("Volleyball", "pallavolo"),
            ("Tennis", "tennis"),
            ("Swimming", "nuoto"),
            ("Running/Athletics", "corsa/atletica"),
            ("Ice hockey", "hockey su ghiaccio"),
            ("Skiing", "sci"),
            ("Cycling", "ciclismo"),
            ("Boxing", "pugilato/boxe"),
            ("Martial arts", "arti marziali"),
            ("Golf", "golf"),
            ("Table tennis", "tennis da tavolo"),
            ("Wrestling", "lotta"),
            ("Handball", "pallamano"),
            ("Baseball", "baseball"),
            ("Surfing", "surf"),
            ("Skating", "pattinaggio"),
            ("Horse riding", "equitazione"),
            ("Diving", "immersione"),
            ("Cricket", "cricket"),
            ("Rugby", "rugby"),
            ("Ballet", "balletto"),
            ("Bowling", "bowling"),
            ("Weightlifting", "sollevamento pesi"),
            ("Windsurfing", "windsurf"),
            ("Ice skating", "pattinaggio su ghiaccio"),
            ("Rowing", "canottaggio"),
            ("Archery", "tiro con l'arco"),
            ("Climbing", "arrampicata")
        ],
        "is_numbers": False
    },
    
    "Lesson 18 - Numbers 51-75": {
        "count": 25,
        "words": [
            ("51", "cinquantuno"),
            ("52", "cinquantadue"),
            ("53", "cinquantatre"),
            ("54", "cinquantaquattro"),
            ("55", "cinquantacinque"),
            ("56", "cinquantasei"),
            ("57", "cinquantasette"),
            ("58", "cinquantotto"),
            ("59", "cinquantanove"),
            ("60", "sessanta"),
            ("61", "sessantuno"),
            ("62", "sessantadue"),
            ("63", "sessantatre"),
            ("64", "sessantaquattro"),
            ("65", "sessantacinque"),
            ("66", "sessantasei"),
            ("67", "sessantasette"),
            ("68", "sessantotto"),
            ("69", "sessantanove"),
            ("70", "settanta"),
            ("71", "settantuno"),
            ("72", "settantadue"),
            ("73", "settantatre"),
            ("74", "settantquattro"),
            ("75", "settantacinque")
        ],
        "is_numbers": True
    },
    
    "Lesson 19 - Clothing": {
        "count": 42,
        "words": [
            ("Shirt", "camicia"),
            ("T-shirt", "maglietta"),
            ("Blouse", "blusa"),
            ("Sweater", "maglione"),
            ("Jacket", "giacca"),
            ("Coat", "cappotto"),
            ("Dress", "vestito"),
            ("Skirt", "gonna"),
            ("Pants", "pantaloni"),
            ("Shorts", "pantaloncini"),
            ("Shoes", "scarpe"),
            ("Boots", "stivali"),
            ("Sneakers", "scarpe da ginnastica"),
            ("Sandals", "sandali"),
            ("Hat/Cap", "cappello"),
            ("Scarf", "sciarpa"),
            ("Gloves", "guanti"),
            ("Belt", "cintura"),
            ("Socks", "calze"),
            ("Winter coat", "cappotto invernale"),
            ("Wool hat", "berretto di lana"),
            ("Snow boots", "doposci"),
            ("Swimsuit", "costume da bagno"),
            ("Sunglasses", "occhiali da sole"),
            ("Flip-flops", "infradito"),
            ("Tank top", "canottiera"),
            ("Suit", "abito"),
            ("Tie", "cravatta"),
            ("Blazer", "blazer"),
            ("High heels", "tacchi alti"),
            ("Evening dress", "abito da sera"),
            ("Black", "nero"),
            ("White", "bianco"),
            ("Red", "rosso"),
            ("Blue", "blu"),
            ("Green", "verde"),
            ("Cotton", "cotone"),
            ("Wool", "lana"),
            ("Leather", "pelle"),
            ("Silk", "seta"),
            ("Linen", "lino")
        ],
        "is_numbers": False
    },
    
    "Lesson 20 - Adverbs": {
        "count": 20,
        "words": [
            ("Quickly", "velocemente"),
            ("Slowly", "lentamente"),
            ("Always", "sempre"),
            ("Never", "mai"),
            ("Often", "spesso"),
            ("Sometimes", "qualche volta"),
            ("Rarely", "raramente"),
            ("Already", "gia"),
            ("Still", "ancora"),
            ("Yet", "ancora"),
            ("Soon", "presto"),
            ("Now", "ora"),
            ("Later", "piu tardi"),
            ("Today", "oggi"),
            ("Tomorrow", "domani"),
            ("Yesterday", "ieri"),
            ("Clearly", "chiaramente"),
            ("Together", "insieme"),
            ("Apart", "separatamente"),
            ("Forever", "per sempre")
        ],
        "is_numbers": False
    },
    
    "Lesson 21 - Animals": {
        "count": 20,
        "words": [
            ("Dog", "cane"),
            ("Cat", "gatto"),
            ("Horse", "cavallo"),
            ("Cow", "mucca"),
            ("Sheep", "pecora"),
            ("Pig", "maiale"),
            ("Goat", "capra"),
            ("Chicken", "pollo"),
            ("Duck", "anatra"),
            ("Bird", "uccello"),
            ("Rabbit", "coniglio"),
            ("Mouse", "topo"),
            ("Lion", "leone"),
            ("Tiger", "tigre"),
            ("Bear", "orso"),
            ("Elephant", "elefante"),
            ("Monkey", "scimmia"),
            ("Fox", "volpe"),
            ("Wolf", "lupo"),
            ("Deer", "cervo")
        ],
        "is_numbers": False
    },
    
    "Lesson 23 - Places in Town": {
        "count": 20,
        "words": [
            ("School", "scuola"),
            ("Hospital", "ospedale"),
            ("Bank", "banca"),
            ("Restaurant", "ristorante"),
            ("Library", "biblioteca"),
            ("Supermarket", "supermercato"),
            ("Cinema", "cinema"),
            ("Post office", "posta"),
            ("Police station", "stazione di polizia"),
            ("Park", "parco"),
            ("Museum", "museo"),
            ("Theatre", "teatro"),
            ("Hotel", "hotel"),
            ("Stadium", "stadio"),
            ("Church", "chiesa"),
            ("Pharmacy", "farmacia"),
            ("Bakery", "panetteria"),
            ("Butcher", "macelleria"),
            ("Market", "mercato"),
            ("Hairdresser", "parrucchiere")
        ],
        "is_numbers": False
    },
    
    "Lesson 24 - School Supplies": {
        "count": 20,
        "words": [
            ("Book", "libro"),
            ("Pen", "penna"),
            ("Pencil", "matita"),
            ("Eraser", "gomma"),
            ("Notebook", "quaderno"),
            ("Ruler", "righello"),
            ("Scissors", "forbici"),
            ("Backpack", "zaino"),
            ("Folder", "cartella"),
            ("Calculator", "calcolatrice"),
            ("Marker", "pennarello"),
            ("Chalk", "gesso"),
            ("Map", "mappa"),
            ("Highlighter", "evidenziatore"),
            ("Projector", "proiettore"),
            ("Laptop", "portatile"),
            ("Printer", "stampante"),
            ("USB stick", "chiavetta usb"),
            ("Schoolbag", "cartella"),
            ("Sharpener", "temperino")
        ],
        "is_numbers": False
    },
    
    "Lesson 25 - Transportation": {
        "count": 20,
        "words": [
            ("Car", "macchina"),
            ("Bus", "autobus"),
            ("Train", "treno"),
            ("Bicycle", "bicicletta"),
            ("Motorcycle", "moto"),
            ("Airplane", "aereo"),
            ("Boat", "barca"),
            ("Tram", "tram"),
            ("Taxi", "taxi"),
            ("Subway", "metropolitana"),
            ("Ferry", "traghetto"),
            ("Yacht", "yacht"),
            ("Hot air balloon", "mongolfiera"),
            ("Spaceship", "astronave"),
            ("Rickshaw", "riscio"),
            ("Gondola", "gondola"),
            ("Zeppelin", "dirigibile"),
            ("Rollerblades", "pattini in linea"),
            ("Canoe", "canoa"),
            ("Submarine", "sottomarino")
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
        for english, italian in words:
            questions.append({
                'type': 'num_to_word',
                'question': f"What is '{english}' in Italian? (Answer with the WORD)",
                'answer': italian,
                'display_answer': italian  # Show WORD
            })
        
        # Type 2: Word to number (Answer: NUMBER)
        for english, italian in words:
            questions.append({
                'type': 'word_to_num',
                'question': f"What number is '{italian}'? (Answer with the NUMBER)",
                'answer': english,
                'display_answer': english  # Show NUMBER
            })
        
        # Type 3: Mixed (Answer based on type)
        for english, italian in words:
            if random.choice([True, False]):
                # Number to word
                questions.append({
                    'type': 'mixed',
                    'question': f"Translate '{english}' to Italian word:",
                    'answer': italian,
                    'display_answer': italian  # WORD
                })
            else:
                # Word to number
                questions.append({
                    'type': 'mixed',
                    'question': f"What number is '{italian}'?",
                    'answer': english,
                    'display_answer': english  # NUMBER
                })
    
    elif count <= 20:
        # 20 or less: 3 different question types
        # Type 1: English -> Italian
        for english, italian in words:
            questions.append({
                'type': 'eng_to_ita',
                'question': f"Translate to Italian: '{english}'",
                'answer': italian,
                'display_answer': italian
            })
        
        # Type 2: Italian -> English
        for english, italian in words:
            questions.append({
                'type': 'ita_to_eng',
                'question': f"Translate to English: '{italian}'",
                'answer': english,
                'display_answer': english
            })
        
        # Type 3: First letter hint
        for english, italian in words:
            first_letter = italian[0] if italian else ""
            blanks = "_" * (len(italian) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}' - Complete the Italian word",
                'answer': italian,
                'display_answer': italian
            })
    
    elif 20 < count <= 40:
        # 20-40: 3 sections, 2 different question types
        third = len(words) // 3
        
        # Section 1: English -> Italian
        for english, italian in words[:third]:
            questions.append({
                'type': 'eng_to_ita',
                'question': f"Translate to Italian: '{english}'",
                'answer': italian,
                'display_answer': italian
            })
        
        # Section 2: Italian -> English
        for english, italian in words[third:third*2]:
            questions.append({
                'type': 'ita_to_eng',
                'question': f"Translate to English: '{italian}'",
                'answer': english,
                'display_answer': english
            })
        
        # Section 3: First letter hint
        for english, italian in words[third*2:]:
            first_letter = italian[0] if italian else ""
            blanks = "_" * (len(italian) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': italian,
                'display_answer': italian
            })
    
    else:  # count > 40
        # 40+: 5 sections, 3-4 different question types
        fifth = len(words) // 5
        
        # Section 1: English -> Italian
        for english, italian in words[:fifth]:
            questions.append({
                'type': 'eng_to_ita',
                'question': f"Translate to Italian: '{english}'",
                'answer': italian,
                'display_answer': italian
            })
        
        # Section 2: Italian -> English
        for english, italian in words[fifth:fifth*2]:
            questions.append({
                'type': 'ita_to_eng',
                'question': f"Translate to English: '{italian}'",
                'answer': english,
                'display_answer': english
            })
        
        # Section 3: First letter
        for english, italian in words[fifth*2:fifth*3]:
            first_letter = italian[0] if italian else ""
            blanks = "_" * (len(italian) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': italian,
                'display_answer': italian
            })
        
        # Section 4: Last letter
        for english, italian in words[fifth*3:fifth*4]:
            last_letter = italian[-1] if italian else ""
            blanks = "_" * (len(italian) - 1)
            questions.append({
                'type': 'last_letter',
                'question': f"'{english}' = '{blanks}{last_letter}'",
                'answer': italian,
                'display_answer': italian
            })
        
        # Section 5: Letter count hint
        for english, italian in words[fifth*4:]:
            questions.append({
                'type': 'letter_hint',
                'question': f"'{english}' = ({len(italian)} letters, starts with {italian[:2]}...)",
                'answer': italian,
                'display_answer': italian
            })
    
    return questions

def create_general_review(lesson_name, words, is_numbers):
    """General review questions after each lesson"""
    review = []
    sample_size = min(20, len(words))
    sampled_words = random.sample(words, sample_size)
    
    for english, italian in sampled_words:
        if is_numbers:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] '{english}' in Italian?",
                    'answer': italian,
                    'display_answer': italian
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] What number is '{italian}'?",
                    'answer': english,
                    'display_answer': english
                })
        else:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{english}'",
                    'answer': italian,
                    'display_answer': italian
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{italian}'",
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
║        COMPREHENSIVE ITALIAN TEST SYSTEM                  ║
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
        print(Fore.GREEN + "🎉🎉🎉 EXCELLENT! You're amazing at Italian! 🎉🎉🎉")
    elif final_percentage >= 70:
        print(Fore.BLUE + "👏👏👏 VERY GOOD! Great performance! 👏👏👏")
    elif final_percentage >= 50:
        print(Fore.YELLOW + "👍👍 GOOD! Keep going and you'll be excellent! 👍👍")
    else:
        print(Fore.RED + "📚📚 Keep studying! You can do it! 📚📚")
    
    print(Fore.GREEN + "\nCongratulations! You completed the entire test! 🎊")

if __name__ == "__main__":
    main()