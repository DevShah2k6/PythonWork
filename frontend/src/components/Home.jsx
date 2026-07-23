
import "../assets/styles/Home.css";
import { Link } from "react-router-dom";
function Home(){
    return (
        <div className="home-container">
            <h1 className="home-title">Employee Management System</h1>
            <div className="home-actions">
                <Link  to="/add-employee">
                <button className="home-btn">Add Employee</button>
                </Link>
                
                <Link to="/viewemployee">
                <button className="home-btn">Show Employee Details</button>
                </Link>
            </div>
        </div>
    )
}
export default Home;