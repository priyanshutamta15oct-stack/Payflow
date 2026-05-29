from pydantic import BaseModel

class VerifyPaymentSchema(BaseModel):

    razorpay_payment_id: str

    razorpay_order_id: str

    razorpay_signature: str

    amount: int

    currency: str