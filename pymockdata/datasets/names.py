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
