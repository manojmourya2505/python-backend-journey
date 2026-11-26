"""Day 2 - Path & Query Parameters.

Run it:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload

Then try:
    http://127.0.0.1:8000/books/2              -> one book (path parameter)
    http://127.0.0.1:8000/books/abc            -> 422 error, FastAPI validates the int for you
    http://127.0.0.1:8000/books?author=james   -> filtered list (query parameter)
    http://127.0.0.1:8000/docs                 -> interactive docs
"""
from fastapi import FastAPI

app = FastAPI(title="Day 2 - Path & Query Parameters")

BOOKS = [
    {"id": 1, "title": "Clean Code", "author": "Robert Martin"},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 3, "title": "Deep Work", "author": "Cal Newport"},
]


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Path parameter: {book_id} comes from the URL and is converted to an int."""
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}


@app.get("/books")
def get_books(author: str | None = None):
    """Query parameter: not in the path, so FastAPI reads it from ?author=...  Optional (default None)."""
    if author:
        return [b for b in BOOKS if author.lower() in b["author"].lower()]
    return BOOKS
