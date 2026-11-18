import { useState } from "react";

function CarForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    brand: "",
    model: "",
    year: "",
    fuelType: "",
    transmission: "",
    kmDriven: "",
    ownerType: "",
    mileage: "",
    engineCC: "",
    conditionRating: "",
    originalPrice: "",
    daysToSell: "",
    carAge: "",
    demandScore: "",
    brandPopularityScore: "",
    premiumCar: "",
  });
  const [errors, setErrors] = useState({});
  function handleChange(e) {
    const { name, value } = e.target;

    setFormData({
      ...formData,
      [name]: value,
    });
  }

function handleSubmit(e) {
  e.preventDefault();

  const errors = {};

  // Required fields
  Object.entries(formData).forEach(([key, value]) => {
    if (!value) {
      errors[key] = "This field is required";
    }
  });

  // Numeric validations
  if (formData.year && (Number(formData.year) < 1900 || Number(formData.year) > 2026)) {
    errors.year = "Enter a valid year";
  }

  if (formData.kmDriven && Number(formData.kmDriven) < 0) {
    errors.kmDriven = "KM Driven cannot be negative";
  }

  if (formData.mileage && Number(formData.mileage) <= 0) {
    errors.mileage = "Mileage must be greater than 0";
  }

  if (formData.engineCC && Number(formData.engineCC) <= 0) {
    errors.engineCC = "Engine CC must be greater than 0";
  }

  if (
    formData.conditionRating &&
    (Number(formData.conditionRating) < 1 ||
      Number(formData.conditionRating) > 5)
  ) {
    errors.conditionRating = "Rating must be between 1 and 5";
  }

  if (formData.originalPrice && Number(formData.originalPrice) <= 0) {
    errors.originalPrice = "Price must be greater than 0";
  }

  if (formData.daysToSell && Number(formData.daysToSell) < 0) {
    errors.daysToSell = "Days to sell cannot be negative";
  }

  if (formData.carAge && Number(formData.carAge) < 0) {
    errors.carAge = "Car age cannot be negative";
  }

  if (
    formData.demandScore &&
    (Number(formData.demandScore) < 1 ||
      Number(formData.demandScore) > 5)
  ) {
    errors.demandScore = "Demand score must be between 1 and 5";
  }

  if (
    formData.brandPopularityScore &&
    (Number(formData.brandPopularityScore) < 1 ||
      Number(formData.brandPopularityScore) > 10)
  ) {
    errors.brandPopularityScore =
      "Brand popularity score must be between 1 and 10";
  }

  setErrors(errors);

if (Object.keys(errors).length > 0) {
  return;
}

onSubmit(formData);
}
  return (
    <form className="prediction-form" onSubmit={handleSubmit}>

      <div className="form-group">
        <label>Brand</label>
        <select name="brand" value={formData.brand} onChange={handleChange}>
          <option value="">Select brand</option>
          <option>Honda</option>
          <option>Hyundai</option>
          <option>Kia</option>
          <option>Mahindra</option>
          <option>Maruti</option>
          <option>Renault</option>
          <option>Tata</option>
          <option>Toyota</option>
          <option>Other</option>
        </select>
      </div>
        {errors.brand && (
      <p className="error-message">{errors.brand}</p>
        )}
      <div className="form-group">
        <label>Model</label>
        <select name="model" value={formData.model} onChange={handleChange}>
          <option value="">Select model</option>
          <option>Altroz</option>
          <option>Amaze</option>
          <option>Baleno</option>
          <option>Brezza</option>
          <option>Carens</option>
          <option>City</option>
          <option>Creta</option>
          <option>Dzire</option>
          <option>Fortuner</option>
          <option>Glanza</option>
          <option>Harrier</option>
          <option>Innova</option>
          <option>Jazz</option>
          <option>Kiger</option>
          <option>Kwid</option>
          <option>Nexon</option>
          <option>Punch</option>
          <option>Scorpio</option>
          <option>Seltos</option>
          <option>Sonet</option>
          <option>Swift</option>
          <option>Thar</option>
          <option>Triber</option>
          <option>Venue</option>
          <option>Verna</option>
          <option>XUV700</option>
          <option>i20</option>
          <option>Other</option>
        </select>
      </div>
          {errors.model && (
      <p className="error-message">{errors.model}</p>
        )}
      <div className="form-group">
        <label>Year</label>
        <input name="year" value={formData.year} onChange={handleChange} placeholder="Enter manufacturing year" />
      </div>
      {errors.year && (
      <p className="error-message">{errors.year}</p>
        )}
      <div className="form-group">
        <label>Fuel Type</label>
        <select name="fuelType" value={formData.fuelType} onChange={handleChange}>
          <option value="">Select fuel type</option>
          <option>CNG</option>
          <option>Diesel</option>
          <option>Petrol</option>
          <option>Other</option>
        </select>
      </div>
        {errors.fuelType && (
      <p className="error-message">{errors.fuelType}</p>
        )}

      <div className="form-group">
        <label>Transmission</label>
        <select name="transmission" value={formData.transmission} onChange={handleChange}>
          <option value="">Select transmission</option>
          <option>Automatic</option>
          <option>Manual</option>
        </select>
      </div>
      {errors.transmission && (
      <p className="error-message">{errors.transmission}</p>
        )}

      <div className="form-group">
        <label>KM Driven</label>
        <input name="kmDriven" value={formData.kmDriven} onChange={handleChange} placeholder="Enter KM driven" />
      </div>
      {errors.transmission && (
      <p className="error-message">{errors.transmission}</p>
        )}
      

      <div className="form-group">
        <label>Owner Type</label>
        <select name="ownerType" value={formData.ownerType} onChange={handleChange}>
          <option value="">Select owner type</option>
          <option>First</option>
          <option>Second</option>
          <option>Third</option>
        </select>
      </div>
{errors.transmission && (
      <p className="error-message">{errors.transmission}</p>
        )}
      <div className="form-group">
        <label>Mileage</label>
        <input name="mileage" value={formData.mileage} onChange={handleChange} placeholder="Enter mileage" />
      </div>
{errors.mileage && (
      <p className="error-message">{errors.mileage}</p>
        )}
      <div className="form-group">
        <label>Engine CC</label>
        <input name="engineCC" value={formData.engineCC} onChange={handleChange} placeholder="Enter engine CC" />
      </div>
{errors.engineCC && (
      <p className="error-message">{errors.engineCC}</p>
        )}
      <div className="form-group">
        <label>Condition Rating</label>
        <input name="conditionRating" value={formData.conditionRating} onChange={handleChange} placeholder="Enter condition rating" />
      </div>
{errors.conditionRating && (
      <p className="error-message">{errors.conditionRating}</p>
        )}
      <div className="form-group">
        <label>Original Price</label>
        <input name="originalPrice" value={formData.originalPrice} onChange={handleChange} placeholder="Enter original price" />
      </div>
{errors.originalPrice && (
      <p className="error-message">{errors.originalPrice}</p>
        )}
      <div className="form-group">
        <label>Days to Sell</label>
        <input name="daysToSell" value={formData.daysToSell} onChange={handleChange} placeholder="Enter days to sell" />
      </div>
{errors.daysToSell && (
      <p className="error-message">{errors.daysToSell}</p>
        )}
      <div className="form-group">
        <label>Car Age</label>
        <input name="carAge" value={formData.carAge} onChange={handleChange} placeholder="Enter car age" />
      </div>
{errors.carAge && (
      <p className="error-message">{errors.carAge}</p>
        )}
      <div className="form-group">
        <label>Demand Score</label>
        <input name="demandScore" value={formData.demandScore} onChange={handleChange} placeholder="Enter demand score" />
      </div>
{errors.demandScoree && (
      <p className="error-message">{errors.demandScore}</p>
        )}
      <div className="form-group">
        <label>Brand Popularity Score</label>
        <input
          name="brandPopularityScore"
          value={formData.brandPopularityScore}
          onChange={handleChange}
          placeholder="Enter brand popularity score"
        />
      </div>
{errors.brandPopularityScore && (
      <p className="error-message">{errors.brandPopularityScore}</p>
        )}
      <div className="form-group">
        <label>Premium Car</label>
        <select name="premiumCar" value={formData.premiumCar} onChange={handleChange}>
          <option value="">Select premium status</option>
          <option>Yes</option>
          <option>No</option>
        </select>
      </div>
    {errors.premiumCar && (
      <p className="error-message">{errors.premiumCar}</p>
        )}
      <div className="form-submit">
        <button type="submit">Predict Resale Value</button>
      </div>

    </form>
  );
}

export default CarForm;