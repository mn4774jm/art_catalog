
import ui
from artist_db import create_art_entry, create_new_artist
import utility
from query import artist_query

def main():
    print('Gallery database')

    while True:
        print_menu()
        choice = ui.get_menu_choice()
        if choice == 1:
            add_artist()
        elif choice == 2:
            add_art()

        elif choice.upper() == 'Q':
            break


def print_menu():
    print('1: New Artist')
    print('2: New Artwork')


def add_artist():
    artist_name = ui.get_name()
    if artist_query(artist_name) == 0:
        email = ui.get_email()
        new_artist = create_new_artist(artist_name, email)
        new_artist.save()
        print(f'{new_artist} has been added to the database\n')


def add_art():
    artist_name = ui.get_name()
    art_name = ui.get_art_name()
    value = utility.validate_price(ui.get_value())
    create_art_entry(artist_query(artist_name), art_name, value)



if __name__ =='__main__':
    main()