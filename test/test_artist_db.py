from unittest import TestCase
import artist_db
from artist_db import EntryError
from peewee import *
from database_config import test_db_path

from models import Artists, Artworks
# DB created for testing purposes
db = SqliteDatabase(test_db_path)

# models from artist_db collected for use with setting up my test db
MODELS = [Artists, Artworks]


class TestArtistDb(TestCase):

    def setUp(self):
        # bind model classes to the new db
        # since list is complete binding dependencies isn't required
        # http://docs.peewee-orm.com/en/latest/peewee/database.html  #connection-management
        db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        db.connect()
        db.create_tables(MODELS)

    def tearDown(self):
        # tables dropped when finished. Useful when working with large data sets in testing
        db.drop_tables(MODELS)
        db.close()

    # populate test database
    def create_test_data(self):
        self.clear_tables()
        Artists(artist='test', email='test@test.com').save()
        Artworks(artist=artist_db.artist_query('test'), artwork_name='test_art_1', price=123, available=False).save()
        Artworks(artist=artist_db.artist_query('test'), artwork_name='test_art_2', price=123).save()
        Artworks(artist=artist_db.artist_query('test'), artwork_name='test_art_3', price=123).save()
        Artists(artist='testNoArt', email='test@test.com').save()

    def clear_tables(self):
        artist_db.delete_all_tables()

    # test artist creation
    def test_add_artist(self):
        self.clear_tables()
        self.create_test_data()
        artist = Artists(artist='dave', email='12345@gmail.com')
        artist.save()
        artist = Artists.select().where(Artists.artist == 'dave').get()
        self.assertEqual(artist.artist, "dave")

    # test to make sure artist entry with empty string not accepted
    def test_add_artist_no_name(self):
        self.clear_tables()
        self.create_test_data()
        with self.assertRaises(EntryError):
            artist_db.create_new_artist('', 'test@test.com').save()

    # test, raises error when no email is provided to the db
    def test_add_artist_no_email(self):
        self.clear_tables()
        with self.assertRaises(EntryError):
            artist_db.create_new_artist('test', '').save()

    # raise error if entry already exists in db
    def test_add_duplicate(self):
        self.clear_tables()
        self.create_test_data()
        artist_db.create_new_artist('dave', '12345@gmail.com')
        with self.assertRaises(EntryError):
            artist_db.create_new_artist('dave', '12345@gmail.com')

    # test artwork insert
    def test_create_art_artist_exists(self):
        self.clear_tables()
        self.create_test_data()
        artist_db.create_art_entry(artist_db.artist_query('test'), 'new_art', 500)
        result = Artworks.select().where(Artworks.artwork_name == 'new_art').get()
        self.assertEqual(result.artwork_name, 'new_art')

    # raise error if artist already in DB. Unique constraint
    def test_art_name_already_exists(self):
        self.clear_tables()
        self.create_test_data()
        with self.assertRaises(EntryError):
            artist_db.create_art_entry(artist_db.artist_query('test'), 'test_art_2', 123)

    # raise error if no artist is in Object when entering to DB
    def test_create_art_no_artist(self):
        self.clear_tables()
        with self.assertRaises(EntryError):
            artist_db.create_art_entry(None, 'new_art', 500)

    # raise error if negative value is passed to db
    def test_create_art_non_positive_float_price(self):
        self.clear_tables()
        with self.assertRaises(EntryError):
            artist_db.create_art_entry(artist_db.artist_query('test'), 'new_art', -500)

    # test queries for expected return data
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
        test_list = ['test_art_2', 'test_art_3']
        artist_name = artist_db.artist_query('test').get()
        result = artist_db.search_by_available(artist_name)

        for expected_art, actual_art in zip(test_list, result):
            self.assertEqual(expected_art, actual_art.artwork_name)
            

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
        self.assertEqual(results, True)
        results = artist_db.get_status('test_art_2')
        self.assertEqual(results, False)










