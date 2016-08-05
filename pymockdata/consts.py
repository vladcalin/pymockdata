class Fields:
    # names
    FEMALE_NAME = "FEMALE_NAME"
    MALE_NAME = "MALE_NAME"
    LAST_NAME = "LAST_NAME"
    FULL_FEMALE_NAME = "FULL_FEMALE_NAME"
    FULL_MALE_NAME = "FULL_MALE_NAME"


class Output:
    DATABASE = 1  # directly for inserting data into database
    XML = 2  # exporting as XML
    CSV = 3  # exporting as CSV
    JSON = 4  # exporting as JSON
    TEMPLATE = 5  # exporting to custom, defined in the template
