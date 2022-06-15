from PassMngrCore import DisplayMenu, UsefulOperations, DataOrders
from PassMngrCore.Ciphers import cezar as cipher
from PassMngrCore.DisplayMenu import menu_size
from PassMngrCore.Error_pmc import *

DATABASE_URL = "DataPass.db"


def option_add_profil() -> None:
    """
    Add profile to database
    :return:
    """
    UsefulOperations.clear_console()
    print(DisplayMenu.add_profile_menu())
    try:
        name = input("    [>] Podaj nazwę aplikacji/strony: ")
        login = cipher.encryption(input("    [>] Podaj login: "))
        password = cipher.encryption(input("    [>] Podaj hasło: "))

        add_data = {"name": name, "login": login, "password": password}

        if any([True if x == '' else False for x in [name, login, password]]):
            raise AddProfileEmptyError

    except AddProfileEmptyError:
        print("[!] Anulowano dodawanie!")
        input("[<] Aby kontynuować wciśnij enter")

    else:  # wyślij do bazy danych
        if_sure = input("    [>] Zatwierdzić dodawanie? (Tak/Nie): ")
        if if_sure.lower() == "tak" or if_sure.lower() == 't':
            UsefulOperations.clear_console()
            print("    [D] Dodawanie danych do bazy...\n")
            with DataOrders.BaseConnect(DATABASE_URL) as conn:
                conn.add_to_database(dict_all=add_data)

            show = f"    [D] DODANO DO BAZY DANYCH: \n\n" \
                   f"        [Aplikacja]: {add_data['name']} \n" \
                   f"        [login]: {cipher.decryption(add_data['login'])} \n" \
                   f"        [Hasło]: {cipher.decryption(add_data['password'])} \n"
            print(show)
            input("[<] Aby kontynuować wciśnij enter.")
        else:
            print("[!] Anulowanie edycji.")
            input("[<] Aby kontynuować wciśnij enter.")


def option_show_profiles() -> None:
    """
    Show profiles from database
    :return:
    """
    stop = False
    while not stop:
        # Emergency stop
        if stop:
            break

        UsefulOperations.clear_console()
        print(DisplayMenu.show_profiles_menu())
        select_option = UsefulOperations.user_input(menu_size['show_profiles'])

        match select_option:
            case 1:  # po nazwie
                UsefulOperations.clear_console()
                print(DisplayMenu.show_by_name_menu())
                name = input("    [>] Podaj nazwę aplikacji: ")

                try:
                    if name == "":
                        raise AddProfileEmptyError

                except AddProfileEmptyError:
                    print("[!] Anulowano wyświetlanie!")
                    input("[<] Aby kontynuować wciśnij enter")

                else:
                    UsefulOperations.clear_console()
                    # print(name)

                    with DataOrders.BaseConnect(DATABASE_URL) as conn:
                        list_names = conn.show_by_name(name)
                        if len(list_names) != 0:
                            print("    [D] Znaleziono pasujące elementy:\n")
                            for row in list_names:
                                show = f"    [id]:. . . . .  {row['id']} \n" \
                                       f"    [Aplikacja]: . {row['name']} \n" \
                                       f"    [login]: . . . {cipher.decryption(row['login'])} \n" \
                                       f"    [Hasło]: . . . {cipher.decryption(row['password'])} \n"
                                print(show)
                        else:
                            print(f"    [-] Baza nie zawiera danych podobnych \n"
                                  f"        do podanej wartości: {name}")
                    input("[<] Aby kontynuować wciśnij enter")

            case 2:  # Wszystko
                UsefulOperations.clear_console()
                print("    [D] Wyświetlono wszystko: \n")

                with DataOrders.BaseConnect(DATABASE_URL) as conn:
                    list_names = conn.show_all()
                    if len(list_names) != 0:
                        for row in list_names:
                            show = f"        [id]:. . . . . {row['id']} \n" \
                                   f"        [Aplikacja]: . {row['name']} \n" \
                                   f"        [login]: . . . {cipher.decryption(row['login'])} \n" \
                                   f"        [Hasło]: . . . {cipher.decryption(row['password'])} \n"
                            print(show)
                    else:
                        print("    [D] Baza nie zawiera danych!")
                input("[<] Aby kontynuować wciśnij enter")

            case 0:
                stop = True
                print("Powrót")


