import sqlite3

# Singleton Database object so that multiple connections aren't created by the application
class Database:
    class __DB_CONNECTION:
        def __init__(self):
            self.connection = sqlite3.connect("local.db")
    
    connection = None
    cursor = None

    def __init__(self):
        if not Database.connection:
            Database.connection = Database.__DB_CONNECTION()
            Database.cursor = Database.connection.cursor()