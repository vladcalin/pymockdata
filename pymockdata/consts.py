class Fields:
    # names
    FEMALE_NAME = "female_name"
    MALE_NAME = "male_name"
    LAST_NAME = "last_name"
    FULL_FEMALE_NAME = "full_female_name"
    FULL_MALE_NAME = "full_male_name"

    # personal details
    AGE = "age"
    ADDRESS = "address"
    HOBBY = "hobby"
    PERSONAL_DESCRIPTION = "personal_desc"
    SKILL = "skills"
    USERNAME = "username"
    PASSWORD = "password"
    EMAIL = "email"
    JOB = "job"

    # computers and internet
    IPV4_ADDRESS_PRIVATE = "ipv4_addr_priv"
    IPV4_ADDRESS_PUBLIC = "ipv4_addr_publ"
    IPV4_ADDRESS = "ipv4_addr"

    IPV6_ADDRESS = "ipv6_addr"
    MAC_ADDRESS = "mac_addr"
    WEBSITE = "website"
    URL = "url"
    MIME_TYPE = "mime_type"

    # extensions
    IMAGE_EXTENSION = "img_ext"
    AUDIO_EXTENSION = "audio_ext"
    DOCUMENT_EXTENSION = "document_ext"

    FILE_EXTENSION = "file_extension"
    WEBPAGE_EXTENSION = "webpage_extension"

    # misc
    FILE_NAME = "file_name"
    FILE_PATH_UNIX = "file_path_unix"
    FILE_PATH_WiNDOWS = "file_path_windows"

    HASH_32 = "hash_32"
    HASH_48 = "hash_48"
    HASH_64 = "hash_64"

    UUID = "uuid"
    SENTENCE = "sentence"
    WORD = "word"


class Output:
    DATABASE = 1  # directly for inserting data into database
    XML = 2  # exporting as XML
    CSV = 3  # exporting as CSV
    JSON = 4  # exporting as JSON
    TEMPLATE = 5  # exporting to custom, defined in the template
