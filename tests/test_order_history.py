def test_get_customer_order_history(client, customer, order):
    response = client.get(f"/api/customers/{customer.id}/orders")

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["id"] == order.id
    assert response.json[0]["customer_id"] == customer.id


def test_get_customer_order_history_empty(client, customer):
    response = client.get(f"/api/customers/{customer.id}/orders")

    assert response.status_code == 200
    assert response.json == []


def test_get_customer_order_history_not_found(client):
    response = client.get("/api/customers/999/orders")

    assert response.status_code == 404
    assert response.json["error"] == "Customer not found."