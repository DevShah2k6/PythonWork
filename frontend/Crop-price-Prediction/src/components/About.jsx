import "../assets/styles/About.css";

function About() {
  return (
    <main className="about-page">

      {/* About Hero */}
      <section className="about-hero">
        <span>ABOUT THE PROJECT</span>

        <h1>
          Crop Price
          <strong> Prediction</strong>
        </h1>

        <p>
          This project uses machine learning to estimate the modal price
          of a selected crop in a particular mandi using market and
          commodity information.
        </p>
      </section>


      {/* What is Modal Price */}
      <section className="modal-price-section">

        <div className="section-title">
          <span>WHAT IS MODAL PRICE?</span>
          <h2>Understanding the price predicted by the model</h2>
        </div>

        <div className="modal-price-content">

          <p>
            The <strong>Modal Price</strong> is the price that occurs
            most frequently for a particular commodity in a mandi
            on a given day.
          </p>

          <p>
            In simple words, it represents the commonly occurring
            market price for that crop in the selected mandi.
          </p>

          <div className="price-example">

            <h3>💡 Simple Example</h3>

            <p>
              Suppose tomatoes are recorded in a mandi at these prices:
            </p>

            <div className="example-prices">
              <span>₹1,800</span>
              <span>₹2,000</span>
              <span>₹2,000</span>
              <span>₹2,000</span>
              <span>₹2,200</span>
            </div>

            <p>
              Here, <strong>₹2,000</strong> is the modal price because
              it occurs most frequently.
            </p>

            <p>
              Therefore, if our model predicts <strong>₹2,000</strong>,
              it means the estimated modal price of the selected crop
              in the selected mandi is around ₹2,000.
            </p>

          </div>

        </div>

      </section>


      {/* How It Works */}
      <section className="how-section">

        <div className="section-title">
          <span>HOW IT WORKS</span>
          <h2>From mandi data to crop price prediction</h2>
        </div>

        <div className="how-grid">

          <div className="how-card">
            <span>01</span>

            <h3>Select Mandi Details</h3>

            <p>
              The system takes state, district and market information
              to identify the selected mandi.
            </p>
          </div>


          <div className="how-card">
            <span>02</span>

            <h3>Select Crop Details</h3>

            <p>
              The user selects the commodity, variety and grade
              for which the price needs to be estimated.
            </p>
          </div>


          <div className="how-card">
            <span>03</span>

            <h3>Generate Prediction</h3>

            <p>
              The trained machine learning model analyzes the selected
              information and estimates the modal crop price.
            </p>
          </div>

        </div>

      </section>


      {/* Input Parameters */}
      <section className="parameters-section">

        <div className="section-title">
          <span>INPUT PARAMETERS</span>
          <h2>Information used for price prediction</h2>
        </div>

        <div className="parameter-grid">

          <div className="parameter-card">
            <div>📍</div>

            <h3>State</h3>

            <p>
              The state where the selected agricultural market
              is located.
            </p>
          </div>


          <div className="parameter-card">
            <div>🏙️</div>

            <h3>District</h3>

            <p>
              The district associated with the selected mandi.
            </p>
          </div>


          <div className="parameter-card">
            <div>🏪</div>

            <h3>Market</h3>

            <p>
              The specific mandi where the crop is traded.
            </p>
          </div>


          <div className="parameter-card">
            <div>🌾</div>

            <h3>Commodity</h3>

            <p>
              The agricultural crop for which the price is being
              predicted.
            </p>
          </div>


          <div className="parameter-card">
            <div>🌱</div>

            <h3>Variety</h3>

            <p>
              The specific variety of the selected crop.
            </p>
          </div>


          <div className="parameter-card">
            <div>📋</div>

            <h3>Grade</h3>

            <p>
              The grade or quality category of the selected crop.
            </p>
          </div>

        </div>

      </section>


      {/* Prediction Example */}
      <section className="prediction-example-section">

        <div className="section-title">
          <span>PREDICTION EXAMPLE</span>
          <h2>How the crop price prediction works</h2>
        </div>

        <div className="prediction-example">

          <div className="example-inputs">

            <h3>Example Input</h3>

            <p><strong>State:</strong> Andhra Pradesh</p>
            <p><strong>District:</strong> Visakhapatnam</p>
            <p><strong>Market:</strong> Visakhapatnam APMC</p>
            <p><strong>Commodity:</strong> Tomato</p>
            <p><strong>Variety:</strong> Local</p>
            <p><strong>Grade:</strong> FAQ</p>

          </div>


          <div className="example-result">

            <span>ESTIMATED MODAL PRICE</span>

            <h2>₹2,519</h2>

            <p>
              For this example input, the model estimates the modal
              price of the selected crop in the selected mandi to be
              approximately ₹2,519.
            </p>

          </div>

        </div>

      </section>


      {/* Technology */}
      <section className="technology-section">

        <div className="technology-content">

          <span>TECHNOLOGY</span>

          <h2>
            Machine Learning for Crop Price Prediction
          </h2>

          <p>
            The project uses a regression-based machine learning approach
            to estimate the modal price of agricultural commodities.
            Multiple regression models are evaluated using cross-validation
            and the model with the best cross-validation performance is
            selected for prediction.
          </p>

          <div className="tech-list">
            <span>Python</span>
            <span>Pandas</span>
            <span>Scikit-learn</span>
            <span>React</span>
            <span>FastAPI</span>
          </div>

        </div>

      </section>

    </main>
  );
}

export default About;