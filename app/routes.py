import logging

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app import db, services
from app.schemas import CustomerSchema, OrderSchema, ProductSchema

logger = logging.getLogger(__name__)

api = Blueprint("api", __name__)

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


def load_request_data(schema, partial=False):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        raise ValidationError(
            {"_schema": ["Request body must be a JSON object."]}
        )

    return schema.load(data, partial=partial)


def database_error_response(error):
    db.session.rollback()
    logger.exception("Database operation failed: %s", error)

    return jsonify({"error": "Database operation failed."}), 409


# Customer routes

@api.route("/customers", methods=["GET"])
def get_customers():
    customers = services.get_customers()

    result = [
        {"id": customer.id, **customer_schema.dump(customer)}
        for customer in customers
    ]

    return jsonify(result), 200


@api.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = services.get_customer(customer_id)

    if customer is None:
        return jsonify({"error": "Customer not found."}), 404

    result = {
        "id": customer.id,
        **customer_schema.dump(customer),
    }

    return jsonify(result), 200


@api.route("/customers", methods=["POST"])
def create_customer():
    try:
        data = load_request_data(customer_schema)
        customer = services.create_customer(data)

        result = {
            "id": customer.id,
            **customer_schema.dump(customer),
        }

        return jsonify(result), 201

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except SQLAlchemyError as error:
        return database_error_response(error)


@api.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    try:
        data = load_request_data(customer_schema, partial=True)
        customer = services.update_customer(customer_id, data)

        if customer is None:
            return jsonify({"error": "Customer not found."}), 404

        result = {
            "id": customer.id,
            **customer_schema.dump(customer),
        }

        return jsonify(result), 200

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except SQLAlchemyError as error:
        return database_error_response(error)


@api.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    try:
        deleted = services.delete_customer(customer_id)

        if not deleted:
            return jsonify({"error": "Customer not found."}), 404

        return jsonify({"message": "Customer deleted successfully."}), 200

    except SQLAlchemyError as error:
        return database_error_response(error)


# Product routes

@api.route("/products", methods=["GET"])
def get_products():
    products = services.get_products()

    result = [
        {"id": product.id, **product_schema.dump(product)}
        for product in products
    ]

    return jsonify(result), 200


@api.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = services.get_product(product_id)

    if product is None:
        return jsonify({"error": "Product not found."}), 404

    result = {
        "id": product.id,
        **product_schema.dump(product),
    }

    return jsonify(result), 200


@api.route("/products", methods=["POST"])
def create_product():
    try:
        data = load_request_data(product_schema)
        product = services.create_product(data)

        result = {
            "id": product.id,
            **product_schema.dump(product),
        }

        return jsonify(result), 201

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except SQLAlchemyError as error:
        return database_error_response(error)


@api.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    try:
        data = load_request_data(product_schema, partial=True)
        product = services.update_product(product_id, data)

        if product is None:
            return jsonify({"error": "Product not found."}), 404

        result = {
            "id": product.id,
            **product_schema.dump(product),
        }

        return jsonify(result), 200

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except SQLAlchemyError as error:
        return database_error_response(error)


@api.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        deleted = services.delete_product(product_id)

        if not deleted:
            return jsonify({"error": "Product not found."}), 404

        return jsonify({"message": "Product deleted successfully."}), 200

    except SQLAlchemyError as error:
        return database_error_response(error)


# Order routes

@api.route("/orders", methods=["GET"])
def get_orders():
    orders = services.get_orders()

    result = [
        {"id": order.id, **order_schema.dump(order)}
        for order in orders
    ]

    return jsonify(result), 200


@api.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = services.get_order(order_id)

    if order is None:
        return jsonify({"error": "Order not found."}), 404

    result = {
        "id": order.id,
        **order_schema.dump(order),
    }

    return jsonify(result), 200


@api.route("/orders", methods=["POST"])
def create_order():
    try:
        data = load_request_data(order_schema)
        order = services.create_order(data)

        result = {
            "id": order.id,
            **order_schema.dump(order),
        }

        return jsonify(result), 201

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    except SQLAlchemyError as error:
        return database_error_response(error)


@api.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    try:
        data = load_request_data(order_schema, partial=True)
        order = services.update_order(order_id, data)

        if order is None:
            return jsonify({"error": "Order not found."}), 404

        result = {
            "id": order.id,
            **order_schema.dump(order),
        }

        return jsonify(result), 200

    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    except SQLAlchemyError as error:
        return database_error_response(error)


@api.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    try:
        deleted = services.delete_order(order_id)

        if not deleted:
            return jsonify({"error": "Order not found."}), 404

        return jsonify({"message": "Order deleted successfully."}), 200

    except SQLAlchemyError as error:
        return database_error_response(error)
