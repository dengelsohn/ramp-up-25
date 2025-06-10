from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

current_id = 0


class Book(BaseModel):
    title: str
    author: str
    year: int


class Stored_Book(BaseModel):
    title: str
    author: str
    year: int
    id: int


books = {}


@app.post("/books")
def create_book(new_book: Book):
    global current_id
    book_dict = {
        "title": new_book.title,
        "author": new_book.author,
        "year": new_book.year,
        "id": current_id,
    }
    books[current_id] = book_dict
    current_id += 1
    return current_id - 1


@app.get("/books")
def get_all_books():
    return [Stored_Book(**book) for book in books.values()]


@app.get("/books/{id}")
def get_book(id: int):
    if id in books.keys():
        return Stored_Book(**books[id])
    else:
        raise HTTPException(404, detail="Book not found.")


@app.put("/books/{id}")
def update_book(id: int, book: Book):
    if id not in books.keys():
        raise HTTPException(404, detail="Book not found.")
    else:
        updated_book = {
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "id": id,
        }
        books[id] = updated_book
        return {}


@app.delete("/books/{id}")
def delete_book(id: int):
    if id not in books.keys():
        raise HTTPException(404, detail="Book not found.")
    else:
        books.pop(id)
        return {}
