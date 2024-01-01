from fastapi import HTTPException
from database import Database

class BookService:
    def __init__(self, database: Database):
        self.database = database

    def add_book(self, book_data: dict):
        return self.database.add_book(book_data)

    def get_book(self, book_id: int):
        book = self.database.get_book(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return {"book_id": book[0], "title": book[1], "author": book[2], "year": book[3]}

    def get_all_books(self):
        books = self.database.get_all_books()
        return [{"book_id": book[0], "title": book[1], "author": book[2], "year": book[3]} for book in books]

    def delete_book(self, book_id: int):
        self.database.delete_book(book_id)

    def update_book(self, book_id: int, new_data: dict):
        self.database.update_book(book_id, new_data)
