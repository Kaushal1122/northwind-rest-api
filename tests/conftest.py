import pytest

from app import create_app, db
from app.config import TestingConfig
from app.models import Customer, Order, OrderDetail, Product


@pytest.fixture
def app():
    app = create_app(TestingConfig)

    with app.app_context():
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()
        db.engine.dispose()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def customer(app):
    customer = Customer(
        first_name="John",
        last_name="Smith",
        email_address="john.smith@example.com",
        city="Bengaluru",
        country_region="India",
    )

    db.session.add(customer)
    db.session.commit()

    return customer


@pytest.fixture
def product(app):
    product = Product(
        product_name="Test Product",
        product_code="TEST001",
        standard_cost=50,
        list_price=100,
        quantity_per_unit="10 units",
        discontinued=False,
        category="Testing",
    )

    db.session.add(product)
    db.session.commit()

    return product


@pytest.fixture
def order(app, customer, product):
    order = Order(
        customer_id=customer.id,
        ship_name="John Smith",
        payment_type="Credit Card",
        shipping_fee=10,
    )

    order.order_details.append(
        OrderDetail(
            product_id=product.id,
            quantity=2,
            unit_price=100,
            discount=0,
        )
    )

    db.session.add(order)
    db.session.commit()

    return order