from sqlalchemy import Column, Integer, String
from database.db import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String(100), index=True)
    amount = Column(Integer)
    currency = Column(String(10))
    status = Column(String(20))
    razorpay_payment_id = Column(String(100), unique=True)
    razorpay_order_id = Column(String(100), unique=True)
    razorpay_signature = Column(String(100), unique=True)