from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from database.session import get_db
from models.user_model import User
from core.dependencies import get_current_user
from services.payment_service import (create_razorpay_order, verify_razorpay_payment)
from schemas.payment_schema import (VerifyPaymentSchema)
from models.payment_model import Payment
from sqlalchemy.orm import Session
from models.payment_model import Payment

router= APIRouter(
    prefix="/payment",
    tags=["Payment"]
)

@router.post("/create-order")
def create_order(
    amount: int,
    current_user: User = Depends(get_current_user)
):
    try:
        order = create_razorpay_order(amount)
        return {
            "order_id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "receipt": order["receipt"],
            "user": current_user.email
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.post("/verify")
def verify_payment(
    payment_data: VerifyPaymentSchema,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    is_verified = verify_razorpay_payment(
        razorpay_order_id=payment_data.razorpay_order_id,
        razorpay_payment_id=payment_data.razorpay_payment_id,
        razorpay_signature=payment_data.razorpay_signature
    )

    if not is_verified:
        raise HTTPException(
            status_code=400,
            detail="Invalid payment details"
        )

    new_payment = Payment(
        user_email=current_user.email,
        amount=payment_data.amount,
        currency=payment_data.currency,
        status="completed",
        razorpay_payment_id=payment_data.razorpay_payment_id,
        razorpay_order_id=payment_data.razorpay_order_id,
        razorpay_signature=payment_data.razorpay_signature
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return {
        "success": True,
        "message": "Payment verified successfully",
        "user": current_user.email,
        "payment_id": new_payment.id
    }

@router.get("/history")
def payment_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    payments = db.query(Payment).filter(
        Payment.user_email ==
        current_user.email
    ).all()

    return payments