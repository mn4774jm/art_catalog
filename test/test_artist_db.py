from unittest import TestCase
from config import db_test_path
import artist_db
from artist_db import EntryError, Artists, Artworks
from query import artist_query
import os
from peewee import *


db_test_path = os.path.join('database', db_test_path)
db = SqliteDatabase(db_test_path)

db.connect()
db.create_tables([Artists, Artworks])


class TestArtistDb(TestCase):

    def test_add_artist(self):
        Artists.delete().execute()
        artist_db.create_new_artist('dave', '12345@gmail.com')
        artist = Artists.select().where(Artists.artist == 'dave').get()
        self.assertEqual(artist.artist, "dave")



    def test_add_duplicate(self):
        Artists.delete().execute()
        artist_db.create_new_artist('dave', '12345@gmail.com')
        with self.assertRaises(EntryError):
            artist_db.create_new_artist('dave', '12345@gmail.com')





