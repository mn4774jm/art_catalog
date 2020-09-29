
import ui

def main():
    print('Gallery database')

    while True:
        print_menu()
        choice = ui.get_menu_choice()
        if choice == 1:
            add_artist()

        elif choice.upper() == 'Q':
            break


def print_menu():
    print('1: New Record')


def add_artist():
    # try:
        artist_record = ui.new_artist()
        artist_record.save()
        print(artist_record)
    # except Exception as e:
    #     print(f'\n{e}\n')



if __name__ =='__main__':
    main()