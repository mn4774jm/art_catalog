
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
        # new_artist.save()
        # print(f'{new_artist} has been added to the database\n')


def search_by_artist_all():
    pass


def search_by_artist_available():
    pass


def add_art():
    artist_name = ui.get_name()
    art_name = ui.get_art_name()
    value = utility.validate_price(ui.get_value())
    create_art_entry(artist_query(artist_name), art_name, value)


def delete_art():
    pass


def change_available_status():
    pass



if __name__ =='__main__':
    main()