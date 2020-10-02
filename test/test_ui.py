from unittest import TestCase, mock
import ui


class TestUI(TestCase):

    #mock is used to provide mock user inputs to test values
    @mock.patch('builtins.input', side_effect=['bbb'])
    def test_get_name(self, mock_input):
        result = ui.get_name()
        self.assertEqual(result, 'bbb')

    @mock.patch('builtins.input', side_effect=['', 'bbb'])
    def test_get_name_no_entry(self, mock_input):
        result = ui.get_name()
        self.assertEqual(result, 'bbb')

    @mock.patch('builtins.input', side_effect=['qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm', 'bbb'])
    def test_get_name_too_many_characters(self, mock_input):
        result = ui.get_name()
        self.assertEqual(result, 'bbb')

    @mock.patch('builtins.input', side_effect=['////', 'bbb'])
    def test_get_name_not_alpha_numeric(self, mock_input):
        result = ui.get_name()
        self.assertEqual(result, 'bbb')

    @mock.patch('builtins.input', side_effect=['test@gmail.com'])
    def test_get_email(self, mock_input):
        result = ui.get_email()
        self.assertEqual(result, 'test@gmail.com')

    @mock.patch('builtins.input', side_effect=['', 'bbb@gmail.com'])
    def test_get_email_no_entry(self, mock_input):
        result = ui.get_email()
        self.assertEqual(result, 'bbb@gmail.com')
        pass

    @mock.patch('builtins.input', side_effect=['////', 'bbb'])
    def test_get_email_too_many_characters(self, mock_input):
        pass

    @mock.patch('builtins.input', side_effect=['////', 'bbb'])
    def test_get_email_not_correct_format(self, mock_input):
        pass

    @mock.patch('builtins.input', side_effect=['////', 'bbb'])
    def test_get_value(self, mock_input):
        pass

    @mock.patch('builtins.input', side_effect=['////', 'bbb'])
    def test_get_value_not_numeric(self, mock_input):
        pass

    @mock.patch('builtins.input', side_effect=['////', 'bbb'])
    def test_remove_art_check_in_database(self, mock_input):
        pass

    @mock.patch('builtins.input', side_effect=['////', 'bbb'])
    def test_remove_art_not_in_database(self, mock_input):
        pass