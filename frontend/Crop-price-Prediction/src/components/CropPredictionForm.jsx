import { useState, useEffect } from "react";
import "../assets/styles/CropPrediction.css";

import {
  predictCropPrice,
  getStates,
  getDistricts,
  getMarkets,
  getCommodities,
  getVarieties,
  getGrades,
  getModelPerformace
} from "../api/api";

function CropPredictionForm() {

  const [loading, setLoading] = useState(false);

  const [formData, setFormData] = useState({
    State: "",
    District: "",
    Market: "",
    Commodity: "",
    Variety: "",
    Grade: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [errors, setErrors] = useState({});

  // Dynamic dropdown states
  const [states, setStates] = useState([]);
  const [districts, setDistricts] = useState([]);
  const [markets, setMarkets] = useState([]);
  const [commodities, setCommodities] = useState([]);
  const [variety, setVariety] = useState([]);
  const [grades, setGrades] = useState([]);
  const [modelPerformance, setModelPerformance] = useState(null);
  // FETCH STATES
  useEffect(() => {

    const fetchStates = async () => {
      const result = await getStates();
      setStates(result.states || []);
    };

    fetchStates();

  }, []);
useEffect(() => {

  const fetchModelPerformance = async () => {
    const result = await getModelPerformace();
    setModelPerformance(result);
  };

  fetchModelPerformance();

}, []);
  // HANDLE CHANGE
  const handleChange = async (e) => {

    const { name, value } = e.target;

    // STATE
    if (name === "State") {

      setFormData({
        ...formData,
        State: value,
        District: "",
        Market: "",
        Commodity: "",
        Variety: "",
        Grade: "",
      });

      setDistricts([]);
      setMarkets([]);
      setCommodities([]);
      setVariety([]);
      setGrades([]);

      setErrors({
        ...errors,
        State: "",
        District: "",
        Market: "",
        Commodity: "",
        Variety: "",
        Grade: "",
      });

      if (value) {
        const result = await getDistricts(value);
        setDistricts(result.districts || []);
      }

      return;
    }

    // DISTRICT
    if (name === "District") {

      setFormData({
        ...formData,
        District: value,
        Market: "",
        Commodity: "",
        Variety: "",
        Grade: "",
      });

      setMarkets([]);
      setCommodities([]);
      setVariety([]);
      setGrades([]);

      setErrors({
        ...errors,
        District: "",
        Market: "",
        Commodity: "",
        Variety: "",
        Grade: "",
      });

      if (value) {

        const result = await getMarkets(
          formData.State,
          value
        );

        setMarkets(result.markets || []);
      }

      return;
    }

    // MARKET
    if (name === "Market") {

      setFormData({
        ...formData,
        Market: value,
        Commodity: "",
        Variety: "",
        Grade: "",
      });

      setCommodities([]);
      setVariety([]);
      setGrades([]);

      setErrors({
        ...errors,
        Market: "",
        Commodity: "",
        Variety: "",
        Grade: "",
      });

      if (value) {

        const result = await getCommodities(
          formData.State,
          formData.District,
          value
        );

        setCommodities(result.commodities || []);
      }

      return;
    }

    // COMMODITY
    if (name === "Commodity") {

      setFormData({
        ...formData,
        Commodity: value,
        Variety: "",
        Grade: "",
      });

      setVariety([]);
      setGrades([]);

      setErrors({
        ...errors,
        Commodity: "",
        Variety: "",
        Grade: "",
      });

      if (value) {

        const result = await getVarieties(
          formData.State,
          formData.District,
          formData.Market,
          value
        );

        setVariety(result.varieties || []);
      }

      return;
    }

    // VARIETY
    if (name === "Variety") {

      setFormData({
        ...formData,
        Variety: value,
        Grade: "",
      });

      setGrades([]);

      setErrors({
        ...errors,
        Variety: "",
        Grade: "",
      });

      if (value) {

        const result = await getGrades(
          formData.State,
          formData.District,
          formData.Market,
          formData.Commodity,
          value
        );

        setGrades(result.grades || []);
      }

      return;
    }

    // OTHER FIELDS
    setFormData({
      ...formData,
      [name]: value,
    });

    if (errors[name]) {

      setErrors({
        ...errors,
        [name]: "",
      });

    }
  };

  // VALIDATION
  const validateForm = () => {

    const newErrors = {};

    Object.keys(formData).forEach((field) => {

      const value = formData[field].trim();

      if (value === "") {
        newErrors[field] = "This field is required";
        return;
      }

      if (!/^[a-zA-Z0-9\s&().,'/-]+$/.test(value)) {
        newErrors[field] = "Please enter a valid value";
      }

    });

    setErrors(newErrors);

    return Object.keys(newErrors).length === 0;
  };

  // SUBMIT
  const handleSubmit = async (e) => {

    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    setLoading(true);
    setPrediction(null);

    try {

      const result = await predictCropPrice(formData);

      setPrediction(result);

    } finally {

      setLoading(false);
    }
  };

  // JSX
  return (

    <main className="prediction-page">

      <section className="prediction-container">

        {/* HEADER */}

        <div className="prediction-header">

          <span>🌱 CROP PRICE PREDICTION</span>

          <h1>Enter Mandi Details</h1>

          <p>
            Provide market and commodity information to estimate
            the modal crop price.
          </p>

        </div>

        {/* FORM */}

        <form
          onSubmit={handleSubmit}
          className="prediction-form"
        >

          {/* MARKET INFORMATION */}

          <div className="form-section">

            <h2>📍 Market Information</h2>

            <div className="form-grid">

              {/* STATE */}

              <div className="form-group">

                <label>State</label>

                <select
                  name="State"
                  value={formData.State}
                  onChange={handleChange}
                  disabled={states.length === 0}
                >

                  <option value="">
                    {states.length > 0
                      ? "Select State"
                      : "No States Available"}
                  </option>

                  {states.map((state) => (

                    <option
                      key={state}
                      value={state}
                    >
                      {state}
                    </option>

                  ))}

                </select>

                {errors.State && (
                  <small>{errors.State}</small>
                )}

              </div>

              {/* DISTRICT */}

              <div className="form-group">

                <label>District</label>

                <select
                  name="District"
                  value={formData.District}
                  onChange={handleChange}
                  disabled={
                    !formData.State ||
                    districts.length === 0
                  }
                >

                  <option value="">
                    {!formData.State
                      ? "Select State First"
                      : districts.length > 0
                      ? "Select District"
                      : "No Districts Available"}
                  </option>

                  {districts.map((district) => (

                    <option
                      key={district}
                      value={district}
                    >
                      {district}
                    </option>

                  ))}

                </select>

                {errors.District && (
                  <small>{errors.District}</small>
                )}

              </div>

              {/* MARKET */}

              <div className="form-group">

                <label>Market</label>

                <select
                  name="Market"
                  value={formData.Market}
                  onChange={handleChange}
                  disabled={
                    !formData.District ||
                    markets.length === 0
                  }
                >

                  <option value="">
                    {!formData.District
                      ? "Select District First"
                      : markets.length > 0
                      ? "Select Market"
                      : "No Markets Available"}
                  </option>

                  {markets.map((market) => (

                    <option
                      key={market}
                      value={market}
                    >
                      {market}
                    </option>

                  ))}

                </select>

                {errors.Market && (
                  <small>{errors.Market}</small>
                )}

              </div>

            </div>

          </div>

          {/* COMMODITY INFORMATION */}

          <div className="form-section">

            <h2>🌾 Commodity Information</h2>

            <div className="form-grid">

              {/* COMMODITY */}

              <div className="form-group">

                <label>Commodity</label>

                <select
                  name="Commodity"
                  value={formData.Commodity}
                  onChange={handleChange}
                  disabled={
                    !formData.Market ||
                    commodities.length === 0
                  }
                >

                  <option value="">
                    {!formData.Market
                      ? "Select Market First"
                      : commodities.length > 0
                      ? "Select Commodity"
                      : "No Commodities Available"}
                  </option>

                  {commodities.map((commodity) => (

                    <option
                      key={commodity}
                      value={commodity}
                    >
                      {commodity}
                    </option>

                  ))}

                </select>

                {errors.Commodity && (
                  <small>{errors.Commodity}</small>
                )}

              </div>

              {/* VARIETY */}

              <div className="form-group">

                <label>Variety</label>

                <select
                  name="Variety"
                  value={formData.Variety}
                  onChange={handleChange}
                  disabled={
                    !formData.Commodity ||
                    variety.length === 0
                  }
                >

                  <option value="">
                    {!formData.Commodity
                      ? "Select Commodity First"
                      : variety.length > 0
                      ? "Select Variety"
                      : "No Varieties Available"}
                  </option>

                  {variety.map((item) => (

                    <option
                      key={item}
                      value={item}
                    >
                      {item}
                    </option>

                  ))}

                </select>

                {errors.Variety && (
                  <small>{errors.Variety}</small>
                )}

              </div>

              {/* GRADE */}

                    <div className="form-group">

        <label>Grade</label>

        <select
          name="Grade"
          value={formData.Grade}
          onChange={handleChange}
          disabled={
            !formData.Variety ||
            grades.length === 0
          }
        >
          <option value="">
            {!formData.Variety
              ? "Select Variety First"
              : grades.length > 0
              ? "Select Grade"
              : "No Grades Available"}
          </option>

          {grades.map((grade) => (
            <option key={grade} value={grade}>
              {grade}
            </option>
          ))}
        </select>

        {errors.Grade && (
          <small>{errors.Grade}</small>
        )}

      </div>

            </div>

          </div>

          {/* SUBMIT */}

          <button
            type="submit"
            className="predict-submit"
            disabled={loading}
          >

            {loading
              ? "Predicting..."
              : "Predict Modal Price"}

            <span>→</span>

          </button>

        </form>

        {/* RESULT */}

        {prediction !== null && (

          <div className="prediction-result">

            <h2>Estimated Modal Price</h2>

            <p>
              ₹{prediction.predicted_price} / quintal
            </p>

            <p>
              ₹{prediction.predicted_price_per_kg} / kg
            </p>

            <small>
              1 quintal = 100 kg
            </small>

          </div>
          

        )}
          {modelPerformance !== null && (

            <div className="model-performance">

              <h2>📊 Model Performance</h2>

              <div className="performance-grid">

                <div className="performance-item">
                  <span>Best Model</span>
                  <strong>{modelPerformance.best_model}</strong>
                </div>

                <div className="performance-item">
                  <span>Training R²</span>
                  <strong>{modelPerformance.train_r2.toFixed(4)}</strong>
                </div>

                <div className="performance-item">
                  <span>Testing R²</span>
                  <strong>{modelPerformance.test_r2.toFixed(4)}</strong>
                </div>

                <div className="performance-item">
                  <span>CV R²</span>
                  <strong>{modelPerformance.cv_r2.toFixed(4)}</strong>
                </div>

                <div className="performance-item">
                  <span>MAE</span>
                  <strong>{modelPerformance.mae.toFixed(4)}</strong>
                </div>

                <div className="performance-item">
                  <span>RMSE</span>
                  <strong>{modelPerformance.rmse.toFixed(4)}</strong>
                </div>

              </div>

            </div>

          )}
      </section>

    </main>
  );
}

export default CropPredictionForm;