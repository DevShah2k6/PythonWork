from sqlalchemy import Column, Integer, String, Float, Text
from database import Base


class Receipt(Base):

    __tablename__ = "receipts"


    id = Column(Integer, primary_key=True, index=True)
    # OCR result stored after upload
    ocr_result = Column(Text)

    # Form fields filled after user submit
    store_name = Column(String)
    invoice_no = Column(String)
    date = Column(String)
    customer_name = Column(String)
    phone_number = Column(String)
    payment_mode = Column(String)
    subtotal = Column(Float)
    cgst = Column(Float)
    sgst = Column(Float)
    total_amount = Column(Float)
    file_hash = Column(String, unique=True, index=True)