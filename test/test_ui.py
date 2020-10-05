from unittest import TestCase, mock
import ui


class TestUI(TestCase):

    #mock is used to provide mock user inputs to test values
    @mock.patch('builtins.input', side_effect=['bbb'])
    def test_get_name(self, mock_input):
        result = ui.get_name()
        self.assertEqual(result, 'bbb')

    # when used in fuctions with multiple entries or while loops, additional paramaters are entered when using side_effect
    @mock.patch('builtins.input', side_effect=['', 'bbb'])
    def test_get_name_no_entry(self, mock_input):
        result = ui.get_name()
        self.assertEqual(result, 'bbb')

    # test to ensure that user entry stays under 50 characters
    @mock.patch('builtins.input', side_effect=['qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm', 'bbb'])
    def test_get_name_too_many_characters(self, mock_input):
        result = ui.get_name()
        self.assertEqual(result, 'bbb')

    # test to check that only alpha characters are submitted
    @mock.patch('builtins.input', side_effect=['////', 'bbb'])
    def test_get_name_not_alpha_numeric(self, mock_input):
        result = ui.get_name()
        self.assertEqual(result, 'bbb')

    # check that email addresses are being accepted
    @mock.patch('builtins.input', side_effect=['test@gmail.com'])
    def test_get_email(self, mock_input):
        result = ui.get_email()
        self.assertEqual(result, 'test@gmail.com')

    # empty string email test
    @mock.patch('builtins.input', side_effect=['', 'bbb@gmail.com'])
    def test_get_email_no_entry(self, mock_input):
        result = ui.get_email()
        self.assertEqual(result, 'bbb@gmail.com')
        pass

    # length test to ensure that email addresses stay under 50 characters
    @mock.patch('builtins.input', side_effect=['qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm@gmail.com', 'bbb@gmail.com'])
    def test_get_email_too_many_characters(self, mock_input):
        result = ui.get_email()
        self.assertEqual(result, 'bbb@gmail.com')

    # test to check email for correct format
    @mock.patch('builtins.input', side_effect=['@gmail.bbb', 'bbb@gmail.com'])
    def test_get_email_not_correct_format(self, mock_input):
        result = ui.get_email()
        self.assertEqual(result, 'bbb@gmail.com')

    # test to make sure price is being accepted
    @mock.patch('builtins.input', side_effect=['400'])
    def test_get_value(self, mock_input):
        result = ui.get_value()
        self.assertEqual(result, 400)

    # test price entry to not allow string datatypes
    @mock.patch('builtins.input', side_effect=['sdfg', '400'])
    def test_get_value_not_numeric(self, mock_input):
        result = ui.get_value()
        self.assertEqual(result, 400)

    # check for negative numbers
    @mock.patch('builtins.input', side_effect=['-400', '400'])
    def test_get_value_negative(self, mock_input):
        result = ui.get_value()
        self.assertEqual(result, 400)

    @mock.patch('builtins.input', side_effect=['Y'])
    def test_remove_art_option(self, mock_input):
        result = ui.remove_art_check('art_name')
        self.assertEqual(result, 'y')
