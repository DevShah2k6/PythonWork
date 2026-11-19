
import { useState } from "react"
import "../assets/style/student-form.css";
import Navbar from "./Navbar";
import {AddStudent} from "../api/api";
import { Navigate, useNavigate } from "react-router-dom";
function StudentForm(){
    const [name,SetName] = useState("");
    const [age,SetAge] = useState(0);
    const [email,SetEmail] = useState("");
    const [course,SetCourse] = useState("");
    const navigate = useNavigate();
    const [errors,SetErrors] = useState("");
    const nameRegex = /^[A-Za-z ]+$/;
    const ageRegex = /^[0-9]+$/;
    const courseRegex = /^[A-Za-z ]+$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

async function handleSubmit(e)
    {
        e.preventDefault()
        if (!validateForm())
        {
            return 
        }
        const studentData = {
            name,
            age,
            email,
            course
        }
        await AddStudent(studentData)
        alert("Student added Successfully")
        navigate("/")
    }
function validateForm() {
   const newErrors = {}
    if (!name.trim()) {
        newErrors.name = "Name cannot be empty";
  
    }else if (!nameRegex.test(name)) {
        newErrors.name = "Name can contain only letters";
    }


    if (!email.trim() || !email.includes("@")) {
        newErrors.email = "Please enter a valid email";
     
    }else if (!emailRegex.test(email)) {
        newErrors.email = "Please enter a valid email";
    }

    if (!age || Number(age) <= 0) {
       newErrors.age = "Please enter a valid age";
      
    }else if (!ageRegex.test(age)) {
        newErrors.age = "Age can contain only numbers";
    }

    if (!course.trim()) {
        newErrors.course = "Course cannot be empty";
      
    }else if (!courseRegex.test(course)) {
        newErrors.course = "Course can contain only letters";
    }
    SetErrors(newErrors);

    return Object.keys(newErrors).length === 0; 
}
    return (
        <>
        <Navbar />
        <div className="student-form-container">
            <div className="student-form-card">
                <h1 className="student-form-title">Student Form</h1>
                <form className="student-form" onSubmit={handleSubmit}>
                    <div className="form-group">

                        <label className="form-label">Full Name</label>
                        <input className="form-input" type="text" value={name} onChange={(e)=>SetName(e.target.value)} required/>
                    </div>
                    {errors.name && <p className="error-message">{errors.name}</p>}
                    <div className="form-group">
                        <label className="form-label">Email</label>
                        <input className="form-input" type="email" value={email} onChange={(e)=>SetEmail(e.target.value)} required/>
                        
                    </div>
                    {errors.email && <p className="error-message">{errors.email}</p>}
                    <div className="form-group">
                        <label className="form-label">Age</label>
                        <input className="form-input" type="text" value={age} onChange={(e)=>SetAge(e.target.value)} required/>
                    </div>
                    {errors.age && <p className="error-message">{errors.age}</p>}
                    <div className="form-group">
                        <label className="form-label">Course</label>
                        <input className="form-input" type="text" value={course} onChange={(e)=>SetCourse(e.target.value)} required/>
                    </div>
                    {errors.course && <p className="error-message">{errors.course}</p>}
                    <button className="submit-button" type="submit">
                            Add Student
                        </button>
                </form>
            </div>
        </div>
        </>
    )
}
export default StudentForm;