import axios from "axios"
import { useState } from "react"
import { useEffect } from "react"

import "../styles/payment.css"

function PaymentPage() {

  const [payments, setPayments] =
    useState([])

  const [paymentDone, setPaymentDone] =
    useState(false)

  const [paymentId, setPaymentId] =
    useState("")

  const [user, setUser] =
  useState(null)

  const fetchProfile = async () => {

  try {

    const token =
      localStorage.getItem("token")

    const response =
      await axios.get(
        "http://localhost:8000/auth/profile",
        {
          headers:{
            Authorization:
            `Bearer ${token}`
          }
        }
      )

    setUser(response.data)

  } catch(error){

    console.log(error)
  }
}
useEffect(() => {

  fetchPayments()

  fetchProfile()

}, [])

  const fetchPayments = async () => {

    try {

      const token =
        localStorage.getItem("token")

      const response =
        await axios.get(
          "http://localhost:8000/payment/history",
          {
            headers: {
              Authorization:
                `Bearer ${token}`
            }
          }
        )

      setPayments(response.data)

    } catch (error) {

      console.log(error)
    }
  }

  useEffect(() => {

    fetchPayments()

  }, [])

  const handlePayment = async () => {

    try {

      const token =
        localStorage.getItem("token")

      const response =
        await axios.post(
          "http://localhost:8000/payment/create-order?amount=500",
          {},
          {
            headers: {
              Authorization:
                `Bearer ${token}`
            }
          }
        )

      const order = response.data

      const options = {

        key:
          "rzp_test_StW6iSvPvmtIGu",

        amount:
          order.amount,

        currency:
          order.currency,

        name:
          "Payflow",

        description:
          "Premium Payment",

        order_id:
          order.order_id,

        handler: async function (
          response
        ) {

          await axios.post(
            "http://localhost:8000/payment/verify",
            {
              razorpay_order_id:
                response.razorpay_order_id,

              razorpay_payment_id:
                response.razorpay_payment_id,

              razorpay_signature:
                response.razorpay_signature,

              amount: 500,

              currency: "INR"
            },
            {
              headers: {
                Authorization:
                  `Bearer ${token}`
              }
            }
          )

          setPaymentDone(true)

          setPaymentId(
            response.razorpay_payment_id
          )

          fetchPayments()
        },

        theme: {
          color: "#2563eb"
        }
      }

      const razor =
        new window.Razorpay(
          options
        )

      razor.open()

    } catch (error) {

      console.log(error)

      alert(
        error.response?.data?.detail ||
        error.message
      )
    }
  }

  const logout = () => {

    localStorage.removeItem(
      "token"
    )

    window.location.reload()
  }

  return (

    <div className="dashboard-container">

      <div className="dashboard-card">

        <div className="dashboard-header">

          <div>

            <p className="welcome-text">
              Welcome Back
            </p>

            <h1 className="username">
              {user?.full_name} 
            </h1>

            <span className="dashboard-text">
              Smart Payment Dashboard
            </span>

          </div>

          <button
            className="logout-btn"
            onClick={logout}
          >
            Logout
          </button>

        </div>

        <div className="balance-card">

          <p>
            Available Balance
          </p>

          <h2>
            ₹12,450
          </h2>

        </div>

        <div className="payment-section">

          <div className="payment-info">

            <span>
              Premium Subscription
            </span>

            <h3>
              ₹500
            </h3>

          </div>

          {
            !paymentDone ? (

              <button
                className="pay-btn"
                onClick={handlePayment}
              >
                Pay Now
              </button>

            ) : (

              <div className="success-box">

                <h2>
                  Payment Successful ✅
                </h2>

                <p>
                  Transaction ID
                </p>

                <strong>
                  {paymentId}
                </strong>

              </div>

            )
          }

        </div>

        <div className="history-section">

          <h3>
            Recent Transactions
          </h3>

          {
            payments.map((item) => (

              <div
                className="history-card"
                key={item.id}
              >

                <div className="history-left">

                  <p>
                    ₹{item.amount}
                  </p>

                  <span className="status-success">
                    ● {item.status}
                  </span>

                </div>

                <div className="history-right">

                  <small>
                    Payment ID
                  </small>

                  <strong>
                    {item.razorpay_payment_id}
                  </strong>

                </div>

              </div>

            ))
          }

        </div>

      </div>

    </div>
  )
}

export default PaymentPage