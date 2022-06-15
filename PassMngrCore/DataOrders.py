import sqlite3
from sqlite3 import Error


#   table: Passwd
#   id int primary key, name text not null, login text not null, password text not null
#   id, name, login, password


class BaseConnect:
    def __init__(self, file_db):
        self.__structure = ["id", "name", "login", "password"]
        self.file_db = file_db
        self.conn = None

    def __enter__(self) -> object:
        """
        connect to database
        :return: conn object with base
        """
        try:
            self.conn = sqlite3.connect(self.file_db)
            # print(f"connect to database {self.file_db}")
        except Error as e:
            print(e)

        else:
            cur = self.conn.cursor()
            # sql_exist = 'SELECT count(name) FROM sqlite_master WHERE type="table" AND name="Passwd"'
            # exist = cur.execute(sql_exist).fetchall()
            # if exist == 0:
            #     sql_create = '''CREATE TABLE Passwd (
            #                           id INTEGER PRIMARY KEY,
            #                           name TEXT NOT NULL,
            #                           login TEXT NOT NULL,
            #                           password TEXT NOT NULL
            #                           )'''
            #     cur.execute(sql_create)
            sql_create = '''CREATE TABLE IF NOT EXISTS Passwd (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                login TEXT NOT NULL,
                                password TEXT NOT NULL
                                )'''
            cur.execute(sql_create)
            self.conn.commit()

        # print(self.conn, self.file_db)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        self.conn = None
        # print(f"close connect with database {self.file_db}")
        # print(self.conn, self.file_db)

    def add_to_database(self, name=None, login=None, password=None, dict_all=None) -> None:
        """
        add values to database
        :param name:
        :param login:
        :param password:
        :param dict_all: ('name','login','password')
        :return:
        """
        cur = self.conn.cursor()
        sql = 'INSERT INTO passwd(name, login, password) VALUES(?, ?, ?)'
        elements = ()

        if not (name is None and login is None and password is None):
            elements = (name, login, password)

        elif dict_all is not None:
            name = dict_all['name']
            login = dict_all['login']
            password = dict_all['password']
            elements = (name, login, password)

        # print(elements)
        cur.execute(sql, elements)
        self.conn.commit()

    def show_by_id(self, find_id) -> dict:
        """
        get dict of values finds by id in database
        :param find_id: id to find
        :return: elements from database
        """
        cur = self.conn.cursor()
        sql = "SELECT * FROM Passwd WHERE id = ?"
        cur.execute(sql, (find_id, ))
        rows = cur.fetchall()
        out_find = None

        for row in rows:
            out_find = dict(zip(self.__structure, row))

        return out_find

    def show_by_name(self, find_name) -> list:
        """
        get values of names look familiar like input name
        :param find_name: name to find
        :return: list of names look like input name
        """
        cur = self.conn.cursor()
        find_like_name = f"%{find_name}%"
        sql = "SELECT * FROM Passwd WHERE name LIKE ?"
        cur.execute(sql, (find_like_name, ))
        rows = cur.fetchall()
        names = []

        for row in rows:
            names.append(dict(zip(self.__structure, row)))

        return names

    def show_all(self) -> list:
        """
        get all value in database
        :return: list all values from database
        """
        cur = self.conn.cursor()
        sql = 'SELECT * FROM Passwd'
        cur.execute(sql)
        rows = cur.fetchall()
        names = []
        for row in rows:
            names.append(dict(zip(self.__structure, row)))

        return names

    def update(self, new_data) -> None:
        """
        update values in database
        :param new_data: data for update
        :return:
        """
        cur = self.conn.cursor()

        if new_data['name'] is not None:
            sql = 'UPDATE Passwd SET name = ? WHERE id = ?'
            cur.execute(sql, (new_data['name'], new_data['id']))
            self.conn.commit()
            print("git nazwa")

        if new_data['login'] is not None:
            sql = 'UPDATE Passwd SET login = ? WHERE id = ?'
            cur.execute(sql, (new_data['login'], new_data['id']))
            self.conn.commit()
            print("git login")

        if new_data['password'] is not None:
            sql = 'UPDATE Passwd SET password = ? WHERE id = ?'
            cur.execute(sql, (new_data['password'], new_data['id']))
            self.conn.commit()
            print("git pass")

    def del_by_id(self, del_id) -> None:
        """
        delete value from database by id
        :param del_id: id to dell
        :return:
        """
        cur = self.conn.cursor()
        sql = "DELETE FROM Passwd WHERE id = ?"
        cur.execute(sql, (del_id, ))

        # sql = 'UPDATE sqlite_sequence SET seq = ? WHERE name = "Passwd"'
        # cur.execute(sql, (del_id, ))

        self.conn.commit()

    def del_all(self) -> None:
        """
        deleting all of value in database
        :return:
        """
        cur = self.conn.cursor()
        sql = "DELETE FROM Passwd"
        cur.execute(sql)
        self.conn.commit()