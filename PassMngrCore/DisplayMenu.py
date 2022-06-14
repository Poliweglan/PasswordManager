from PassMngrCore import Config
import os


# [2] WYŚWIETL PROFIL
# [3] EDYTUJ PROFIL
# [4] USUŃ PROFIL
# [5] O PROGRAMIE
menu_size = {
    "main_menu": 5,
    "add_profile_menu": None,
    "show_profiles": 2,
}


def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def program_full_name() -> str:
    return f"{Config.get_program_name()} [{Config.get_version_stage()} {Config.get_version_number()}]"


def main_menu() -> str:
    menu = f"""
    {program_full_name()}
    
        [ ] Menu [ ]
        
        [1] DODAJ PROFIL
        [2] WYŚWIETL PROFIL
        [3] EDYTUJ PROFIL
        [4] USUŃ PROFIL
        [5] O PROGRAMIE
        
        [0] WYJŚCIE
"""
    return menu


def add_profile_menu() -> str:
    menu = f"""
    {program_full_name()}
    
        [ ] DODAJ PROFIL [ ]

    [-] Należy podać:
            - nazwę aplikacji,
            - login/mail,
            - hasło
            
    [-] Jeżeli jakiekolwiek pole zostanie puste
        nastąpi anulowanie dodawania oraz powrót.
"""
    return menu


def show_profiles_menu() -> str:
    menu = f"""
    {program_full_name()}

        [ ] WYŚWIETL PROFIL [ ]

        [1] WYŚWIETL PO NAZWIE
        [2] WYŚWIETL WSZYSTKO

        [0] POWRÓT
    """
    return menu


def show_by_name_menu() -> str:
    menu = f"""
    {program_full_name()}
    
        [ ] WYŚWIETL PO NAZWIE [ ]
        
    [-] Należy podać:
            - nazwę aplikacji
    
    [-] Jeżeli jakiekolwiek pole zostanie puste
        nastąpi anulowanie dodawania oraz powrót.
    """

    return menu

# def show_all_menu() -> str:
#     ...















if __name__ == '__main__':
    pass
