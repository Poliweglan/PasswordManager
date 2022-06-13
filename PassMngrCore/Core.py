from PassMngrCore import DisplayMenu, SelectOptions
from PassMngrCore import UsefulOperations
from PassMngrCore.DisplayMenu import menu_size
# import cursor
# cursor.hide()


def start() -> None:
    """
    Start program
    :return:
    """
    stop = False
    while not stop:
        # Emergency stop
        if stop:
            break

        DisplayMenu.clear_console()
        print(DisplayMenu.main_menu())
        select_option = UsefulOperations.user_input(menu_size['main_menu'])

        match select_option:
            case 1:
                DisplayMenu.clear_console()
                SelectOptions.option_add_profil()
            case 2:
                ...
            case 3:
                ...
            case 4:
                ...
            case 5:
                ...
            case 0:
                stop = True
                print("Do widzenia!")
                input("Aby zamknąć wciśnij enter")
