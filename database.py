import sqlite3

class Database:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                year INTEGER
            )
        ''')
        self.conn.commit()

    def add_book(self, book: dict):
        self.cursor.execute('''
            INSERT INTO books (title, author, year) VALUES (?, ?, ?)
        ''', (book["title"], book["author"], book["year"]))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_book(self, book_id: int):
        self.cursor.execute('''
            SELECT * FROM books WHERE id = ?
        ''', (book_id,))
        return self.cursor.fetchone()

    def get_all_books(self):
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()

    def delete_book(self, book_id: int):
        self.cursor.execute('''
            DELETE FROM books WHERE id = ?
        ''', (book_id,))
        self.conn.commit()

    def update_book(self, book_id: int, new_data: dict):
        update_query = '''
            UPDATE books
            SET title = ?,
                author = ?,
                year = ?
            WHERE id = ?
        '''
        self.cursor.execute(update_query, (new_data["title"], new_data["author"], new_data["year"], book_id))
        self.conn.commit()