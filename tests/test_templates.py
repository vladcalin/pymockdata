from unittest import TestCase
from unittest.mock import MagicMock, patch
import string

from pymockdata.core.template import Token, Template, TokenParsingError
import pymockdata.data as datasets


class TemplateUnitTests(TestCase):
    def test_token_digit_valid(self):
        t = Template(
            Token.DIGIT
        )
        for _ in range(250):
            self.assertIn(t.render(), string.digits)

    def test_token_digit_generates_all(self):
        t = Template(
            Token.DIGIT
        )
        items = set()
        for i in range(250):
            items.add(t.render(seed=i))
        items = list(items)
        items.sort()
        self.assertEqual(items, list(string.digits))

    def test_token_letter_lower_valid(self):
        t = Template(
            Token.LETTER_LOWER
        )
        for _ in range(250):
            self.assertIn(t.render(), string.ascii_lowercase)

    def test_token_letter_lower_generates_all(self):
        t = Template(
            Token.LETTER_LOWER
        )
        items = set()
        for i in range(250):
            items.add(t.render(seed=i))
        items = list(items)
        items.sort()
        self.assertEqual(items, list(string.ascii_lowercase))

    def test_token_letter_upper_valid(self):
        t = Template(
            Token.LETTER_UPPER
        )
        for _ in range(250):
            self.assertIn(t.render(), string.ascii_uppercase)

    def test_token_letter_upper_generates_all(self):
        t = Template(
            Token.LETTER_UPPER
        )
        items = set()
        for i in range(250):
            items.add(t.render(seed=i))
        items = list(items)
        items.sort()
        self.assertEqual(items, list(string.ascii_uppercase))

    def test_token_letter_valid(self):
        t = Template(
            Token.LETTER
        )
        for _ in range(250):
            self.assertIn(t.render(), string.ascii_letters)

    def test_token_letter_generates_all(self):
        t = Template(
            Token.LETTER
        )
        items = set()
        for i in range(250):
            items.add(t.render(seed=i))
        items = list(items)
        items.sort()
        self.assertCountEqual(items, list(string.ascii_letters))

    def test_token_dot_valid(self):
        t = Template(
            Token.DOT
        )
        self.assertEqual(t.render(), ".")

    def test_token_space_valid(self):
        t = Template(
            Token.SPACE
        )
        self.assertEqual(t.render(), " ")

    def test_token_symbol_valid(self):
        t = Template(
            Token.SYMBOL
        )
        for _ in range(250):
            self.assertIn(t.render(), string.punctuation)

    def test_token_symbol_generates_all(self):
        t = Template(
            Token.SYMBOL
        )
        items = set()
        for i in range(250):
            items.add(t.render(seed=i))
        items = list(items)
        items.sort()
        self.assertEqual(items, list(string.punctuation))

    def test_token_dataset_value(self):
        t = Template(
            Token.DatasetValue(datasets.NOUNS)
        )

        for i in range(250):
            self.assertIn(t.render(seed=i), datasets.nouns)

        t = Template(
            Token.DatasetValue("not_existing")
        )
        with self.assertRaises(TokenParsingError):
            t.render()

    def test_token_number_interval(self):
        MIN = 10
        MAX = 20
        t = Template(
            Token.NumberInverval(MIN, MAX)
        )

        for i in range(250):
            generated = t.render(seed=i)
            self.assertRegex(generated, "\d\d")
            self.assertTrue(MIN <= int(generated) <= MAX)

    def test_token_literal(self):
        t = Template(
            Token.Literal("hello")
        )
        self.assertEqual(t.render(), "hello")

    def test_token_random_symbol(self):
        SYMBOL_SET = "abcdefghijklmnopqrstuvwxyz"
        t = Template(
            Token.RandomSymbol(SYMBOL_SET)
        )
        for i in range(250):
            self.assertIn(t.render(seed=i), SYMBOL_SET)

    def test_token_custom(self):
        TO_RETURN = "it works!"
        func_to_call = MagicMock(return_value=TO_RETURN)
        ARGS = (0, 1, 2)
        KWARGS = {"a": True, "b": 5, "c": "hi"}
        t = Template(
            Token.Custom(func_to_call, args=ARGS, kwargs=KWARGS)
        )

        self.assertEqual(t.render(), TO_RETURN)
        func_to_call.assert_called_once_with(*ARGS, **KWARGS)

        t = Template(
            Token.Custom(func_to_call)
        )
        self.assertEqual(t.render(), TO_RETURN)
        func_to_call.assert_called_with()

    def test_token_special_repeat(self):
        STR = "repeat_me;"
        t = Template(
            Token.Repeat(Token.Literal(STR), repeat=10)
        )
        self.assertEqual(t.render(), STR * 10)

        t = Template(
            Token.Repeat(Token.Literal(STR), random_repeat=(5, 10))
        )
        for i in range(250):
            self.assertTrue(5 <= len(t.render(seed=i).split(";")) - 1 <= 10)

    def test_token_special_transform(self):
        STR = "upper_me"
        STR_FINAL = "UPPER_ME"
        t = Template(
            Token.Transform(Token.Literal(STR), lambda x: x.upper())
        )
        self.assertEqual(t.render(), STR_FINAL)

    def test_token_special_generator(self):
        t = Template(
            Token.Generator("noun")
        )
        self.assertIn(t.render(), datasets.nouns)

    def test_token_special_generator_rising(self):
        with self.assertRaises(TokenParsingError):
            t = Template(
                Token.Generator("does_not_exist")
            )
            t.render()

    def test_token_special_choice(self):
        t = Template(
            Token.Choice(Token.Literal("a"), Token.Literal("b"), Token.Literal("c"))
        )
        value = t.render()
        self.assertIn(value, "abc")
        self.assertEqual(len(value), 1)

        t = Template(
            Token.Choice(Token.Literal("a"), Token.Literal("b"), Token.Literal("c"), count=2)
        )
        self.assertEqual(len(t.render()), 2)

        t = Template(
            Token.Choice(Token.Literal("a"), Token.Literal("b"), Token.Literal("c"), count_range=(1, 3))
        )
        self.assertTrue(1 <= len(t.render()) <= 3)

    def test_token_special_internal_variables(self):
        # one internal variable
        t = Template(
            Token.SetInternalVariable("a", Token.Literal("hello world")),
            Token.GetInternalVariable("a", lambda x: x.upper())
        )
        self.assertEqual(t.render(), "HELLO WORLD")

        # multiple variables
        t = Template(
            Token.SetInternalVariable("a", Token.Literal("hello ")),
            Token.SetInternalVariable("b", Token.Literal("world")),
            Token.GetInternalVariable("a", lambda x: x.strip()),
            Token.GetInternalVariable("b", lambda x: x.upper())
        )
        self.assertEqual(t.render(), "helloWORLD")

        # test overwriting
        t = Template(
            Token.SetInternalVariable("a", Token.Literal("initial")),
            Token.SetInternalVariable("a", Token.Literal("final")),
            Token.GetInternalVariable("a")
        )
        self.assertEqual(t.render(), "final")

        # test bad identifier
        t = Template(
            Token.SetInternalVariable("a", Token.Literal("test")),
            Token.GetInternalVariable("b")
        )
        with self.assertRaises(TokenParsingError):
            t.render()


