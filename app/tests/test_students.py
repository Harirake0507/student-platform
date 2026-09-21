import uuid

from fastapi.testclient import TestClient

from app.main1 import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Student Platform API is running"
    }


def test_create_student():
    email = f"test-{uuid.uuid4()}@example.com"

    response = client.post(
        "/students",
        json={
            "name": "Test Student",
            "email": email,
            "course": "DevOps"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Test Student"
    assert data["email"] == email
    assert data["course"] == "DevOps"
    assert "id" in data