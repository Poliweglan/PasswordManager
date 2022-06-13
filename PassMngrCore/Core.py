from PassMngrCore import DisplayMenu
from PassMngrCore.DisplayMenu import menu_size
from PassMngrCore.Error_pmc import EmptyUserInputError, ToHighUserOptionError, ToLowUserOptionError
# import cursor
# cursor.hide()


def user_input(size) -> int:
    """
    Validate the specified value
    :param size: max size of menu options
    :return: number of menus
    """
    input_user = input("Podaj opcję: ")

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
        print("Należy wybrać opcję!")
        input("Aby kontynuować wciśnij enter")

    except ValueError:
        print("Należy podać wartość cyfrową!")
        input("Aby kontynuować wciśnij enter")

    except ToHighUserOptionError:
        print("Należy podać mniejszą wartość cyfrową!")
        print(f"Wartość musi być z zakresu (0, {size})!")
        input("Aby kontynuować wciśnij enter")

    except ToLowUserOptionError:
        print("Należy podać większą wartość cyfrową!")
        print(f"Wartość musi być z zakresu (0, {size})!")
        input("Aby kontynuować wciśnij enter")

    else:
        return user_option


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
        select_option = user_input(menu_size['main_menu'])

        match select_option:
            case 1:
                ...
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
