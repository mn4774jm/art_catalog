
def validate_price(value):
    while True:
        try:
            new_price = float(value)
            break
        except ValueError:
            value = input('Please enter only numbers: ')
    return new_price


def artwork_output(record):
    for artworks in record:
        print(f'Name: {artworks.artwork_name} | Price: {artworks.price} | Status: {artworks.available}')
    print(f'{record.count()} item(s) found\n')

