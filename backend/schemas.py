from pydantic import BaseModel


class ReceiptCreate(BaseModel):
    store_name: str
    invoice_no: str
    date: str
    customer_name: str
    phone_number: str
    payment_mode: str

    subtotal: float
    cgst: float
    sgst: float
    total_amount: float
class ReceiptResponse(BaseModel):
    id: int
    ocr_result: str | None = None

    store_name: str | None = None
    invoice_no: str | None = None
    date: str | None = None
    customer_name: str | None = None
    phone_number: str | None = None
    payment_mode: str | None = None

    subtotal: float | None = None
    cgst: float | None = None
    sgst: float | None = None
    total_amount: float | None = None

    class Config:
        from_attributes = True