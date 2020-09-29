from artist_db import Artists, Artworks, artist_query


def get_menu_choice():
    choice = input('\nPlease choose an option (1-4) or press "Q" to quit: ')
    while choice.isnumeric() is False and choice.upper() != 'Q':
        choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    if choice.isnumeric():
        choice = int(choice)
    return choice


def add_artwork():
    artist_name = input('Artist name: ')
    new_artist_check(artist_name)
    name_query = artist_query(artist_name)
    artwork = input("Enter the name of artwork: ")
    new_price = float(input('Enter price: '))
    record = Artworks(artist=name_query, artwork_name=artwork, price=new_price)
    return record


def new_artist_check(name):
    name_query = artist_query(name)
    if name_query.count() == 0:
        email = input('new_email:')
        noa = Artists(artist=name, email=email)
        noa.save()

