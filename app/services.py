import logging

from sqlalchemy.exc import SQLAlchemyError

from app import db, repositories
from app.models import Order, OrderDetail

logger = logging.getLogger(__name__)


def commit_changes(action):
    try:
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        logger.exception("Failed to %s", action)
        raise


# Customer services

def get_customers():
    return repositories.get_all_customers()


def get_customer(customer_id):
    return repositories.get_customer_by_id(customer_id)


def create_customer(data):
    try:
        customer = repositories.add_customer(data)
        commit_changes("create customer")
        logger.info("Created customer with ID %s", customer.id)
        return customer
    except SQLAlchemyError:
        db.session.rollback()
        raise


def update_customer(customer_id, data):
    customer = repositories.get_customer_by_id(customer_id)

    if customer is None:
        return None

    try:
        repositories.update_customer(customer, data)
        commit_changes("update customer")
        logger.info("Updated customer with ID %s", customer.id)
        return customer
    except SQLAlchemyError:
        db.session.rollback()
        raise


def delete_customer(customer_id):
    customer = repositories.get_customer_by_id(customer_id)

    if customer is None:
        return False

    try:
        repositories.delete_customer(customer)
        commit_changes("delete customer")
        logger.info("Deleted customer with ID %s", customer_id)
        return True
    except SQLAlchemyError:
        db.session.rollback()
        raise


# Product services

def get_products():
    return repositories.get_all_products()


def get_product(product_id):
    return repositories.get_product_by_id(product_id)


def create_product(data):
    try:
        product = repositories.add_product(data)
        commit_changes("create product")
        logger.info("Created product with ID %s", product.id)
        return product
    except SQLAlchemyError:
        db.session.rollback()
        raise


def update_product(product_id, data):
    product = repositories.get_product_by_id(product_id)

    if product is None:
        return None

    try:
        repositories.update_product(product, data)
        commit_changes("update product")
        logger.info("Updated product with ID %s", product.id)
        return product
    except SQLAlchemyError:
        db.session.rollback()
        raise


def delete_product(product_id):
    product = repositories.get_product_by_id(product_id)

    if product is None:
        return False

    try:
        repositories.delete_product(product)
        commit_changes("delete product")
        logger.info("Deleted product with ID %s", product_id)
        return True
    except SQLAlchemyError:
        db.session.rollback()
        raise


# Order services

def get_orders():
    return repositories.get_all_orders()


def get_order(order_id):
    return repositories.get_order_by_id(order_id)


def create_order(data):
    order_details_data = data.pop("order_details", [])

    customer = repositories.get_customer_by_id(data["customer_id"])

    if customer is None:
        raise ValueError("Customer does not exist.")

    for detail in order_details_data:
        product = repositories.get_product_by_id(detail["product_id"])

        if product is None:
            raise ValueError(
                f"Product with ID {detail['product_id']} does not exist."
            )

    try:
        order = Order(**data)

        for detail_data in order_details_data:
            order_detail = OrderDetail(**detail_data)
            order.order_details.append(order_detail)

        repositories.add_order(order)
        commit_changes("create order")

        logger.info("Created order with ID %s", order.id)
        return order

    except SQLAlchemyError:
        db.session.rollback()
        raise


def update_order(order_id, data):
    order = repositories.get_order_by_id(order_id)

    if order is None:
        return None

    data.pop("order_details", None)

    try:
        repositories.update_order(order, data)
        commit_changes("update order")
        logger.info("Updated order with ID %s", order.id)
        return order
    except SQLAlchemyError:
        db.session.rollback()
        raise


def delete_order(order_id):
    order = repositories.get_order_by_id(order_id)

    if order is None:
        return False

    try:
        repositories.delete_order(order)
        commit_changes("delete order")
        logger.info("Deleted order with ID %s", order_id)
        return True
    except SQLAlchemyError:
        db.session.rollback()
        raise
