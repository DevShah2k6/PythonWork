// import { useState } from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css'
import Home from "./components/Home";
import StudentForm from "./components/StudentForm";
import StudentList from "./components/StudentList";
import EditForm from "./components/EditForm";
function App() {

  return (
    <div>
      <BrowserRouter>
        <Routes>
            <Route path="/" element = {<Home />}/>
            <Route path="/add-student" element={<StudentForm />}/>
            <Route path="/students" element={<StudentList />}/>
            <Route path="/edit-student" element={<EditForm />}/>
        </Routes>
      </BrowserRouter>
    </div>
  )
} 
export default App
