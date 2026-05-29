import razorpay

from core.config import settings


client = razorpay.Client(
    auth=(
        settings.RAZORPAY_KEY_ID,
        settings.RAZORPAY_KEY_SECRET
    )
)


def create_razorpay_order(
    amount: int
):

    order_data = {
        "amount": amount * 100,
        "currency": "INR"
    }

    order = client.order.create(
        data=order_data
    )

    return order

def verify_razorpay_payment(
        razorpay_order_id: str,
        razorpay_payment_id: str,
        razorpay_signature: str
):
    data = {
        "razorpay_order_id": razorpay_order_id,
        "razorpay_payment_id": razorpay_payment_id,
        "razorpay_signature": razorpay_signature
    }
    try:
        client.utility.verify_payment_signature(data)
        return True
    except Exception:
        return False    