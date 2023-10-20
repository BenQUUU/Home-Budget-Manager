import sqlite3
from application import Application

if __name__ == '__main__':
    with sqlite3.connect('budget.db') as database:
        main = Application()
        main.main()





