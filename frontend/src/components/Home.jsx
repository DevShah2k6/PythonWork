import { Link } from "react-router-dom";
import "../assets/styles/Home.css";

function Home() {
  return (
    <div className="library-home">

      <div className="library-home-card">

        <h1 className="library-home-title">
          Library Management System
        </h1>

        <p className="library-home-subtitle">
          Manage books, authors and collections easily
        </p>

        <div className="library-home-buttons">

          <Link
            className="library-home-btn add-book-btn"
            to="/add-book"
          >
            Add Book
          </Link>


          <Link
            className="library-home-btn view-book-btn"
            to="/viewbooks"
          >
            View Books
          </Link>

        </div>

      </div>

    </div>
  );
}

export default Home;