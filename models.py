from peewee import *
from unittest import TestCase
from database_config import db_path

db = SqliteDatabase(db_path)


class EntryError(Exception):
    pass

# basemodel is used to assign the db in meta to be inherited by other models in case more models are added in the future
class BaseModel(Model):
    class Meta:
        database = db


# controls requirments for Artists table. Constraints used to avoid duplicate artist entries by name and does not allow of null entries
class Artists(BaseModel):
    artist_id = AutoField()
    artist = CharField(null=False, unique=True, max_length=50)
    email = CharField(null=False, max_length=50)

# Used to ensure information is easy to read when returned to the user
    def __str__(self):
        return f'Name: {self.artist} | email: {self.email}'

# sets model requirements for Artworks table and object requirements
class Artworks(BaseModel):
    artwork_id = AutoField()
    # Artists table used as foreign key to connect tables
    artist = ForeignKeyField(Artists, backref= 'works', null=False)
    artwork_name = CharField(null=False, unique=True)
    price = DecimalField(null=False, constraints=[Check('price > 0.0')])
    available = BooleanField(default=True, null=False)

    def __str__(self):
        status = 'Available' if self.available else 'Sold'
        return f'Artist: {self.artist} | Name: {self.artwork_name} | Price: '+'{0:.2f}'.format(self.price)+f' | Status: {status}'

# connects and populates tables in database
db.connect()
db.create_tables([Artists, Artworks])
