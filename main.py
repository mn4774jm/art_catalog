from peewee import *
db = SqliteDatabase('gallery.sqlite')

#TODO split tables and classes into seperate file
class Artists(Model):
    artist = CharField()
    email = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'Name: {self.artist} | email: {self.email}'

class Artworks(Model):
    artist = ForeignKeyField(Artists, backref= 'works')
    artwork_name = CharField()
    price = DecimalField()
    available = CharField(default='Available')

    class Meta:
        database = db

    def __str__(self):
        return f'Artist: {self.artist} | Name: {self.artwork_name} | Price: {self.price} | Available: {self.available}'

db.connect()
db.create_tables([Artists, Artworks])


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
    print(noa)

if __name__ =='__main__':
    main()