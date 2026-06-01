from fastapi.testclient import TestClient

from main import app

from tests.test_database import db_session

client = TestClient(app)


def test_health_check(db_session):

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "Backend Running"
    }

def test_signup(db_session):

    response = client.post(
        "/auth/signup",
        json={
            "full_name": "Test User",
            "email": "test@example.com",
            "password": "test123"
        }
    )

    assert response.status_code == 200

    assert response.json() == {
        "message": "User Created Successfully"
    }

def test_login(db_session):

    client.post(
        "/auth/signup",
        json={
            "full_name": "Test User",
            "email": "test@example.com",
            "password": "test123"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "test@example.com",
            "password": "test123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data

    assert "refresh_token" in data

    assert data["token_type"] == "bearer"

def test_profile_route(db_session):

    signup_response = client.post(
        "/auth/signup",
        json={
            "full_name": "Test User",
            "email": "profile@example.com",
            "password": "test123"
        }
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "profile@example.com",
            "password": "test123"
        }
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/auth/profile",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "profile@example.com"

    assert data["full_name"] == "Test User"

def test_logout_blacklist(db_session):

    client.post(
        "/auth/signup",
        json={
            "full_name": "Logout User",
            "email": "logout@example.com",
            "password": "test123"
        }
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "logout@example.com",
            "password": "test123"
        }
    )

    token = login_response.json()["access_token"]

    logout_response = client.post(
        "/auth/logout",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert logout_response.status_code == 200

    profile_response = client.get(
        "/auth/profile",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert profile_response.status_code == 401

    assert profile_response.json() == {
        "detail": "You have been logged out"
    }