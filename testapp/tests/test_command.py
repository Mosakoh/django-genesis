from django.test import TestCase

from genesis.management.commands.let_there_be_light import Command
from adam.management.commands.adam_bootstrap import MyClass


class CommandTests(TestCase):
    def setUp(self):
        self.let_there_be_light = Command()

    def test_calls_app_bootstrap_command(self):
        before_counter = MyClass.counter

        #eve bootstrap command raises ArithmeticError
        with self.assertRaises(ArithmeticError):
            self.let_there_be_light.handle()

        after_counter = MyClass.counter

        #adam bootstrap command increments MyClass counter
        self.assertEqual(after_counter - before_counter, 1)
