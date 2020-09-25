from peewee import *
db = SqliteDatabase('gallery.sqlite')


class Artists(Model):
    artist = CharField(unique=True)
    email = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'Name: {self.artist_name} | email: {self.email}'

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
    print('Chainsaw Juggling Record Holders as of July 2018')
    while True:
        print_menu()
        choice = get_menu_choice()
        if choice == 1:
            new_artist()

        elif choice.upper() == 'Q':
            break


def print_menu():
    print('1: New Record')
    print('2: Search')
    print('3: Edit a record')
    print('4: Delete a record')

def get_menu_choice():
    choice = input('\nPlease choose an option (1-4) or press "Q" to quit: ')
    while choice.isnumeric() is False and choice.upper() != 'Q':
        choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    if choice.isnumeric():
        choice = int(choice)
    return choice

if __name__ =='__main__':
    main()