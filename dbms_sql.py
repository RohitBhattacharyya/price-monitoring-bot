import sqlite3 as sql, os


class DBMS:
    def __init__ (self, db_path: os.path, tableName: str) -> None:
        self.db_path = db_path
        self.tableName = tableName

        self.conn = None
        self.cursor = None

    def connect (self) -> None:
        # if self.dp_path exists, connect to it, else create it
        if os.path.exists (self.db_path):
            self.conn = sql.connect (self.db_path)
            self.cursor = self.conn.cursor ()

        else:
            self.conn = sql.connect (self.db_path)
            self.cursor = self.conn.cursor ()
            self.create_table ()

    def create_table (self) -> None:
        '''name TEXT, URL TEXT, priceLimit TEXT, dateLimit TEXT OR BOOL'''

        self.cursor.execute (f'''CREATE TABLE IF NOT EXISTS {self.tableName} (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                URL TEXT,
                                priceLimit TEXT,
                                dateLimit TEXT OR BOOL)
                            ''')

    def insert_data (self, data: dict) -> None:
        '''name TEXT, URL TEXT, priceLimit TEXT, dateLimit TEXT OR BOOL'''

        self.cursor.execute ('''INSERT INTO items (name, URL, priceLimit, dateLimit)
                                VALUES (?, ?, ?, ?)''', (data ['name'], data ['URL'], data ['priceLimit'], data ['dateLimit']))
        self.conn.commit ()

    def update_data (self, id: int, data: dict) -> None:
        self.cursor.execute (f'''UPDATE items SET name = ?, URL = ?, priceLimit = ?, dateLimit = ? WHERE id = {id}''', (data ['name'], data ['URL'], data ['priceLimit'], data ['dateLimit']))
        self.conn.commit ()

    def get_all_data (self) -> list:
        self.cursor.execute ('''SELECT * FROM items''')
        return self.cursor.fetchall ()

    def get_data (self, id: int) -> list:
        self.cursor.execute (f'''SELECT * FROM items WHERE id = {id}''')
        return self.cursor.fetchone ()

    def delete_data (self, id: int) -> None:
        self.cursor.execute (f'''DELETE FROM items WHERE id = {id}''')
        self.conn.commit ()

    def delete_all_data (self) -> None:
        self.cursor.execute ('''DELETE FROM items''')
        self.conn.commit ()

    def close (self) -> None:
        self.conn.close ()
