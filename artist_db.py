

from models import Artists, Artworks, EntryError
from peewee import *

def delete_all_tables():
    Artworks.delete().execute()
    Artists.delete().execute()

def create_new_artist(name, email):
    new_artist = Artists(artist=name, email=email)
    try:
        new_artist.save()
    except IntegrityError as e:
        raise EntryError(f'Entry error\n') from e


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
    Artworks.update(available=status).where(Artworks.artwork_name == name).execute()


def artist_query(name):
    try:
        return Artists.select().where(Artists.artist == name)
    except IntegrityError:
        print('error entry')


def search_all_by_artist(name):
    return Artworks.select().where(Artworks.artist == name).order_by(Artworks.artwork_name)


def search_by_available(name):
    return Artworks.select().where((Artworks.artist == name) & (Artworks.available == 'Available'))


def search_artwork_by_name(name):
    return Artworks.select().where(Artworks.artwork_name == name)


def get_status(name):
    art = Artworks.get_or_none((Artworks.artwork_name == name) & (Artworks.available == 'Available'))
    if art is not None:
        return False
    else:
        return True









