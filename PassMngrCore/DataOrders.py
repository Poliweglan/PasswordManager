import sqlite3
from sqlite3 import Error


class BaseConnect:
    def __init__(self, file_db):
        self.file_db = file_db
        self.conn = None

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.file_db)
            print(f"connect to database {self.file_db}")
        except Error as e:
            print(e)

        print(self.conn, self.file_db)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        self.conn = None
        print(f"close connect with database {self.file_db}")
        print(self.conn, self.file_db)
