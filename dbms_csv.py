import os, csv, pandas as pd


class DBMS:
    def __init__ (self, dbPath: os.path, tableName: str):
        self.dbPath = dbPath
        self.create_db ()

        if '.csv' not in tableName and '.' not in tableName:
            self.tableName = tableName + '.csv'

        if '.' in tableName and '.csv' not in tableName:
            print ('\033[91m' + '[ERROR] Invalid table type' + '\033[0m')
            exit ()

        else:
            self.tableName = tableName

    def create_db (self):
        if not os.path.exists (self.dbPath):
            os.makedirs (self.dbPath)

        if os.getcwd () != self.dbPath:
            os.chdir (self.dbPath)

    def create_table (self):
        if not os.path.exists (self.tableName):
            with open (self.tableName, 'w') as f:
                pass

    def insert_data (self, data: dict):
        with open (self.tableName, 'a') as f:
            writer = csv.writer (f)
            writer.writerow (data.values ())

    def read_data (self):
        df = pd.read_csv (self.tableName)
        return df

    def update_data (self, data: dict):
        df = self.read_data ()
        df.update (data)
        df.to_csv (self.tableName, index = False)

    def delete_data (self, data: dict):
        df = self.read_data ()
        df.drop (data)
        df.to_csv (self.tableName, index = False)

    def delete_all_data (self):
        with open (self.tableName, 'w') as f:
            pass

    def close_db (self):
        os.chdir (os.path.dirname (os.path.abspath (__file__)))