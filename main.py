#python -m uvicorn main:app --reload  
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import Database
from book_service import BookService
from typing import Dict

app = FastAPI()
db_instance = Database('books.db')
book_service = BookService(db_instance)

class Book(BaseModel):
    title: str
    author: str
    year: int

# Kitap eklemek için POST isteği
@app.post("/add_book")
async def add_book(book: Book):
    book_data = book.dict()
    book_id = book_service.add_book(book_data)
    return {"message": "Book added successfully", "book_id": book_id}

# Belirli bir kitabın özelliklerini görüntülemek için GET isteği
@app.get("/get_book/{book_id}")
async def get_book(book_id: int):
    return book_service.get_book(book_id)

# Tüm kitapları görüntülemek için GET isteği
@app.get("/get_all_books")
async def get_all_books():
    return {"books": book_service.get_all_books()}

# Kitap silme
@app.delete("/delete_book/{book_id}")
async def delete_book(book_id: int):
    book_service.delete_book(book_id)
    return {"message": "Book deleted successfully"}

# Kitap güncelleme
@app.put("/update_book/{book_id}")
async def update_book(book_id: int, new_data: Book):
    book_service.update_book(book_id, new_data.dict())
    return {"message": "Book updated successfully"}
