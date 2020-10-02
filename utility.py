
from peewee_validates import Validator, StringField, validate_email, validate_not_empty


def artwork_output(record):
    for artworks in record:
        print(f'Name: {artworks.artwork_name} | Price: {artworks.price} | Status: {artworks.available}')
    print(f'{record.count()} item(s) found\n')



