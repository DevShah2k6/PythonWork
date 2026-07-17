import EmployeeTable from "../assets/employees/EmployeeTable";
import "../assets/styles/ViewEmployee.css";

function ViewEmployee({employee, handleDeleteEmployee}){

    return (
        <div className="view-container">
            <h1 className="view-title">Employee List</h1>

            <div className="view-content">
                <EmployeeTable 
                    employee={employee} 
                    handleDeleteEmployee={handleDeleteEmployee}
                />
            </div>
        </div>
    )
}

export default ViewEmployee;