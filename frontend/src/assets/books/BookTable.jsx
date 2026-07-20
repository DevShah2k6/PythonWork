import "../styles/BookTable.css";
import { Link } from "react-router-dom";
function BookTable({books,handleDeleteBook}){
console.log("---",books);
    return (
        <div className="booktable-wrapper">
            <div>
                <table className="booktable">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Book Name</th>
                        <th>Author Name</th>
                        <th>Category</th>
                        <th>Quantity</th>
                         <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
    books?.map((book, index) => (
        <tr key={index}>
            <td>{index + 1}</td>
            <td>{book.bookname}</td>
            <td>{book.authorname}</td>
            <td>{book.category}</td>
            <td>{book.quantity}</td>
            <td>
           <Link className="book-edit-btn"
  to={`/edit-book/${book.id}`} 
  state={{ book:book }}
>
  Edit
</Link>
            <button 
                className="book-delete-btn"
                onClick={() => handleDeleteBook(book.id)}>
                Delete
                </button>
                </td>

        </tr>
    ))
}
</tbody>
                </table>
            </div>
        </div>
    )
}
export default BookTable