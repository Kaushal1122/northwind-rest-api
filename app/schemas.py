from marshmallow import Schema, fields, validate


class CustomerSchema(Schema):
    company = fields.String(
        allow_none=True,
        validate=validate.Length(max=50),
    )
    first_name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=50),
    )
    last_name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=50),
    )
    email_address = fields.Email(
        allow_none=True,
        validate=validate.Length(max=50),
    )
    business_phone = fields.String(
        allow_none=True,
        validate=validate.Length(max=25),
    )
    city = fields.String(
        allow_none=True,
        validate=validate.Length(max=50),
    )
    country_region = fields.String(
        allow_none=True,
        validate=validate.Length(max=50),
    )


class ProductSchema(Schema):
    product_code = fields.String(
        allow_none=True,
        validate=validate.Length(max=25),
    )
    product_name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=50),
    )
    description = fields.String(allow_none=True)
    standard_cost = fields.Decimal(
        allow_none=True,
        as_string=True,
        validate=validate.Range(min=0),
    )
    list_price = fields.Decimal(
        required=True,
        as_string=True,
        validate=validate.Range(min=0),
    )
    quantity_per_unit = fields.String(
        allow_none=True,
        validate=validate.Length(max=50),
    )
    discontinued = fields.Boolean(load_default=False)
    category = fields.String(
        allow_none=True,
        validate=validate.Length(max=50),
    )


class OrderDetailSchema(Schema):
    product_id = fields.Integer(
        required=True,
        validate=validate.Range(min=1),
    )
    quantity = fields.Decimal(
        required=True,
        as_string=True,
        validate=validate.Range(min=0, min_inclusive=False),
    )
    unit_price = fields.Decimal(
        required=True,
        as_string=True,
        validate=validate.Range(min=0),
    )
    discount = fields.Float(
        load_default=0,
        validate=validate.Range(min=0, max=1),
    )


class OrderSchema(Schema):
    customer_id = fields.Integer(
        required=True,
        validate=validate.Range(min=1),
    )
    order_date = fields.DateTime(allow_none=True)
    shipped_date = fields.DateTime(allow_none=True)
    ship_name = fields.String(
        allow_none=True,
        validate=validate.Length(max=50),
    )
    shipping_fee = fields.Decimal(
        allow_none=True,
        as_string=True,
        validate=validate.Range(min=0),
    )
    payment_type = fields.String(
        allow_none=True,
        validate=validate.Length(max=50),
    )
    notes = fields.String(allow_none=True)
    order_details = fields.List(
        fields.Nested(OrderDetailSchema),
        load_default=list,
    )