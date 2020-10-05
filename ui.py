from artist_db import Artists, Artworks
import re

# ui.py is used to collect and validate user entry data before being sent to other functions.

def get_menu_choice():
    choice = input('\nPlease choose an option (1-4) or press "Q" to quit: ')
    while choice.isnumeric() is False and choice.upper() != 'Q':
        choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    if choice.isnumeric():
        choice = int(choice)
    return choice


def get_name():
    name = input('Enter artist name: ').strip().capitalize()
    while not name.isalpha() or len(name) > 50 or len(name) < 1:
        name = input('Enter artist name (Char limit 50): ')
    return name


# admittedly it could have been better to create a custom constraint in db to handle validation, but the regular
# expression used below still ensures that the correct format must be used. Length is also enforced both here and in the
# Model constraints
def get_email():
    email_pattern = re.compile(r'\w+@\w+\.\w{2,}')
    email = input('Enter new artist email: ').strip()
    mo = email_pattern.search(email)
    while len(email) > 50 or len(email) < 1 or mo is None:
        email = input("Enter valid email address (Char limit 50): ")
        mo = email_pattern.search(email)
    return email


# Does not allow for empty strings and capitalizes entries for uniformity
def get_art_name():
    art_name = input('Enter art title: ').strip().capitalize()
    while len(art_name) < 1:
        art_name = input('Please enter art title: ')
    return art_name


# Does not allow for use of 0 or negative numbers in validation. Converts to float for use with DecimaField in DB
def get_value():
    value = input('Enter Price: ').strip()
    while True or value < 0:
        try:
            value = float(value)
            break
        except ValueError:
            value = input('Please enter only non-negative numbers: ')
    return value


def remove_art_check(art_name):
    return input(f'Remove {art_name}? Enter Y to delete: ').lower().strip()



