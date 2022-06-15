from PassMngrCore import DisplayMenu, SelectOptions, UsefulOperations
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

        UsefulOperations.clear_console()
        print(DisplayMenu.main_menu())
        select_option = UsefulOperations.user_input(menu_size['main_menu'])

        match select_option:
            case 1:  # DODAJ PROFIL
                SelectOptions.option_add_profil()

            case 2:  # WYŚWIETL PROFIL
                SelectOptions.option_show_profiles()

            case 3:  # EDYTUJ PROFIL
                SelectOptions.option_edit_profiles()

            case 4:  # USUŃ PROFIL
                SelectOptions.option_delete_profiles()

            case 5:  # O PROGRAMIE
                SelectOptions.option_about()

            case 0:  # WYJŚCIE
                stop = True
                print("Do widzenia!")
                input("Aby zamknąć wciśnij enter")
