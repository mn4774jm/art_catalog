

from models import Artists, Artworks, EntryError
from peewee import *


def delete_all_tables():
    Artworks.delete().execute()
    Artists.delete().execute()

# validates name length to avoid empty strings being entered to the database; raises error
def create_new_artist(name, email):
    if len(name) < 1 or len(email) <1:
        raise EntryError('No artist name entered')
    else:
        # Artists object created and submitted with exception handling
        new_artist = Artists(artist=name, email=email)
        try:
            new_artist.save()
            print(f'{new_artist}\n')
        except IntegrityError as e:
            raise EntryError(f'Entry error\n') from e


def create_art_entry(artist_name, art_name, value):
    new_art = Artworks(artist=artist_name, artwork_name=art_name, price=value)
    try:
        new_art.save()
        print(f'{new_art}\n')
    except IntegrityError as e:
        print('Entry error\n')


# peewee sqlite operation to delete by name of artwork in DB
def delete_artwork_by_name(artwork):
    Artworks.delete().where(Artworks.artwork_name == artwork).execute()
    print(f'{artwork} has been deleted')


# sqlite operation to change the boolean status of a single row based on name of artwork
def change_artwork_status(name, status):
    Artworks.update(available=status).where(Artworks.artwork_name == name).execute()


# exception handling used to avoid error if artist is not listed in the DB
def artist_query(name):
    try:
        return Artists.select().where(Artists.artist == name)
    except IntegrityError:
        print('error entry')


# sqlite query to find all rows with matching artist name. Sorted alphabetically by the name of the artwork
def search_all_by_artist(name):
    return Artworks.select().where(Artworks.artist == name).order_by(Artworks.artwork_name)


# same as previous but with the additional search requirment that
def search_by_available(name):
    return Artworks.select().where((Artworks.artist == name) & (Artworks.available == 'Available'))

# search for artworks using art name as the where condition
def search_artwork_by_name(name):
    return Artworks.select().where(Artworks.artwork_name == name)

# used to get existing status to change status in db
def get_status(name):
    art = Artworks.get_or_none((Artworks.artwork_name == name) & (Artworks.available == 'Available'))
    if art is not None:
        return False
    else:
        return True









