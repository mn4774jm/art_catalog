from peewee import *
from config import db_path
import os

db_path = os.path.join('database', db_path)
db = SqliteDatabase(db_path)


class EntryError(Exception):
    pass


class Artists(Model):
    artist_id = AutoField()
    artist = CharField(unique=True)
    email = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'Name: {self.artist} | email: {self.email}'


class Artworks(Model):
    artwork_id = AutoField()
    artist = ForeignKeyField(Artists, backref= 'works')
    artwork_name = CharField(unique=True)
    price = DecimalField()
    available = CharField(default='Available')

    class Meta:
        database = db

    def __str__(self):
        return f'Artist: {self.artist} | Name: {self.artwork_name} | Price: '+'{0:.2f}'.format(self.price)+f' | Available: {self.available}'


db.connect()
db.create_tables([Artists, Artworks])


def create_new_artist(name, email):
    try:
        new_artist = Artists(artist=name, email=email)
        new_artist.save()
        print(f'{new_artist} has been added to the database\n')
    except IntegrityError as e:
        # raise EntryError(f'Artist is already in the database\n') from e
        print("artist already in database")


def create_art_entry(artist_name, art_name, value):
    try:
        new_art = Artworks(artist=artist_name, artwork_name=art_name, price=value)
        new_art.save()
        print(f'{new_art}\n')
    except IntegrityError as e:
        print(f'Unable to process entry request {e}')


def delete_artwork_by_name(artwork):
    Artworks.delete().where(Artworks.artwork_name == artwork).execute()
    print(f'{artwork} has been deleted')








