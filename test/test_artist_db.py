from unittest import TestCase
import os

import artist_db
from artist_db import EntryError, Artists, Artworks

class TestArtistDb(TestCase):

    @classmethod
    def setUpClass(cls):
        artist_db.db = os.path.join('database', 'test_books.db')
        Artists.instance = None
        Artworks.instance = None
