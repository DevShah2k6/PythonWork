import { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { GetBooks, DeleteBook as DeleteBookApi } from "./api/api.js";

import "./App.css";

import AddBook from "./components/AddBook";
import ViewBook from "./components/ViewBook";
import EditBook from "./components/EditBook";
import Home from "./components/Home";


function App() {

    const [books, SetBooks] = useState([]);


    // Get all books
    useEffect(() => {

        async function fetchBooks() {

            const data = await GetBooks();

            SetBooks(data);
        }

        fetchBooks();

    }, []);



    // Add book
    function handleAddBook(newBook) {

        SetBooks((prevBooks) => [
            ...prevBooks,
            newBook
        ]);
    }



    // Edit book
   function handleEditBook(updatedBook) {

    console.log("EDIT DATA RECEIVED IN APP:", updatedBook);

    SetBooks((prevBooks) => {
        const updated = prevBooks.map((book) =>
            book.id === updatedBook.id
                ? updatedBook
                : book
        );

        console.log("NEW BOOK ARRAY:", updated);

        return updated;
    });
}


    // Delete book
    async function handleDeleteBook(id) {

        await DeleteBookApi(id);

        SetBooks((prevBooks) =>
            prevBooks.filter(
                (book) => book.id !== id
            )
        );
    }



    return (

        <BrowserRouter>

            <Routes>

                <Route 
                    path="/" 
                    element={<Home />} 
                />


                <Route
                    path="/add-book"
                    element={
                        <AddBook 
                            handleAddBook={handleAddBook}
                        />
                    }
                />


                <Route
                    path="/edit-book/:id"
                    element={
                        <EditBook 
                            handleEditBook={handleEditBook}
                        />
                    }
                />


                <Route
                    path="/viewbooks"
                    element={
                        <ViewBook
                            books={books}
                            handleDeleteBook={handleDeleteBook}
                        />
                    }
                />


            </Routes>

        </BrowserRouter>

    );
}

export default App;
