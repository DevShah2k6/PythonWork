import { useState } from "react"
import { Link, useNavigate } from "react-router-dom"
import "../styles/BookForm.css";
import { useEffect } from "react";
function BookForm({editData, handleChange, handleSubmit, onSubmit,title,buttonText}){
console.log("edit data", editData);
 const navigate = useNavigate();
   const [bookData, SetBook] = useState(
      editData || {
        bookname:"",
        authorname:"",
        category:"",
        quantity:""
      }
   );
   useEffect(() => {
    if(editData){
        SetBook(editData);
    }
}, [editData]);
    function handleChange(e){
        SetBook({
            ...bookData,[e.target.name]:e.target.value
        })
        SetError("")
    }
    const [error, SetError] = useState("");

async function handleSubmit(e) {
    let errors = [];
    console.log("Submit clicked", bookData);
    e.preventDefault();

    if (bookData.bookname.trim() === "") {
        errors.push("Book Name is Required");
    }
    else if (!/^[A-Za-z ]+$/.test(bookData.bookname)) {
        errors.push("Book Name Should contain names only");
    }

    if (bookData.authorname.trim() === "") {
        errors.push("Author Name is Required");
    }
    else if (!/^[A-Za-z ]+$/.test(bookData.authorname)) {
        errors.push("Author Name Should contain names only");
    }

    if (bookData.category.trim() === "") {
        errors.push("Category is Required");
    }
    else if (!/^[A-Za-z ]+$/.test(bookData.category)) {
        errors.push("Category Should contain names only");
    }
    if (String(bookData.quantity).trim() === "") {
        errors.push("Quantity is Required");
    }
    else if (!/^[0-9]+$/.test(bookData.quantity)) {
        errors.push("Quantity contains number only");
    }
    else if (Number(bookData.quantity) < 0) {
        errors.push("Invalid Quantity");
    }

    if (errors.length > 0) {
        SetError(errors.join(", "));
        return;
    }
if(onSubmit){
    onSubmit({
        ...bookData,
        quantity: Number(bookData.quantity)
    });
}
else{
    console.log("onSubmit is missing");
}
navigate("/viewbooks");
}
 return (
        <div className="addbook-page">

            <Link 
                to="/"
                className="addbook-home"
            >
                Home Page
            </Link>


            <div className="addbook-container">

                <h2>Book Details</h2>

                <h1>{title}</h1>


                <form className="addbook-form" onSubmit={handleSubmit}>
                    <p className="error-text">{error}</p>
                    <div className="form-group">
                        <label>Book Title</label>
                        <input type="text" name="bookname" value={bookData.bookname}
    onChange={handleChange}/>
                    </div>


                    <div className="form-group">
                        <label>Author Name</label>
                        <input type="text" name="authorname" value={bookData.authorname}
    onChange={handleChange}/>
                    </div>


                    <div className="form-group">
                        <label>Category</label>
                        <select name="category"
    value={bookData.category}
    onChange={handleChange}>
                            <option>Select Category</option>
                            <option>Fiction</option>
                            <option>Technology</option>
                            <option>History</option>
                        </select>
                    </div>


                    <div className="form-group">
                        <label>Quantity</label>
                        <input type="text" name="quantity" value={bookData.quantity}
    onChange={handleChange}/>
                    </div>


                    <button type="submit"className="addbook-btn">
                        {buttonText}
                    </button>

                </form>

            </div>

        </div>
    )
}
export default BookForm