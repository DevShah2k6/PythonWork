import { useState } from "react";
import "../styles/EmployeeForm.css";
function EmployeeForm({onSubmit}){
const [employeeData, setEmployeeData] = useState({
        fullname: "",
        age: "",
        salary: "",
        desgination: ""
    });
    // this fucntion will do "name":"dev" like that all values
function handleChange(e){
    setEmployeeData({
        ...employeeData,
        [e.target.name]: e.target.value
    });
    SetError("");
}
// this is for showing the erro message to validate the data and state is cretaed
//  it is insdie ti creates new state so outisde it is declared as when click evry time 
// happend then evry time new state is there and old is deleted so
const [error,SetError] = useState("")
    function handleSubmit(e){
    let errors = []
    e.preventDefault();       // stops the native browser submission
    if (employeeData.age.trim()==""){
        errors.push("Age is Required")
    }

    else if(!/^-?[0-9]+$/.test(employeeData.age)){
        errors.push("Age contains number only")
    }
    else if (employeeData.age<0){
        errors.push("Invalid Age ")
    
    }
     else if (employeeData.age>100){
        errors.push("Age entered greater than 100 not allowed")
    }
    if (employeeData.salary.trim()==""){
        errors.push("Salary is Required")
    }
    else  if(!/^-?[0-9]+$/.test(employeeData.salary)){
        errors.push("Salary contains number only")
    }
    else if (employeeData.salary<0){
        errors.push("Invalid Salary")
        
    }
    if (employeeData.fullname.trim()==""){
        errors.push("Full Name is Required")
    }
    else if (!/^[A-Za-z ]+$/.test(employeeData.fullname)){
        errors.push("Full Name Should contain names only")
        
    }
    if (employeeData.desgination.trim()==""){
        errors.push("Desgination is Required")
    }
    
    else if (!/^[A-Za-z ]+$/.test(employeeData.desgination)){
        errors.push("Desgnation Should contain names only")
        
    }
    
    
    if(errors.length > 0){
        // here in array is is join by the comman so that in ui it is like this
        // error1,error2
        SetError(errors.join(", "));
        return
    }
    onSubmit(employeeData);   // sends data up to AddEmployee.jsx
}

    return (
        <div className="form-container">
            <form className="employee-form" onSubmit={handleSubmit}>
                   <p className="error-text">{error}</p>
                <div className="form-group">
                <label>FullName</label>
                <input type="text" placeholder="Enter Your FullName" name="fullname" value={employeeData.name} onChange={handleChange} required></input>
                </div>
                <div className="form-group">
                <label>Age</label>
                <input type="text" placeholder="Enter Your Age" name="age" value={employeeData.age} onChange={handleChange} required></input>
                </div>
                <div className="form-group">
                <label>Salary</label>
                <input type="text" placeholder="Enter Your Salary" name="salary" value={employeeData.salary} onChange={handleChange} required></input>
                </div>
                <div className="form-group">
                <label>Designation</label>
                <input type="text" placeholder="Enter Your Designation" name="desgination" value={employeeData.desg} onChange={handleChange} required></input>
                </div>
                <button className="submit-btn" type="submit">Submit</button>
            </form>
        </div>
    )
}
export default EmployeeForm;