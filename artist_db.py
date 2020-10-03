from peewee import *

from config import db_path
import os

db_path = os.path.join('database', db_path)
db = SqliteDatabase(db_path)


class EntryError(Exception):
    pass


class Artists(Model):
    artist_id = AutoField()
    artist = CharField(null=False, unique=True, max_length=50)
    email = CharField(null=False, max_length=50)

    class Meta:
        database = db

    def __str__(self):
        return f'Name: {self.artist} | email: {self.email}'

    # def delete_all_artists(self):
    #     Artists.delete().execute()


class Artworks(Model):
    artwork_id = AutoField()
    artist = ForeignKeyField(Artists, backref= 'works')
    artwork_name = CharField(null=False, unique=True)
    price = DecimalField(null=False)
    available = CharField(default='Available', null=False)

    class Meta:
        database = db

    def __str__(self):
        return f'Artist: {self.artist} | Name: {self.artwork_name} | Price: '+'{0:.2f}'.format(self.price)+f' | Status: {self.available}'

    # def delete_all_artworks(self):
    #     Artworks.delete().execute()


db.connect()
db.create_tables([Artists, Artworks])


def create_new_artist(name, email):
    try:
        new_artist = Artists(artist=name, email=email)
        new_artist.save()
        print(new_artist)
    except IntegrityError as e:
        raise EntryError(f'Artist is already in the database\n') from e


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


def change_artwork_status(name, status):
    if status:
        Artworks.update(available='Sold').where(Artworks.artwork_name == name).execute()
        print(f'The status of {name} has been changed to sold\n')
    else:
        Artworks.update(available='Available').where(Artworks.artwork_name == name).execute()
        print(f'The status of {name} has been changed to Available\n')











