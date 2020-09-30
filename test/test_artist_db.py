from unittest import TestCase
import os

import artist_db
from artist_db import EntryError, Artists, Artworks, delete_all_artists, delete_all_artworks

class TestArtistDb(TestCase):

    @classmethod
    def setUpClass(cls):
        artist_db.db = os.path.join('database', 'test_books.db')
        Artists.instance = None
        Artworks.instance = None


    def setUp(self):
        self.Artist = Artists()
        self.Artwork = Artworks()
        self.clear_tables()

    def clear_tables(self):
        self.Artwork.delete_all_artworks()
        self.Artist.delete_all_artists()
