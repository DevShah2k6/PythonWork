
import "../assets/styles/About.css";
function About() {
  return (
    <div className="about-page">

      {/* Hero */}
      <section className="about-hero">
        <p className="about-tag">ABOUT THE PROJECT</p>

        <h1>
          Smart Car Resale
          <span>Price Prediction</span>
        </h1>

        <p className="about-intro">
          CarPredict is a machine learning based web application that
          estimates the resale value of used cars using important vehicle
          details and historical market data.
        </p>
      </section>

      {/* Project Overview */}
      <section className="about-section">
        <div className="section-heading">
          <p>PROJECT OVERVIEW</p>
          <h2>Making car price estimation smarter</h2>
        </div>

        <div className="about-grid">

          <div className="about-card">
            <div className="card-number">01</div>
            <h3>Machine Learning</h3>
            <p>
              The project uses regression algorithms to predict the
              estimated resale price of a used car.
            </p>
          </div>

          <div className="about-card">
            <div className="card-number">02</div>
            <h3>Vehicle Data</h3>
            <p>
              Prediction is based on details such as brand, model, year,
              fuel type, transmission, mileage and other car features.
            </p>
          </div>

          <div className="about-card">
            <div className="card-number">03</div>
            <h3>Easy Prediction</h3>
            <p>
              Users can enter their car details through a simple form and
              receive an estimated resale value.
            </p>
          </div>

        </div>
      </section>

      {/* Technology */}
      <section className="technology-section">
        <div className="section-heading">
          <p>TECHNOLOGY</p>
          <h2>Built with modern technologies</h2>
        </div>

        <div className="technology-list">
          <div className="technology-item">
            <strong>React</strong>
            <span>Frontend</span>
          </div>

          <div className="technology-item">
            <strong>FastAPI</strong>
            <span>Backend API</span>
          </div>

          <div className="technology-item">
            <strong>Python</strong>
            <span>Machine Learning</span>
          </div>

          <div className="technology-item">
            <strong>Scikit-learn</strong>
            <span>ML Models</span>
          </div>
        </div>
      </section>

      {/* Goal */}
      <section className="project-goal">
        <div>
          <p className="about-tag">PROJECT GOAL</p>

          <h2>
            Helping users make
            <span>better car decisions.</span>
          </h2>

          <p>
            CarPredict aims to provide a simple and data-driven way to
            estimate the resale value of used cars and make the pricing
            process easier for users.
          </p>
        </div>
      </section>

    </div>
  );
}

export default About;

