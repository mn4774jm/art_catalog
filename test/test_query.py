from unittest import TestCase

import query

class TestQuery(TestCase):

    def test_artist_query_not_in_database(self):
        result = query.artist_query('test_name_not_in_db')
        self.assertEqual(result, '')

    def test_artist_query_in_database(self):
        result = query.artist_query('test').get()
        self.assertEqual(result.artist, 'test')

    def test_search_for_all_by_artist_in_db(self):
        index_count = 0
        test_list = ['test_art_1', 'test_art_2', 'test_art_3']
        artist_name = query.artist_query('test').get()
        result = query.search_all_by_artist(artist_name)
        for art in result:
            self.assertEqual(test_list[index_count], art.artwork_name)
            index_count += 1

    def test_search_for_all_by_artist_no_art_in_db(self):
        artist_name = query.artist_query('testNoArt').get()
        result = query.search_all_by_artist(artist_name)
        art_count = len(list(result))
        self.assertEqual(art_count, 0)

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
