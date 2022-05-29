import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Kat", 20)
        self.guest_2 = Guest("Raff", 15)
        self.guest_3 = Guest("Oskar", 30)

    def test_has_guest_name(self):
        self.assertEqual("Kat", self.guest_1.guest_name)

    