from unittest import TestCase, mock
import ui


class TestUI(TestCase):

    #mock is used to provide mock user inputs to test values
    def test_get_name(self):
        with mock.patch('ui.get_name', return_value='bbb'):
            result = ui.get_name()
        expected_value = 'bbb'
        self.assertEqual(result, expected_value)

    @mock.patch('ui.get_name', create=True)
    def test_get_name_no_entry(self, mock_input):
        mock_input.side_effect= ['', 'bbb']
        result = ui.get_name()
        self.assertEqual(result, 'bbb')

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