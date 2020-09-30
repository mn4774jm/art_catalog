from unittest import TestCase
import os

import artist_db
from artist_db import EntryError, Artists, Artworks
from query import artist_query

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

    def add_test_data(self):
        self.clear_artwork_table()
        self.clear_artist_table()

        self.artist1 = Artists(name='dave', email='asdfgh@gmail.com')
        self.artist2 = Artists(name='phil', email='iamphil@gmail.com')
        self.artist1.save()
        self.artist2.save()

        self.art1 = Artworks(name=artist_query('dave'), artwork_name='art1', price=43)
        self.art2 = Artworks(name=artist_query('phil'), artwork_name='art2', price=34)

    def clear_artist_table(self):
        self.Artist.delete_all_artists()

    def clear_artwork_table(self):
        self.Artwork.delete_all_artworks()

    def test_add_artist(self):
        new_artist = Artists(name='aa', email='aaa123@gmail.com')
        new_artist.save()


    def test_add_artist_duplicate(self):
        new_artist = Artists(name='dave', email='aaa123@gmail.com')
        new_artist.save()


        # with self.assertRaises(EntryError):
        #     art_dupe = Artists(name='dave', email='aaa123@gmail.com')
        #     art_dupe.save()



    def test_art_no_artist_in_database(self):

        pass

