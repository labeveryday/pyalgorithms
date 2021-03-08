import ngenerator
import unittest


class TestMytest(unittest.TestCase):
    def test_get_names(self):
        self.assertNotEqual(ngenerator.get_names(1), 'Amy')