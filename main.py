from peewee import *
import ui
from artist_db import create_art_entry, create_new_artist
import utility
from query import artist_query, search_all_by_artist, search_by_available

def main():
    print('Gallery database')

    while True:
        print_menu()
        choice = ui.get_menu_choice()
        if choice == 1:
            add_artist()
        elif choice == 2:
            search_by_artist_all()
        elif choice ==3:
            search_by_artist_available()
        elif choice ==4:
            add_art()
        elif choice ==5:
            delete_art()
        elif choice ==6:
            change_available_status()

        elif choice.upper() == 'Q':
            break


def print_menu():
    print('1: New Artist')
    print('2: Search artwork by artist')
    print('3: Search available by artist')
    print('4: Add new artwork')
    print('5: Delete artwork')
    print('6: Change art availability')


def add_artist():
    artist_name = ui.get_name()
    if artist_query(artist_name) == 0:
        email = ui.get_email()
        create_new_artist(artist_name, email)


def search_by_artist_all():
    name = ui.get_name()
    artist_object = artist_query(name)
    artwork_objects = search_all_by_artist(artist_object)
    utility.artwork_output(artwork_objects)


def search_by_artist_available():
    name = ui.get_name()
    artist_object = artist_query(name)
    artwork_objects = search_by_available(artist_object)
    utility.artwork_output(artwork_objects)


def add_art():
    try:
        artist_name = ui.get_name()
        art_name = ui.get_art_name()
        value = utility.validate_price(ui.get_value())
        create_art_entry(artist_query(artist_name), art_name, value)
    except IntegrityError as e:
        pass


def delete_art():
    pass


def change_available_status():
    pass



if __name__ =='__main__':
    main()