from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import os
from crud import create_receipt_data, get_receipts, create_ocr_receipt
from ocr import extract_text

from database import engine, get_db
from models import Base,Receipt
from schemas import ReceiptCreate
from crud import create_receipt_data, get_receipts,create_ocr_receipt
import hashlib
from schemas import ReceiptCreate, ReceiptResponse
# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI()


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://10.37.57.44:5173",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# OCR Upload API
@app.post("/upload")
async def upload_receipt(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    try:

        os.makedirs("upload", exist_ok=True)

        file_path = os.path.join(
            "upload",
            file.filename
        )

        file_content = await file.read()

        # Create hash of uploaded file
        file_hash = hashlib.sha256(file_content).hexdigest()

        # Check duplicate before OCR
        existing_receipt = db.query(Receipt).filter(
            Receipt.file_hash == file_hash
        ).first()

        if existing_receipt:
            return {
                "error": "This receipt has already been uploaded."
            }


        # Save file
        with open(file_path, "wb") as f:
            f.write(file_content)

        # OCR
        result = extract_text(file_path)

        # Save OCR result
        receipt = create_ocr_receipt(
            db,
            result,
            file_hash
        )
        return result
    except Exception as e:

        print("UPLOAD ERROR:", e)

        return {
            "error": str(e)
        }
    
@app.get("/receipts", response_model=list[ReceiptResponse])
def read_receipts(db: Session = Depends(get_db)):
    return get_receipts(db)


@app.put("/receipts/{receipt_id}")
def update_receipt(
    receipt_id: int,
    data: ReceiptCreate,
    db: Session = Depends(get_db)
):
    return create_receipt_data(db, data, receipt_id)
# Save receipt form data after submit
# @app.post("/receipts")
# def create_receipt(
#     data: ReceiptCreate,
#     db: Session = Depends(get_db)
# ):

#     return create_receipt_data(db, data)