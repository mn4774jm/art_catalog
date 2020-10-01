from artist_db import Artists, Artworks


def get_menu_choice():
    choice = input('\nPlease choose an option (1-4) or press "Q" to quit: ')
    while choice.isnumeric() is False and choice.upper() != 'Q':
        choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    if choice.isnumeric():
        choice = int(choice)
    return choice


def get_name():
    name = input('Enter artist name: ').strip()
    while not name.isalpha() or name.isspace():
        name = input('Enter artist name: ')
    return name


def get_email():
    return input('Enter new artist email: ').strip()


def get_art_name():
    return input('Enter art title: ').strip()


def get_value():
    return input('Enter price: ').strip()


def remove_art_check(art_name):
    return input(f'Remove {art_name}? Enter Y to delete: ').lower().strip()



