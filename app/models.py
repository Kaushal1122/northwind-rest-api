from sqlalchemy import DateTime, Float, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from app import db


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email_address = db.Column(db.String(50))
    business_phone = db.Column(db.String(25))
    city = db.Column(db.String(50))
    country_region = db.Column(db.String(50))

    orders = relationship("Order", back_populates="customer")


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(25))
    product_name = db.Column(db.String(50))
    description = db.Column(db.Text)
    standard_cost = db.Column(Numeric(19, 4))
    list_price = db.Column(Numeric(19, 4), nullable=False)
    quantity_per_unit = db.Column(db.String(50))
    discontinued = db.Column(db.Boolean, nullable=False)
    category = db.Column(db.String(50))

    order_details = relationship(
        "OrderDetail",
        back_populates="product",
    )


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(
        db.Integer,
        ForeignKey("customers.id"),
    )
    order_date = db.Column(DateTime)
    shipped_date = db.Column(DateTime)
    ship_name = db.Column(db.String(50))
    shipping_fee = db.Column(Numeric(19, 4))
    payment_type = db.Column(db.String(50))
    notes = db.Column(db.Text)

    customer = relationship("Customer", back_populates="orders")
    order_details = relationship(
        "OrderDetail",
        back_populates="order",
    )


class OrderDetail(db.Model):
    __tablename__ = "order_details"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(
        db.Integer,
        ForeignKey("orders.id"),
        nullable=False,
    )
    product_id = db.Column(
        db.Integer,
        ForeignKey("products.id"),
    )
    quantity = db.Column(Numeric(18, 4), nullable=False)
    unit_price = db.Column(Numeric(19, 4))
    discount = db.Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="order_details")
