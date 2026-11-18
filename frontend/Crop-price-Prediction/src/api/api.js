const API_URL = "http://127.0.0.1:8000";

export const predictCropPrice = async (formData) => {
  const response = await fetch(`${API_URL}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  });

  if (!response.ok) {
    throw new Error("Prediction request failed");
  }

  return response.json();
};
export const getDistricts = async (state) => {
  const response = await fetch(
    `${API_URL}/districts?state=${state}`
  );

  return response.json();
};
export const getStates = async () => {
  const response = await fetch(
    `${API_URL}/states`
  );

  return response.json();
};
export const getMarkets = async (state, district) => {
  const response = await fetch(
    `${API_URL}/markets?state=${state}&district=${district}`
  );

  return response.json();
};
export const getCommodities = async (state, district, market) => {
  const response = await fetch(
    `${API_URL}/commodities?state=${state}&district=${district}&market=${market}`
  );

  return response.json();
};
export const getVarieties = async (state, district, market,commodity) => {
  const response = await fetch(
    `${API_URL}/variety?state=${state}&district=${district}&market=${market}&commodity=${commodity}`
  );

  return response.json();
};
export const getGrades = async (state, district, market, commodity, variety) => {
  const response = await fetch(
    `${API_URL}/grades?state=${state}&district=${district}&market=${market}&commodity=${commodity}&variety=${variety}`
  );

  return response.json();
};
export const getModelPerformace = async () => {
  const response = await fetch(
     `${API_URL}/model-performance`
  );

  return response.json();
};