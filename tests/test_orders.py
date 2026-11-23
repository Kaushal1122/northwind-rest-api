def test_get_orders(client, order):
    response = client.get("/api/orders")

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["id"] == order.id


def test_get_order_by_id(client, order):
    response = client.get(
        f"/api/orders/{order.id}"
    )

    assert response.status_code == 200
    assert response.json["id"] == order.id
    assert len(response.json["order_details"]) == 1


def test_get_order_not_found(client):
    response = client.get("/api/orders/999")

    assert response.status_code == 404
    assert response.json["error"] == "Order not found."


def test_create_order(client, customer, product):
    response = client.post(
        "/api/orders",
        json={
            "customer_id": customer.id,
            "ship_name": "John Smith",
            "payment_type": "Credit Card",
            "shipping_fee": "10.0000",
            "order_details": [
                {
                    "product_id": product.id,
                    "quantity": "2.0000",
                    "unit_price": "100.0000",
                    "discount": 0,
                }
            ],
        },
    )

    assert response.status_code == 201
    assert response.json["customer_id"] == customer.id
    assert len(response.json["order_details"]) == 1


def test_create_order_with_invalid_customer(client, product):
    response = client.post(
        "/api/orders",
        json={
            "customer_id": 999,
            "order_details": [
                {
                    "product_id": product.id,
                    "quantity": "2.0000",
                    "unit_price": "100.0000",
                }
            ],
        },
    )

    assert response.status_code == 400
    assert response.json["error"] == "Customer does not exist."


def test_update_order(client, order):
    response = client.put(
        f"/api/orders/{order.id}",
        json={"payment_type": "Cash"},
    )

    assert response.status_code == 200
    assert response.json["payment_type"] == "Cash"


def test_delete_order(client, order):
    response = client.delete(
        f"/api/orders/{order.id}"
    )

    assert response.status_code == 200

    get_response = client.get(
        f"/api/orders/{order.id}"
    )

    assert get_response.status_code == 404
