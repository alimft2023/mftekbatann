import sqlite3

class DatabaseSingleton:
    _instance = None

    def __new__(cls, db_name):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance._initialize(db_name)
        return cls._instance

    def _initialize(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def query(self, sql, params=None):
        if params is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

# Usage
if __name__ == "__main__":
    db_name = "example.db"

    # First instance
    db1 = DatabaseSingleton(db_name)
    db1.query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    db1.query("INSERT INTO users (name) VALUES (?)", ("Alice",))
    db1.commit()

    # Second instance
    db2 = DatabaseSingleton(db_name)
    result = db2.query("SELECT * FROM users")
    print(result)

    # Both db1 and db2 refer to the same instance