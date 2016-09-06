import string

from ..datasets import Dataset


uppercase_ascii_letters = Dataset("uppercase_letter", None, string.ascii_uppercase)
lowercase_ascii_letters = Dataset("lowercase_letter", None, string.ascii_lowercase)
ascii_letters = Dataset("letter", None, string.ascii_letters)
digits = Dataset("digit", None, string.digits)
hex_digit = Dataset("hex_digit", None, string.hexdigits)
