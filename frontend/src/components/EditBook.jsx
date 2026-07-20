import { useState } from "react";
import BookForm from "../assets/books/BookForm";
import { useLocation, useNavigate } from "react-router-dom";
import { EditBook as EditBookAPI } from "../api/api.js";
import "../assets/styles/EditBook.css";

function EditBook({ handleEditBook }) {

    const location = useLocation();
    const navigate = useNavigate();

    const [error, SetError] = useState("");

    
    async function handleSubmit(updatedBook) { 

        

        let errors = [];


        if (updatedBook.bookname.trim() === "") {
            errors.push("Book Name is Required");
        }
        else if (!/^[A-Za-z ]+$/.test(updatedBook.bookname)) {
            errors.push("Book Name Should contain names only");
        }


        if (updatedBook.authorname.trim() === "") {
            errors.push("Author Name is Required");
        }
        else if (!/^[A-Za-z ]+$/.test(updatedBook.authorname)) {
            errors.push("Author Name Should contain names only");
        }


        if (updatedBook.category.trim() === "") {
            errors.push("Category is Required");
        }
        else if (!/^[A-Za-z ]+$/.test(updatedBook.category)) {
            errors.push("Category Should contain names only");
        }


        if (updatedBook.quantity.toString().trim() === "") {
            errors.push("Quantity is Required");
        }
        else if (!/^[0-9]+$/.test(updatedBook.quantity)) {
            errors.push("Quantity contains number only");
        }
        else if (Number(updatedBook.quantity) < 0) {
            errors.push("Invalid Quantity");
        }


        if (errors.length > 0) {
            SetError(errors.join(", "));
            return;
        }
    await EditBookAPI(location.state.book.id, updatedBook);
    handleEditBook({
        ...updatedBook,
        id: location.state.book.id,
        quantity: Number(updatedBook.quantity)
    });

    navigate("/viewbooks");

    }
    return (
        <div className="editbook-page">

            <a href="/" className="editbook-home">
                Home page
            </a>


            <div className="editbook-card">

                <h2 className="editbook-title">
                    Update Book
                </h2>


                {error && (
                    <p className="error-message">
                        {error}
                    </p>
                )}

<BookForm
    editData={location.state.book}
    onSubmit={handleSubmit}
    title = "Update Book"
    buttonText = "Update"
/>
            </div>

        </div>
    );
}

export default EditBook