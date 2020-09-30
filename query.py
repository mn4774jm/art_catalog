from artist_db import Artists, Artworks


def artist_query(name):
    return Artists.select().where(Artists.artist == name)