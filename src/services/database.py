import sqlite3
from sqlite3 import Error

class Database:
    """Database service class.
    """
    def __init__(self, db_path: str):
        """Creates a new instance of the Database class.
        Takes the path of the database file.

        Args:
            db_path (str): Path of the database file.
        """
        self.db_path = db_path
        self.conn = None

    def connect(self):
        """Connects to the database.
        """
        if self.conn is not None:
            self.disconnect()
        print(f"Connecting to database...")
        try:
            self.conn = sqlite3.connect(self.db_path)
        except Error as e:
            print(e)
        
    def disconnect(self):
        """Disconnects from the database.
        """
        if self.conn is None:
            return
        print(f"Disconnecting from database...")
        self.conn.close()
        
    def create_table(self, sql_create_table: str):
        """Creates a database table.
        NOT MEANT TO BE CALLED DIRECTLY.

        Args:
            sql_create_table (str): An sql create table statement.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_create_table)
        except Error as e:
            print(e)
    
    def get_table(self, table_name: str):
        """Gets a table from the database.

        Args:
            table_name (str): The name of the table to get.

        Returns:
            List: A list of database table entries.
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            return cursor.fetchall()
        except Error as e:
            print(e)
    
    def add_entry(self, table_name: str, entry: tuple):
        """Adds an entry to the database.

        Args:
            table_name (str): The name of the table to add the entry to.
            entry (tuple): The entry to add to the database.
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"INSERT INTO {table_name} VALUES {entry}")
            self.conn.commit()
        except Error as e:
            print(e)
        