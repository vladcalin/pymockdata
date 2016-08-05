import random
import string

import pymockdata.data as mockdata
from pymockdata.mockdataengine import _load_generators

class TokenParsingError(Exception):
    pass


class Token:
    """This class contains token identifiers that compose a valid template object.

    Attributes:

    DIGIT                       : generates a random digit
    LETTER_LOWER                : generates a lowercase letter
    LETTER_UPPER                : generates an uppercase letter
    LETTER                      : generates a letter (lowercase or uppercase)
    DOT                         : generates a dot
    SYMBOL                      : generates a printable symbol from string.punctuation
    SPACE                       : generates a space
    VALUE(value_id)             : generates a random value from a data set. Data sets are defined in pymockdata.data
        and their IDs are the constants defined in that module
    NUMBER_INTERVAL(min, max)   : generates a random number in the [min, max] interval in decimal representation
    LITERAL(string): generates a string literal. Basically, copies the string parameter into the output.
    """
    _TOKEN_ID_DIGIT = 0
    _TOKEN_ID_LETTER = 1
    _TOKEN_ID_DOT = 2
    _TOKEN_ID_SYMBOL = 3
    _TOKEN_ID_FIELD = 4
    _TOKEN_ID_INTERVAL = 5
    _TOKEN_ID_LITERAL = 6
    _TOKEN_ID_SPACE = 7

    DIGIT = (_TOKEN_ID_DIGIT, None)
    LETTER_LOWER = (_TOKEN_ID_LETTER, "lower")
    LETTER_UPPER = (_TOKEN_ID_LETTER, "upper")
    LETTER = (_TOKEN_ID_LETTER, None)
    DOT = (_TOKEN_ID_DOT, None)
    SYMBOL = (_TOKEN_ID_SYMBOL, None)
    SPACE = (_TOKEN_ID_SPACE, None)

    @classmethod
    def VALUE(cls, field_name):
        return cls._TOKEN_ID_FIELD, field_name

    @classmethod
    def NUMBER_INTERVAL(cls, min, max):
        return cls._TOKEN_ID_INTERVAL, (min, max)

    @classmethod
    def LITERAL(cls, str_literal):
        return cls._TOKEN_ID_LITERAL, str_literal

    @classmethod
    def RANDOM_SYMBOL(cls, symbol_set):
        return cls._TOKEN_ID_SYMBOL, symbol_set

    class Repeat:
        """
        Causes the designated token to repeat multiple times

        Example: (Token.Repeat(Token.DIGIT, 3)) is equivalent to (Token.DIGIT, Token.DIGIT, Token.DIGIT)
        """
        def __init__(self, token, repeat=1, random_repeat=None):
            self._token = token
            if random_repeat:
                self._repeat = random.randint(random_repeat[0], random_repeat[1])
            else:
                self._repeat = repeat

        def get(self):
            return [self._token for _ in range(self._repeat)]

    class Generator:
        # TODO: implement this
        def __init__(self, generator_id):
            self._generator_id = generator_id

        def get(self):
            generator = [gen for gen in _load_generators() if gen.ID == self._generator_id]
            if len(generator):
                return generator[0]().generate()

            raise TokenParsingError("No suitable generator found for ID={}".format(self._generator_id))


class TokenTemplate:

    def __init__(self, token, template=lambda x: x):
        self._token = token
        self._template = template


class Template:
    def __init__(self, *tokens):
        self._tokens = tokens

    def render(self, *, seed=None):
        if seed:
            random.seed(seed)

        parsed_tokens = []
        for token in self._tokens:
            if isinstance(token, Token.Repeat):
                for subtoken in token.get():
                    parsed_tokens.append(self._resolve_token(subtoken))
                continue
            elif isinstance(token, Token.Generator):
                parsed_tokens.append(token.get())
                continue
            parsed_tokens.append(self._resolve_token(token))

        return "".join(parsed_tokens)

    def _resolve_token(self, token):
        token_id, token_data = token
        return self._token_resolvers[token_id](self, token_data)

    def _token_digit_resolver(self, token_data):
        return random.choice(string.digits)

    def _token_letter_resolver(self, token_data):
        if token_data == "upper":
            return random.choice(string.ascii_uppercase)
        elif token_data == "lower":
            return random.choice(string.ascii_lowercase)
        else:
            return random.choice(string.ascii_letters)

    def _token_symbol_resolver(self, token_data):
        if token_data:
            return random.choice(token_data)
        else:
            return random.choice(string.punctuation)

    def _token_field_resolver(self, token_data):
        if not hasattr(mockdata, token_data):
            raise TokenParsingError("field '{}' does not exist in pymockdata.data".format(token_data))
        return random.choice(getattr(mockdata, token_data))

    def _token_interval_resolver(self, token_data):
        return str(random.randint(token_data[0], token_data[1]))

    def _token_literal_resolver(self, token_data):
        return token_data

    def _token_point_resolver(self, token_data):
        return "."

    def _token_space_resolver(self, token_data):
        return " "

    _token_resolvers = {
        Token._TOKEN_ID_DIGIT: _token_digit_resolver,
        Token._TOKEN_ID_LETTER: _token_letter_resolver,
        Token._TOKEN_ID_DOT: _token_point_resolver,
        Token._TOKEN_ID_SYMBOL: _token_symbol_resolver,
        Token._TOKEN_ID_FIELD: _token_field_resolver,
        Token._TOKEN_ID_INTERVAL: _token_interval_resolver,
        Token._TOKEN_ID_LITERAL: _token_literal_resolver,
        Token._TOKEN_ID_SPACE: _token_space_resolver,
    }


if __name__ == '__main__':
    # Example definition of a Template object which will generate items similar to:
    # Lindsay Z. Adams
    # Miya C. Bradshaw
    # Saniyah M. Harding
    # etc.
    t = Template(
        Token.Generator("female_name"),
        Token.LITERAL(" loves "),
        Token.Generator("male_name")
    )
    print(t.render())
    print(t.render())
    print(t.render())
