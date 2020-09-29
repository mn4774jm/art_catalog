
import ui

def main():
    print('Gallery database')

    while True:
        print_menu()
        choice = ui.get_menu_choice()
        if choice == 1:
            add_art()

        elif choice.upper() == 'Q':
            break


def print_menu():
    print('1: New Record')


def add_art():
    try:
        artist_record = ui.add_artwork()
        artist_record.save()
        print(artist_record)
    except Exception as e:
        print(f'\n{e}\n')



if __name__ =='__main__':
    main()