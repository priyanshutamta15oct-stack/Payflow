# Payflow

Scalable payment backend built with FastAPI, PostgreSQL, Redis, Docker, JWT Authentication, and Razorpay integration.

Designed with production-oriented backend architecture including authentication observability, centralized exception handling, integration testing, and CI automation.

---

# Features

## Authentication & Security

- JWT Authentication & Authorization
- Access Token + Refresh Token Flow
- Secure Login & Signup System
- Password Hashing
- Protected API Routes
- Redis-based Token Blacklisting
- Logout Token Invalidation
- JWT Security Validation
- Authentication Observability

---

## Payment Infrastructure

- Razorpay Payment Gateway Integration
- Secure Server-side Payment Verification
- Signature Validation
- Payment History Tracking
- Transaction Persistence

---

## Backend Architecture

- FastAPI Layered Architecture
- Service Layer Separation
- Dependency Injection
- Centralized Exception Handling
- Structured Logging
- ORM-based Database Design
- Environment Variable Configuration
- Production-oriented Backend Structure

---

## Infrastructure & DevOps

- Dockerized Backend Infrastructure
- PostgreSQL Database Integration
- Redis Integration
- Nginx Reverse Proxy
- GitHub Actions CI Pipeline
- Automated Backend Testing
- Environment-based Configuration

---

## Reliability & Testing

- Pytest Integration Testing
- Isolated Test Database
- Authentication Lifecycle Tests
- Logout Blacklist Tests
- Protected Route Tests
- CI-based Automatic Validation

---

# Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication
- Razorpay SDK
- Redis
- Alembic

---

## Database

- PostgreSQL

---

## Infrastructure

- Docker
- Docker Compose
- Nginx
- GitHub Actions

---

## Frontend

- React.js
- Axios

---

# Project Architecture

```text
Backend/
│
├── routers/
├── services/
├── models/
├── schemas/
├── core/
├── database/
├── tests/
│
├── main.py
├── requirements.txt
└── Dockerfile
```

---

# Architecture Highlights

- Layered Backend Architecture
- Thin Router Design
- Service-layer Business Logic
- Centralized Exception Handling
- Structured Logging System
- Dependency Injection
- JWT Security Architecture
- Redis-based Session Invalidation
- ORM-based Persistence Layer
- Infrastructure-aware Backend Design

---

# Authentication Flow

```text
User Login
↓
Credentials Validated
↓
JWT Access Token Generated
↓
Refresh Token Generated
↓
Frontend Stores Tokens
↓
Protected Requests Send Bearer Token
↓
Backend Validates JWT
↓
Redis Blacklist Checked
↓
Authenticated User Access Granted
```

---

# Logout Flow

```text
User Logout
↓
JWT Token Added To Redis Blacklist
↓
Future Requests With Same Token Rejected
↓
Unauthorized Response Returned
```

---

# Payment Flow

```text
Frontend Requests Payment Order
↓
Backend Creates Razorpay Order
↓
User Completes Payment
↓
Razorpay Returns Payment Signature
↓
Backend Verifies Signature Securely
↓
Payment Stored In PostgreSQL
↓
Transaction Added To History
```

---

# Observability & Logging

The backend includes structured logging and authentication observability for monitoring security and operational events.

## Logged Events

- Signup Attempts
- Duplicate Signup Attempts
- Login Attempts
- Invalid Login Attempts
- Successful Authentication
- Invalid JWT Usage
- Blacklisted Token Access Attempts
- Protected Route Access
- Application Exceptions
- Unexpected Server Errors

---

# Security Features

- Password Hashing
- JWT Authentication
- Refresh Token Architecture
- Protected Routes
- Redis Token Blacklisting
- Secure Payment Verification
- Signature Validation
- Centralized Exception Handling
- Secure Error Responses
- Environment Variable Secrets

---

# Testing

The backend includes automated integration testing using Pytest.

## Tested Flows

- Health Check Validation
- User Signup
- User Login
- JWT Authentication
- Protected Route Access
- Logout Token Blacklisting

Run tests:

```bash
docker exec -it payflow_backend pytest
```

---

# CI Pipeline

GitHub Actions automatically:

- Starts PostgreSQL
- Starts Redis
- Installs Dependencies
- Runs Pytest Suite
- Validates Backend Integrity

Pipeline runs automatically on:
- Push to `main`
- Pull Requests

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd Payflow
```

---

# Run With Docker

```bash
docker compose up --build
```

Backend available at:

```text
http://localhost:8000
```

---

# API Documentation

FastAPI automatically provides Swagger documentation:

```text
http://localhost:8000/docs
```

---

# Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@postgres:5432/payflow
SECRET_KEY=your_secret_key
ALGORITHM=HS256

REDIS_HOST=redis
REDIS_PORT=6379

RAZORPAY_KEY_ID=your_key
RAZORPAY_KEY_SECRET=your_secret
```

---

# Future Improvements

- Role-Based Access Control (RBAC)
- Email Verification
- Password Reset System
- Razorpay Webhooks
- Request Rate Limiting
- Monitoring & Metrics
- Cloud Deployment
- Background Task Queue
- Prometheus/Grafana Observability

---

# Author

## Priyansh Tamta

Backend Developer focused on scalable backend systems, authentication architecture, observability, and infrastructure-oriented engineering.
