import { useState } from "react"

import AuthPage from "./pages/AuthPage"
import PaymentPage from "./pages/PaymentPage"

import "./App.css"

function App() {

  const [token, setToken] = useState(
    localStorage.getItem("token")
  )

  const handleLogin = (newToken) => {

    localStorage.setItem(
      "token",
      newToken
    )

    setToken(newToken)
  }

  const handleLogout = () => {

    localStorage.removeItem(
      "token"
    )

    setToken(null)
  }

  return (

    <div className="app-container">

      {
        token ? (

          <PaymentPage
            onLogout={handleLogout}
          />

        ) : (

          <AuthPage
            onLogin={handleLogin}
          />

        )
      }

    </div>

  )
}

export default App