import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    co = None
    try: co = sqlite3.connect(db_file)
    except Error as e: print(e)
    finally:
        if co: co.close()fffff


if __name__ == '__main__':
    create_connection(r"T:\- 4 Suivi Appuis\25_BDD\DLG\DLG.db")
