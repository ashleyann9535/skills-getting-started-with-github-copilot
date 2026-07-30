from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_get_activities_returns_data():
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    assert "Chess Club" in response.json()


def test_signup_for_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "teststudent@mergington.edu"
    endpoint = f"/activities/{activity_name}/signup?email={email}"

    # Act
    response = client.post(endpoint)

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]


def test_duplicate_signup_is_rejected():
    # Arrange
    activity_name = "Chess Club"
    email = "teststudent@mergington.edu"
    endpoint = f"/activities/{activity_name}/signup?email={email}"

    # Act
    response = client.post(endpoint)

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()
