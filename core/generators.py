import random
import faker
import morfeusz2

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
    "ból pleców",
    "migrena",
    "depresja",
    "otyłość",
    "bezsenność",
    "artretyzm",
    "niedoczynność tarczycy",
    "choroba serca",
    "rak",
    "osteoporoza",
    "kamica nerkowa",
    "zespół jelita drażliwego",
    "anemia",
    "niedosłuch",
    "krótkowzroczność",
    "choroba autoimmunologiczna",
    "przewlekłe zmęczenie",
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

faker = faker.Faker()

def relative():
    male_prepositions = []
    female_prepositions = []
    male_relatives = []
    female_relatives = []
    ch = random.random()
    if ch < 0.25:
        return random.choice(male_prepositions) + " " + random.choice(male_relatives)
    elif ch < 0.5:
        return random.choice(female_prepositions) + " " + random.choice(female_relatives)

    return random.choice(male_prepositions + female_prepositions) + " " + faker.full_name()