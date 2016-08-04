import pymockdata.consts as constants
from pymockdata.engine import generate_data

# constants

FEMALE_NAME = constants.Fields.FEMALE_NAME
MALE_NAME = constants.Fields.MALE_NAME
LAST_NAME = constants.Fields.LAST_NAME
FULL_FEMALE_NAME = constants.Fields.FULL_FEMALE_NAME
FULL_MALE_NAME = constants.Fields.FULL_MALE_NAME

generate = generate_data

if __name__ == '__main__':
    print(generate_data(FEMALE_NAME, instances=10, seed=100))
    print(generate_data(MALE_NAME, instances=10, seed=100))
    print(generate_data(LAST_NAME, instances=10, seed=100))
    print(generate_data(FULL_FEMALE_NAME, instances=10, seed=100))
    print(generate_data(FULL_MALE_NAME, instances=10, seed=101))
