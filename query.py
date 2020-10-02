from artist_db import Artists, Artworks
from peewee import *


def artist_query(name):
    try:
        return Artists.select().where(Artists.artist == name)
    except IntegrityError:
        print('Entry error ')


def search_all_by_artist(name):
    try:
        return Artworks.select().where(Artworks.artist == name).order_by(Artworks.artwork_name)
    except IntegrityError:
        print("Entry error ")


def search_by_available(name):
    try:
        return Artworks.select().where((Artworks.artist == name) & (Artworks.available == 'Available'))
    except IntegrityError:
        print("Entry error ")


def search_artwork_by_name(name):
    return Artworks.select().where(Artworks.artwork_name == name)


def get_status(name):
    try:
        art = Artworks.get_or_none((Artworks.artwork_name == name) & (Artworks.available == 'Available'))
        if art is not None:
            return True
        else:
            return False
    except IntegrityError:
        print("Entry error ")

