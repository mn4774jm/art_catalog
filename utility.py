
# simple function to neatly print formatted strings from the created objects based on their Model
def artwork_output(record):
    for artworks in record:
        print(artworks)
    print(f'{record.count()} item(s) found\n')



