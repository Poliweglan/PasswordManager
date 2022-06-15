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

##### - Po nazwie

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
      
      - Jeżeli tak:
        
        - wyszukuje `where name = %name%` 
          
          - nie znajduje: 
            
            - zwraca (brak pasujacych profili)
          
          - znajduje:
            
            - zwraca dict do wyświetl profil
  
  - dostaje dane , dekoduje i wyświetla
    
    ```python
    # id: 1, Aplikacja: Facebook
    # login: login, hasło: hasło
    # 
    # id: 3, Aplikacja: facebook
    # login: login, hasło: hasło
    ```

##### - Wszystko

- Wysyła funkcje do `DataOrders.py`
  
  - `DataOrders.py` sprawdza czy baza istnieje:
    
    - jeżeli nie:
      
      - błąd i anulowanie (Wprowadź najpierw dane!)
    
    - Jeżeli tak:
      
      - zwraca dane
        
- dostaje dane, dekoduje i wyświetla:
        
  ```python
  # id: 1, Aplikacja: Facebook
  # login: login, hasło: hasło
  # 
  # id: 2, Aplikacja: facebook
  # login: login, hasło: hasło
  ```

#### EDYTUJ PROFIL
- pobiera dane:

  - `id` - id profilu

  - `name` - nazwa aplikacji
  
  - `login` - nazwa aplikacji
  
  - `password` - hasło
  
Schemat działania:

 - pyta o id:
   - pole puste:
     - anulowanie zadania - bład (pole puste)
   - pole z literą:
     - anulowanie zadania - błąd (musi być cyfra)
   - pole z cyfrą:
     - pobiera dane o nazwie, loginie i haśle
       - jeśli jakieś pole jest puste to zapisuje jako None
       - przekazuje do `DataOrders.py`
         - `DataOrders.py` sprawdza czy baza istnieje:
           - jeżeli nie:
             - błąd i anulowanie (Wprowadź najpierw dane!)
           - Jeżeli tak:
             - dokonuje aktualizacji na podstawie id
 

#### USUŃ PROFIL

##### - Na podstawie id:
  
- pyta o id:
   - pole puste:
     - anulowanie zadania - bład (pole puste)
   - pole z literą:
     - anulowanie zadania - błąd (musi być cyfra)
   - pole z cyfrą:
     - nalezy potwierdzić (input == delete):
       - przekazuje do `DataOrders.py`
     - (input != delete):
       - anulowanie 

##### - Wszystko

- należy potwierdzić:
  - input == kasuj wszystko:
    - wysyła do `DataOrders.py` kasowanie
  - input != kasuj wszystko:
    - anulowanie

#### O PROGRAMIE

  info o programie xD