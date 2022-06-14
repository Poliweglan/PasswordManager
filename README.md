# Password Manager

Program konsolowy służący do zarządzania hasłami, powstał w celach osobistych oraz w ramach nauki języka python w raz sql. 

## Zawartość:

### Main.py

- uruchamia program

### Core.py ???

- Spina całość, aby przekazać do main funkcję `start_program()`

### DisplayMenu.py

- Zwraca string menu

### DataOrders.py

- Zawiera polecenia sql:
  
  - Tworzenie bazy danych i tabeli jeżeli nie istnieją
  
  - Dodawanie profilu <- przekazanie zmiennych:
    
    - nazwa aplikacji: name
    
    - login/mail/nazwa użytkownika: login
    
    - hasło: password
  
  - Wyświetlanie profilu:
    
    - Wyświetlanie po nazwie aplikacji:
      
      należy przekazać wartość - name.
    
    - Wyświetlanie po loginie do aplikacji:
      
      Należy przekazać wartość - login.
      
      Zwraca dane: id, name, login, password
  
  - Aktualizacja danych:
    
    - Aktualizowanie danych: (name, login, password) po podaniu id
      
      jeżeli jakaś wartość została pusta nie podlega zmianie
  
  - usuwanie danych:
    
    - usuwanie pod podaniu id
    
    - usuwanie wszystkiego: (przed wykonaniem operacji trzeba potwierdzić)

### About.py

- Informacje o programie, wersja, autor, data wydania wersji, licencja

### Menu:

#### DODAJ PROFIL

- Pobiera od użytkownika:
  
  - `name` - nazwa użytkownika
  
  - `login` - login konta
  
  - `password` - hasło do konta

Schemat działania:

- Jeżeli jakiekolwiek pole puste:
  
  - Anuluje dodawania profilu

- Jeżeli wszystkie zapełnione:
  
  - Wszystkie dane szyfruje i przesyła do `DataOrders.py`
    
    - `DataOrders.py` sprawdza czy baza istnieje:
      
      - Jeżeli nie:
        
        - tworzy bazę i tabelę 
        
        - dodaje dane
      
      - Jeżeli tak:
        
        - dodaje dane

#### WYŚWIETL PROFIL

##### Po nazwie

- Pobiera od użytkownia:
  
  - `name` - nazwa użytkownika

Schemat działania:

- Jeśli pole puste:
  
  - Anuluje wyświetlanie powórt do menu głównego / wyświetl zastanów się

- jeśli zapełnione: 
  
  - wysyła do `DataOrders.py`
    
    - `DataOrders.py` sprawdza czy baza istnieje:
      
      - jeżeli nie:
        
        - błąd i anulowanie (Wprowadź najpierw dane!)

##### Wszystko

#### EDYTUJ PROFIL

#### USUŃ PROFIL

#### O PROGRAMIE