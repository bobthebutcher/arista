import unittest

from arista.eos import EAPI

host = '10.1.1.72'
username = 'lab'
password = 'Password'


class TestEAPI(unittest.TestCase):

    def setUp(self):
        self.eos = EAPI(host=host, username=username, password=password)

    def test_init_method_successfully_connects(self):
        self.assertIsInstance(self.eos, EAPI)
