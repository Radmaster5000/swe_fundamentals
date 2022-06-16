from Exceptions import *
# Load data

# Launch UI
def main_menu():
    selection = 0
    while selection != 5:
        selection = input("""
        
        Please select an option:
        1 = Create a project
        2 = Remove a project
        3 = Update a project
        4 = Display a project
        5 = Quit
        
        """)

        try:
            selection = int(selection)
        except ValueError:
            pass

        if selection == 1:
            print("create_record()")
        elif selection == 2:
            print("remove_record()")
        elif selection == 3:
            print("update_record()")
        elif selection == 4:
            print("display_record()")
        elif selection == 5:
            selection = quit_app()
        else:
            print("Invalid selection")


def quit_app():
    confirm = input("Are you sure you want to quit?").lower()
    if confirm == 'y':
        print("Save file?")
        quit()
    else:
        return 0


if __name__ == '__main__':
    main_menu()


