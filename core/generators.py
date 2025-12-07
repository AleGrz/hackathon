import random

sex = lambda: random.choice(["mężczyzna", "kobieta"])

religion = lambda: random.choice(["chrześcijanin", "żyd", "ateista", "muzułmanin"])

sexual_orientation = lambda: random.choice(["heteroseksualny", "homoseksualny", "biseksualny", "aseksualny"])

political_view = lambda: random.choice(["liberał", "konserwatywny", "socjalista", "centrysta", "anarchista", "narodowiec"])

ethnicity = lambda: random.choice(["Polak", "Niemiec", "Ukrainiec", "Azjata", "Arab", "Rom"])

health = lambda: random.choice([
    "zdrowy",
    "przeziębienie",
    "grypa",
    "alergia",
    "astma",
    "nadciśnienie",
    "cukrzyca",
    "migrena",
    "depresja",
    "otyłość",
    "bezsenność",
    "artretyzm",
    "rak",
    "osteoporoza",
    "anemia",
    "niedosłuch",
    "krótkowzroczność",
])

school_name = lambda: random.choice([
    "Uniwersytet Jagielloński",
    "Uniwersytet Warszawski",
    "Politechnika Warszawska",
    "Akademia Górniczo-Hutnicza w Krakowie",
    "Uniwersytet Adama Mickiewicza w Poznaniu",
    "Politechnika Gdańska",
    "Szkoła Główna Handlowa w Warszawie (SGH)",
    "Uniwersytet Wrocławski",
    "Politechnika Wrocławska",
    "Uniwersytet Łódzki",
    "Akademia Sztuk Pięknych w Krakowie",
    "Gdański Uniwersytet Medyczny",
    "Uniwersytet Ekonomiczny w Katowicach",

    "I Liceum Ogólnokształcące im. Mikołaja Kopernika",
    "Liceum Ogólnokształcące z Oddziałami Dwujęzycznymi",
    "Prywatne Liceum Ogólnokształcące 'Sapere Aude'",
    "II Liceum Ogólnokształcące im. Jana III Sobieskiego",
    "V Liceum Ogólnokształcące im. Augusta Witkowskiego",

    "Technikum Informatyczne Zespołu Szkół Łączności",
    "Technikum Geodezyjne Nr 1 w Warszawie",
    "Zespół Szkół Zawodowych i Ogólnokształcących",
    "Szkoła Policealna dla Dorosłych",
    "Branżowa Szkoła I Stopnia (mechanik)",

    "Szkoła Podstawowa Nr 12 im. Marii Konopnickiej",
    "Publiczna Szkoła Podstawowa w Małej Wsi",
    "Specjalny Ośrodek Szkolno-Wychowawczy",
    "Niepubliczna Szkoła Muzyczna I Stopnia",
    "Szkoła Języków Obcych 'Global'",

    "Instytut Naukowo-Badawczy",
    "Kolegium Nauczycielskie",
    "Centrum Kształcenia Ustawicznego",
    "Akademia Wychowania Fizycznego",
    "Szkoła Aspirantów Państwowej Straży Pożarnej"
])


relative = lambda: random.choice([
    'brat',
    'ojciec',
    'syn',
    'dziadek',
    'wujek',
    'siostra',
    'matka',
    'córka',
    'babcia',
    'ciocia',
])

