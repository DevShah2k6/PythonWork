import "../assets/styles/PredictionForm.css";
import CarForm from "./CarForm";
import { predictCar } from "../api/api";
import { useState } from "react";
function PredictionForm() {
  const [value, setValue] = useState(null);
  async function handlePrediction(data) {
    console.log(data);
    const response = await predictCar(data);
    setValue(response);
      // const [value, setValue] = useState(null);
    console.log("API response:", response);
}


  return (
    <div className="prediction-page">

      <main className="prediction-main">

        <div className="prediction-header">
          <p className="prediction-tag">AI POWERED PREDICTION</p>

          <h1>Predict Your Car's Resale Value</h1>

          <p className="prediction-description">
            Enter your car details below to get an estimated resale value
            powered by machine learning.
          </p>
        </div>

        <CarForm onSubmit={handlePrediction} />

      </main>
      {value && <h2>Predicted Price: ₹{value}</h2>}
      <footer className="prediction-footer">
        <p>© 2026 CarPredict. AI-powered car resale price prediction.</p>
      </footer>

    </div>
  );
}

export default PredictionForm;