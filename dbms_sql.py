import sqlite3 as sql, sys, os


class DBMS:
    def __init__(self, db_path: os.path, ip: str, port: int, user: str, password: str, db: str):
        self.db_path = db_path
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sql.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def create_table (self):
        self.cursor.execute ('''CREATE TABLE IF NOT EXISTS items (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                URL TEXT,
                                priceLimit TEXT,
                                dateLimit,
                            ''')

    def insert_data (self, data: dict):
        '''name TEXT, URL TEXT, priceLimit TEXT, dateLimit TEXT OR BOOL'''

        self.cursor.execute ('''INSERT INTO items (name, URL, priceLimit, dateLimit)
                                VALUES (?, ?, ?, ?)''', (data ['name'], data ['URL'], data ['priceLimit'], data ['dateLimit']))
        self.conn.commit()
