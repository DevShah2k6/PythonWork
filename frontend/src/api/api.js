// const BASE_URL = "http://127.0.0.1:8000"
const BASE_URL = import.meta.env.VITE_API_URL;
console.log("API URL:", BASE_URL);
export async function AddBooks(params) {
  console.log("ADD BOOK FUNCTION CALLED", params);
    const response  = await fetch(`${BASE_URL}/add-books`,{
        
        method:"POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(params)
    })
    return response.json()
}
export async function GetBooks() {
    const response = await fetch(`${BASE_URL}/books`)
     if (!response.ok) {
        throw new Error("Failed to fetch books");
    }
    return response.json()
}
export async function EditBook(id,bookData){
    const response = await fetch(`${BASE_URL}/edit-books/${id}`,{
        method:"PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(bookData)
    })
    return response.json()
}
export async function DeleteBook(id) {
    const response = await fetch(`${BASE_URL}/delete-books/${id}`,{
        method:"DELETE",
        headers: {
            "Content-Type": "application/json"
        },
    })
      return await response.json();
}