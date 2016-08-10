from unittest import TestCase

from pymockdata import DataModel
from pymockdata.core.template import Template, Token
from pymockdata.core.base import BaseGenerator

class EngineUnitTests(TestCase):

    def test_data_model_init(self):
        data_model = DataModel(
            field1=DataModel.email,
            field2=DataModel.domain
        )

        generated = data_model.generate_one()
        self.assertIsInstance(generated, dict)
        self.assertCountEqual(list(generated.keys()), ["field1", "field2"])

        generated = data_model.generate_batch(10)
        self.assertIsInstance(generated, list)
        self.assertEqual(len(generated), 10)

    def test_data_model_raises(self):
        data_model = DataModel(
            field1="not_existing"
        )
        with self.assertRaises(AttributeError):
            data_model.generate_one()

    def test_register_generator(self):
        data_model = DataModel()

        class TestGenerator(BaseGenerator):

            ID = "test"
            _templates = [
                Template(Token.Literal("hello world"))
            ]

        data_model.register_generator(TestGenerator)

        self.assertEqual(data_model.value_for("test"), "hello world")

    def test_register_wrong_class(self):
        data_model = DataModel()

        class TestGenerator:
            ID = "test"
            _templates = [
                Template(Token.Literal("hello world"))
            ]
        with self.assertRaises(TypeError):
            data_model.register_generator(TestGenerator)