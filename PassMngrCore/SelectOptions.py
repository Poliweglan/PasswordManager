from PassMngrCore import DisplayMenu, Core
from PassMngrCore.ciphers import cezar as cipher


# [1] DODAJ PROFIL
# [2] WYŚWIETL PROFIL
# [3] EDYTUJ PROFIL
# [4] USUŃ PROFIL
# [5] O PROGRAMIE
def option_add_profil() -> None:
    """
    Add profile option
    :return:
    """
    print(DisplayMenu.add_profile_menu())
