from app import db
from app.models import Customer, Order, Product

# Customer operations

def get_all_customers():
    return db.session.scalars(
        db.select(Customer).order_by(Customer.id)
    ).all()


def get_customer_by_id(customer_id):
    return db.session.get(Customer, customer_id)


def add_customer(data):
    customer = Customer(**data)
    db.session.add(customer)
    return customer


def update_customer(customer, data):
    for key, value in data.items():
        setattr(customer, key, value)

    return customer


def delete_customer(customer):
    db.session.delete(customer)


# Product operations

def get_all_products():
    return db.session.scalars(
        db.select(Product).order_by(Product.id)
    ).all()


def get_product_by_id(product_id):
    return db.session.get(Product, product_id)


def add_product(data):
    product = Product(**data)
    db.session.add(product)
    return product


def update_product(product, data):
    for key, value in data.items():
        setattr(product, key, value)

    return product


def delete_product(product):
    db.session.delete(product)


# Order operations

def get_all_orders():
    return db.session.scalars(
        db.select(Order).order_by(Order.id)
    ).all()


def get_order_by_id(order_id):
    return db.session.get(Order, order_id)


def add_order(order):
    db.session.add(order)
    return order


def update_order(order, data):
    for key, value in data.items():
        setattr(order, key, value)

    return order


def delete_order(order):
    for detail in order.order_details:
        db.session.delete(detail)

    db.session.delete(order)
