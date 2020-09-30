from artist_db import Artists, Artworks


def artist_query(name):
    return Artists.select().where(Artists.artist == name)


def search_all_by_artist(name):
    return Artworks.select().where(Artworks.artist == name)
    pass

def search_by_available(name):
    return Artworks.select().where((Artworks.artist == name) & (Artworks.available == 'Available'))
    pass