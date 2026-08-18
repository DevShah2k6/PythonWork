// import { uploadFile } from "../api/api";
import "../assets/styles/UploadFile.css";
import { useState } from "react";
import { uploadFile } from "../api/api";
import ReceiptForm from "../components/ReceiptForm";

function UploadFile(){
 const [file, setFile] = useState(null);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const handleUpload = async () => {
            if (!file) {
        alert("Please select a PDF first.");
        return;
    }
    const formData = new FormData();
    formData.append("file", file);

        
    try {
        setLoading(true);
        setError(""); 

        const data = await uploadFile(formData);

        setResult(data);

    } catch (error) {
        setError("File processing failed. Please try again.");
    }
    finally {
        setLoading(false);
    }
    };

    return (
        <div>
            <div className="upload-container">
                <div className="upload-card">
                <h1>Receipt OCR</h1>

                <input
  type="file"
  accept="application/pdf"
  onChange={(e) => setFile(e.target.files[0])}
/>

                <button onClick={handleUpload}>Upload</button>

                {/* Processing status */}
        {loading && (
            <div className="status">
                <p>🔄 Processing your document...</p>
            </div>
        )}

        {/* Error message */}
        {error && (
            <div className="error">
                <p>{error}</p>
            </div>
        )}
                {result && (
          <pre>
            {JSON.stringify(result, null, 2)}
          </pre>
        )}
        </div>
                </div>
        </div>
    )
}
export default UploadFile;