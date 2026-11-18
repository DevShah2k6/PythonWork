import { Link } from "react-router-dom";
import "../assets/styles/Home.css";

function Home() {
  return (
    <main className="home">

      {/* Hero Section */}
      <section className="hero-section">

        <div className="hero-content">

          <div className="hero-badge">
            🌾 Machine Learning for Crop Prices
          </div>

          <h1>
            Predict Crop Prices
            <span> in Mandi</span>
          </h1>

          <p>
            Estimate the modal price of a crop in a selected mandi
            using state, district, market, commodity, variety and
            grade information.
          </p>

          <div className="hero-actions">

            <Link to="/predict" className="predict-btn">
              Predict Crop Price
              <span>→</span>
            </Link>

            <Link to="/about" className="learn-btn">
              Learn About Project
            </Link>

          </div>

          <div className="hero-highlights">

            <div>
              <strong>6</strong>
              <span>Input Parameters</span>
            </div>

            <div>
              <strong>1</strong>
              <span>Price to Predict</span>
            </div>

            <div>
              <strong>AGMARKNET</strong>
              <span>Mandi Data</span>
            </div>

          </div>

        </div>

        {/* Visual */}
        <div className="hero-visual">

          <div className="main-circle">
            <div className="circle-inner">
              🌾
            </div>
          </div>

          <div className="info-card soil-card">
            <div className="info-icon">🏪</div>

            <div>
              <strong>Mandi Details</strong>
              <span>State • District • Market</span>
            </div>
          </div>

          <div className="info-card weather-card">
            <div className="info-icon">🌱</div>

            <div>
              <strong>Crop Details</strong>
              <span>Commodity • Variety • Grade</span>
            </div>
          </div>

          <div className="price-card">
            <span>Estimated Mandi Price</span>
            <strong>₹ Crop Price</strong>
            <small>Powered by Machine Learning</small>
          </div>

        </div>

      </section>

      {/* Bottom Strip */}
      <section className="project-strip">

        <div className="strip-item">
          <span>01</span>

          <div>
            <strong>Select Mandi Details</strong>
            <p>
              Choose state, district and market
            </p>
          </div>
        </div>

        <div className="strip-line"></div>

        <div className="strip-item">
          <span>02</span>

          <div>
            <strong>Select Crop Details</strong>
            <p>
              Choose commodity, variety and grade
            </p>
          </div>
        </div>

        <div className="strip-line"></div>

        <div className="strip-item">
          <span>03</span>

          <div>
            <strong>Get Crop Price</strong>
            <p>
              Get the estimated modal price in the mandi
            </p>
          </div>
        </div>

      </section>

    </main>
  );
}

export default Home;