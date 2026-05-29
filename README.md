# Payflow

Production-ready FastAPI payment backend with JWT authentication, Razorpay integration, SQLAlchemy ORM, and secure payment verification.

---

## Features

* JWT Authentication & Authorization
* Secure Login & Signup System
* Razorpay Payment Gateway Integration
* Server-side Payment Verification
* Payment History Tracking
* SQLAlchemy ORM Integration
* FastAPI Clean Architecture
* Environment Variable Configuration
* Protected API Routes
* Transaction Persistence
* Modular Backend Structure

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication
* Razorpay SDK

### Database

* SQLite (Current)
* PostgreSQL (Planned)

### Frontend

* React.js
* Axios

---

## Project Architecture

```text
routers/
services/
models/
schemas/
core/
database/
```

### Architecture Highlights

* Clean Architecture
* Dependency Injection
* Service Layer Separation
* ORM-based Database Design
* Secure JWT Authentication Flow

---

## Authentication Flow

```text
User Login
↓
JWT Token Generated
↓
Frontend Stores Token
↓
Protected Requests Send Bearer Token
↓
Backend Verifies JWT
↓
Authenticated User Access Granted
```

---

## Payment Flow

```text
Frontend Requests Order
↓
Backend Creates Razorpay Order
↓
User Completes Payment
↓
Backend Verifies Signature
↓
Payment Stored Securely
↓
Transaction Added To History
```

---

## Security Features

* Password Hashing
* JWT Authentication
* Protected Routes
* Server-side Payment Verification
* Environment Variable Secrets
* Signature Validation
* Secure Transaction Storage

---

## Future Improvements

* PostgreSQL Migration
* Docker Deployment
* Razorpay Webhooks
* Redis Integration
* Refresh Tokens
* Role-Based Access Control
* Email Verification
* Password Reset System
* Alembic Database Migrations

---

## Installation

### Backend

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
npm install
npm run dev
```

---

## API Documentation

FastAPI automatically provides Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Author

Priyansh Tamta
