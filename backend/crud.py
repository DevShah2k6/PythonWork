from models import Receipt
import json


# Step 1: Save OCR result after upload
def create_ocr_receipt(db, ocr_data,file_hash):

    existing_receipt = db.query(Receipt).filter(
        Receipt.file_hash == file_hash
    ).first()

    if existing_receipt:
          return None

    receipt = Receipt(
        file_hash=file_hash,
        ocr_result=json.dumps(ocr_data, default=str)
    )

    db.add(receipt)
    db.commit()
    db.refresh(receipt)

    return receipt



def create_receipt_data(db, data, receipt_id):

    receipt = db.query(Receipt).filter(
        Receipt.id == receipt_id
    ).first()

    receipt.store_name = data.store_name
    receipt.invoice_no = data.invoice_no
    receipt.date = data.date
    receipt.customer_name = data.customer_name
    receipt.phone_number = data.phone_number
    receipt.payment_mode = data.payment_mode
    receipt.subtotal = data.subtotal
    receipt.cgst = data.cgst
    receipt.sgst = data.sgst
    receipt.total_amount = data.total_amount

    db.commit()
    db.refresh(receipt)

    return receipt

def get_receipts(db):
    receipts = db.query(Receipt).all()
    return receipts
# Get all receipts for Navbar Receipts page
def get_receipts(db):

    receipts = db.query(Receipt).all()

    return receipts