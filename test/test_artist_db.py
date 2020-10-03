from unittest import TestCase
from config import db_test_path
import artist_db
from artist_db import EntryError, Artists, Artworks
import os
from peewee import *
import config
import models
import query


db_test_path = os.path.join('database', db_test_path)
db = SqliteDatabase(db_test_path)


db.connect()
db.create_tables([Artists, Artworks])


class TestArtistDb(TestCase):

    # @classmethod
    def setUp(self):
        config.db_path = os.path.join('database', 'test_art.db')
        artist_db.delete_all_tables()
        # artist_db.Artists.instance = None
        # artist_db.Artworks.instance = None

    # def setUp(self):
    #     self.Artists = artist_db.Artists()
    #     self.Artworks = artist_db.Artworks()


    def create_test_data(self):
        self.clear_tables()
        self.artist = Artists(artist='test', email='test@test.com')
        self.artist.save()

        self.art = Artworks(artist=query.artist_query('test'), artwork_name='test_art_1', price=123, available='Sold')
        self.art.save()
        self.art = Artworks(artist=query.artist_query('test'), artwork_name='test_art_2', price=123)
        self.art.save()
        self.art = Artworks(artist=query.artist_query('test'), artwork_name='test_art_3', price=123)
        self.art.save()
        self.artist = Artists(artist='testNoArt', email='test@test.com')
        self.artist.save()


    # def create_test_data(self):
    #     artist_db.delete_all_tables()
    #     art_list = ['test_art_1', 'test_art_2', 'test_art_3']
    #     Artists.delete().execute()
    #     new_artist1 = artist_db.create_new_artist('test', 'test@test.com')
    #     new_artist1.save()
    #     new_artist2 = artist_db.create_new_artist('testNoArt', 'test@test.com')
    #     new_artist2.save()
    #     for i in range(3):
    #         new_art = artist_db.create_art_entry('test', art_list[i])
    #         new_art.save()


    def test_add_artist(self):
        Artists.delete().execute()
        artist = Artists(artist='dave', email='12345@gmail.com')
        artist.save()
        artist = Artists.select().where(Artists.artist == 'dave').get()
        self.assertEqual(artist.artist, "dave")

    def test_add_duplicate(self):
        Artists.delete().execute()
        artist_db.create_new_artist('dave', '12345@gmail.com')
        with self.assertRaises(EntryError):
            artist_db.create_new_artist('dave', '12345@gmail.com')

    def test_create_art_artist_exists(self):

        # artist_db.create_art_entry()
        pass

    def test_create_art_no_artist(self):
        pass

    def clear_tables(self):
        artist_db.delete_all_tables()






