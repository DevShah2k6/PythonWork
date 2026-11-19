import Navbar from "./Navbar";
import { useState } from "react";
import "../assets/style/student-list.css";
import { GetStudent } from "../api/api";
import {DeleteStudent} from "../api/api";
import {EditStudent} from "../api/api"
import { useNavigate } from "react-router-dom";
function StudentList(){
    async function loadStudents(){
        const data = await GetStudent();
         setStudents(data);

    } 
    const navigate = useNavigate()
    async function handleDelete(id){
        await DeleteStudent(id)
        setStudents(students.filter((student) => student.id !== id));
    }
 function handleEdit(id, studentData) {
    navigate("/edit-student", {
        state: { student: studentData }
    });
}
    const [students, setStudents] = useState([]);
    return (
        <>
        <Navbar/>
        <div className="student-list-container">
            <div className="student-list-card">
                <div className="student-list-header">
                    <h1 className="student-list-title">
                        Student List
                    </h1>
                    <p className="student-list-subtitle">
                        View all registered students
                    </p>
                      <button className="load-students-btn" onClick={loadStudents}>
                        Load Students
                    </button>
                </div>
                <div className="student-table-wrapper">
    <table className="student-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Age</th>
                <th>Course</th>
                <th>Actions</th>
            </tr>
        </thead>

        <tbody>
            {students.map((student) => (
                <tr key={student.id}>
                    <td>{student.name}</td>
                    <td>{student.email}</td>
                    <td>{student.age}</td>
                    <td>{student.course}</td>
                    <td>
                        <div className="action-buttons">
                            <button className="edit-btn" onClick={()=>handleEdit(student.id,student)}>
                                Edit
                            </button>

                            <button className="delete-btn" onClick={()=>handleDelete(student.id)}>
                                Delete
                            </button>
                        </div>
                    </td>
                </tr>
                        ))}
                    </tbody>
        </table>
                </div>

            </div>
        </div>
        </>
    );
}
export default StudentList;