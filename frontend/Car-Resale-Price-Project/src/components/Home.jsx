import { Link } from "react-router-dom";
import "../assets/styles/Home.css";
function Home() {
  return (
    <div className="app">

      {/* Main Content */}
      <main className="hero-section">
        <div className="hero-content">

          <p className="hero-tag">
            AI POWERED CAR PRICE PREDICTION
          </p>

          <h1>
            Predict Your Car's
            <span>Resale Value</span>
          </h1>

          <p className="hero-description">
            Get an estimated resale price for your used car based on
            important vehicle details and machine learning.
          </p>

          {/* Prediction Card */}
          <div className="prediction-card">
            <div className="card-icon">🚗</div>

            <h2>Car Price Prediction</h2>

            <p>
              Enter your car details and get an estimated resale value
              powered by machine learning.
            </p>

            <Link to="/prediction" className="prediction-btn">
              Predict Your Car Value
            </Link>
          </div>

        </div>
      </main>
    </div>
  );
}

export default Home;