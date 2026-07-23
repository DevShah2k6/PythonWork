import { useState } from "react";
import { Navigate } from "react-router-dom";
import  "../assets/styles/EmployeeForm.css";
import { Link } from "react-router-dom";
import "../assets/styles/AddEmployee.css";
import EmployeeForm from "../assets/employees/EmployeeForm";
import { AddEmployee as AddEmployeeAPI } from "../api/api.js";
function AddEmployee(){
     const [submitted, setSubmitted] = useState(false);
     async function submitEmployee(Employeedata) {
    try {
        await AddEmployeeAPI(Employeedata);
        setSubmitted(true);
    } catch (error) {
        console.log(error);
    }
}
    if(submitted){
        return <Navigate to="/viewemployee" />;
    }

    return (
        <div className="form-container">
         <a href="/">HomePage</a>
        <h1 className="form-title">Employee Details</h1>
       
        <div className="form-content">
            
            <EmployeeForm onSubmit={submitEmployee}/>
          
            
        </div>
        </div>
    )
}
export default AddEmployee;