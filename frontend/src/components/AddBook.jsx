import { useState } from "react";
import "../assets/styles/AddBook.css";
import { Navigate } from "react-router-dom";
import { AddBooks } from "../api/api.js";
import BookForm from "../assets/books/BookForm.jsx";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
function AddBook({handleAddBook}){
const [submitted,SetSubmitted] = useState(false)
const navigate = useNavigate();
const [book, setBook] = useState({
    bookname: "",
    authorname: "",
    category: "",
    quantity: ""
});
function handleChange(e) {
    setBook({
        ...book,
        [e.target.name]: e.target.value
    });
}

async function SubmitBook(bookData) {
    console.log(bookData);

    try {
        const response = await AddBooks(bookData);
        console.log(response);

        handleAddBook(response);
        navigate("/viewbooks");
    } catch (error) {
        console.log(error);
    }
}


    // if (submitted){
    //     return <Navigate to="/viewbooks"/>
    // }
    // return (
    //     <BookForm onSubmit={SubmitBook} />
    // )
return (
    <div className="addbook-page">

        <a href="/" className="addbook-home">
            Home Page
        </a>

        <div className="addbook-card">

            <h2 className="addbook-title">
                Book Details
            </h2>

            <BookForm onSubmit={SubmitBook} title="Add Book" buttonText = "Add Book"/>

        </div>

    </div>
)
}
export default AddBook