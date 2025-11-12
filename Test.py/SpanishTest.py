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
            ("Hello", "hola"),
            ("How are you?", "como estas"),
            ("Nice to meet you", "mucho gusto"),
            ("Nice to meet you (alt)", "encantado de conocerte"),
            ("See you tomorrow", "hasta manana"),
            ("Good morning", "buenos dias"),
            ("Good afternoon", "buenas tardes"),
            ("Good night", "buenas noches"),
            ("What is your name?", "cual es su nombre"),
            ("My name is", "me llamo"),
            ("Where do you live?", "donde vives"),
            ("Where are you from?", "de donde eres"),
            ("Nice to see you", "encantado de verte"),
            ("Have a nice day", "que tengas un buen dia"),
            ("See you later", "hasta luego"),
            ("Goodbye", "adios"),
            ("Please", "por favor"),
            ("Thank you", "gracias")
        ],
        "is_numbers": False
    },
    
    "Lesson 3 - Regular -AR Verbs": {
        "count": 75,
        "words": [
            ("to pass", "pasar"), ("to stay", "quedar"), ("to speak", "hablar"),
            ("to carry", "llevar"), ("to leave", "dejar"), ("to call", "llamar"),
            ("to take", "tomar"), ("to treat", "tratar"), ("to watch", "mirar"),
            ("to wait", "esperar"), ("to enter", "entrar"), ("to work", "trabajar"),
            ("to finish", "terminar"), ("to need", "necesitar"), ("to turn out", "resultar"),
            ("to change", "cambiar"), ("to introduce", "presentar"), ("to create", "crear"),
            ("to consider", "considerar"), ("to end", "acabar"), ("to win", "ganar"),
            ("to form", "formar"), ("to accept", "aceptar"), ("to achieve", "lograr"),
            ("to ask", "preguntar"), ("to study", "estudiar"), ("to help", "ayudar"),
            ("to please", "gustar"), ("to listen", "escuchar"), ("to raise", "levantar"),
            ("to try", "intentar"), ("to use", "usar"), ("to forget", "olvidar"),
            ("to occupy", "ocupar"), ("to fix", "fijar"), ("to buy", "comprar"),
            ("to avoid", "evitar"), ("to interest", "interesar"), ("to throw", "echar"),
            ("to import", "importar"), ("to observe", "observar"), ("to imagine", "imaginar"),
            ("to develop", "desarrollar"), ("to point out", "señalar"), ("to prepare", "preparar"),
            ("to lack", "faltar"), ("to accompany", "acompañar"), ("to desire", "desear"),
            ("to teach", "enseñar"), ("to represent", "representar"), ("to order", "mandar"),
            ("to assure", "asegurar"), ("to kill", "matar"), ("to guard", "guardar"),
            ("to initiate", "iniciar"), ("to lower", "bajar"), ("to note", "notar"),
            ("to cut", "cortar"), ("to take advantage", "aprovechar"), ("to support", "apoyar"),
            ("to increase", "aumentar"), ("to abandon", "abandonar"), ("to remove", "quitar"),
            ("to preserve", "conservar"), ("to function", "funcionar"), ("to announce", "anunciar"),
            ("to comment", "comentar"), ("to participate", "participar"), ("to escape", "escapar"),
            ("to pull", "tirar"), ("to answer", "contestar"), ("to worry", "preocupar"),
            ("to lend", "prestar"), ("to weigh", "pesar"), ("to travel", "viajar")
        ],
        "is_numbers": False
    },
    
    "Lesson 3 - Regular -ER Verbs": {
        "count": 12,
        "words": [
            ("to owe", "deber"), ("to understand", "comprender"), ("to run", "correr"),
            ("to eat", "comer"), ("to happen", "suceder"), ("to learn", "aprender"),
            ("to respond", "responder"), ("to sell", "vender"), ("to put in", "meter"),
            ("to attempt", "pretender"), ("to correspond", "corresponder"), ("to depend", "depender")
        ],
        "is_numbers": False
    },
    
    "Lesson 3 - Regular -IR Verbs": {
        "count": 13,
        "words": [
            ("to live", "vivir"), ("to exist", "existir"), ("to occur", "ocurrir"),
            ("to receive", "recibir"), ("to permit", "permitir"), ("to divide", "partir"),
            ("to fulfill", "cumplir"), ("to decide", "decidir"), ("to go up", "subir"),
            ("to suffer", "sufrir"), ("to share", "compartir"), ("to consist", "consistir"),
            ("to insist", "insistir")
        ],
        "is_numbers": False
    },
    
    "Lesson 4 - Adjectives": {
        "count": 35,
        "words": [
            ("Noisy", "ruidoso"), ("Quiet", "silencioso"), ("Strong", "fuerte"),
            ("Weak", "debil"), ("Hard", "duro"), ("Soft", "blando"),
            ("More", "mas"), ("Less", "menos"), ("Clean", "limpio"),
            ("Dirty", "sucio"), ("Old", "viejo"), ("New", "nuevo"),
            ("Big", "grande"), ("Small", "pequeño"), ("Young", "joven"),
            ("Skinny", "flaco"), ("Fat", "gordo"), ("Pretty", "guapo"),
            ("Ugly", "feo"), ("Thick", "grueso"), ("Thin", "delgado"),
            ("Rough", "aspero"), ("Smooth", "liso"), ("Happy", "feliz"),
            ("Sad", "triste"), ("Angry", "enfadado"), ("Afraid", "asustado"),
            ("Joy", "alegria"), ("Surprised", "sorprendido"), ("Calm", "tranquilo"),
            ("Bored", "aburrido"), ("Easy", "facil"), ("Difficult", "dificil"),
            ("Bad", "malo"), ("Good", "bueno")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.1 - Days": {
        "count": 11,
        "words": [
            ("Day", "dia"), ("Week", "semana"), ("Monday", "lunes"),
            ("Tuesday", "martes"), ("Wednesday", "miercoles"), ("Thursday", "jueves"),
            ("Friday", "viernes"), ("Saturday", "sabado"), ("Sunday", "domingo"),
            ("Weekend", "fin de semana"), ("The days of the week", "los dias de la semana")
        ],
        "is_numbers": False
    },
    
    "Lesson 5.2 - Months": {
        "count": 15,
        "words": [
            ("Month", "mes"), ("Year", "ano"), ("January", "enero"),
            ("February", "febrero"), ("March", "marzo"), ("April", "abril"),
            ("May", "mayo"), ("June", "junio"), ("July", "julio"),
            ("August", "agosto"), ("September", "septiembre"), ("October", "octubre"),
            ("November", "noviembre"), ("December", "diciembre"), ("The months", "los meses del ano")
        ],
        "is_numbers": False
    },
    
    "Lesson 6 - Seasons & Weather": {
        "count": 23,
        "words": [
            ("Seasons", "las estaciones"), ("Winter", "invierno"), ("Summer", "verano"),
            ("Spring", "primavera"), ("Autumn", "otoño"), ("Sky", "cielo"),
            ("Cloud", "nube"), ("Rainbow", "arco iris"), ("Cold", "frio"),
            ("Hot", "calido"), ("It is hot", "hace calor"), ("It is cold", "hace frio"),
            ("It is sunny", "hace sol"), ("It is cloudy", "esta nublado"), ("It is humid", "hay humedad"),
            ("It is raining", "esta lloviendo"), ("It is snowing", "esta nevando"), ("It is windy", "hace viento"),
            ("How is the weather?", "que tiempo hace"), ("Good weather", "buen tiempo"), ("Bad weather", "mal tiempo"),
            ("What is the temperature?", "a que temperatura estamos"), ("It is 24 degrees", "estamos a 24 grados")
        ],
        "is_numbers": False
    },
    
    "Lesson 7 - Colors": {
        "count": 14,
        "words": [
            ("Black", "negro"), ("Blue", "azul"), ("Brown", "marron"),
            ("Green", "verde"), ("Orange", "naranja"), ("Purple", "morado"),
            ("Red", "rojo"), ("White", "blanco"), ("Yellow", "amarillo"),
            ("Gray", "gris"), ("Gold", "oro"), ("Silver", "plata"),
            ("What color is it?", "que color es"), ("The color is", "el color es")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.1 - Family": {
        "count": 37,
        "words": [
            ("the (masculine)", "el"), ("the (feminine)", "la"), ("Mother", "madre"),
            ("Father", "padre"), ("Brother", "hermano"), ("Sister", "hermana"),
            ("Son", "hijo"), ("Daughter", "hija"), ("Parents", "padres"),
            ("Children", "niños"), ("Child", "niño"), ("Stepmother", "madrastra"),
            ("Stepfather", "padrastro"), ("Stepsister", "hermanastra"), ("Stepbrother", "hermanastro"),
            ("Son-in-law", "yerno"), ("Daughter-in-law", "nuera"), ("Wife", "esposa"),
            ("Husband", "marido"), ("Grandparents", "abuelos"), ("Grandfather", "abuelo"),
            ("Grandmother", "abuela"), ("Grandson", "nieto"), ("Granddaughter", "nieta"),
            ("Grandchildren", "nietos"), ("Aunt", "tia"), ("Uncle", "tio"),
            ("Cousin (female)", "prima"), ("Cousin (male)", "primo"), ("Nephew", "sobrino"),
            ("Niece", "sobrina"), ("Father-in-law", "suegro"), ("Mother-in-law", "suegra"),
            ("Brother-in-law", "cuñado"), ("Sister-in-law", "cuñada"), ("Relative", "pariente")
        ],
        "is_numbers": False
    },
    
    "Lesson 8.2 - Friends": {
        "count": 14,
        "words": [
            ("Miss", "señorita"), ("Boy", "chico"), ("Girl", "chica"),
            ("Baby", "bebe"), ("Woman", "mujer"), ("Man", "hombre"),
            ("Friend (male)", "amigo"), ("Friend (female)", "amiga"), ("Boyfriend", "novio"),
            ("Girlfriend", "novia"), ("Gentleman", "caballero"), ("Lady", "dama"),
            ("Neighbor (male)", "vecino"), ("Neighbor (female)", "vecina")
        ],
        "is_numbers": False
    },
    
    "Lesson 9 - Numbers 11-30": {
        "count": 20,
        "words": [
            ("11", "once"), ("12", "doce"), ("13", "trece"),
            ("14", "catorce"), ("15", "quince"), ("16", "dieciseis"),
            ("17", "diecisiete"), ("18", "dieciocho"), ("19", "diecinueve"),
            ("20", "veinte"), ("21", "veintiuno"), ("22", "veintidos"),
            ("23", "veintitres"), ("24", "veinticuatro"), ("25", "veinticinco"),
            ("26", "veintiseis"), ("27", "veintisiete"), ("28", "veintiocho"),
            ("29", "veintinueve"), ("30", "treinta")
        ],
        "is_numbers": True
    },
    
    "Lesson 10.1 - Prepositions": {
        "count": 37,
        "words": [
            ("For", "para"), ("From", "de"), ("In", "en"),
            ("Inside", "dentro"), ("Near", "cerca"), ("Out", "fuera de"),
            ("To", "a"), ("Under", "debajo de"), ("With", "con"),
            ("Without", "sin"), ("Above", "encima de"), ("Across", "a traves de"),
            ("After", "despues"), ("Against", "contra"), ("Along", "a lo largo de"),
            ("Around", "alrededor de"), ("At", "en"), ("Behind", "detras"),
            ("Below", "debajo"), ("Beside", "al lado de"), ("Between", "entre"),
            ("By", "junto a"), ("During", "durante"), ("Except", "excepto"),
            ("And", "y"), ("Because", "porque"), ("But", "pero"),
            ("Or", "o"), ("Everywhere", "en todas partes"), ("Everyone", "todos"),
            ("Everything", "todo"), ("Here", "aqui"), ("Few", "pocos"),
            ("Some", "algunos"), ("Many", "muchos"), ("Into", "en"),
            ("Outside", "fuera de")
        ],
        "is_numbers": False
    },
    
    "Lesson 10.2 - Useful Words": {
        "count": 29,
        "words": [
            ("Question", "pregunta"), ("Answer", "respuesta"), ("Truth", "verdad"),
            ("Lie", "mentira"), ("Nothing", "nada"), ("Something", "algo"),
            ("Same", "igual"), ("Different", "diferente"), ("Pull", "tirar"),
            ("Push", "empujar"), ("Long", "largo"), ("Short", "corto"),
            ("Cold", "frio"), ("Hot", "caliente"), ("Light", "luz"),
            ("Dark", "oscuridad"), ("Wet", "mojado"), ("Dry", "seco"),
            ("Empty", "vacio"), ("Full", "lleno"), ("How?", "como"),
            ("What?", "que"), ("When?", "cuando"), ("Where?", "donde"),
            ("Which?", "cual"), ("Who?", "quien"), ("Why?", "por que"),
            ("How long?", "cuanto tiempo"), ("How much?", "cuanto")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.1 - Drinks": {
        "count": 9,
        "words": [
            ("Coffee", "cafe"), ("Tea", "te"), ("Soft drink", "gaseosa"),
            ("Water", "agua"), ("Lemonade", "limonada"), ("Juice", "zumo"),
            ("Orange juice", "zumo de naranja"), ("With ice", "con hielo"),
            ("I would like a glass of water please", "quiero un vaso de agua por favor")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.2 - Dairy Products": {
        "count": 18,
        "words": [
            ("Milk", "leche"), ("Ice cream", "helado"), ("Butter", "mantequilla"),
            ("Cheese", "queso"), ("Cottage cheese", "requeson"), ("Cream", "crema"),
            ("Sour cream", "crema agria"), ("Yogurt", "yogur"), ("Eggs", "huevos"),
            ("Whipping cream", "crema batida"), ("Baguette", "baguette"), ("Doughnut", "donut"),
            ("Cookie", "galleta"), ("Roll", "panecillo"), ("Dessert", "postre"),
            ("Cake", "pastel"), ("Bread", "pan"), ("Pie", "tarta")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.3 - Meats": {
        "count": 14,
        "words": [
            ("Beef", "carne de vacuno"), ("Veal", "ternera"), ("Ham", "jamon"),
            ("Chicken", "pollo"), ("Turkey", "pavo"), ("Duck", "pato"),
            ("Bacon", "beicon"), ("Pork", "cerdo"), ("Filet mignon", "filete miñon"),
            ("Sausage", "salchicha"), ("Lamb chop", "chuleta de cordero"),
            ("Pork chop", "chuleta de cerdo"), ("Meat", "carne")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.4 - Seafoods": {
        "count": 20,
        "words": [
            ("Fish", "pescado"), ("Shellfish", "marisco"), ("Bass", "perca"),
            ("Salmon", "salmon"), ("Lobster", "langosta"), ("Crab", "cangrejo"),
            ("Mussel", "mejillon"), ("Oyster", "ostra"), ("Cod", "bacalao"),
            ("Clam", "almeja"), ("Shrimp", "gamba"), ("Tuna", "atun"),
            ("Trout", "trucha"), ("Sole", "lenguado"), ("Shark", "tiburon"),
            ("Carp", "carpa"), ("Tilapia", "tilapia"), ("Eel", "anguila"),
            ("Catfish", "siluro"), ("Swordfish", "pez espada")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.5 - Herbs & Spices": {
        "count": 17,
        "words": [
            ("Salt", "sal"), ("Pepper", "pimienta"), ("Caraway", "alcaravea"),
            ("Garlic", "ajo"), ("Basil", "albahaca"), ("Coriander", "cilantro"),
            ("Fennel", "hinojo"), ("Marjoram", "mejorana"), ("Oregano", "oregano"),
            ("Parsley", "perejil"), ("Rosemary", "romero"), ("Sage", "salvia"),
            ("Thyme", "tomillo"), ("Nutmeg", "nuez moscada"), ("Paprika", "pimenton"),
            ("Cayenne", "cayena"), ("Ginger", "jengibre")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.6 - Vegetables": {
        "count": 28,
        "words": [
            ("Celery", "apio"), ("Eggplant", "berenjena"), ("Zucchini", "calabacin"),
            ("Onion", "cebolla"), ("Spinach", "espinaca"), ("Salad", "ensalada"),
            ("Green beans", "judias verdes"), ("Cucumber", "pepino"), ("Radish", "rabano"),
            ("Cabbage", "repollo"), ("Mushrooms", "setas"), ("Lettuce", "lechuga"),
            ("Corn", "maiz"), ("Potatoes", "patatas"), ("Tomato", "tomate"),
            ("Carrot", "zanahoria"), ("Plantain", "platano macho"), ("Beans", "alubias"),
            ("Leek", "puerro"), ("Lotus root", "raiz de loto"), ("Bamboo shoot", "brotes de bambu"),
            ("Artichoke", "alcachofa"), ("Asparagus", "esparragos"), ("Brussels sprouts", "coles de bruselas"),
            ("Broccoli", "brocoli"), ("Peas", "guisantes"), ("Cauliflower", "coliflor"),
            ("Chili pepper", "chile")
        ],
        "is_numbers": False
    },
    
    "Lesson 11.7 - Fruits": {
        "count": 27,
        "words": [
            ("Cherries", "cerezas"), ("Raspberries", "frambuesas"), ("Blueberries", "arandanos"),
            ("Strawberries", "fresas"), ("Lemon", "limon"), ("Lime", "lima"),
            ("Apple", "manzana"), ("Orange", "naranja"), ("Pear", "pera"),
            ("Banana", "platano"), ("Grapes", "uvas"), ("Grapefruit", "pomelo"),
            ("Watermelon", "sandia"), ("Pineapple", "piña"), ("Plum", "ciruela"),
            ("Peach", "melocoton"), ("Mango", "mango"), ("Apricot", "albaricoque"),
            ("Pomegranate", "granada"), ("Persimmon", "caqui"), ("Kiwi", "kiwi"),
            ("Litchi", "litchi"), ("Longan", "longan"), ("Balsam pear", "melon amargo"),
            ("Passion fruit", "maracuya"), ("Avocado", "aguacate"), ("Coconut", "coco")
        ],
        "is_numbers": False
    },
    
    "Lesson 12.1 - Irregular Verbs -AR": {
        "count": 46,
        "words": [
            ("to have lunch", "almorzar"), ("to pass (test)", "aprobar"), ("to hang", "colgar"),
            ("to count", "contar"), ("to demonstrate", "demostrar"), ("to find", "encontrar"),
            ("to show", "mostrar"), ("to try/taste", "probar"), ("to remember", "recordar"),
            ("to dream", "soñar"), ("to close", "cerrar"), ("to begin", "comenzar"),
            ("to wake up", "despertar"), ("to start", "empezar"), ("to deny", "negar"),
            ("to think", "pensar"), ("to break", "quebrar"), ("to tremble", "temblar"),
            ("to cross", "atravesar"), ("to sit", "sentar"), ("to recommend", "recomendar"),
            ("to govern", "gobernar"), ("to express", "manifestar"), ("to snack", "merendar"),
            ("to cry", "llorar"), ("to warm", "calentar"), ("to look", "regar"),
            ("to fly", "volar"), ("to beg", "rogar"), ("to bury", "enterrar"),
            ("to scrub", "fregar"), ("to snow", "nevar")
        ],
        "is_numbers": False
    },
    
    "Lesson 12.2 - Irregular Verbs -ER": {
        "count": 38,
        "words": [
            ("to understand", "entender"), ("to rain", "llover"), ("to bite", "morder"),
            ("to move", "mover"), ("to lose", "perder"), ("to can/be able", "poder"),
            ("to return", "volver"), ("to solve", "resolver"), ("to satisfy", "satisfacer"),
            ("to know (person)", "conocer"), ("to be born", "nacer"), ("to seem", "parecer"),
            ("to bring", "traer"), ("to fall", "caer"), ("to be worth", "valer"),
            ("to fit", "caber"), ("to recognize", "reconocer"), ("to disappear", "desaparecer"),
            ("to obey", "obedecer"), ("to be", "ser"), ("to have", "tener"),
            ("to see", "ver"), ("to do/make", "hacer"), ("to put", "poner"),
            ("to undo", "deshacer"), ("to thank", "agradecer"), ("to establish", "establecer"),
            ("to drink", "beber"), ("to read", "leer"), ("to break", "romper"),
            ("to promise", "prometer"), ("to possess", "poseer"), ("to surprise", "sorprender"),
            ("to fear", "temer"), ("to believe", "creer"), ("to have (aux)", "haber")
        ],
        "is_numbers": False
    },
    
    "Lesson 12.3 - Irregular Verbs -IR": {
        "count": 38,
        "words": [
            ("to warn", "advertir"), ("to confer", "conferir"), ("to allow", "consentir"),
            ("to convert", "convertir"), ("to digest", "digerir"), ("to have fun", "divertirse"),
            ("to lie", "mentir"), ("to prefer", "preferir"), ("to feel", "sentir"),
            ("to suggest", "sugerir"), ("to drive", "conducir"), ("to translate", "traducir"),
            ("to introduce", "introducir"), ("to produce", "producir"), ("to reduce", "reducir"),
            ("to follow", "seguir"), ("to get/obtain", "conseguir"), ("to repeat", "repetir"),
            ("to dress", "vestir"), ("to serve", "servir"), ("to boil", "hervir"),
            ("to prevent", "impedir"), ("to die", "morir"), ("to go out", "salir"),
            ("to hear", "oir"), ("to come", "venir"), ("to ask for", "pedir"),
            ("to go", "ir"), ("to say/tell", "decir"), ("to write", "escribir"),
            ("to attend", "asistir"), ("to discuss", "discutir"), ("to join", "unir"),
            ("to admit", "admitir"), ("to sleep", "dormir")
        ],
        "is_numbers": False
    },
    
    "Lesson 14 - Numbers 31-50": {
        "count": 20,
        "words": [
            ("31", "treinta y uno"), ("32", "treinta y dos"), ("33", "treinta y tres"),
            ("34", "treinta y cuatro"), ("35", "treinta y cinco"), ("36", "treinta y seis"),
            ("37", "treinta y siete"), ("38", "treinta y ocho"), ("39", "treinta y nueve"),
            ("40", "cuarenta"), ("41", "cuarenta y uno"), ("42", "cuarenta y dos"),
            ("43", "cuarenta y tres"), ("44", "cuarenta y cuatro"), ("45", "cuarenta y cinco"),
            ("46", "cuarenta y seis"), ("47", "cuarenta y siete"), ("48", "cuarenta y ocho"),
            ("49", "cuarenta y nueve"), ("50", "cincuenta")
        ],
        "is_numbers": True
    },
    
    "Lesson 15 - Physical Appearance": {
        "count": 39,
        "words": [
            ("Tall", "alto"), ("Short (height)", "bajo"), ("Slim", "delgado"),
            ("Fat", "gordo"), ("Muscular", "musculoso"), ("Blonde", "rubio"),
            ("Brown-haired", "castaño"), ("Black-haired", "negro"), ("Curly hair", "rizado"),
            ("Straight hair", "liso"), ("Blue eyes", "ojos azules"), ("Brown eyes", "ojos marrones"),
            ("Green eyes", "ojos verdes"), ("Beautiful", "guapo"), ("Ugly", "feo"),
            ("Young", "joven"), ("Old", "viejo"), ("Beard", "barba"),
            ("Light-skinned", "piel clara"), ("Dark-skinned", "piel oscura"), ("Freckles", "pecas"),
            ("Wrinkles", "arrugas"), ("Bald", "calvo"), ("Hairy (body)", "peludo"),
            ("Straight nose", "nariz recta"), ("Big nose", "nariz grande"), ("Small nose", "nariz pequeña"),
            ("Thin lips", "labios finos"), ("Full lips", "labios carnosos"), ("Broad shoulders", "hombros anchos"),
            ("Narrow shoulders", "hombros estrechos"), ("Tanned skin", "piel bronceada"), ("Pale skin", "piel palida"),
            ("Wavy hair", "cabello ondulado"), ("Ponytail", "cola de caballo"), ("Braids", "trenzas"),
            ("Beard and mustache", "barba y bigote")
        ],
        "is_numbers": False
    },
    
    "Lesson 16 - Occupations": {
        "count": 30,
        "words": [
            ("Teacher", "profesor"), ("Doctor", "medico"), ("Engineer", "ingeniero"),
            ("Nurse", "enfermero"), ("Police officer", "policia"), ("Firefighter", "bombero"),
            ("Chef", "cocinero"), ("Waiter", "camarero"), ("Mechanic", "mecanico"),
            ("Electrician", "electricista"), ("Plumber", "fontanero"), ("Carpenter", "carpintero"),
            ("Farmer", "granjero"), ("Dentist", "dentista"), ("Pharmacist", "farmaceutico"),
            ("Lawyer", "abogado"), ("Judge", "juez"), ("Journalist", "periodista"),
            ("Actor", "actor"), ("Musician", "musico"), ("Driver", "conductor"),
            ("Pilot", "piloto"), ("Scientist", "cientifico"), ("Architect", "arquitecto"),
            ("Cashier", "cajero"), ("Cleaner", "limpiador"), ("Salesperson", "vendedor"),
            ("Programmer", "programador"), ("Designer", "diseñador"), ("Translator", "traductor")
        ],
        "is_numbers": False
    },
    
    "Lesson 17 - Sports": {
        "count": 30,
        "words": [
            ("Football/Soccer", "futbol"), ("Basketball", "baloncesto"), ("Volleyball", "voleibol"),
            ("Tennis", "tenis"), ("Swimming", "natacion"), ("Running", "carreras"),
            ("Ice hockey", "hockey sobre hielo"), ("Skiing", "esqui"), ("Cycling", "ciclismo"),
            ("Boxing", "boxeo"), ("Martial arts", "artes marciales"), ("Golf", "golf"),
            ("Table tennis", "tenis de mesa"), ("Wrestling", "lucha libre"), ("Handball", "balonmano"),
            ("Baseball", "beisbol"), ("Surfing", "surf"), ("Skating", "patinaje"),
            ("Horse riding", "equitacion"), ("Diving", "buceo"), ("Cricket", "cricket"),
            ("Rugby", "rugby"), ("Ballet", "ballet"), ("Bowling", "bolos"),
            ("Weightlifting", "levantamiento de pesas"), ("Windsurfing", "windsurf"), ("Ice skating", "patinaje sobre hielo"),
            ("Rowing", "remo"), ("Archery", "tiro con arco"), ("Climbing", "escalada")
        ],
        "is_numbers": False
    },
    
    "Lesson 18 - Numbers 51-75": {
        "count": 25,
        "words": [
            ("51", "cincuenta y uno"), ("52", "cincuenta y dos"), ("53", "cincuenta y tres"),
            ("54", "cincuenta y cuatro"), ("55", "cincuenta y cinco"), ("56", "cincuenta y seis"),
            ("57", "cincuenta y siete"), ("58", "cincuenta y ocho"), ("59", "cincuenta y nueve"),
            ("60", "sesenta"), ("61", "sesenta y uno"), ("62", "sesenta y dos"),
            ("63", "sesenta y tres"), ("64", "sesenta y cuatro"), ("65", "sesenta y cinco"),
            ("66", "sesenta y seis"), ("67", "sesenta y siete"), ("68", "sesenta y ocho"),
            ("69", "sesenta y nueve"), ("70", "setenta"), ("71", "setenta y uno"),
            ("72", "setenta y dos"), ("73", "setenta y tres"), ("74", "setenta y cuatro"),
            ("75", "setenta y cinco")
        ],
        "is_numbers": True
    },
    
    "Lesson 19 - Clothing": {
        "count": 36,
        "words": [
            ("Shirt", "camisa"), ("T-shirt", "camiseta"), ("Blouse", "blusa"),
            ("Sweater", "jersey"), ("Jacket", "chaqueta"), ("Coat", "abrigo"),
            ("Dress", "vestido"), ("Skirt", "falda"), ("Pants", "pantalones"),
            ("Shorts", "pantalones cortos"), ("Shoes", "zapatos"), ("Boots", "botas"),
            ("Sneakers", "zapatillas"), ("Sandals", "sandalias"), ("Hat", "gorra"),
            ("Scarf", "bufanda"), ("Gloves", "guantes"), ("Belt", "cinturon"),
            ("Socks", "calcetines"), ("Winter coat", "abrigo de invierno"), ("Wool hat", "gorro de lana"),
            ("Snow boots", "botas de nieve"), ("Swimsuit", "traje de baño"), ("Sunglasses", "gafas de sol"),
            ("Flip-flops", "chanclas"), ("Tank top", "camiseta sin mangas"), ("Suit", "traje"),
            ("Tie", "corbata"), ("Blazer", "americana"), ("High heels", "tacones altos"),
            ("Evening dress", "vestido de noche"), ("Cotton", "algodon"), ("Wool", "lana"),
            ("Leather", "cuero"), ("Silk", "seda"), ("Linen", "lino")
        ],
        "is_numbers": False
    },
    
    "Lesson 20 - Adverbs": {
        "count": 20,
        "words": [
            ("Quickly", "rapidamente"), ("Slowly", "lentamente"), ("Always", "siempre"),
            ("Never", "nunca"), ("Often", "a menudo"), ("Sometimes", "a veces"),
            ("Rarely", "raramente"), ("Already", "ya"), ("Still", "todavia"),
            ("Yet", "aun"), ("Soon", "pronto"), ("Now", "ahora"),
            ("Later", "mas tarde"), ("Today", "hoy"), ("Tomorrow", "mañana"),
            ("Yesterday", "ayer"), ("Clearly", "claramente"), ("Together", "juntos"),
            ("Apart", "separados"), ("Forever", "para siempre")
        ],
        "is_numbers": False
    },
    
    "Lesson 21 - Animals": {
        "count": 20,
        "words": [
            ("Dog", "perro"), ("Cat", "gato"), ("Horse", "caballo"),
            ("Cow", "vaca"), ("Sheep", "oveja"), ("Pig", "cerdo"),
            ("Goat", "cabra"), ("Chicken", "pollo"), ("Duck", "pato"),
            ("Bird", "pajaro"), ("Rabbit", "conejo"), ("Mouse", "raton"),
            ("Lion", "leon"), ("Tiger", "tigre"), ("Bear", "oso"),
            ("Elephant", "elefante"), ("Monkey", "mono"), ("Fox", "zorro"),
            ("Wolf", "lobo"), ("Deer", "ciervo")
        ],
        "is_numbers": False
    },
    
    "Lesson 22 - Numbers 76-110": {
        "count": 35,
        "words": [
            ("76", "setenta y seis"), ("77", "setenta y siete"), ("78", "setenta y ocho"),
            ("79", "setenta y nueve"), ("80", "ochenta"), ("81", "ochenta y uno"),
            ("82", "ochenta y dos"), ("83", "ochenta y tres"), ("84", "ochenta y cuatro"),
            ("85", "ochenta y cinco"), ("86", "ochenta y seis"), ("87", "ochenta y siete"),
            ("88", "ochenta y ocho"), ("89", "ochenta y nueve"), ("90", "noventa"),
            ("91", "noventa y uno"), ("92", "noventa y dos"), ("93", "noventa y tres"),
            ("94", "noventa y cuatro"), ("95", "noventa y cinco"), ("96", "noventa y seis"),
            ("97", "noventa y siete"), ("98", "noventa y ocho"), ("99", "noventa y nueve"),
            ("100", "cien"), ("101", "ciento uno"), ("102", "ciento dos"),
            ("103", "ciento tres"), ("104", "ciento cuatro"), ("105", "ciento cinco"),
            ("106", "ciento seis"), ("107", "ciento siete"), ("108", "ciento ocho"),
            ("109", "ciento nueve"), ("110", "ciento diez")
        ],
        "is_numbers": True
    },
    
    "Lesson 23 - Places in Town": {
        "count": 20,
        "words": [
            ("School", "escuela"), ("Hospital", "hospital"), ("Bank", "banco"),
            ("Restaurant", "restaurante"), ("Library", "biblioteca"), ("Supermarket", "supermercado"),
            ("Cinema", "cine"), ("Post office", "correos"), ("Police station", "comisaria"),
            ("Park", "parque"), ("Museum", "museo"), ("Theatre", "teatro"),
            ("Hotel", "hotel"), ("Stadium", "estadio"), ("Church", "iglesia"),
            ("Pharmacy", "farmacia"), ("Bakery", "panaderia"), ("Butcher", "carniceria"),
            ("Market", "mercado"), ("Hairdresser", "peluqueria")
        ],
        "is_numbers": False
    },
    
    "Lesson 24 - School Supplies": {
        "count": 20,
        "words": [
            ("Book", "libro"), ("Pen", "boligrafo"), ("Pencil", "lapiz"),
            ("Eraser", "borrador"), ("Notebook", "cuaderno"), ("Ruler", "regla"),
            ("Scissors", "tijeras"), ("Backpack", "mochila"), ("Folder", "carpeta"),
            ("Calculator", "calculadora"), ("Marker", "marcador"), ("Chalk", "tiza"),
            ("Map", "mapa"), ("Highlighter", "resaltador"), ("Projector", "proyector"),
            ("Laptop", "portatil"), ("Printer", "impresora"), ("USB stick", "memoria usb"),
            ("Schoolbag", "mochila escolar"), ("Sharpener", "sacapuntas")
        ],
        "is_numbers": False
    },
    
    "Lesson 25 - Transportation": {
        "count": 20,
        "words": [
            ("Car", "coche"), ("Bus", "autobus"), ("Train", "tren"),
            ("Bicycle", "bicicleta"), ("Motorcycle", "motocicleta"), ("Airplane", "avion"),
            ("Boat", "barco"), ("Tram", "tranvia"), ("Taxi", "taxi"),
            ("Subway", "metro"), ("Ferry", "ferry"), ("Yacht", "yate"),
            ("Hot air balloon", "globo aerostatico"), ("Spaceship", "nave espacial"), ("Rickshaw", "rickshaw"),
            ("Gondola", "gondola"), ("Zeppelin", "zepelin"), ("Rollerblades", "patines en linea"),
            ("Canoe", "canoa"), ("Submarine", "submarino")
        ],
        "is_numbers": False
    },
    
    "Lesson 26 - Numbers 111-150": {
        "count": 31,
        "words": [
            ("111", "ciento once"), ("112", "ciento doce"), ("113", "ciento trece"),
            ("114", "ciento catorce"), ("115", "ciento quince"), ("116", "ciento dieciseis"),
            ("117", "ciento diecisiete"), ("118", "ciento dieciocho"), ("119", "ciento diecinueve"),
            ("120", "ciento veinte"), ("121", "ciento veintiuno"), ("122", "ciento veintidos"),
            ("123", "ciento veintitres"), ("124", "ciento veinticuatro"), ("125", "ciento veinticinco"),
            ("126", "ciento veintiseis"), ("127", "ciento veintisiete"), ("128", "ciento veintiocho"),
            ("129", "ciento veintinueve"), ("130", "ciento treinta"), ("131", "ciento treinta y uno"),
            ("132", "ciento treinta y dos"), ("133", "ciento treinta y tres"), ("134", "ciento treinta y cuatro"),
            ("135", "ciento treinta y cinco"), ("136", "ciento treinta y seis"), ("137", "ciento treinta y siete"),
            ("140", "ciento cuarenta"), ("145", "ciento cuarenta y cinco"), ("149", "ciento cuarenta y nueve"),
            ("150", "ciento cincuenta")
        ],
        "is_numbers": True
    }
}

def generate_questions(lesson_name, words, count, is_numbers):
    """Madde sayısına göre farklı soru tarzları oluştur"""
    questions = []
    
    if is_numbers:
        # Sayı dersleri için özel soru tarzları
        # Tarz 1: Sayıdan kelimeye (Cevap: KELIME)
        for english, spanish in words:
            questions.append({
                'type': 'num_to_word',
                'question': f"What is '{english}' in Spanish? (Answer with the WORD)",
                'answer': spanish,
                'display_answer': spanish  # KELIME göster
            })
        
        # Tarz 2: Kelimeden sayıya (Cevap: SAYI)
        for english, spanish in words:
            questions.append({
                'type': 'word_to_num',
                'question': f"What number is '{spanish}'? (Answer with the NUMBER)",
                'answer': english,
                'display_answer': english  # SAYI göster
            })
        
        # Tarz 3: Karışık (Cevap türüne göre)
        for english, spanish in words:
            if random.choice([True, False]):
                # Sayıdan kelimeye
                questions.append({
                    'type': 'mixed',
                    'question': f"Translate '{english}' to Spanish word:",
                    'answer': spanish,
                    'display_answer': spanish  # KELIME
                })
            else:
                # Kelimeden sayıya
                questions.append({
                    'type': 'mixed',
                    'question': f"What number is '{spanish}'?",
                    'answer': english,
                    'display_answer': english  # SAYI
                })
    
    elif count <= 20:
        # 20 ve altı: 3 farklı soru tarzı
        # Tarz 1: English -> Spanish
        for english, spanish in words:
            questions.append({
                'type': 'eng_to_spa',
                'question': f"Translate to Spanish: '{english}'",
                'answer': spanish,
                'display_answer': spanish
            })
        
        # Tarz 2: Spanish -> English
        for english, spanish in words:
            questions.append({
                'type': 'spa_to_eng',
                'question': f"Translate to English: '{spanish}'",
                'answer': english,
                'display_answer': english
            })
        
        # Tarz 3: İlk harf ipucu
        for english, spanish in words:
            first_letter = spanish[0] if spanish else ""
            blanks = "_" * (len(spanish) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}' - Complete the Spanish word",
                'answer': spanish,
                'display_answer': spanish
            })
    
    elif 20 < count <= 40:
        # 20-40 arası: 3 bölüm, 2 farklı soru tarzı
        third = len(words) // 3
        
        # Bölüm 1: English -> Spanish
        for english, spanish in words[:third]:
            questions.append({
                'type': 'eng_to_spa',
                'question': f"Translate to Spanish: '{english}'",
                'answer': spanish,
                'display_answer': spanish
            })
        
        # Bölüm 2: Spanish -> English
        for english, spanish in words[third:third*2]:
            questions.append({
                'type': 'spa_to_eng',
                'question': f"Translate to English: '{spanish}'",
                'answer': english,
                'display_answer': english
            })
        
        # Bölüm 3: İlk harf ipucu
        for english, spanish in words[third*2:]:
            first_letter = spanish[0] if spanish else ""
            blanks = "_" * (len(spanish) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': spanish,
                'display_answer': spanish
            })
    
    else:  # count > 40
        # 40+ : 5 bölüm, 3-4 farklı soru tarzı
        fifth = len(words) // 5
        
        # Bölüm 1: English -> Spanish
        for english, spanish in words[:fifth]:
            questions.append({
                'type': 'eng_to_spa',
                'question': f"Translate to Spanish: '{english}'",
                'answer': spanish,
                'display_answer': spanish
            })
        
        # Bölüm 2: Spanish -> English
        for english, spanish in words[fifth:fifth*2]:
            questions.append({
                'type': 'spa_to_eng',
                'question': f"Translate to English: '{spanish}'",
                'answer': english,
                'display_answer': english
            })
        
        # Bölüm 3: İlk harf
        for english, spanish in words[fifth*2:fifth*3]:
            first_letter = spanish[0] if spanish else ""
            blanks = "_" * (len(spanish) - 1)
            questions.append({
                'type': 'first_letter',
                'question': f"'{english}' = '{first_letter}{blanks}'",
                'answer': spanish,
                'display_answer': spanish
            })
        
        # Bölüm 4: Son harf
        for english, spanish in words[fifth*3:fifth*4]:
            last_letter = spanish[-1] if spanish else ""
            blanks = "_" * (len(spanish) - 1)
            questions.append({
                'type': 'last_letter',
                'question': f"'{english}' = '{blanks}{last_letter}'",
                'answer': spanish,
                'display_answer': spanish
            })
        
        # Bölüm 5: Harf sayısı ipucu
        for english, spanish in words[fifth*4:]:
            questions.append({
                'type': 'letter_hint',
                'question': f"'{english}' = ({len(spanish)} letters, starts with {spanish[:2]}...)",
                'answer': spanish,
                'display_answer': spanish
            })
    
    return questions

def create_general_review(lesson_name, words, is_numbers):
    """Her bölümün sonunda genel tekrar soruları"""
    review = []
    sample_size = min(20, len(words))
    sampled_words = random.sample(words, sample_size)
    
    for english, spanish in sampled_words:
        if is_numbers:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] '{english}' in Spanish?",
                    'answer': spanish,
                    'display_answer': spanish
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] What number is '{spanish}'?",
                    'answer': english,
                    'display_answer': english
                })
        else:
            if random.choice([True, False]):
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{english}'",
                    'answer': spanish,
                    'display_answer': spanish
                })
            else:
                review.append({
                    'type': 'review',
                    'question': f"[GENERAL REVIEW] Translate: '{spanish}'",
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
║        COMPREHENSIVE SPANISH TEST SYSTEM                  ║
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
        print(Fore.GREEN + "🎉🎉🎉 EXCELLENT! You're amazing at Spanish! 🎉🎉🎉")
    elif final_percentage >= 70:
        print(Fore.BLUE + "👏👏👏 VERY GOOD! Great performance! 👏👏👏")
    elif final_percentage >= 50:
        print(Fore.YELLOW + "👍👍 GOOD! Keep going and you'll be excellent! 👍👍")
    else:
        print(Fore.RED + "📚📚 Keep studying! You can do it! 📚📚")
    
    print(Fore.GREEN + "\nCongratulations! You completed the entire test! 🎊")

if __name__ == "__main__":
    main()