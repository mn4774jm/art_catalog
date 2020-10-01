from artist_db import Artists, Artworks


def artist_query(name):
    return Artists.select().where(Artists.artist == name)


def search_all_by_artist(name):
    return Artworks.select().where(Artworks.artist == name).order_by(Artworks.artwork_name).order_by(Artworks.available)


def search_by_available(name):
    return Artworks.select().where((Artworks.artist == name) & (Artworks.available == 'Available'))


def search_artwork_by_name(name):
    return Artworks.select().where(Artworks.artwork_name == name)


def get_status(name):
    art = Artworks.get_or_none((Artworks.artwork_name == name) & (Artworks.available == 'Available'))
    if art is not None:
        return True
    else:
        return False

