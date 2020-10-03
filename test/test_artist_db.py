from unittest import TestCase
import artist_db
from artist_db import EntryError
from peewee import *
import database_config

from models import Artists, Artworks
database_config.db_path = 'database/test_gallery.sqlite'
db = SqliteDatabase(database_config.db_path)


MODELS = [Artists, Artworks]

db.bind(MODELS, bind_refs=False, bind_backrefs=False)
db.connect()
db.create_tables(MODELS)


class TestArtistDb(TestCase):

    def setUp(self):

        self.clear_tables()

    def create_test_data(self):
        self.clear_tables()
        self.artist = Artists(artist='test', email='test@test.com')
        self.artist.save()

        self.art = Artworks(artist=artist_db.artist_query('test'), artwork_name='test_art_1', price=123, available='Sold')
        self.art.save()
        self.art = Artworks(artist=artist_db.artist_query('test'), artwork_name='test_art_2', price=123)
        self.art.save()
        self.art = Artworks(artist=artist_db.artist_query('test'), artwork_name='test_art_3', price=123)
        self.art.save()
        self.artist = Artists(artist='testNoArt', email='test@test.com')
        self.artist.save()

    def clear_tables(self):
        artist_db.delete_all_tables()

    def test_add_artist(self):
        self.clear_tables()
        self.create_test_data()
        artist = Artists(artist='dave', email='12345@gmail.com')
        artist.save()
        artist = Artists.select().where(Artists.artist == 'dave').get()
        self.assertEqual(artist.artist, "dave")

    def test_add_artist_no_name(self):
        pass

    def test_add_artist_no_email(self):
        pass

    def test_add_duplicate(self):
        self.clear_tables()
        self.create_test_data()
        artist_db.create_new_artist('dave', '12345@gmail.com')
        with self.assertRaises(EntryError):
            artist_db.create_new_artist('dave', '12345@gmail.com')

    def test_create_art_artist_exists(self):
        #TODO
        pass

    def test_art_name_already_exists(self):
        pass

    def test_create_art_no_artist(self):
        #TODO
        pass

    def test_create_art_non_positive_float_price(self):
        pass


    def test_artist_query_not_in_database(self):
        self.clear_tables()
        self.create_test_data()
        result = artist_db.artist_query('test_name_not_in_db')
        self.assertEqual(result, '')

    def test_artist_query_in_database(self):
        self.clear_tables()
        self.create_test_data()
        result = artist_db.artist_query('test').get()
        self.assertEqual(result.artist, 'test')

    def test_search_for_all_by_artist_no_art_in_db(self):
        self.clear_tables()
        self.create_test_data()
        artist_name = artist_db.artist_query('testNoArt').get()
        result = artist_db.search_all_by_artist(artist_name)
        art_count = result.count()
        self.assertEqual(art_count, 0)

    def test_search_available_by_artist_in_db(self):
        self.clear_tables()
        self.create_test_data()
        index_count = 0
        test_list = ['test_art_2', 'test_art_3']
        artist_name = artist_db.artist_query('test').get()
        result = artist_db.search_by_available(artist_name)
        for art in result:
            self.assertEqual(test_list[index_count], art.artwork_name)
            index_count += 1

    def test_search_for_all_by_artist_in_db(self):
        self.clear_tables()
        self.create_test_data()
        index_count = 0
        test_list = ['test_art_1', 'test_art_2', 'test_art_3']
        artist_name = artist_db.artist_query('test').get()
        result = artist_db.search_all_by_artist(artist_name)
        for art in result:
            self.assertEqual(test_list[index_count], art.artwork_name)
            index_count += 1

    def test_search_artwork_by_art_name_in_db(self):
        self.clear_tables()
        self.create_test_data()
        result = artist_db.search_artwork_by_name('test_art_1').get()
        self.assertEqual(result.artwork_name, 'test_art_1')

    def test_search_artwork_by_art_name_not_in_db(self):
        self.clear_tables()
        self.create_test_data()
        results_returned = len(artist_db.search_artwork_by_name('not_in_db'))
        self.assertEqual(results_returned, 0)

    def test_status_available(self):
        self.clear_tables()
        self.create_test_data()
        results = artist_db.get_status('test_art_1')
        self.assertEqual(results, False)
        results = artist_db.get_status('test_art_2')
        self.assertEqual(results, True)

db.close()








