from PassMngrCore import DisplayMenu, UsefulOperations
from PassMngrCore.Ciphers import cezar as cipher
from PassMngrCore.DisplayMenu import menu_size
from PassMngrCore.Error_pmc import *


# [1] DODAJ PROFIL - GIT
# [2] WYŚWIETL PROFIL
# [3] EDYTUJ PROFIL
# [4] USUŃ PROFIL
# [5] O PROGRAMIE
def option_add_profil() -> None:
    """
    Add profile to database
    :return:
    """
    print(DisplayMenu.add_profile_menu())
    try:
        name = input("    Podaj nazwę aplikacji/strony:")
        login = cipher.encryption(input("    Podaj login:"))
        password = cipher.encryption(input("    Podaj hasło:"))

        if name == '' or login == '' or password == '':
            raise AddProfileEmptyError

    except AddProfileEmptyError:
        print("Anulowano dodawanie!")
        input("Aby kontynuować wciśnij enter")

    else: # wyślij do bazy danych
        DisplayMenu.clear_console()
        print(name, login, password)
        print('name', name)
        print('login', cipher.decryption(login))
        print('password', cipher.decryption(password))
        input("Aby kontynuować wciśnij enter")


def option_show_profiles():
    """
    Show profiles from database
    :return:
    """
    stop = False
    while not stop:
        # Emergency stop
        if stop:
            break

        DisplayMenu.clear_console()
        print(DisplayMenu.show_profiles_menu())
        select_option = UsefulOperations.user_input(menu_size['show_profiles'])

        match select_option:
            case 1:
                DisplayMenu.clear_console()
                print(DisplayMenu.show_by_name_menu())

                try:
                    name = input("    Podaj nazwę aplikacji: ")

                    if name == "":
                        raise AddProfileEmptyError

                except AddProfileEmptyError:
                    print("Anulowano wyświetlanie!")
                    input("Aby kontynuować wciśnij enter")

                else:
                    DisplayMenu.clear_console()
                    print(name)
                    input("Aby kontynuować wciśnij enter")

            case 2:
                DisplayMenu.clear_console()
                print("Wyświetlono wszystko")
                input("Aby kontynuować wciśnij enter")

            case 0:
                stop = True
                print("Powrót")
