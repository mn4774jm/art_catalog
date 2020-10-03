

from models import Artists, Artworks, EntryError
from peewee import *

def delete_all_tables():
    Artworks.delete().execute()
    Artists.delete().execute()

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











