// export async function predictCar(data) {
//   const response = await fetch("http://localhost:8000/predict", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(data),
//   });

//   return await response.json();
// }
export async function predictCar(data) {
  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    

    const result = await response.json();
    return result;
  } catch (error) {
    throw error;
  }
}