import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "../assets/styles/EditEmployee.css";
import { EditEmployee as EditEmployeeAPI } from "../api/api.js";
function EditEmployee({handleEditEmployee}){
    const location  = useLocation()
    const navigate = useNavigate();
    const emp = location.state.emp;
      const [employee,SetEmployee] = useState(emp)
function handleChange(e){
    SetEmployee({
        ...employee,
        [e.target.name]: e.target.value
    });
    console.log(employee);
    SetError("")

}
const [error, SetError] = useState("")
async function handleSubmit(e){

    let errors = [];
    e.preventDefault();


    // Age Validation
    if (String(employee.age).trim() === "") {
        errors.push("Age is Required");
    }
    else if (!/^-?[0-9]+$/.test(String(employee.age))) {
        errors.push("Age contains number only");
    }
    else if (employee.age < 0) {
        errors.push("Invalid Age");
    }
    else if (employee.age > 100) {
        errors.push("Age entered greater than 100 not allowed");
    }


    // Salary Validation
    if (String(employee.salary).trim() === "") {
        errors.push("Salary is Required");
    }
    else if (!/^-?[0-9]+$/.test(String(employee.salary))) {
        errors.push("Salary contains number only");
    }
    else if (employee.salary < 0) {
        errors.push("Invalid Salary");
    }


    // Fullname Validation
    if (employee.fullname.trim() === "") {
        errors.push("Full Name is Required");
    }
    else if (!/^[A-Za-z ]+$/.test(employee.fullname)) {
        errors.push("Full Name Should contain names only");
    }


    // Designation Validation
    if (employee.desgination.trim() === "") {
        errors.push("Designation is Required");
    }
    else if (!/^[A-Za-z ]+$/.test(employee.desgination)) {
        errors.push("Designation Should contain names only");
    }


    if(errors.length > 0){
        SetError(errors.join(", "));
        return;
    }

    console.log("Sending data:", employee);
    // Backend update
    const response = await EditEmployeeAPI(employee.id, employee);

    console.log("Updated response:", response);


    // Update UI state
    handleEditEmployee(employee);


    navigate("/viewemployee");
}
  return (
    <>
     <a href="/">HomePage</a>
    <div className="edit-conatiner">
        <h2 className="edit-title">Edit Employee</h2>
    
        <div className="edit-form-container">
            <p className="error-text">{error}</p>
            <form className="edit-form" onSubmit={handleSubmit}>
                <div className="form-group">
                    <label>FullName</label>
                    <input type="text" placeholder="Enter Your FullName" name="fullname" value={employee.fullname} onChange={handleChange} required></input>
                </div>
                <div className="form-group">
                    <label>Age</label>
                    <input type="text" placeholder="Enter Your Age" name="age" value={Number(employee.age)} onChange={handleChange} required></input>
                </div>
                <div className="form-group">
                    <label>Salary</label>
                    <input type="text" placeholder="Enter Your Salary" name="salary" value={Number(employee.salary)} onChange={handleChange} required></input>
                </div>
                <div className="form-group">
                    <label>Designation</label>
                    <input type="text" placeholder="Enter Your Designation" name="desgination" value={employee.desgination} onChange={handleChange} required></input>
                </div>

                <button className="update-btn" type="submit">Update</button>
            </form>
    
        </div>
    </div>
    </>
    )
}
export default EditEmployee;