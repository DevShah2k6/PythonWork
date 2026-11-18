import { useState } from 'react'
import Home from "./components/Home";
import CropPredictionForm from "./components/CropPredictionForm";
import './App.css'
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import Navbar from "./components/Navbar";
import About from './components/About';
function App() {
  return (
    
    <BrowserRouter>
     <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path='/about' element={<About />}/>
        <Route path="/predict" element={<CropPredictionForm />} />
      </Routes>
    </BrowserRouter>
  );
}


export default App
