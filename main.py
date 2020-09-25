from peewee import *
db = SqliteDatabase('gallery.sqlite')


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
    inputs()


def inputs():
    new_name = input('Artist name: ')
    name_query =  Artists.select().where(Artists.artist == new_name)
    if name_query.count() == 0:
        email = input('new_email:' )
        noa = Artists(artist = new_name, email = email)
        noa.save()
    artwork = input("Enter the name of artwork: ")
    new_price = float(input('Enter price: '))
    record = Artworks(artist=noa, artwork_name=artwork, price=new_price)
    record.save()
    print(record)
    print(noa)




main()