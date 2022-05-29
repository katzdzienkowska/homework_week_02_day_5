import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Blue Room", 2)
        self.room_2 = Room("Red Room", 3)
        self.room_3 = Room("Green Room", 5)

    def test_has_name(self):
        self.assertEqual("Blue Room", self.room_1.room_name)

    def test_has_capacity(self):
        self.assertEqual(5, self.room_3.capacity)

    def test_guest_count(self):
        self.assertEqual(0, self.room_1.guest_count())

    def test_can_check_in_guests(self):
        guest_1 = Guest("Kat")
        guest_2 = Guest("Raff")
        self.room_1.check_in(guest_1)
        self.room_1.check_in(guest_2)
        self.assertEqual(2, self.room_1.guest_count())

    def test_can_check_out_guests(self):
        guest_1 = Guest("Kat")
        guest_2 = Guest("Raff")
        self.room_1.check_in(guest_1)
        self.room_1.check_in(guest_2)
        self.room_1.check_out(guest_2)
        self.assertEqual(1, self.room_1.guest_count())

    def test_song_list_starts_empty(self):
        self.assertEqual([], self.room_1.songs)

    def test_can_add_song_to_room(self):
        song_1 = Song("Massive Attack", "Teardrop")
        self.room_1.add_song_to_room(song_1)
        self.assertEqual([song_1], self.room_1.songs)

    def test_mvp_functionality_in_one_go(self):
        guest_1 = Guest("Kat")
        guest_2 = Guest("Raff")
        song_1 = Song("Massive Attack", "Teardrop")
        self.room_1.check_in(guest_1)
        self.room_1.check_in(guest_2)
        self.room_1.check_out(guest_2)
        self.room_1.add_song_to_room(song_1)
        self.assertEqual(1, self.room_1.guest_count())
        self.assertEqual([song_1], self.room_1.songs)