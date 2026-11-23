def test_get_products(client, product):
    response = client.get("/api/products")

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["product_name"] == "Test Product"


def test_get_product_by_id(client, product):
    response = client.get(
        f"/api/products/{product.id}"
    )

    assert response.status_code == 200
    assert response.json["id"] == product.id
    assert response.json["product_name"] == "Test Product"


def test_get_product_not_found(client):
    response = client.get("/api/products/999")

    assert response.status_code == 404
    assert response.json["error"] == "Product not found."


def test_create_product(client):
    response = client.post(
        "/api/products",
        json={
            "product_code": "TEST002",
            "product_name": "New Product",
            "description": "Product for testing",
            "standard_cost": "25.0000",
            "list_price": "50.0000",
            "quantity_per_unit": "5 units",
            "discontinued": False,
            "category": "Testing",
        },
    )

    assert response.status_code == 201
    assert response.json["product_name"] == "New Product"
    assert response.json["list_price"] == "50.0000"


def test_create_product_invalid_data(client):
    response = client.post(
        "/api/products",
        json={
            "product_name": "   ",
            "list_price": "-10",
        },
    )

    assert response.status_code == 400
    assert "errors" in response.json


def test_update_product(client, product):
    response = client.put(
        f"/api/products/{product.id}",
        json={"list_price": "150.0000"},
    )

    assert response.status_code == 200
    assert response.json["list_price"] == "150.0000"
    assert response.json["product_name"] == "Test Product"


def test_delete_product(client, product):
    response = client.delete(
        f"/api/products/{product.id}"
    )

    assert response.status_code == 200

    get_response = client.get(
        f"/api/products/{product.id}"
    )

    assert get_response.status_code == 404
