from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Token, Template


def name_to_email(name):
    names = name.split()
    return (names[0][0] + names[-1]).lower()


class PersonProfile(BaseGenerator):
    ID = "profile"

    _templates = [
        Template(
            Token.SetInternalVariable("person_name", Token.Generator("full_name")),

            Token.GetInternalVariable("person_name"),
            Token.Literal("#"),

            Token.GetInternalVariable("person_name", template=name_to_email),
            Token.Literal("@"),
            Token.Generator("domain"),
            Token.Literal("#"),

            Token.Generator("forum_username")
        )
    ]

    def on_finish(self, result_string):
        items = result_string.split("#")

        return {
            "name": items[0],
            "email": items[1],
            "internet_username": items[2]
        }


class SomeWeirdNameGenerator(BaseGenerator):
    ID = "weird_name"
    _templates = [
        Template(
            Token.Generator("full_name")
        )
    ]

    def on_finish(self, result_string):
        chars = {"a": "4", "e": "3", "t": "7", "i": "1", "o": "0"}
        for char in chars:
            result_string = result_string.replace(char, chars[char])
        return result_string.upper()


if __name__ == "__main__":
    print(SomeWeirdNameGenerator().generate())
