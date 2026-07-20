from pydantic import BaseModel

#Tbale Struture and validation in schemas.py
class BookCreate(BaseModel):
    bookname:str
    authorname:str
    category:str
    quantity:int

class BookResponse(BaseModel):
    id : int
    bookname:str
    authorname:str
    category:str
    quantity:int

    class Config:
        from_attributes = True