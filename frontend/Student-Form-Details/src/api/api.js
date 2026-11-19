

 export async function AddStudent(studentData){
    const response = await fetch(`http://localhost:8000/students`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(studentData)
    });

    const data = await response.json();

    console.log(data)
}


export  async function GetStudent(){
    const response = await fetch(`http://localhost:8000/students`, {
        method: "GET",
     
  
    });
    console.log("Status:", response.status);

    const data = await response.json();

    console.log(data)
    return data
}
export async function EditStudent(id, studentData) {
    const response = await fetch(`http://localhost:8000/students/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(studentData)
    });

    const data = await response.json();
    console.log(data);
    return data;
}
export  async function DeleteStudent(id){
    const response = await fetch(`http://localhost:8000/student/${id}`, {
        method: "DELETE",
     
  
    });
    // console.log("Status:", response.status);

    // const data = await response.json();

    // console.log(data)
    // return data
}
export default {AddStudent,GetStudent};