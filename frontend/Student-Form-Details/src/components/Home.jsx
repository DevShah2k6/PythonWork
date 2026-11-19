import { useNavigate } from "react-router-dom";
import "../assets/style/home.css";
import Navbar from "./Navbar";
function Home() {
  const navigate = useNavigate();

  return (
    <>
    <Navbar />
    <div className="home-container">
      <div className="home-card">
        <div className="home-header">
          <h1>Student Management System</h1>
          <p>
            Manage student records quickly, efficiently, and securely.
          </p>
        </div>

        <div className="home-actions">
          <button
            className="home-button primary-button"
            onClick={() => navigate("/add-student")}
          >
            <span className="button-icon">+</span>
            <span>
              <strong>Add Student</strong>
              <small>Create a new student record</small>
            </span>
          </button>

          <button
            className="home-button secondary-button"
            onClick={() => navigate("/students")}
          >
            <span className="button-icon">☰</span>
            <span>
              <strong>View Students</strong>
              <small>View and manage student records</small>
            </span>
          </button>
        </div>
      </div>
    </div>
    </>
  );
}

export default Home;