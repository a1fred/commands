import unittest
import argparse

from management_commands import utils, Command


class Calculate(Command):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def handle(self, **kwargs):
        return self.a + self.b


class AsyncCalculate(Command):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    async def handle(self, **kwargs):
        return self.a + self.b


class UtilsTests(unittest.TestCase):
    def test_underscore(self):
        self.assertEqual(
            utils.underscore('HelpMe'),
            'help_me'
        )

    def test_initialize_argument_parser(self, commands=()):
        parser = utils.initialize_argument_parser(commands, '__handler')
        self.assertIsInstance(parser, argparse.ArgumentParser)
        return parser

    def test_run_command(self):
        parser = self.test_initialize_argument_parser([
            Calculate(1, 2),
        ])
        result = utils.run_command(parser, "__handler", ['calculate'])
        self.assertEqual(result, 3)

        with self.assertRaises(SystemExit):
            utils.run_command(parser, "__handler", ['notexistcommand'])

    def test_run_command_async(self):
        parser = self.test_initialize_argument_parser([
            AsyncCalculate(1, 2),
        ])
        result = utils.run_command(parser, "__handler", ['async_calculate'])
        self.assertEqual(result, 3)

        with self.assertRaises(SystemExit):
            utils.run_command(parser, "__handler", ['notexistcommand'])
