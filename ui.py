from artist_db import Artists, Artworks

def get_menu_choice():
    choice = input('\nPlease choose an option (1-4) or press "Q" to quit: ')
    while choice.isnumeric() is False and choice.upper() != 'Q':
        choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    if choice.isnumeric():
        choice = int(choice)
    return choice


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

    return record
