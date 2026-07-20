import BookTable from "../assets/books/BookTable";
import "../assets/styles/ViewBook.css";
import { useState, useEffect } from "react";
import { GetBooks } from "../api/api";
function ViewBook({books=[],handleDeleteBook}){


//   useEffect(() => {
//         GetBooks();
//     }, []);




    
    return (
        <div className="viewbook-page">
            <a href="/">Home Page</a>
            <h1 className="viewbook-title"> Book List</h1>
            <div className="viewbook-table-container">
                <BookTable books={books} handleDeleteBook={handleDeleteBook} />
            </div>
        </div>
    ) 
}
export default ViewBook