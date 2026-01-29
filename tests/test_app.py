import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_index_contains_title(client):
    response = client.get("/")
    assert b"Mid Florida IT" in response.data


def test_index_contains_services(client):
    response = client.get("/")
    assert b"Managed IT" in response.data
    assert b"Network Solutions" in response.data
    assert b"Cloud Services" in response.data


def test_index_content_type(client):
    response = client.get("/")
    assert "text/html" in response.content_type


def test_404_on_unknown_route(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404
