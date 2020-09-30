
def validate_price(value):
    while True:
        try:
            new_price = float(value)
            break
        except ValueError:
            value = input('Please enter only numbers: ')
    return new_price
