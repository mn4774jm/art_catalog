from unittest import TestCase, mock
from unittest.mock import patch
import ui


class TestUI(TestCase):

    #mock is used to provide mock user inputs to test values
    @mock.patch('ui.get_name', return_value='bbb')
    def test_get_name(self, mock_input):
        # mocked_input.side_effect = ['bbb']
        result = ui.get_name()
        self.assertEqual(result, 'bbb')
        pass

    def test_get_name_no_entry(self):
        pass

    def test_get_name_too_many_characters(self):
        pass

    def test_get_name_not_alpha_numeric(self):
        pass

    def test_get_email(self):
        pass

    def test_get_email_no_entry(self):
        pass

    def test_get_email_too_many_characters(self):
        pass

    def test_get_email_not_correct_format(self):
        pass

    def test_get_value(self):
        pass

    def test_get_value_not_numeric(self):
        pass

    def test_remove_art_check_in_database(self):
        pass

    def test_remove_art_not_in_database(self):
        pass