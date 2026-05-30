import { useState } from "react"

import axios from "axios"

import {
  FaEnvelope,
  FaLock,
  FaUser
} from "react-icons/fa"

function AuthPage({ onLogin }) {

  const [isLogin, setIsLogin] =
    useState(true)

  const [fullName, setFullName] =
    useState("")

  const [email, setEmail] =
    useState("")

  const [password, setPassword] =
    useState("")

  const [showPassword, setShowPassword] =
    useState(false)

  const [loading, setLoading] =
    useState(false)

  const [error, setError] =
    useState("")

  const [success, setSuccess] =
    useState("")

  const handleSignup = async () => {

    try {

      setLoading(true)

      setError("")

      setSuccess("")

      await axios.post(
        "http://localhost:8000/auth/signup",
        {
          full_name: fullName,
          email: email,
          password: password
        }
      )

      setLoading(false)

      setSuccess(
        "Account created successfully"
      )

      setTimeout(() => {

        setIsLogin(true)

        setSuccess("")

      }, 1500)

    } catch (error) {

      console.log(error)

      setLoading(false)

      setError(
        error.response?.data?.detail ||
        "Something went wrong"
      )
    }
  }

  const handleLogin = async () => {

    try {

      setLoading(true)

      setError("")

      setSuccess("")

      const formData =
        new FormData()

      formData.append(
        "username",
        email
      )

      formData.append(
        "password",
        password
      )

      const response =
        await axios.post(
          "http://localhost:8000/auth/login",
          formData
        )

      const token =
        response.data.access_token

      setLoading(false)

      setSuccess(
        "Login successful"
      )

      setTimeout(() => {

        onLogin(token)

      }, 1000)

    } catch (error) {

      console.log(error)

      setLoading(false)

      setError(
        error.response?.data?.detail ||
        "Invalid credentials"
      )
    }
  }

  return (

    <div className="auth-container">

      <div className="auth-box">

        <h1 className="login-title">
          Payflow
        </h1>

        <p className="login-subtitle">

          {
            isLogin
              ? "Secure payment dashboard"
              : "Create your account"
          }

        </p>

        {
          !isLogin && (

            <div className="input-box">

              <FaUser className="input-icon" />

              <input
                type="text"
                placeholder="Full Name"
                value={fullName}
                onChange={(e) =>
                  setFullName(
                    e.target.value
                  )
                }
              />

            </div>

          )
        }

        <div className="input-box">

          <FaEnvelope className="input-icon" />

          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) =>
              setEmail(e.target.value)
            }
          />

        </div>

        <div className="input-box">

          <FaLock className="input-icon" />

          <input
            type={
              showPassword
                ? "text"
                : "password"
            }

            placeholder="Password"

            value={password}

            onChange={(e) =>
              setPassword(
                e.target.value
              )
            }
          />

          <span
            className="toggle-password"

            onClick={() =>
              setShowPassword(
                !showPassword
              )
            }
          >
            {
              showPassword
                ? "Hide"
                : "Show"
            }
          </span>

        </div>

        {
          error && (

            <p className="error-text">
              {error}
            </p>

          )
        }

        {
          success && (

            <p className="success-text">
              {success}
            </p>

          )
        }

        <button
          className="primary-btn"
          onClick={
            isLogin
              ? handleLogin
              : handleSignup
          }
        >

          {
            loading
              ? "Please wait..."
              : (
                isLogin
                  ? "Login"
                  : "Create Account"
              )
          }

        </button>

        <button
          className="secondary-btn"
          onClick={() =>
            setIsLogin(!isLogin)
          }
        >

          {
            isLogin
              ? "Create Account"
              : "Already have account?"
          }

        </button>

      </div>

    </div>
  )
}

export default AuthPage