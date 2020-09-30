from artist_db import Artists, Artworks


def get_menu_choice():
    choice = input('\nPlease choose an option (1-4) or press "Q" to quit: ')
    while choice.isnumeric() is False and choice.upper() != 'Q':
        choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    if choice.isnumeric():
        return int(choice)


<<<<<<< HEAD
def add_artwork():

    artist_name = input('Artist name: ')
    new_artist_check(artist_name)
    name_query = artist_query(artist_name)
    artwork = input("Enter the name of artwork: ")
    new_price = numeric_validation(message='Enter price: ')
    return Artworks(artist=name_query, artwork_name=artwork, price=new_price)


def new_artist_check(name):
    name_query = artist_query(name)
    if name_query.count() == 0:
        email = input('new_email:')
        noa = Artists(artist=name, email=email)
        noa.save()


def numeric_validation(message):
    numeric_pattern = re.compile(r'^[+|-]?\d+[.]?(\d+)?$')
    price_input = input(message).strip().replace(',', '')
    match_object = numeric_pattern.search(price_input)
    while match_object is None:
        price_input = input('Please enter only numeric values: ').strip().replace(',', '')
        match_object = numeric_pattern.search(price_input)
    return float(price_input)
=======
def get_name():
    return input('Enter artist name: ')


def get_email():
    return input('Enter new artist email: ')


def get_art_name():
    return input('Enter art title: ')


def get_value():
    return input('Enter price: ')


# def add_artwork():
#     artist_name = input('Artist name: ')
#     new_artist_check(artist_name)
#     name_query = artist_query(artist_name)
#     artwork = input("Enter the name of artwork: ")
#
#     while True:
#         try:
#             new_price = float(input('Enter price: '))
#             break
#         except ValueError:
#             print('Please enter only numbers')
#     return Artworks(artist=name_query, artwork_name=artwork, price=new_price)
#
#
# def new_artist_check(name):
#     name_query = artist_query(name)
#     if name_query.count() == 0:
#         email = input('new_email:')
#         noa = Artists(artist=name, email=email)
#         noa.save()

>>>>>>> test
