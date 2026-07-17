import { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./components/Home";
import EditEmployee from "./components/EditEmployee";
import ViewEmployee from "./components/ViewEmployee";
import AddEmployee from "./components/AddEmployee";

import { GetEmployee } from "./api/api.js";
import { DeleteEmployee as DeleteEmployeeAPI } from "./api/api.js";


function App() {

  const [employee, setEmployee] = useState([]);


  // Fetch employee data from backend
  useEffect(() => {
    async function fetchEmployee() {
      const data = await GetEmployee();
      console.log("Employees:", data);
      setEmployee(data);
    }

    fetchEmployee();
  }, []);


  // Edit employee UI update
  function handleEditEmployee(updatedEmployee) {

    setEmployee((prevEmployee) =>
      prevEmployee.map((emp) =>
        emp.id === updatedEmployee.id ? updatedEmployee : emp
      )
    );

  }


  // Delete employee
  async function handleDeleteEmployee(id) {

    console.log("Delete id:", id);

    const response = await DeleteEmployeeAPI(id);

    console.log("Delete response:", response);


    setEmployee((prevEmployee) =>
      prevEmployee.filter((emp) => emp.id !== id)
    );

  }


  return (
    <div>

      <BrowserRouter>

        <Routes>

          <Route 
            path="/" 
            element={<Home />} 
          />


          <Route 
            path="/add-employee" 
            element={<AddEmployee />} 
          />


          <Route 
            path="/edit-employee/:id"
            element={
              <EditEmployee 
                handleEditEmployee={handleEditEmployee}
              />
            }
          />


          <Route 
            path="/viewemployee"
            element={
              <ViewEmployee
                employee={employee}
                handleDeleteEmployee={handleDeleteEmployee}
              />
            }
          />


        </Routes>

      </BrowserRouter>

    </div>
  );
}


export default App;