import sqlite3
from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Concrete Observer
class ConsoleLogger(Observer):
    def update(self, message):
        print(f"ConsoleLogger: {message}")

class EmailNotifier(Observer):
    def update(self, message):
        print(f"EmailNotifier: Sending email notification: {message}")

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, message):
        pass

# Concrete Subject
class UserDatabase(Subject):
    def __init__(self, db_name):
        self._observers = []
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )
            ''')

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

    def add_user(self, name):
        with self.connection:
            self.connection.execute('INSERT INTO users (name) VALUES (?)', (name,))
            self.notify(f"User  '{name}' added to the database.")

    def close(self):
        self.connection.close()

# Example usage
if __name__ == "__main__":
    # Create a user database
    user_db = UserDatabase("users.db")

    # Create observers
    console_logger = ConsoleLogger()
    email_notifier = EmailNotifier()

    # Attach observers to the user database
    user_db.attach(console_logger)
    user_db.attach(email_notifier)

    # Add users
    user_db.add_user("Alice")
    user_db.add_user("Bob")

    # Detach an observer
    user_db.detach(email_notifier)

    # Add another user
    user_db.add_user("Charlie")

    # Close the database connection
    user_db.close()