from unittest import TestCase
from config import db_test_path
import artist_db
from artist_db import EntryError, Artists, Artworks
import os
from peewee import *
import config
import query


# db_test_path = os.path.join('database', db_test_path)
# db = SqliteDatabase(db_test_path)
#
#
# db.connect()
# db.create_tables([Artists, Artworks])


def clear_tables():
    artist_db.delete_all_tables()


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
        clear_tables()
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

    def test_add_artist(self):
        clear_tables()
        artist = Artists(artist='dave', email='12345@gmail.com')
        artist.save()
        artist = Artists.select().where(Artists.artist == 'dave').get()
        self.assertEqual(artist.artist, "dave")

    def test_add_duplicate(self):
        clear_tables()
        artist_db.create_new_artist('dave', '12345@gmail.com')
        with self.assertRaises(EntryError):
            artist_db.create_new_artist('dave', '12345@gmail.com')

    def test_create_art_artist_exists(self):

        # artist_db.create_art_entry()
        pass

    def test_create_art_no_artist(self):
        pass



    def test_artist_query_not_in_database(self):
        self.create_test_data()
        result = query.artist_query('test_name_not_in_db')
        self.assertEqual(result, '')

    def test_artist_query_in_database(self):
        clear_tables()
        self.create_test_data()
        result = query.artist_query('test').get()
        self.assertEqual(result.artist, 'test')

    def test_search_for_all_by_artist_no_art_in_db(self):
        clear_tables()
        self.create_test_data()
        artist_name = query.artist_query('testNoArt').get()
        result = query.search_all_by_artist(artist_name)
        art_count = result.count()
        self.assertEqual(art_count, 0)

    def test_search_available_by_artist_in_db(self):
        clear_tables()
        self.create_test_data()
        index_count = 0
        test_list = ['test_art_2', 'test_art_3']
        artist_name = query.artist_query('test').get()
        result = query.search_by_available(artist_name)
        for art in result:
            self.assertEqual(test_list[index_count], art.artwork_name)
            index_count += 1

    def test_search_for_all_by_artist_in_db(self):
        clear_tables()
        self.create_test_data()
        index_count = 0
        test_list = ['test_art_1', 'test_art_2', 'test_art_3']
        artist_name = query.artist_query('test').get()
        result = query.search_all_by_artist(artist_name)
        for art in result:
            self.assertEqual(test_list[index_count], art.artwork_name)
            index_count += 1

    def test_search_artwork_by_art_name_in_db(self):
        clear_tables()
        self.create_test_data()
        result = query.search_artwork_by_name('test_art_1').get()
        self.assertEqual(result.artwork_name, 'test_art_1')

    def test_search_artwork_by_art_name_not_in_db(self):
        clear_tables()
        self.create_test_data()
        results_returned = len(query.search_artwork_by_name('not_in_db'))
        self.assertEqual(results_returned, 0)

    def test_status_available(self):
        clear_tables()
        self.create_test_data()
        results = query.get_status('test_art_1')
        self.assertEqual(results, False)
        results = query.get_status('test_art_2')
        self.assertEqual(results, True)








