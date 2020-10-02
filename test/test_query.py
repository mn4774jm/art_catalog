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
        result = query.search_artwork_by_name(artist_name)
        for art in result:
            self.assertEqual(test_list[index_count], f'{art.artwork_name}')
            index_count += 1

    def test_search_for_all_by_artist_not_in_db(self):
        pass

    def test_search_for_all_entry_not_alpha(self):
        pass

    def test_search_available_by_artist_in_db(self):
        pass

    def test_search_available_by_artist_not_in_db(self):
        pass

    def test_search_available_entry_not_alpha(self):
        pass

    def test_search_artwork_by_art_name_in_db(self):
        pass

    def test_search_artwork_by_art_name_not_in_db(self):
        pass
