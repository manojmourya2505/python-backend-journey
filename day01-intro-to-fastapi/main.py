"""Day 1 - What is FastAPI? Your first API in 5 minutes.

Run it:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload

Then open:
    http://127.0.0.1:8000/books   -> the JSON response
    http://127.0.0.1:8000/docs    -> interactive API docs (Swagger UI)
"""
from fastapi import FastAPI

app = FastAPI(title="Day 1 - My First API")

BOOKS = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 3, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
]


@app.get("/")
def home():
    """A simple welcome message."""
    return {"message": "Hello from FastAPI! Try /books or /docs"}


@app.get("/books")
def get_books():
    """Return every book. FastAPI turns this Python list into JSON."""
    return BOOKS
