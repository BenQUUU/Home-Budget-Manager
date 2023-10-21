import sqlite3
from application import Application


def init_db(db_cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS categories
            (id INTEGER PRIMARY KEY, name TEXT)''')
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS items(
            id INTEGER PRIMARY KEY,
            category_id INTEGER,
            amount REAL,
            date TEXT,
            FOREIGN KEY (category_id) REFERENCES categories(id))''')


if __name__ == '__main__':
    with sqlite3.connect('budget.db') as database:
        cursor = database.cursor()
        init_db(cursor)

        main = Application()
        main.main()





