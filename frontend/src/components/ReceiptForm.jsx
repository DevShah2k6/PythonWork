import { useEffect, useState } from "react";
import "../assets/styles/ReceiptForm.css";
import { updateReceipt } from "../api/api";
import { useNavigate } from "react-router-dom";

function ReceiptForm({ receipt,onBack }) {

    const navigate = useNavigate();
  const [formData, setFormData] = useState({
    store_name: "",
    invoice_no: "",
    date: "",
    customer_name: "",
    phone_number: "",
    payment_mode: "",
    subtotal: "",
    cgst: "",
    sgst: "",
    total_amount: "",
  });


  useEffect(() => {

    if (receipt) {

      const ocrData = JSON.parse(receipt.ocr_result);

     const text = ocrData.map(item => item.text);


      const getValue = (prefix, defaultValue = "0") => {

        const line = text.find(item => item.startsWith(prefix));

        return line
          ? line.replace(prefix, "").trim()
          : defaultValue;
      };


      const getNextValue = (key) => {

        const index = text.indexOf(key);

        return index !== -1 && index + 1 < text.length
          ? text[index + 1]
          : "0";
      };


      let totalAmount = "0";


      const totalLine = text.find(
        item => item.startsWith("Total Amount:")
      );


      if (totalLine) {

        totalAmount = totalLine
          .replace("Total Amount:", "")
          .trim();

      } 
      else {

        totalAmount = getNextValue("TOTAL AMOUNT:");

      }



      setFormData({

        store_name: text[0] || "0",

        invoice_no: getValue("Invoice No:"),

        date: getValue("Date:"),

        customer_name: getValue("Customer:"),

        phone_number: getValue("Phone:"),

        payment_mode: getValue(
          "Payment Mode:",
          "No"
        ),

        subtotal: getNextValue("Subtotal:"),

        cgst: getNextValue("CGST (2.5%):"),

        sgst: getNextValue("SGST (2.5%):"),

        total_amount: totalAmount,

      });


    }

  }, [receipt]);




  const handleChange = (e) => {

    setFormData({

      ...formData,

      [e.target.name]: e.target.value,

    });

  };



const handleSubmit = async (e) => {

  e.preventDefault();

  try {

    await updateReceipt(receipt.id, formData);

    alert("Receipt updated successfully");
    navigate("/");

  } catch(error) {

    console.log(error);

  }

};

  return (
    <div>
      <button
      type="button"
      className="back-btn"
      onClick={onBack}
    >
      ← Back to Receipts
    </button>
      <h3>Receipt Form</h3>
      

      <form 
        className="receipt-form"
        onSubmit={handleSubmit}
      >


        <div className="form-group">

          <label>Store Name</label>

          <input
            type="text"
            name="store_name"
            value={formData.store_name}
            onChange={handleChange}
          />

        </div>



        <div className="form-group">

          <label>Invoice Number</label>

          <input
            type="text"
            name="invoice_no"
            value={formData.invoice_no}
            onChange={handleChange}
          />

        </div>



        <div className="form-group">

          <label>Date</label>

          <input
            type="text"
            name="date"
            value={formData.date}
            onChange={handleChange}
          />

        </div>



        <div className="form-group">

          <label>Customer Name</label>

          <input
            type="text"
            name="customer_name"
            value={formData.customer_name}
            onChange={handleChange}
          />

        </div>



        <div className="form-group">

          <label>Phone Number</label>

          <input
            type="text"
            name="phone_number"
            value={formData.phone_number}
            onChange={handleChange}
          />

        </div>



        <div className="form-group">

          <label>Payment Mode</label>

          <input
            type="text"
            name="payment_mode"
            value={formData.payment_mode}
            onChange={handleChange}
          />

        </div>



        <div className="form-group">

          <label>Subtotal</label>

          <input
            type="number"
            name="subtotal"
            value={formData.subtotal}
            onChange={handleChange}
          />

        </div>



        <div className="form-group">

          <label>CGST</label>

          <input
            type="number"
            name="cgst"
            value={formData.cgst}
            onChange={handleChange}
          />

        </div>



        <div className="form-group">

          <label>SGST</label>

          <input
            type="number"
            name="sgst"
            value={formData.sgst}
            onChange={handleChange}
          />

        </div>



        <div className="form-group">

          <label>Total Amount</label>

          <input
            type="number"
            name="total_amount"
            value={formData.total_amount}
            onChange={handleChange}
          />

        </div>



        <div className="full-width">

          <button 
            type="submit"
            className="submit-btn"
          >
            Submit Receipt
          </button>

        </div>


      </form>


    </div>

  );

}


export default ReceiptForm;