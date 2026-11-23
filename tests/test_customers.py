from unittest.mock import patch

from sqlalchemy.exc import SQLAlchemyError


def test_get_customers(client, customer):
    response = client.get("/api/customers")

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["first_name"] == "John"


def test_get_customer_by_id(client, customer):
    response = client.get(
        f"/api/customers/{customer.id}"
    )

    assert response.status_code == 200
    assert response.json["id"] == customer.id
    assert response.json["first_name"] == "John"


def test_get_customer_not_found(client):
    response = client.get("/api/customers/999")

    assert response.status_code == 404
    assert response.json["error"] == "Customer not found."


def test_create_customer(client):
    response = client.post(
        "/api/customers",
        json={
            "first_name": "Alice",
            "last_name": "Brown",
            "email_address": "alice@example.com",
            "city": "Mumbai",
        },
    )

    assert response.status_code == 201
    assert response.json["first_name"] == "Alice"
    assert response.json["last_name"] == "Brown"
    assert "id" in response.json


def test_create_customer_invalid_data(client):
    response = client.post(
        "/api/customers",
        json={
            "first_name": "   ",
            "last_name": "Brown",
        },
    )

    assert response.status_code == 400
    assert "errors" in response.json


def test_update_customer(client, customer):
    response = client.put(
        f"/api/customers/{customer.id}",
        json={"city": "Mumbai"},
    )

    assert response.status_code == 200
    assert response.json["city"] == "Mumbai"
    assert response.json["first_name"] == "John"


def test_delete_customer(client, customer):
    response = client.delete(
        f"/api/customers/{customer.id}"
    )

    assert response.status_code == 200

    get_response = client.get(
        f"/api/customers/{customer.id}"
    )

    assert get_response.status_code == 404


def test_create_customer_database_error(client):
    with patch(
        "app.routes.services.create_customer",
        side_effect=SQLAlchemyError("Simulated database error"),
    ):
        response = client.post(
            "/api/customers",
            json={
                "first_name": "Test",
                "last_name": "Customer",
            },
        )

    assert response.status_code == 409
    assert response.json["error"] == "Database operation failed."