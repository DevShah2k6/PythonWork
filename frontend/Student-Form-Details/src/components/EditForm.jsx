import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { EditStudent } from "../api/api";
import "../assets/style/edit-form.css";
import Navbar from "./Navbar";

function EditForm() {
    const location = useLocation();
    const navigate = useNavigate();

    const student = location.state?.student;
    console.log(student)
    const [name, setName] = useState(student?.name || "");
    const [email, setEmail] = useState(student?.email || "");
    const [age, setAge] = useState(student?.age || "");
    const [course, setCourse] = useState(student?.course || "");

    async function handleSubmit(e) {
        e.preventDefault();

        const studentData = {
            name,
            email,
            age,
            course
        };

        await EditStudent(student.id, studentData);

        navigate("/students");
    }

    return (
        <div className="edit-form-container">
             <Navbar />
            <div className="edit-form-card">
                <div className="edit-form-header">
                    <h1>Edit Student</h1>
                    <p>Update the student's information</p>
                </div>

                <form onSubmit={handleSubmit}>

                    <div className="form-group">
                        <label>Name</label>
                        <input
                            type="text"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            placeholder="Enter student name"
                        />
                    </div>

                    <div className="form-group">
                        <label>Email</label>
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder="Enter email"
                        />
                    </div>

                    <div className="form-group">
                        <label>Age</label>
                        <input
                            type="text"
                            value={age}
                            onChange={(e) => setAge(e.target.value)}
                            placeholder="Enter age"
                        />
                    </div>

                    <div className="form-group">
                        <label>Course</label>
                        <input
                            type="text"
                            value={course}
                            onChange={(e) => setCourse(e.target.value)}
                            placeholder="Enter course"
                        />
                    </div>

                    <div className="edit-form-actions">
                        <button
                            type="button"
                            className="cancel-btn"
                            onClick={() => navigate("/students")}
                        >
                            Cancel
                        </button>

                        <button type="submit" className="update-btn">
                            Update Student
                        </button>
                    </div>

                </form>
            </div>
        </div>
    );
}

export default EditForm;