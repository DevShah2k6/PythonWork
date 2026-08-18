import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import UploadFile from "./components/UploadFile";
import Navbar from "./components/Navbar";
import Receipts from "./pages/Receipts";

function App() {
  return (
    <BrowserRouter>

      <Navbar />

      <div className="app">

        <Routes>

          <Route path="/" element={<UploadFile />} />

          <Route path="/receipts" element={<Receipts />} />
        </Routes>

      </div>

    </BrowserRouter>
  );
}

export default App;