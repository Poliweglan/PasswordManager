from PassMngrCore.Error_pmc import EmptyUserInputError, ToHighUserOptionError, ToLowUserOptionError


def user_input(size) -> int:
    """
    Validate the specified value
    :param size: max size of menu options
    :return: number of menus
    """
    input_user = input("    Podaj opcję: ")

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