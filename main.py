from peewee import *
from artist_db import Artists, Artworks
db = SqliteDatabase('gallery.sqlite')

def main():
    print('Gallery database')

    while True:
        print_menu()
        choice = get_menu_choice()
        if choice == 1:
            new_artist()

        elif choice.upper() == 'Q':
            break


def print_menu():
    print('1: New Record')

# TODO split menu into new file
def get_menu_choice():
    choice = input('\nPlease choose an option (1-4) or press "Q" to quit: ')
    while choice.isnumeric() is False and choice.upper() != 'Q':
        choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    if choice.isnumeric():
        choice = int(choice)
    return choice

# TODO user input into new file
def new_artist():
    new_name = input('Artist name: ')
    name_query = Artists.select().where(Artists.artist == new_name)
    if name_query.count() == 0:
        email = input('new_email:')
        noa = Artists(artist=new_name, email=email)
        noa.save()
    artwork = input("Enter the name of artwork: ")
    new_price = float(input('Enter price: '))
    record = Artworks(artist=noa, artwork_name=artwork, price=new_price)
    record.save()
    print(record)

if __name__ =='__main__':
    main()