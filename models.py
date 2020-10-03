from peewee import *

from database_config import db_path

db = SqliteDatabase(db_path)


class EntryError(Exception):
    pass

class BaseModel(Model):
    class Meta:
        database = db

#TODO Create additional constraints
class Artists(BaseModel):
    artist_id = AutoField()
    artist = CharField(null=False, unique=True, max_length=50)
    email = CharField(null=False, max_length=50)

    def __str__(self):
        return f'Name: {self.artist} | email: {self.email}'


class Artworks(BaseModel):
    artwork_id = AutoField()
    artist = ForeignKeyField(Artists, backref= 'works', null=False)
    artwork_name = CharField(null=False, unique=True)
    price = DecimalField(null=False, constraints=[Check('price > 0.0')])
    available = CharField(default='Available', null=False)

    def __str__(self):
        return f'Artist: {self.artist} | Name: {self.artwork_name} | Price: '+'{0:.2f}'.format(self.price)+f' | Status: {self.available}'


db.connect()
db.create_tables([Artists, Artworks])
