from fastapi import APIRouter,Depends
from database import get_db
import crud
import schemas 

from sqlalchemy.orm import Session


route = APIRouter()


@route.get("/books")
def getbooks(db:Session = Depends(get_db)):
    return crud.get_books(db)

@route.post("/add-books")
def create_book( book: schemas.BookCreate,db: Session = Depends(get_db)):
    return crud.create_book(db,book)

@route.put("/edit-books/{id}")
def update_book(id:int,book:schemas.BookCreate,db:Session = Depends(get_db)):
    return crud.update_books(db=db,id=id,bookname=book.bookname,authorname=book.authorname,category=book.category,quantity=book.quantity)

@route.delete("/delete-books/{id}")
def delete_book(id:int,db:Session = Depends(get_db)):
    return crud.delete_book(db=db,id=id)