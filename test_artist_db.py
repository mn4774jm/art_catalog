from unittest import TestCase
import os

import artist_db
from artist_db import EntryError, Artists, Artworks

class TestArtistDb(TestCase):

    @classmethod
    def setUpClass(cls):
        artist_db.db = os.path.join('database', 'test_gallery.db')
        Artists.instance = None
        Artworks.instance = None

    def setUp(self):
        self.Artist = Artists()
        self.Artwork = Artworks()
        self.clear_artwork_table()
        self.clear_artist_table()

    def clear_artist_table(self):
        self.Artist.delete_all_artists()

    def clear_artwork_table(self):
        self.Artwork.delete_all_artworks()

    def test_art_no_artist(self):
        pass

