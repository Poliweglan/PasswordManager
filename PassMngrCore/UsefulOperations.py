from PassMngrCore.Error_pmc import *
from PassMngrCore.Ciphers import cezar as cipher
import os


def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def user_input(size) -> int:
    """
    Validate the specified value
    :param size: max size of menu options
    :return: number of menus
    """
    input_user = input("[>] Podaj opcję: ")

    try:
        if input_user == '':
            raise EmptyUserInputError
        else:
            user_option = int(input_user)

            if user_option > size:
                raise ToHighUserOptionError

            if user_option < 0:
                raise ToLowUserOptionError

    except EmptyUserInputError:
        print("[!]Należy wybrać opcję!")
        input("[<] Aby kontynuować wciśnij enter.")

    except ValueError:
        print("[!]Należy podać wartość cyfrową!")
        input("[<] Aby kontynuować wciśnij enter.")

    except ToHighUserOptionError:
        print("[!]Należy podać mniejszą wartość cyfrową!")
        print(f"[!]Wartość musi być z zakresu (0, {size})!")
        input("[<] Aby kontynuować wciśnij enter.")

    except ToLowUserOptionError:
        print("[!]Należy podać większą wartość cyfrową!")
        print(f"[!] Wartość musi być z zakresu (0, {size})!")
        input("[<] Aby kontynuować wciśnij enter.")

    else:
        return user_option


def user_input_id() -> int:
    """
    Validate the specified value
    :return: number of id
    """
    input_id = input("    [>] Podaj id: ")

    try:
        if input_id == '':
            raise EmptyUserInputError
        else:
            uid = int(input_id)

            if uid <= 0:
                raise ToLowUserOptionError

    except EmptyUserInputError:
        print("[!] Nie podano id. Anulowanie!")

    except ValueError:
        print("[!] Id musi być wartością cyfrową! Anulowanie!")

    except ToLowUserOptionError:
        print("[!] Id musi być większa od zera! Anulowanie!")

    else:
        return uid

    return -1


def user_input_data(puid=None, name=False, login=False, password=False) -> dict:
    """
    Validate data, name, login, password
    :param puid: edit for give id
    :param name: if True add value else add None to list
    :param login: if True add value else add None to list
    :param password: if True add value else add None to list
    :return: if any value is not empty return list
    """
    input_pass = None
    input_login = None
    input_name = None

    if name:
        input_name = input(f"    [>] Podaj nową nazwę aplikacji: ")
        if input_name == '':
            input_name = None

    if login:
        input_login = cipher.encryption(input(f"    [>] Podaj nowy login: "))
        if input_login == '':
            input_login = None

    if password:
        input_pass = cipher.encryption(input(f"    [>] Podaj nowe hasło: "))
        if input_pass == '':
            input_pass = None

    # print({'id': puid, 'name': input_name, 'login': input_login, 'password': input_pass})
    return {'id': puid, 'name': input_name, 'login': input_login, 'password': input_pass}
