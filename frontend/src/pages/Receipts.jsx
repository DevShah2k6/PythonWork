import { useEffect, useState } from "react";
import { getReceipts } from "../api/api";
import ReceiptForm from "../components/ReceiptForm";
import "../assets/styles/Receipts.css";
function Receipts() {

  const [receipts, setReceipts] = useState([]);
  const [selectedReceipt, setSelectedReceipt] = useState(null);


   useEffect(() => {

    getReceipts()
      .then((response) => {
        console.log(response.data);
        setReceipts(response.data);
      })
      .catch((error) => {
        console.log(error);
      });

  }, []);
    return (

    <div className="receipts-page">

      {
        selectedReceipt ? (

          <ReceiptForm
  receipt={selectedReceipt}
  onBack={() => setSelectedReceipt(null)}
/>
        ) : (

          <>

            <h1>Receipts</h1>

            {
              receipts.length > 0 ? (

                <div className="receipts-list">

                  {receipts.map((receipt) => {

                    const ocrData = JSON.parse(receipt.ocr_result);

                    const text = ocrData.map(item => item.text);

                    const storeName = text[0] || "Unknown Store";

                    const getValue = (prefix, defaultValue = "N/A") => {

                      const line = text.find(
                        item => item.startsWith(prefix)
                      );

                      return line
                        ? line.replace(prefix, "").trim()
                        : defaultValue;
                    };

                    const invoiceNo = getValue("Invoice No:");

                    const date = getValue("Date:");

                    const totalLine = text.find(
                      item => item.startsWith("Total Amount:")
                    );

                    const totalAmount = totalLine
                      ? totalLine.replace("Total Amount:", "").trim()
                      : "N/A";

                    return (

                      <div
                        className="receipt-card"
                        key={receipt.id}
                      >

                        <h3 className="receipt-store">
                          {storeName}
                        </h3>

                        <p className="receipt-info">
                          Invoice: {invoiceNo}
                        </p>

                        <p className="receipt-info">
                          Date: {date}
                        </p>

                        <p className="receipt-info">
                          Total: ₹{totalAmount}
                        </p>

                        <button
                          className="view-receipt-btn"
                          onClick={() => setSelectedReceipt(receipt)}
                        >
                          View Receipt
                        </button>

                      </div>

                    );

                  })}

                </div>

              ) : (

                <p className="no-receipts">
                  No receipts found
                </p>

              )
            }

          </>

        )
      }

    </div>

  );
}
export default Receipts