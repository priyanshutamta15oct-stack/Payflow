import "./PaymentCard.css"

function PaymentCard() {

  return (

    <div className="payment-container">

      <div className="payment-left">

        <h1>
          Payflow
        </h1>

        <p>
          Fast. Secure. Modern Payments.
        </p>

        <div className="card-preview">

          <div className="card-chip"></div>

          <h2>
            4242 4242 4242 4242
          </h2>

          <div className="card-bottom">

            <div>
              <span>
                Card Holder
              </span>

              <p>
                PRIYANSH TAMTA
              </p>
            </div>

            <div>
              <span>
                Expires
              </span>

              <p>
                12/29
              </p>
            </div>

          </div>

        </div>

      </div>

      <div className="payment-right">

        <h2>
          Payment Details
        </h2>

        <input
          type="text"
          placeholder="Card Holder Name"
        />

        <input
          type="text"
          placeholder="Card Number"
        />

        <div className="row">

          <input
            type="text"
            placeholder="MM/YY"
          />

          <input
            type="text"
            placeholder="CVV"
          />

        </div>

        <button>
          Pay ₹500
        </button>

      </div>

    </div>
  )
}

export default PaymentCard