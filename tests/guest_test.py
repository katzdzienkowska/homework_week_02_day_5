import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Kat")
        self.guest_2 = Guest("Raff")
        self.guest_3 = Guest("Oskar")

    def test_has_guest_name(self):
        self.assertEqual("Kat", self.guest_1.guest_name)

    