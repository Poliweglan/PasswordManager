from PassMngrCore import Config


menu_size = {
    "main_menu": 5,
    "add_profile_menu": None,
    "show_profiles": 2,
    "delete_profiles": 2,
    "about": 0
}


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


def edit_profiles_id_menu() -> str:
    menu = f"""
    {program_full_name()}

        [ ] EDYTUJ PROFIL [ ]
    
    [-] Należy podać id do edycji.

    [-] Jeżeli pole zostanie puste
        nastąpi anulowanie.
    """

    return menu


def edit_profiles_nlp_menu() -> str:
    menu = f"""
    {program_full_name()}

        [ ] EDYTUJ PROFIL [ ]

    [-] Edycji podlega:
            - nazwa aplikacji
            - login/mail
            - hasło

    [-] Jeżeli wszystkie pola zostaną puste,
        nastąpi anulowanie.
    """

    return menu


def delete_profiles_menu() -> str:
    menu = f"""
    {program_full_name()}

        [ ] USUŃ PROFIL [ ]

        [1] USUŃ PO ID
        [2] USUŃ WSZYSTKO

        [0] POWRÓT
    """
    return menu


def delete_profiles_byid_menu() -> str:
    menu = f"""
    {program_full_name()}

        [ ] USUŃ PO ID [ ]

    [-] Należy podać id do usunięcia.
    
    [-] Puste pole oznacza anulowanie.
    """
    return menu


def delete_profiles_delall_menu() -> str:
    menu = f"""
    {program_full_name()}

        [ ] USUŃ WSZYSTKO [ ]

    [-] Potwierdź aby wszystko usunąć!
    
    [-] By potwierdzić wpisz: 
        "kasuj wszystko" 
    """
    return menu


def about() -> str:
    menu = f"""
    {program_full_name()}

        [ ] O PROGRAMIE [ ]

    [-] Jest to program testowy,
        stworzony tylko i wyłącznie
        w celach naukowych
        
    [-] Nie biorę odpowiedzialności za:
        - wycieki danych
        - dziwne błędy
        - przypadkowe usunięcie bazy danych
        - wszystko inne związane z tym programem
    
    [-] Nazwa: {Config.get_program_name()}
    [-] Wersja: [{Config.get_version_stage()} {Config.get_version_number()}]
    [-] Autor: {Config.get_author_username()}, {Config.get_author_git()}
    [-] Licencja: {Config.get_license()}
    
        [0] POWRÓT
    """
    return menu
