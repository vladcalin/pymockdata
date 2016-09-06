from collections import namedtuple

from pymockdata.core.constants import Localisation
from ..datasets import Dataset


# <editor-fold desc="en_US">
# items taken from http://www.lifesmith.com/comnames.html
en_us_male_names = Dataset(name="male_name", localisation=Localisation.en_US, items=[
    "James", "John", "Robert", "Michael", "William", "David", "Richard", "Charles", "Joseph", "Thomas", "Christopher",
    "Daniel", "Paul", "Mark", "Donald", "George", "Kenneth", "Steven", "Edward", "Brian", "Ronald", "Anthony", "Kevin",
    "Jason", "Jeff"
])

en_us_female_names = Dataset(name="female_name", localisation=Localisation.en_US, items=[
    "Mary", "Patricia", "Linda", "Barbara", "Elizabeth", "Jennifer", "Maria", "Susan", "Margaret", "Dorothy", "Lisa",
    "Nancy", "Karen", "Betty", "Helen", "Sandra", "Donna", "Carol", "Ruth", "Sharon", "Michelle", "Laura", "Sarah",
    "Kimberly", "Deborah"
])

en_us_last_names = Dataset(name="last_name", localisation=Localisation.en_US, items=[
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson",
    "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark",
    "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill",
    "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner",
    "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins"
])
# </editor-fold>


# <editor-fold desc="ro_RO">
# items taken from https://ro.wikipedia.org/wiki/Lista_celor_mai_uzuale_nume_de_familie#Rom.C3.A2nia
ro_ro_last_names = Dataset(name="last_name", localisation=Localisation.ro_RO, items=[
    "Popa", "Pop", "Popescu", "Ionescu", "Neme?", "Stan", "Dumitrescu", "Dima", "Ioni??", "Marin", "Tudor", "Dobre",
    "Barbu", "Nistor", "Florea", "Ene", "Dinu", "Georgescu", "Stoica", "Diaconu", "Diaconescu", "Mazilescu", "Mocanu",
    "Oprea", "Voinea", "Dochioiu", "Albu", "Tabacu", "Manole", "Cristea", "Toma", "St?nescu", "Preda"
])

ro_ro_female_names = Dataset(name="female_name", localisation=Localisation.ro_RO, items=[
    "Adelina", "Adina", "Adriana", "Alina", "Ana", "Ancuta", "Angelica", "Aurelia", "Camelia", "Cecilia", "Doina",
    "Ecaterina", "Eliza", "Elizabeta", "Eugenia", "Evelina", "Felicia", "Florentina", "Gabriela", "Geanina", "Georgeta",
    "Georgiana", "Gianina", "Hortensia", "Iasmina", "Ileana", "Ilinca", "Ingrid", "Ionela", "Irina", "Lacramioara",
    "Larisa", "Laura", "Liliana", "Livia", "Luminita", "Madalina", "Magdalena", "Marcela", "Margareta", "Maria",
    "Mariana", "Mirela", "Nadia", "Natalia", "Nicoleta", "Oana", "Olivia", "Patricia", "Petronela", "Paula", "Rebeca",
    "Roxana", "Ruxandra", "Silvia", "Simona", "Sonia", "Sorina", "Teodora", "Valeria", "Veronica", "Viviana"
])

ro_ro_male_names = Dataset(name="male_name", localisation=Localisation.ro_RO, items=[
    "Adelin", "Adrian", "Alin", "Andrei", "Anton", "Augustin", "Ciprian", "Dinu", "Doru", "Dragos", "Emil", "Emilian",
    "Eric", "Eugen", "Eusebiu", "Felix", "Filip", "Flavian", "Florentin", "Florin", "Gabriel", "George", "Gheorghe",
    "Horatiu", "Iancu", "Ilie", "Ioan", "Ion", "Ionel", "Ionut", "Iustin", "Laurentiu", "Leonard", "Liviu", "Lucian",
    "Madalin", "Manuel", "Marcel", "Mihai", "Mihail", "Mihnea", "Mircea", "Nicolae", "Octav", "Octavian", "Olivian",
    "Ovidiu", "Paul", "Pavel", "Petre", "Petru", "Radu", "Rares", "Robert", "Sandu", "Sebastian", "Serban", "Sergiu",
    "Silviu", "Sorin", "Stefan", "Stelian", "Teodor", "Timotei", "Toma", "Traian", "Tudor", "Vadim", "Valerian",
    "Vasile", "Victor", "Viorel", "Virgil", "Zaharia"
])
# </editor-fold>
