import unittest

from arista.eos import EAPI
from pyeapi.eapilib import CommandError, ConnectionError

host = '10.1.1.72'
username = 'lab'
password = 'Password'


class TestEAPI(unittest.TestCase):

    def setUp(self):
        self.eos = EAPI(host=host, username=username, password=password)

    def test_init_method_successfully_connects(self):
        self.assertIsInstance(self.eos, EAPI)

    def test_init_method_with_invalid_host_raises_ConnectionError(self):
        self.assertRaises(ConnectionError, EAPI, host='1.1.1.1', username=username,
                          password=password, timeout=2)

    def test_inti_method_with_invalid_username_raises_ConnectionError(self):
        self.assertRaises(ConnectionError, EAPI, host=host, username='no-one', password=password)

    def test_inti_method_with_invalid_password_raises_ConnectionError(self):
        self.assertRaises(ConnectionError, EAPI, host=host, username=username, password='wrong')

    def test_show_command_raises_type_error_if_command_is_not_a_string_type(self):
        self.assertRaises(TypeError, self.eos.show_command, ['blah'])

    def test_show_command_returns_a_dict(self):
        self.assertIsInstance(self.eos.show_command(), dict)

    def test_show_command_with_invalid_command_raises_CommandError(self):
        self.assertRaises(CommandError, self.eos.show_command, 'not a command')

    def test_show_commands_raises_type_error_if_command_list_is_none(self):
        self.assertRaises(TypeError, self.eos.show_commands)

    def test_show_commands_returns_a_list(self):
        self.assertIsInstance(self.eos.show_commands(['show version', 'show ip interface']), list)

    def test_show_commands_with_invalid_command_raises_CommandError(self):
        self.assertRaises(CommandError, self.eos.show_commands, ['show version', 'not a command'])
