import sqlite3
from abc import ABC, abstractmethod

# Abstract Factory
class DatabaseConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self):
        pass

# Concrete Factory for SQLite
class SQLiteConnectionFactory(DatabaseConnectionFactory):
    def __init__(self, db_name):
        self.db_name = db_name

    def create_connection(self):
        return sqlite3.connect(self.db_name)

# Example usage
if __name__ == "__main__":
    # Create a SQLite connection factory
    sqlite_factory = SQLiteConnectionFactory("example.db")

    # Create a connection using the factory
    connection = sqlite_factory.create_connection()

    # Create a cursor and execute a simple query
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
    cursor.execute('''INSERT INTO users (name) VALUES (?)''', ("Alice",))
    cursor.execute('''INSERT INTO users (name) VALUES (?)''', ("Bob",))

    # Commit the changes
    connection.commit()

    # Query the database
    cursor.execute('''SELECT * FROM users''')
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the connection
    connection.close()