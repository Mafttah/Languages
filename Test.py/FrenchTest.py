import random
from colorama import Fore, Style, init
import unicodedata

# Colorama'yı başlat
init(autoreset=True)

def normalize_text(text):
    """Normalize text by removing accents"""
    text = text.lower().strip()
    # Remove accents
    text = unicodedata.normalize('NFD', text)
    text = ''.join(char for char in text if unicodedata.category(char) != 'Mn')
    return text

# KODUNUZDAN ALINAN TÜM MADDELER - SIRAYLA
lessons_data = {
    "Lesson 1 - Numbers 1-10": {
        "count": 10,
        "words": [
            ("1", "une"),
            ("2", "deux"),
            ("3", "trois"),
            ("4", "quatre"),
            ("5", "cinq"),
            ("6", "six"),
            ("7", "sept"),
            ("8", "huit"),
            ("9", "neuf"),
            ("10", "dix")
        ],
        "is_numbers": True
    },
    
    "Lesson 2 - Greetings": {
        "count": 18,
        "words": [
            ("Hello", "salut"),
            ("How are you?", "comment allez-vous"),
            ("Nice to see you", "content de vous voir"),
            ("Nice to meet you", "enchante"),
            ("See you tomorrow", "a demain"),
            ("Good morning", "bonjour"),
            ("Good afternoon", "bonne apres-midi"),
            ("Good evening", "bonsoir"),
            ("Good night", "bonne nuit"),
            ("What is your name?", "quel est ton nom"),
            ("My name is", "mon nom est"),
            ("Where do you live?", "ou habites-tu"),
            ("Where are you from?", "d'ou venez-vous"),
            ("Have a nice day", "bonne journee"),
            ("See you later", "a la prochaine"),
            ("Goodbye", "au revoir"),
            ("Please", "s'il vous plait"),
            ("Thank you", "merci")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.1 - Regular -ER Verbs": {
        "count": 38,
        "words": [
            ("to lower", "abaisser"),
            ("to ruin", "abimer"),
            ("to like/love", "aimer"),
            ("to arrive", "arriver"),
            ("to move", "bouger"),
            ("to brush", "brosser"),
            ("to change", "changer"),
            ("to sing", "chanter"),
            ("to look for", "chercher"),
            ("to begin", "commencer"),
            ("to correct", "corriger"),
            ("to dance", "danser"),
            ("to ask for", "demander"),
            ("to hate", "detester"),
            ("to give", "donner"),
            ("to listen to", "ecouter"),
            ("to erase", "effacer"),
            ("to study", "etudier"),
            ("to congratulate", "feliciter"),
            ("to celebrate", "feter"),
            ("to win/earn", "gagner"),
            ("to slide", "glisser"),
            ("to live", "habiter"),
            ("to play", "jouer"),
            ("to eat", "manger"),
            ("to miss", "manquer"),
            ("to walk", "marcher"),
            ("to climb", "monter"),
            ("to swim", "nager"),
            ("to speak", "parler"),
            ("to share", "partager"),
            ("to think", "penser"),
            ("to watch", "regarder"),
            ("to ski", "skier"),
            ("to work", "travailler"),
            ("to find", "trouver"),
            ("to visit", "visiter"),
            ("to travel", "voyager")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.2 - Regular -IR Verbs": {
        "count": 28,
        "words": [
            ("to abolish", "abolir"),
            ("to accomplish", "accomplir"),
            ("to act", "agir"),
            ("to enlarge", "agrandir"),
            ("to warn", "avertir"),
            ("to build", "batir"),
            ("to bless", "benir"),
            ("to whiten", "blanchir"),
            ("to choose", "choisir"),
            ("to convert", "convertir"),
            ("to define", "definir"),
            ("to establish", "etablir"),
            ("to stun", "etourdir"),
            ("to finish", "finir"),
            ("to clear", "franchir"),
            ("to gain weight", "grossir"),
            ("to cure", "guerir"),
            ("to invest", "investir"),
            ("to lose weight", "maigrir"),
            ("to feed", "nourrir"),
            ("to obey", "obeir"),
            ("to punish", "punir"),
            ("to reflect", "reflechir"),
            ("to fill", "remplir"),
            ("to succeed", "reussir"),
            ("to blush", "rougir"),
            ("to seize", "saisir"),
            ("to age", "vieillir")
        ],
        "is_numbers": False
    },
    
    "Lesson 3.3 - Regular -RE Verbs": {
        "count": 19,
        "words": [
            ("to wait for", "attendre"),
            ("to confuse", "confondre"),
            ("to correspond", "correspondre"),
            ("to defend", "defendre"),
            ("to depend", "dependre"),
            ("to descend", "descendre"),
            ("to hear", "entendre"),
            ("to stretch", "etendre"),
            ("to melt", "fondre"),
            ("to bite", "mordre"),
            ("to hang", "pendre"),
            ("to lose", "perdre"),
            ("to claim", "pretendre"),
            ("to give back", "rendre"),
            ("to spread", "repandre"),
            ("to answer", "repondre"),
            ("to suspend", "suspendre"),
            ("to twist", "tordre"),
            ("to sell", "vendre")
        ],
        "is_numbers": False
    },
    
    "Lesson 4 - Adjectives": {
        "count": 35,
        "words": [
            ("Happy", "heureux"),
            ("Sad", "triste"),
            ("Angry", "enerve"),
            ("Afraid", "peur"),
            ("Joy", "joie"),
            ("Surprised", "surpris"),
            ("Calm", "calme"),
            ("Bored", "ennuye"),
            ("Easy", "facile"),
            ("Difficult", "difficile"),
            ("Bad", "mauvais"),
            ("Good", "bon"),
            ("Noisy", "bruyant"),
            ("Quiet", "silencieux"),
            ("Strong", "fort"),
            ("Weak", "faible"),
            ("Hard", "dur"),
            ("Soft", "mou"),
            ("More", "plus"),
            ("Less", "moins"),
            ("Clean", "propre"),
            ("Dirty", "sale"),
            ("Old", "vieux"),
            ("New", "nouveau"),
            ("Big", "grand"),
            ("Small", "petit"),
            ("Young", "jeune"),
            ("Skinny", "maigre"),
            ("Fat", "gros"),
            ("Pretty", "joli"),
            ("Ugly", "laid"),
            ("Thick", "epais"),
            ("Thin", "mince"),
            ("Rough", "reche"),
            ("Smooth", "lisse")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.1 - Days": {
        "count": 11,
        "words": [
            ("The days of the week", "les jours de la semaine"),
            ("Day", "jour"),
            ("Week", "semaine"),
            ("Monday", "lundi"),
            ("Tuesday", "mardi"),
            ("Wednesday", "mercredi"),
            ("Thursday", "jeudi"),
            ("Friday", "vendredi"),
            ("Saturday", "samedi"),
            ("Sunday", "dimanche"),
            ("Weekend", "fin de semaine")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.2 - Months": {
        "count": 15,
        "words": [
            ("The months of the year", "les mois de l'annee"),
            ("Month", "mois"),
            ("Year", "annee"),
            ("January", "janvier"),
            ("February", "fevrier"),
            ("March", "mars"),
            ("April", "avril"),
            ("May", "mai"),
            ("June", "juin"),
            ("July", "juillet"),
            ("August", "aout"),
            ("September", "septembre"),
            ("October", "octobre"),
            ("November", "novembre"),
            ("December", "decembre")
        ],
        "is_numbers": False
    },
    
    "Lesson 6 - Seasons & Weather": {
        "count": 23,
        "words": [
            ("Seasons", "les saisons"),
            ("Winter", "hiver"),
            ("Summer", "ete"),
            ("Spring", "printemps"),
            ("Autumn", "automne"),
            ("Sky", "ciel"),
            ("Cloud", "nuage"),
            ("Rainbow", "arc-en-ciel"),
            ("Cold", "froid"),
            ("Hot", "chaud"),
            ("It is hot", "il fait chaud"),
            ("It is cold", "il fait froid"),
            ("It is sunny", "il y a du soleil"),
            ("It is cloudy", "il fait nuageux"),
            ("It is humid", "il fait humide"),
            ("It is raining", "il pleut"),
            ("It is snowing", "il neige"),
            ("It is windy", "il y a du vent"),
            ("How is the weather?", "quel temps fait-il"),
            ("Good weather", "beau temps"),
            ("Bad weather", "mauvais temps"),
            ("What is the temperature?", "quelle temperature fait-il"),
            ("It is 24 degrees", "il fait 24 degres")
        ],
        "is_numbers": False
    },
    
    "Lesson 7 - Colors": {
        "count": 14,
        "words": [
            ("Black", "noir"),
            ("Blue", "bleu"),
            ("Brown", "marron"),
            ("Green", "vert"),
            ("Orange", "orange"),
            ("Purple", "violet"),
            ("Red", "rouge"),
            ("White", "blanc"),
            ("Yellow", "jaune"),
            ("Gray", "gris"),
            ("Gold", "dore"),
            ("Silver", "argente"),
            ("What color is it?", "quelle couleur est-ce"),
            ("The color is", "c'est")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.1 - Family": {
        "count": 36,
        "words": [
            ("Mother", "mere"),
            ("Father", "pere"),
            ("Brother", "frere"),
            ("Sister", "soeur"),
            ("Son", "fils"),
            ("Daughter", "fille"),
            ("Parents", "parents"),
            ("Children", "enfants"),
            ("Child", "enfant"),
            ("Stepmother", "belle-mere"),
            ("Stepfather", "beau-pere"),
            ("Stepsister", "demi-soeur"),
            ("Stepbrother", "demi-frere"),
            ("Son-in-law", "gendre"),
            ("Daughter-in-law", "belle-fille"),
            ("Wife", "epouse"),
            ("Husband", "mari"),
            ("Grandparents", "grands-parents"),
            ("Grandfather", "grand-pere"),
            ("Grandmother", "grand-mere"),
            ("Grandson", "petit-fils"),
            ("Granddaughter", "petite-fille"),
            ("Grandchildren", "petits-enfants"),
            ("Grandchild", "petit enfant"),
            ("Aunt", "tante"),
            ("Uncle", "oncle"),
            ("Cousin (female)", "cousine"),
            ("Cousin (male)", "cousin"),
            ("Nephew", "neveu"),
            ("Niece", "niece"),
            ("Father-in-law", "beau-pere"),
            ("Mother-in-law", "belle-mere"),
            ("Brother-in-law", "beau-frere"),
            ("Sister-in-law", "belle-soeur"),
            ("Relative", "proche")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.2 - Friends": {
        "count": 14,
        "words": [
            ("Miss", "mademoiselle"),
            ("Boy", "garcon"),
            ("Girl", "fille"),
            ("Baby", "bebe"),
            ("Woman", "femme"),
            ("Man", "homme"),
            ("Friend (male)", "ami"),
            ("Friend (female)", "amie"),
            ("Boyfriend", "petit ami"),
            ("Girlfriend", "petite amie"),
            ("Gentleman", "monsieur"),
            ("Lady", "dame"),
            ("Neighbor (male)", "voisin"),
            ("Neighbor (female)", "voisine")
        ],
        "is_numbers": False
    },
    
    "Lesson 9 - Numbers 11-30": {
        "count": 20,
        "words": [
            ("11", "onze"),
            ("12", "douze"),
            ("13", "treize"),
            ("14", "quatorze"),
            ("15", "quinze"),
            ("16", "seize"),
            ("17", "dix-sept"),
            ("18", "dix-huit"),
            ("19", "dix-neuf"),
            ("20", "vingt"),
            ("21", "vingt et un"),
            ("22", "vingt-deux"),
            ("23", "vingt-trois"),
            ("24", "vingt-quatre"),
            ("25", "vingt-cinq"),
            ("26", "vingt-six"),
            ("27", "vingt-sept"),
            ("28", "vingt-huit"),
            ("29", "vingt-neuf"),
            ("30", "trente")
        ],
        "is_numbers": True
    },
    
    "Lesson 10.1 - Prepositions": {
        "count": 36,
        "words": [
            ("For", "pour"),
            ("From", "depuis"),
            ("In", "dans"),
            ("Inside", "a l'interieur"),
            ("Into", "dans"),
            ("Near", "pres"),
            ("Of", "de"),
            ("Out", "hors"),
            ("Outside", "a l'exterieur"),
            ("To", "a"),
            ("Under", "sous"),
            ("With", "avec"),
            ("Without", "sans"),
            ("Above", "au-dessus"),
            ("Across", "de l'autre cote"),
            ("After", "apres"),
            ("Against", "contre"),
            ("Along", "le long"),
            ("Around", "autour"),
            ("At", "a"),
            ("Behind", "derriere"),
            ("Below", "en-dessous"),
            ("Beside", "a cote de"),
            ("Between", "entre"),
            ("By", "pres"),
            ("During", "pendant"),
            ("Except", "sauf"),
            ("And", "et"),
            ("Because", "parce que"),
            ("But", "mais"),
            ("Or", "ou"),
            ("Everywhere", "partout"),
            ("Everyone", "tout le monde"),
            ("Everything", "tout"),
            ("Few", "peu"),
            ("Some", "certains"),
            ("Many", "beaucoup")
        ],
        "is_numbers": False
    },
    
    "Lesson 10.2 - Useful Words": {
        "count": 29,
        "words": [
            ("Question", "question"),
            ("Answer", "reponse"),
            ("Truth", "verite"),
            ("Lie", "mensonge"),
            ("Nothing", "rien"),
            ("Something", "quelque chose"),
            ("Same", "le meme"),
            ("Different", "different"),
            ("Pull", "tirer"),
            ("Push", "pousser"),
            ("Long", "long"),
            ("Short", "court"),
            ("Cold", "froid"),
            ("Hot", "chaud"),
            ("Light", "clair"),
            ("Dark", "fonce"),
            ("Wet", "mouille"),
            ("Dry", "sec"),
            ("Empty", "vide"),
            ("Full", "plein"),
            ("How?", "comment"),
            ("What?", "quoi"),
            ("When?", "quand"),
            ("Where?", "ou"),
            ("Which?", "lequel"),
            ("Who?", "qui"),
            ("Why?", "pourquoi"),
            ("How long?", "combien de temps"),
            ("How much?", "combien")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.1 - Drinks": {
        "count": 9,
        "words": [
            ("Coffee", "cafe"),
            ("Tea", "the"),
            ("Soft drink", "boisson gazeuse"),
            ("Water", "eau"),
            ("Lemonade", "limonade"),
            ("Juice", "jus"),
            ("Orange juice", "jus d'orange"),
            ("I would like a glass of water please", "je voudrais un verre d'eau s'il vous plait"),
            ("With ice", "avec glaçons")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.2 - Dairy Products": {
        "count": 19,
        "words": [
            ("Milk", "lait"),
            ("Ice cream", "glace"),
            ("Butter", "beurre"),
            ("Cheese", "fromage"),
            ("Cottage cheese", "fromage cottage"),
            ("Cream", "creme"),
            ("Sour cream", "creme fraiche"),
            ("Yogurt", "yaourt"),
            ("Eggs", "oeufs"),
            ("Whipping cream", "creme chantilly"),
            ("Bakery", "boulangerie-patisserie"),
            ("Baguette", "baguette"),
            ("Doughnut", "beignet"),
            ("Cookie", "petit gateau"),
            ("Roll", "petit pain"),
            ("Dessert", "dessert"),
            ("Cake", "gateau"),
            ("Bread", "pain"),
            ("Pie", "tarte")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.3 - Meats": {
        "count": 13,
        "words": [
            ("Beef", "boeuf"),
            ("Veal", "veau"),
            ("Ham", "jambon"),
            ("Chicken", "poulet"),
            ("Turkey", "dinde"),
            ("Duck", "canard"),
            ("Bacon", "lard"),
            ("Pork", "porc"),
            ("Filet mignon", "filet mignon"),
            ("Sausage", "saucisse"),
            ("Lamb chop", "cotelette d'agneau"),
            ("Pork chop", "cotelette de porc"),
            ("Meat", "viande")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.4 - Seafoods": {
        "count": 20,
        "words": [
            ("Fish", "poisson"),
            ("Shellfish", "fruits de mer"),
            ("Bass", "perche"),
            ("Salmon", "saumon"),
            ("Lobster", "homard"),
            ("Crab", "crabe"),
            ("Mussel", "moule"),
            ("Oyster", "huitre"),
            ("Cod", "cabillaud"),
            ("Clam", "palourde"),
            ("Shrimp", "crevette"),
            ("Tuna", "thon"),
            ("Trout", "truite"),
            ("Sole", "sole"),
            ("Shark", "requin"),
            ("Carp", "carpe"),
            ("Tilapia", "tilapia"),
            ("Eel", "anguille"),
            ("Catfish", "poisson-chat"),
            ("Swordfish", "espadon")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.5 - Herbs & Spices": {
        "count": 17,
        "words": [
            ("Salt", "sel"),
            ("Pepper", "poivre"),
            ("Caraway", "carvi"),
            ("Garlic", "ail"),
            ("Basil", "basilic"),
            ("Coriander", "coriandre"),
            ("Fennel", "fenouil"),
            ("Marjoram", "marjolaine"),
            ("Oregano", "origan"),
            ("Parsley", "persil"),
            ("Rosemary", "romarin"),
            ("Sage", "sauge"),
            ("Thyme", "thym"),
            ("Nutmeg", "muscade"),
            ("Paprika", "paprika"),
            ("Cayenne", "cayenne"),
            ("Ginger", "gingembre")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.6 - Vegetables": {
        "count": 28,
        "words": [
            ("Celery", "celeri"),
            ("Eggplant", "aubergine"),
            ("Zucchini", "courgette"),
            ("Onion", "oignon"),
            ("Spinach", "epinards"),
            ("Salad", "salade"),
            ("Green beans", "haricots verts"),
            ("Cucumber", "concombre"),
            ("Radish", "radis"),
            ("Cabbage", "chou"),
            ("Mushrooms", "champignons"),
            ("Lettuce", "laitue"),
            ("Corn", "mais"),
            ("Potatoes", "pommes de terre"),
            ("Tomato", "tomate"),
            ("Carrot", "carotte"),
            ("Plantain", "banane plantain"),
            ("Beans", "haricots"),
            ("Leek", "poireau"),
            ("Lotus root", "racine de lotus"),
            ("Bamboo shoot", "pousse de bambou"),
            ("Artichoke", "artichaut"),
            ("Asparagus", "asperge"),
            ("Brussels sprouts", "choux de bruxelles"),
            ("Broccoli", "brocoli"),
            ("Peas", "pois"),
            ("Cauliflower", "chou-fleur"),
            ("Chili pepper", "piment")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.7 - Fruits": {
        "count": 27,
        "words": [
            ("Cherries", "cerises"),
            ("Raspberries", "framboises"),
            ("Blueberries", "myrtilles"),
            ("Strawberries", "fraises"),
            ("Lemon", "citron"),
            ("Lime", "citron vert"),
            ("Apple", "pomme"),
            ("Orange", "orange"),
            ("Pear", "poire"),
            ("Banana", "banane"),
            ("Grapes", "raisins"),
            ("Grapefruit", "pamplemousse"),
            ("Watermelon", "pasteque"),
            ("Pineapple", "ananas"),
            ("Plum", "prune"),
            ("Peach", "peche"),
            ("Mango", "mangue"),
            ("Apricot", "abricot"),
            ("Pomegranate", "grenade"),
            ("Persimmon", "kaki"),
            ("Kiwi", "kiwi"),
            ("Litchi", "litchi"),
            ("Longan", "longane"),
            ("Balsam pear", "melon amer"),
            ("Passion fruit", "fruit de la passion"),
            ("Avocado", "avocat"),
            ("Coconut", "noix de coco")
        ],
        "is_numbers": False
    },
    
    "Lesson 12 - Irregular Verbs": {
        "count": 68,
        "words": [
            ("to be", "etre"),
            ("to lie down", "etre couche"),
            ("to say", "dire"),
            ("to understand", "comprendre"),
            ("to take", "prendre"),
            ("to write", "ecrire"),
            ("to hear", "entendre"),
            ("to begin", "commencer"),
            ("to break", "casser"),
            ("to build", "construire"),
            ("to choose", "choisir"),
            ("to do/make", "faire"),
            ("to drive", "conduire"),
            ("to forget", "oublier"),
            ("to get", "obtenir"),
            ("to hold", "tenir"),
            ("to leave", "partir"),
            ("to meet", "rencontrer"),
            ("to pay", "payer"),
            ("to put", "mettre"),
            ("to read", "lire"),
            ("to run", "courir"),
            ("to see", "voir"),
            ("to send", "envoyer"),
            ("to sleep", "dormir"),
            ("to speak", "parler"),
            ("to spend (time)", "passer"),
            ("to swim", "nager"),
            ("to teach", "enseigner"),
            ("to tell", "raconter"),
            ("to think", "penser"),
            ("to throw", "jeter"),
            ("to win", "gagner"),
            ("to drink", "boire"),
            ("to go", "aller"),
            ("to give", "donner"),
            ("to eat", "manger"),
            ("to find", "trouver"),
            ("to fall", "tomber"),
            ("to bring", "apporter"),
            ("to have", "avoir"),
            ("to come", "venir"),
            ("to know (fact)", "savoir"),
            ("to want", "vouloir"),
            ("to sit", "s'asseoir"),
            ("to stand", "se tenir debout")
        ],
        "is_numbers": False
    },
    
    "Lesson 14 - Numbers 31-50": {
        "count": 20,
        "words": [
            ("31", "trente et un"),
            ("32", "trente-deux"),
            ("33", "trente-trois"),
            ("34", "trente-quatre"),
            ("35", "trente-cinq"),
            ("36", "trente-six"),
            ("37", "trente-sept"),
            ("38", "trente-huit"),
            ("39", "trente-neuf"),
            ("40", "quarante"),
            ("41", "quarante et un"),
            ("42", "quarante-deux"),
            ("43", "quarante-trois"),
            ("44", "quarante-quatre"),
            ("45", "quarante-cinq"),
            ("46", "quarante-six"),
            ("47", "quarante-sept"),
            ("48", "quarante-huit"),
            ("49", "quarante-neuf"),
            ("50", "cinquante")
        ],
        "is_numbers": True
    },
    
    "Lesson 15 - Physical Appearance": {
        "count": 38,
        "words": [
            ("Tall", "grand"),
            ("Short (height)", "petit"),
            ("Slim", "mince"),
            ("Fat", "gros"),
            ("Muscular", "muscle"),
            ("Blonde", "blond"),
            ("Brown-haired", "brun"),
            ("Black-haired", "noir"),
            ("Curly hair", "cheveux boucles"),
            ("Straight hair", "cheveux lisses"),
            ("Blue eyes", "yeux bleus"),
            ("Brown eyes", "yeux marron"),
            ("Green eyes", "yeux verts"),
            ("Beautiful", "beau/belle"),
            ("Handsome", "beau"),
            ("Ugly", "laid"),
            ("Young", "jeune"),
            ("Old", "vieux/vieille"),
            ("Beard", "barbe"),
            ("Light-skinned", "peau claire"),
            ("Dark-skinned", "peau foncee"),
            ("Freckles", "taches de rousseur"),
            ("Wrinkles", "rides"),
            ("Bald", "chauve"),
            ("Hairy (body)", "poilu"),
            ("Straight nose", "nez droit"),
            ("Big nose", "gros nez"),
            ("Small nose", "petit nez"),
            ("Thin lips", "levres fines"),
            ("Full lips", "levres pulpeuses"),
            ("Broad shoulders", "larges epaules"),
            ("Narrow shoulders", "epaules etroites"),
            ("Tanned skin", "peau bronzee"),
            ("Pale skin", "peau pale"),
            ("Wavy hair", "cheveux ondules"),
            ("Ponytail", "queue de cheval"),
            ("Braids", "tresses"),
            ("Beard and mustache", "barbe et moustache")
        ],
        "is_numbers": False
    },
    
    "Lesson 16 - Occupations": {
        "count": 25,
        "words": [
            ("Doctor", "medecin"),
            ("Teacher", "enseignant"),
            ("Engineer", "ingenieur"),
            ("Lawyer", "avocat"),
            ("Salesperson", "vendeur/vendeuse"),
            ("Police officer", "policier/policiere"),
            ("Firefighter", "pompier/pompiere"),
            ("Programmer", "programmeur/programmeuse"),
            ("Cook/Chef", "cuisinier/cuisiniere"),
            ("Journalist", "journaliste"),
            ("Nurse", "infirmier/infirmiere"),
            ("Architect", "architecte"),
            ("Accountant", "comptable"),
            ("Pharmacist", "pharmacien/pharmacienne"),
            ("Driver", "chauffeur"),
            ("Mechanic", "mecanicien/mecanicienne"),
            ("Scientist", "scientifique"),
            ("Dentist", "dentiste"),
            ("Musician", "musicien/musicienne"),
            ("Actor", "acteur/actrice"),
            ("Artist", "artiste"),
            ("Pilot", "pilote"),
            ("Farmer", "agriculteur/agricultrice"),
            ("Photographer", "photographe"),
            ("Waiter/Waitress", "serveur/serveuse")
        ],
        "is_numbers": False
    },
    
    "Lesson 17 - Sports": {
        "count": 30,
        "words": [
            ("Football/Soccer", "football"),
            ("Basketball", "basket"),
            ("Volleyball", "volley-ball"),
            ("Tennis", "tennis"),
            ("Swimming", "natation"),
            ("Running/Athletics", "course/athletisme"),
            ("Ice hockey", "hockey sur glace"),
            ("Skiing", "ski"),
            ("Cycling", "cyclisme"),
            ("Boxing", "boxe"),
            ("Martial arts", "arts martiaux"),
            ("Golf", "golf"),
            ("Table tennis", "tennis de table"),
            ("Wrestling", "lutte"),
            ("Handball", "handball"),
            ("Baseball", "base-ball"),
            ("Surfing", "surf"),
            ("Skating", "patinage"),
            ("Horse riding", "equitation"),
            ("Diving", "plongee"),
            ("Cricket", "cricket"),
            ("Rugby", "rugby"),
            ("Ballet", "ballet"),
            ("Bowling", "bowling"),
            ("Weightlifting", "halterophilie"),
            ("Windsurfing", "planche a voile"),
            ("Ice skating", "patinage sur glace"),
            ("Rowing", "aviron"),
            ("Archery", "tir a l'arc"),
            ("Climbing", "escalade")
        ],
        "is_numbers": False
    },
    
    "Lesson 18 - Numbers 51-75": {
        "count": 25,
        "words": [
            ("51", "cinquante et un"),
            ("52", "cinquante-deux"),
            ("53", "cinquante-trois"),
            ("54", "cinquante-quatre"),
            ("55", "cinquante-cinq"),
            ("56", "cinquante-six"),
            ("57", "cinquante-sept"),
            ("58", "cinquante-huit"),
            ("59", "cinquante-neuf"),
            ("60", "soixante"),
            ("61", "soixante et un"),
            ("62", "soixante-deux"),
            ("63", "soixante-trois"),
            ("64", "soixante-quatre"),
            ("65", "soixante-cinq"),
            ("66", "soixante-six"),
            ("67", "soixante-sept"),
            ("68", "soixante-huit"),
            ("69", "soixante-neuf"),
            ("70", "soixante-dix"),
            ("71", "soixante et onze"),
            ("72", "soixante-douze"),
            ("73", "soixante-treize"),
            ("74", "soixante-quatorze"),
            ("75", "soixante-quinze")
        ],
        "is_numbers": True
    },
    
    "Lesson 19 - Clothing": {
        "count": 42,
        "words": [
            ("Shirt", "chemise"),
            ("T-shirt", "t-shirt"),
            ("Blouse", "blouse"),
            ("Sweater", "pull/chandail"),
            ("Jacket", "veste"),
            ("Coat", "manteau"),
            ("Dress", "robe"),
            ("Skirt", "jupe"),
            ("Pants", "pantalon"),
            ("Shorts", "short"),
            ("Shoes", "chaussures"),
            ("Boots", "bottes"),
            ("Sneakers", "baskets"),
            ("Sandals", "sandales"),
            ("Hat/Cap", "chapeau/casquette"),
            ("Scarf", "echarpe"),
            ("Gloves", "gants"),
            ("Belt", "ceinture"),
            ("Socks", "chaussettes"),
            ("Winter coat", "manteau d'hiver"),
            ("Wool hat", "bonnet en laine"),
            ("Snow boots", "bottes de neige"),
            ("Swimsuit", "maillot de bain"),
            ("Sunglasses", "lunettes de soleil"),
            ("Flip-flops", "tongs"),
            ("Tank top", "debardeur"),
            ("Suit", "costume"),
            ("Tie", "cravate"),
            ("Blazer", "blazer"),
            ("High heels", "talons hauts"),
            ("Evening dress", "robe de soiree"),
            ("Black", "noir"),
            ("White", "blanc"),
            ("Red", "rouge"),
            ("Blue", "bleu"),
            ("Green", "vert"),
            ("Cotton", "coton"),
            ("Wool", "laine"),
            ("Leather", "cuir"),
            ("Silk", "soie"),
            ("Linen", "lin")
        ],
        "is_numbers": False
    },
    
    "Lesson 20 - Adverbs": {
        "count": 20,
        "words": [
            ("Quickly", "vite"),
            ("Slowly", "lentement"),
            ("Always", "toujours"),
            ("Never", "jamais"),
            ("Often", "souvent"),
            ("Sometimes", "parfois"),
            ("Rarely", "rarement"),
            ("Already", "deja"),
            ("Still", "encore"),
            ("Yet", "encore"),
            ("Soon", "bientot"),
            ("Now", "maintenant"),
            ("Later", "plus tard"),
            ("Today", "aujourd'hui"),
            ("Tomorrow", "demain"),
            ("Yesterday", "hier"),
            ("Clearly", "clairement"),
            ("Together", "ensemble"),
            ("Apart", "separement"),
            ("Forever", "pour toujours")
        ],
        "is_numbers": False
    },
    
    "Lesson 21 - Animals": {
        "count": 20,
        "words": [
            ("Dog", "chien"),
            ("Cat", "chat"),
            ("Horse", "cheval"),
            ("Cow", "vache"),
            ("Sheep", "mouton"),
            ("Pig", "cochon"),
            ("Goat", "chevre"),
            ("Chicken", "poulet"),
            ("Duck", "canard"),
            ("Bird", "oiseau"),
            ("Rabbit", "lapin"),
            ("Mouse", "souris"),
            ("Lion", "lion"),
            ("Tiger", "tigre"),
            ("Bear", "ours"),
            ("Elephant", "elephant"),
            ("Monkey", "singe"),
            ("Fox", "renard"),
            ("Wolf", "loup"),
            ("Deer", "cerf")
        ],
        "is_numbers": False
    },
    
    "Lesson 23 - Places in Town": {
        "count": 20,
        "words": [
            ("School", "ecole"),
            ("Hospital", "hopital"),
            ("Bank", "banque"),
            ("Restaurant", "restaurant"),
            ("Library", "bibliotheque"),
            ("Supermarket", "supermarche"),
            ("Cinema", "cinema"),
            ("Post office", "poste"),
            ("Police station", "commissariat"),
            ("Park", "parc"),
            ("Museum", "musee"),
            ("Theatre", "theatre"),
            ("Hotel", "hotel"),
            ("Stadium", "stade"),
            ("Church", "eglise"),
            ("Pharmacy", "pharmacie"),
            ("Bakery", "boulangerie"),
            ("Butcher", "boucherie"),
            ("Market", "marche"),
            ("Hairdresser", "coiffeur")
        ],
        "is_numbers": False
    },
    
    "Lesson 24 - School Supplies": {
        "count": 20,
        "words": [
            ("Book", "livre"),
            ("Pen", "stylo"),
            ("Pencil", "crayon"),
            ("Eraser", "gomme"),
            ("Notebook", "cahier"),
            ("Ruler", "regle"),
            ("Scissors", "ciseaux"),
            ("Backpack", "sac a dos"),
            ("Folder", "dossier"),
            ("Calculator", "calculatrice"),
            ("Marker", "feutre"),
            ("Chalk", "craie"),
            ("Map", "carte"),
            ("Highlighter", "surligneur"),
            ("Projector", "projecteur"),
            ("Laptop", "ordinateur portable"),
            ("Printer", "imprimante"),
            ("USB stick", "cle usb"),
            ("Schoolbag", "cartable"),
            ("Sharpener", "taille-crayon")
        ],
        "is_numbers": False
    },
    
    "Lesson 25 - Transportation": {
        "count": 20,
        "words": [
            ("Car", "voiture"),
            ("Bus", "bus"),
            ("Train", "train"),
            ("Bicycle", "velo"),
            ("Motorcycle", "moto"),
            ("Airplane", "avion"),
            ("Boat", "bateau"),
            ("Tram", "tramway"),
            ("Taxi", "taxi"),
            ("Subway", "metro"),
            ("Ferry", "ferry"),
            ("Yacht", "yacht"),
            ("Hot air balloon", "montgolfiere"),
            ("Spaceship", "vaisseau spatial"),
            ("Rickshaw", "pousse-pousse"),
            ("Gondola", "gondole"),
            ("Zeppelin", "dirigeable"),
            ("Rollerblades", "rollers"),
            ("Canoe", "canoe"),
            ("Submarine", "sous-marin")
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
        for english, french in words:
            questions.append({
                'type': 'num_to_word',
                'question': f"What is '{english}' in French? (Answer with the WORD)",
                'answer': french,
                'display_answer': french  # KELIME göster
            })
        
        # Tarz 2: Kelimeden sayıya (Cevap: SAYI)
        for english, french in words:
            questions.append({
                'type': 'word_to_num',
                'question': f"What number is '{french}'? (Answer with the NUMBER)",
                'answer': english,
                'display_answer': english  # SAYI göster
            })
        
        # Tarz 3: Karışık (Cevap türüne göre)
        for english, french in words:
            if random.choice([True, False]):
                # Sayıdan kelimeye
                questions.append({
                    'type': 'mixed',
                    'question': f"Translate '{english}' to French word:",
                    'answer': french,
                    'display_answer': french  # KELIME
                })
            else:
                # Kelimeden sayıya
                questions.append({
                    'type': 'mixed',
                    'question': f"What number is '{french}'?",
                    'answer': english,
                    'display_answer': english  # SAYI
                })
    
    elif count <= 20:
        # 20 ve altı: 3 farklı soru tarzı
        # Tarz 1: English -> French
        for english, french in words:
            questions.append({
                'type': 'eng_to_fre',
                'question': f"Translate to French: '{english}'",
                'answer': french,
                'display_answer': french
            })
        
        # Tarz 2: French -> English
        for english, french in words:
            questions.append({
                'type': 'fre_to_eng',
                'question': f"Translate to English: '{french}'",
                'answer': english,
                'display_answer': english
            })
        
        # Tarz 3: İlk harf ipucu
        for english, french in words:
            first_letter = french[0] if french else ""
            blanks = "_" * (len(french) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}' - Complete the French word",
                'answer': french,
                'display_answer': french
            })
    
    elif 20 < count <= 40:
        # 20-40 arası: 3 bölüm, 2 farklı soru tarzı
        third = len(words) // 3
        
        # Bölüm 1: English -> French
        for english, french in words[:third]:
            questions.append({
                'type': 'eng_to_fre',
                'question': f"Translate to French: '{english}'",
                'answer': french,
                'display_answer': french
            })
        
        # Bölüm 2: French -> English
        for english, french in words[third:third*2]:
            questions.append({
                'type': 'fre_to_eng',
                'question': f"Translate to English: '{french}'",
                'answer': english,
                'display_answer': english
            })
        
        # Bölüm 3: İlk harf ipucu
        for english, french in words[third*2:]:
            first_letter = french[0] if french else ""
            blanks = "_" * (len(french) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': french,
                'display_answer': french
            })
    
    else:  # count > 40
        # 40+ : 5 bölüm, 3-4 farklı soru tarzı
        fifth = len(words) // 5
        
        # Bölüm 1: English -> French
        for english, french in words[:fifth]:
            questions.append({
                'type': 'eng_to_fre',
                'question': f"Translate to French: '{english}'",
                'answer': french,
                'display_answer': french
            })
        
        # Bölüm 2: French -> English
        for english, french in words[fifth:fifth*2]:
            questions.append({
                'type': 'fre_to_eng',
                'question': f"Translate to English: '{french}'",
                'answer': english,
                'display_answer': english
            })
        
        # Bölüm 3: İlk harf
        for english, french in words[fifth*2:fifth*3]:
            first_letter = french[0] if french else ""
            blanks = "_" * (len(french) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': french,
                'display_answer': french
            })
        
        # Bölüm 4: Son harf
        for english, french in words[fifth*3:fifth*4]:
            last_letter = french[-1] if french else ""
            blanks = "_" * (len(french) - 1)
            questions.append({
                'type': 'last_letter',
                'question': f"'{english}' = '{blanks}{last_letter}'",
                'answer': french,
                'display_answer': french
            })
        
        # Bölüm 5: Harf sayısı ipucu
        for english, french in words[fifth*4:]:
            questions.append({
                'type': 'letter_hint',
                'question': f"'{english}' = ({len(french)} letters, starts with {french[:2]}...)",
                'answer': french,
                'display_answer': french
            })
    
    return questions

def create_general_review(lesson_name, words, is_numbers):
    """Her bölümün sonunda genel tekrar soruları"""
    review = []
    sample_size = min(20, len(words))
    sampled_words = random.sample(words, sample_size)
    
    for english, french in sampled_words:
        if is_numbers:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] '{english}' in French?",
                    'answer': french,
                    'display_answer': french
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] What number is '{french}'?",
                    'answer': english,
                    'display_answer': english
                })
        else:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{english}'",
                    'answer': french,
                    'display_answer': french
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{french}'",
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
║        COMPREHENSIVE FRENCH TEST SYSTEM                   ║
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
        print(Fore.GREEN + "🎉🎉🎉 EXCELLENT! You're amazing at French! 🎉🎉🎉")
    elif final_percentage >= 70:
        print(Fore.BLUE + "👏👏👏 VERY GOOD! Great performance! 👏👏👏")
    elif final_percentage >= 50:
        print(Fore.YELLOW + "👍👍 GOOD! Keep going and you'll be excellent! 👍👍")
    else:
        print(Fore.RED + "📚📚 Keep studying! You can do it! 📚📚")
    
    print(Fore.GREEN + "\nCongratulations! You completed the entire test! 🎊")

if __name__ == "__main__":
    main()