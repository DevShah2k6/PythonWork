import axios from "axios";

const BASE_URL = "http://10.37.57.44:8000";


// Upload receipt image for OCR
export const uploadFile = async (formData) => {

  const response = await axios.post(
    `${BASE_URL}/upload`,
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};

// Update receipt form data after submit
export const updateReceipt = async (id, receiptData) => {
  const response = await axios.put(
    `${BASE_URL}/receipts/${id}`,
    receiptData
  );
  return response.data;
};

// Get receipts list (only if you need to open old receipts)
export const getReceipts = () => {
  return axios.get(`${BASE_URL}/receipts`);
};