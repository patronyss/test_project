import sqlite3


class DateBase:
    def __init__(self):
        self.connection = sqlite3.connect('main_db.sl3', 5)
        self.cursor = self.connection.cursor()

    def add_site(self, site):
        self.cursor.execute(f"INSERT INTO main_table (site, count) VALUES ('{site}', 0);")
        self.connection.commit()

    def clear_db(self):
        self.cursor.execute('DELETE FROM main_table')
        self.connection.commit()

    def get_sites(self):
        self.cursor.execute('SELECT rowid, site, count FROM main_table')
        self.connection.commit()
        return self.cursor.fetchall()

    def sort_db(self):
        pass

    def update_db(self):
        self.cursor.execute('DELETE FROM main_table')
        self.connection.commit()
