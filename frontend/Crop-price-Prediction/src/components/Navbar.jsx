import { Link } from "react-router-dom";
import "../assets/styles/Navbar.css";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        CropPrice
      </div>

      <div className="navbar-links">
        <Link to="/">Home</Link>
        <Link to="/predict">Predict</Link>
        <Link to="/about">About</Link>
      </div>
    </nav>
  );
}

export default Navbar;