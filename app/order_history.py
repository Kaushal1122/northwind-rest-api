from flask import Blueprint, jsonify

from app import services
from app.schemas import OrderSchema

order_history_api = Blueprint("order_history", __name__)

order_schema = OrderSchema()


@order_history_api.route(
    "/customers/<int:customer_id>/orders",
    methods=["GET"],
)
def get_customer_order_history(customer_id):
    customer = services.get_customer(customer_id)

    if customer is None:
        return jsonify({"error": "Customer not found."}), 404

    orders = services.get_orders()

    customer_orders = [
        {"id": order.id, **order_schema.dump(order)}
        for order in orders
        if order.customer_id == customer_id
    ]

    return jsonify(customer_orders), 200