def option_edit_profiles() -> None:
    """
    edit profile option
    :return:
    """
    UsefulOperations.clear_console()
    print(DisplayMenu.edit_profiles_id_menu())

    try:
        select_id = UsefulOperations.user_input_id()

        if select_id > 0:
            # Wyjście do bazy z zapytaniem o podanie danych na podstawie id np. select_id = 3
            # data_for_edit = {'id': 3, 'name': 'Facebook', 'login': 'Karol Kowalski', 'password': 'WTF123'}
            # jeżeli id za wysokie zwraca None

            with DataOrders.BaseConnect(DATABASE_URL) as conn:
                data_for_edit = conn.show_by_id(select_id)

                if data_for_edit is not None:
                    show_old_data = f"\n" \
                                    f"    [D] Dane wybrane do edycji: \n\n" \
                                    f"    [id]:. . . . . {data_for_edit['id']} \n" \
                                    f"    [Aplikacja]: . {data_for_edit['name']} \n" \
                                    f"    [login]: . . . {cipher.decryption(data_for_edit['login'])} \n" \
                                    f"    [Hasło]: . . . {cipher.decryption(data_for_edit['password'])} \n"
                else:
                    raise ToHighUserOptionError

                print(show_old_data)

            new_data = UsefulOperations.user_input_data(
                select_id,
                name=True,
                login=True,
                password=True
            )  # [id, name, login, password]

            # if new_data['name'] is None and new_data['login'] is None and new_data['password'] is None:
            # print(list(new_data.values()))
            if all(element is None for element in list(new_data.values())[1:]):
                raise EmptyUserInputError

            if new_data['id'] is None or new_data['id'] <= 0:
                raise ToLowUserOptionError
        else:
            raise Error

    except Error:
        input("[<] Aby kontynuować wciśnij enter.")

    except EmptyUserInputError:
        print("[!] Nie podano danych! Anulowanie edycji.")
        input("[<] Aby kontynuować wciśnij enter.")

    except ToHighUserOptionError:
        print("[!] Podano zbyt wysokie id! Anulowanie edycji.")
        input("[<] Aby kontynuować wciśnij enter.")

    else:
        if_sure = input("    [>] Zatwierdzić zmiany? (Tak/Nie): ")
        if if_sure.lower() == "tak" or if_sure.lower() == 't':
            UsefulOperations.clear_console()

            with DataOrders.BaseConnect(DATABASE_URL) as conn:
                conn.update(new_data)

            input("[<] Aby kontynuować wciśnij enter.")
        else:
            print("[!] Anulowanie edycji.")
            input("[<] Aby kontynuować wciśnij enter.")


def option_delete_profiles() -> None:
    stop = False
    while not stop:
        # secure break
        if stop:
            break

        UsefulOperations.clear_console()
        print(DisplayMenu.delete_profiles_menu())
        select_option = UsefulOperations.user_input(menu_size['delete_profiles'])

        match select_option:
            case 1:
                UsefulOperations.clear_console()
                print(DisplayMenu.delete_profiles_byid_menu())
                try:
                    del_id = UsefulOperations.user_input_id()
                    if del_id <= 0:
                        raise ToLowUserOptionError

                except ToLowUserOptionError:
                    input("[<] Aby kontynuować wciśnij enter.")

                else:
                    try:
                        # wyjście do bazy z zapytaniem o podanie danych na podstawie id
                        with DataOrders.BaseConnect(DATABASE_URL) as conn:
                            data_dict = conn.show_by_id(del_id)

                            # przykład zwrotu
                            if data_dict is not None:
                                show_data_del = f"    [D] Dane wybrane do usunięcia: \n\n" \
                                                f"    [id]:. . . . . {data_dict['id']} \n" \
                                                f"    [Aplikacja]: . {data_dict['name']} \n" \
                                                f"    [login]: . . . {cipher.decryption(data_dict['login'])} \n" \
                                                f"    [Hasło]: . . . {cipher.decryption(data_dict['password'])} \n"

                                print(show_data_del)
                            else:
                                raise ToHighUserOptionError

                        if_sure = input("    [>] Zatwierdzić usuwanie? (Tak/Nie): ")

                        if if_sure.lower() == "tak" or if_sure.lower() == 't':
                            UsefulOperations.clear_console()
                            print("    [D] Usunięto dane o podanym id")
                            with DataOrders.BaseConnect(DATABASE_URL) as conn:
                                conn.del_by_id(del_id)

                            input("[<] Aby kontynuować wciśnij enter.")

                        else:
                            print("[!] Anulowano!")
                            input("[<] Aby kontynuować wciśnij enter.")

                    except ToHighUserOptionError:
                        print("[!] Podano zbyt wysokie id! Anulowanie edycji.")
                        input("[<] Aby kontynuować wciśnij enter.")
            case 2:
                UsefulOperations.clear_console()
                print(DisplayMenu.delete_profiles_delall_menu())

                if_sure = input("    [>] ZATWIERDZENIE USUWANIA: ")
                if if_sure.lower() == "kasuj wszystko":
                    UsefulOperations.clear_console()

                    with DataOrders.BaseConnect(DATABASE_URL) as conn:
                        conn.del_all()

                    print("    [D] KASOWANIE WSZYSTKIEGO")
                    input("[<] Aby kontynuować wciśnij enter.")

                else:
                    print("[!] Anulowano!")
                    input("[<] Aby kontynuować wciśnij enter.")

            case 0:
                stop = True
                print("Powrót")


def option_about() -> None:
    stop = False
    while not stop:
        # critical if
        if stop:
            break
        UsefulOperations.clear_console()
        print(DisplayMenu.about())
        select_option = UsefulOperations.user_input(menu_size['about'])

        match select_option:
            case 0:
                stop = True
                print("POWRÓT")
