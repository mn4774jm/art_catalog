from unittest import TestCase
import config
config.db_path = 'database/test_art.db'
import query
import artist_db
import os
import artist_db
from models import Artworks, Artists

class TestQuery(TestCase):



    @classmethod
    def setUp(self):
        config.db_path = 'database/test_art.db'
        artist_db.Artists.instance = None
        artist_db.Artworks.instance = None

    # def setUp(self):
    #     self.Artists = artist_db.Artists()
    #     self.Artworks = artist_db.Artworks()

    def create_test_data(self):
        # self.Artists.delete().execute()
        # self.Artworks.delete().execute()
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

    def test_artist_query_not_in_database(self):
        result = query.artist_query('test_name_not_in_db')
        self.assertEqual(result, '')

    # TODO***********

    def test_artist_query_in_database(self):
        result = query.artist_query('test').get()
        self.assertEqual(result.artist, 'test')

    # TODO***********

    def test_search_for_all_by_artist_in_db(self):
        index_count = 0
        test_list = ['test_art_1', 'test_art_2', 'test_art_3']
        artist_name = query.artist_query('test').get()
        result = query.search_all_by_artist(artist_name)
        for art in result:
            self.assertEqual(test_list[index_count], art.artwork_name)
            index_count += 1

    # TODO***********

    def test_search_for_all_by_artist_no_art_in_db(self):
        artist_name = query.artist_query('testNoArt').get()
        result = query.search_all_by_artist(artist_name)
        art_count = result.count()
        self.assertEqual(art_count, 0)

    # TODO***********

    def test_search_available_by_artist_in_db(self):
        index_count = 0
        test_list = ['test_art_2', 'test_art_3']
        artist_name = query.artist_query('test').get()
        result = query.search_by_available(artist_name)
        for art in result:
            print(art)
            self.assertEqual(test_list[index_count], art.artwork_name)
            index_count += 1

    def test_search_artwork_by_art_name_in_db(self):
        result = query.search_artwork_by_name('test_art_1').get()
        self.assertEqual(result.artwork_name, 'test_art_1')

    def test_search_artwork_by_art_name_not_in_db(self):
        results_returned = len(query.search_artwork_by_name('not_in_db'))
        self.assertEqual(results_returned, 0)

    def test_status_available(self):
        results = query.get_status('test_art_1')
        self.assertEqual(results, False)
        results = query.get_status('test_art_2')
        self.assertEqual(results, True)







