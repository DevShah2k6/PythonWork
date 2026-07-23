import { Link } from "react-router-dom";
import "../styles/EmployeeTable.css";
function EmployeeTable({employee,handleDeleteEmployee}){

return (
<div className="table-container">
    <div className="table-card">
        <table className="employee-table">
            <thead>
                <tr>
                <th>FullName</th>
                <th>Age</th>
                <th>Salary</th>
                <th>Designation</th>
                <th>Actions</th>
                </tr>
            </thead>

                <tbody>
        {
            employee.map((emp, index) => (
                <tr key={index}>
                    <td style={{color:"black"}}>{emp.fullname}</td>
                    <td>{emp.age}</td>
                    <td>{emp.salary}</td>
                    <td>{emp.desgination}</td>
                    <td>

                    <Link className="action-link" to={`/edit-employee/${emp.id}`} state={{ emp }}>
                        <button className="action-btn edit-btn">Edit</button>
                        </Link>
                        <button 
    className="action-btn delete-btn" 
        onClick={() => {
    console.log("delete clicked", emp.id);
    handleDeleteEmployee(emp.id);
 }}
>
Delete
</button>
                    </td>
                </tr> 
    ))


        }
                    
                </tbody>
            </table>
        </div>
</div>
)
}
export default EmployeeTable;