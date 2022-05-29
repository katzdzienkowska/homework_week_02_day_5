import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Massive Attack", "Teardrop")
        self.song_2 = Song("Moderat", "Bad Kingdom")
        self.song_3 = Song("The Knife", "Heartbeats")

    def test_has_artist(self):
        self.assertEqual("Moderat", self.song_2.artist)

    def test_has_song_title(self):
        self.assertEqual("Heartbeats", self.song_3.title)
    
