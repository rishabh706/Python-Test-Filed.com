import sqlite3
import pandas as pd
import sys

class Database:

    def __init__(self,table_name=None):
        self.table_name=table_name

    def create_table(self):
        # connecting to SQLITE Database
        with sqlite3.connect('database.db') as con:

            cursor = con.cursor()

            cursor.execute('CREATE TABLE IF NOT EXISTS SONG (ID INTEGER PRIMARY KEY UNIQUE NOT NULL,NAME VARCHAR(100) NOT NULL,DURATION INTEGER NOT NULL,UPLOADED_TIME DATETIME NOT NULL)')

            cursor.execute(
                'CREATE TABLE IF NOT EXISTS PODCAST (ID INTEGER PRIMARY KEY UNIQUE NOT NULL,NAME VARCHAR(100) NOT NULL,DURATION INTEGER NOT NULL,UPLOADED_TIME DATETIME NOT NULL,HOST VARCHAR(100) NOT NULL,PARTICIPANTS VARCHAR(100))')

            cursor.execute(
                'CREATE TABLE IF NOT EXISTS AUDIOBOOK (ID INTEGER PRIMARY KEY UNIQUE NOT NULL,TITLE VARCHAR(100) NOT NULL,AUTHOR VARCHAR(100) NOT NULL,NARRATOR VARCHAR(100) NOT NULL,DURATION INTEGER NOT NULL,UPLOADED_TIME DATETIME NOT NULL)')

            cursor.close()

    def list_tables(self):
        with sqlite3.connect("database.db") as con:
            table_names=pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'",con)

        return table_names

    def get_table_data(self,table_name):

        # Connecting to the Database
        with sqlite3.connect("database.db") as con:
            # table_names=pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'",con)
            if self.table_name=="SONG":
                table_data=pd.read_sql_query("SELECT * FROM SONG",con)

            elif self.table_name=="PODCAST":
                table_data=pd.read_sql_query("SELECT * FROM PODCAST",con)

            else:
                table_data=pd.read_sql_query("SELECT * FROM AUDIOBOOK",con)

        return table_data

if __name__=="__main__":
    if len(sys.argv)==1:
        table_data=Database()
        tables=table_data.list_tables()
        print(tables)

    else:
        table_name_arg=sys.argv[1]
        table_data=Database(str(table_name_arg).upper())
        data=table_data.get_table_data(str(table_name_arg).upper())
        print(data)
