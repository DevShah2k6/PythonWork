from sqlalchemy.orm import Session
from schemas import BookCreate,BookResponse
from models import Book

#as book is sqlalchmey model so it is written and data is apssed to save into the database

def create_book(db:Session ,book:BookCreate):
    new_book = Book(
    bookname=book.bookname,
    authorname=book.authorname,
    category=book.category,
    quantity=book.quantity
)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

def get_books(db:Session):
    books = db.query(Book).all()
    return books

def update_books(db:Session,id:int,bookname:str,authorname:str,category:str,quantity:int):
    book_update = db.query(Book).filter(Book.id == id).first()
    book_update.bookname = bookname
    book_update.authorname = authorname
    book_update.category = category
    book_update.quantity=quantity

    db.commit()
    db.refresh(book_update)
    return book_update

def delete_book(db:Session,id:int):
  deleted_book = db.query(Book).filter(Book.id == id).first()
  db.delete(deleted_book)
  db.commit()

