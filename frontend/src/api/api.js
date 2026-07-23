const BASE_URL = "http://127.0.0.1:8000";

export async function GetEmployee() {
    const response = await fetch(`${BASE_URL}/employee`)
    return await response.json() 
}
export async function AddEmployee(employeeData){
    const response = await fetch(`${BASE_URL}/addemployee`,{
        method:"POST",
         headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(employeeData)

})
return await response.json()
}
export async function EditEmployee(id,employeeData){
    const response = await fetch(`${BASE_URL}/editemployee/${id}`,{
        method:"PUT",
         headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(employeeData)
    })
    return await response.json()
}

export async function DeleteEmployee(id){
    const response = await fetch(`${BASE_URL}/deleteemployee/${id}`,{
        method:"DELETE",
    })
    return await response.json()
}