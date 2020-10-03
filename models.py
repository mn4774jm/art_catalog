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

    def delete_all_artists(self):
        Artists.delete().execute()


class Artworks(Model):
    artwork_id = AutoField()
    artist = ForeignKeyField(Artists, backref= 'works', null=False)
    artwork_name = CharField(null=False, unique=True)
    price = DecimalField(null=False, )
    available = CharField(default='Available', null=False)

    class Meta:
        database = db

    def __str__(self):
        return f'Artist: {self.artist} | Name: {self.artwork_name} | Price: '+'{0:.2f}'.format(self.price)+f' | Status: {self.available}'



db.connect()
db.create_tables([Artists, Artworks])