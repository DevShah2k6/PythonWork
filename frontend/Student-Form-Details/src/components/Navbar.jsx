import { Link } from "react-router-dom";
import "../assets/style/navbar.css";

function Navbar() {
    return (
        <nav className="navbar">
            <h2 className="navbar-logo">Student Management</h2>

            <div className="navbar-links">
                <Link to="/">Home</Link>
                <Link to="/add-student">Add Student</Link>
                <Link to="/students">View Students</Link>
            </div>
        </nav>
    );
}

export default Navbar;