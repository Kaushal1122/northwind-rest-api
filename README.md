# Northwind REST API

A REST API built using Python and Flask to perform CRUD operations on the Northwind database. It supports managing customers, products, and orders, along with retrieving a customer's order history.

**GitHub Repository:** [Kaushal1122/northwind-rest-api](https://github.com/Kaushal1122/northwind-rest-api)

## Features

- Customer management: Insert, update, retrieve, and delete customers.
- Product management: Insert, update, retrieve, and delete products.
- Order management: Insert, update, retrieve, and delete orders.
- Customer order history: Retrieve all orders associated with a customer.
- Schema and data validation using Marshmallow.
- Database operations using Flask-SQLAlchemy ORM.
- Logging and exception handling.
- Unit testing using Pytest and mocking.

## Technology Stack

- **Language:** Python
- **Framework:** Flask
- **ORM:** Flask-SQLAlchemy
- **Database:** MySQL (Northwind dataset)
- **Validation:** Marshmallow
- **Testing:** Pytest, pytest-cov
- **Code Quality:** Ruff
- **Version Control:** Git and GitHub
- **IDE:** Visual Studio Code

## Project Structure

```text
northwind-rest-api/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│   ├── services.py
│   ├── repositories.py
│   └── order_history.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_customers.py
│   ├── test_products.py
│   ├── test_orders.py
│   └── test_order_history.py
├── .github/
│   └── workflows/
├── .env.example
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── README.md
└── run.py
```

## Setup and Installation

### Prerequisites

- Python 3.11 or later
- MySQL Server
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Kaushal1122/northwind-rest-api.git
cd northwind-rest-api
```

### 2. Create and activate a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the database

Import the Northwind database schema and data into MySQL.

Create a `.env` file in the project root:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/northwind
SECRET_KEY=your-secret-key
```

Replace the database credentials with your local MySQL credentials.

### 5. Run the application

```bash
python run.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## API Endpoints

All endpoints use the `/api` prefix.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/customers` | Retrieve all customers |
| GET | `/api/customers/<id>` | Retrieve a customer |
| POST | `/api/customers` | Create a customer |
| PUT | `/api/customers/<id>` | Update a customer |
| DELETE | `/api/customers/<id>` | Delete a customer |
| GET | `/api/products` | Retrieve all products |
| GET | `/api/products/<id>` | Retrieve a product |
| POST | `/api/products` | Create a product |
| PUT | `/api/products/<id>` | Update a product |
| DELETE | `/api/products/<id>` | Delete a product |
| GET | `/api/orders` | Retrieve all orders |
| GET | `/api/orders/<id>` | Retrieve an order |
| POST | `/api/orders` | Create an order |
| PUT | `/api/orders/<id>` | Update an order |
| DELETE | `/api/orders/<id>` | Delete an order |
| GET | `/api/customers/<id>/orders` | Retrieve customer order history |

## API Examples

The following examples demonstrate actual responses obtained while testing the API against the Northwind database. Outputs are shortened where necessary for readability.

### 1. Retrieve Customers

**Request:**

```http
GET /api/customers
```

**Sample Response:**

```json
{
  "value": [
    {
      "id": 1,
      "company": "Company A",
      "first_name": "Anna",
      "last_name": "Bedecs",
      "city": "Seattle",
      "country_region": "USA",
      "business_phone": "(123)555-0100",
      "email_address": null
    },
    {
      "id": 2,
      "company": "Company B",
      "first_name": "Antonio",
      "last_name": "Gratacos Solsona",
      "city": "Boston",
      "country_region": "USA",
      "business_phone": "(123)555-0100",
      "email_address": null
    }
  ],
  "Count": 29
}
```

### 2. Retrieve Products

**Request:**

```http
GET /api/products
```

**Sample Response:**

```json
{
  "value": [
    {
      "id": 1,
      "product_code": "NWTB-1",
      "product_name": "Northwind Traders Chai",
      "category": "Beverages",
      "standard_cost": "13.5000",
      "list_price": "18.0000",
      "quantity_per_unit": "10 boxes x 20 bags",
      "discontinued": false,
      "description": null
    },
    {
      "id": 3,
      "product_code": "NWTCO-3",
      "product_name": "Northwind Traders Syrup",
      "category": "Condiments",
      "standard_cost": "7.5000",
      "list_price": "10.0000",
      "quantity_per_unit": "12 - 550 ml bottles",
      "discontinued": false,
      "description": null
    }
  ],
  "Count": 45
}
```

### 3. Retrieve Orders

**Request:**

```http
GET /api/orders
```

**Sample Response:**

```json
{
  "value": [
    {
      "id": 30,
      "customer_id": 27,
      "order_date": "2006-01-15T00:00:00",
      "shipped_date": "2006-01-22T00:00:00",
      "ship_name": "Karen Toh",
      "shipping_fee": "200.0000",
      "payment_type": "Check",
      "notes": null,
      "order_details": [
        {
          "product_id": 34,
          "quantity": "100.0000",
          "unit_price": "14.0000",
          "discount": 0.0
        },
        {
          "product_id": 80,
          "quantity": "30.0000",
          "unit_price": "3.5000",
          "discount": 0.0
        }
      ]
    }
  ],
  "Count": 48
}
```

### 4. Retrieve Customer Order History

**Request:**

```http
GET /api/customers/6/orders
```

**Sample Response:**

```json
{
  "value": [
    {
      "id": 37,
      "customer_id": 6,
      "ship_name": "Francisco Pérez-Olaeta",
      "order_date": "2006-03-06T00:00:00",
      "shipped_date": "2006-03-09T00:00:00",
      "payment_type": "Credit Card",
      "shipping_fee": "12.0000",
      "order_details": [
        {
          "product_id": 8,
          "quantity": "17.0000",
          "unit_price": "40.0000",
          "discount": 0.0
        }
      ]
    }
  ],
  "Count": 6
}
```

The actual response contains all six orders associated with customer ID `6`.

### 5. Create a Customer

**Request:**

```http
POST /api/customers
Content-Type: application/json
```

**Request Body:**

```json
{
  "company": "README Demo",
  "first_name": "Sample",
  "last_name": "Customer",
  "business_phone": "9876543210",
  "city": "Bengaluru",
  "country_region": "India"
}
```

**Response:** Returns the created customer with its generated ID and submitted details.

### 6. Update a Customer

**Request:**

```http
PUT /api/customers/30
Content-Type: application/json
```

**Request Body:**

```json
{
  "city": "Pune"
}
```

**Response:** Returns the updated customer with the new city value.

### 7. Delete a Customer

**Request:**

```http
DELETE /api/customers/30
```

**Response:**

```json
{
  "message": "Customer deleted successfully."
}
```

The same CRUD operations are supported for products and orders.

## Validation and Error Handling

Marshmallow schemas are used to validate incoming request data before database operations.

Examples of validation include:

- Required fields and field length restrictions.
- Valid email addresses.
- Positive product prices and quantities.
- Valid customer and product IDs when creating orders.
- Discount values within the allowed range.

The API also handles common errors, including:

- `400 Bad Request` – Invalid request data.
- `404 Not Found` – Requested customer, product, or order does not exist.
- `409 Conflict` – Database operation failure.

Logging is used to record application events and database errors.

## Testing

Unit tests are written using Pytest.

The test suite covers:

- Customer CRUD operations.
- Product CRUD operations.
- Order CRUD operations.
- Customer order history.
- Invalid request data.
- Missing records.
- Database error handling.

Mocking is used to simulate database/service failures and isolate application behaviour during testing.

### Run Tests

```bash
python -m pytest -v
```

### Run Tests with Coverage

```bash
python -m pytest --cov=app --cov-report=term-missing --cov-report=html
```

### Test Results

Latest test execution:

- **Total tests:** 25
- **Passed:** 25
- **Failed:** 0
- **Code coverage:** 85%

### Coverage Summary

| Module | Coverage |
|---|---:|
| `__init__.py` | 100% |
| `config.py` | 100% |
| `models.py` | 100% |
| `order_history.py` | 100% |
| `repositories.py` | 100% |
| `schemas.py` | 100% |
| `routes.py` | 81% |
| `services.py` | 72% |
| **Overall** | **85%** |

The HTML coverage report is generated inside the `htmlcov/` directory.

## Code Quality

Ruff is used to check Python code for common errors, unused imports, import ordering, and selected style issues.

Run:

```bash
ruff check .
```

Latest result:

```text
All checks passed!
```

## Version Control

The project was developed using Visual Studio Code with Git for version control and GitHub for repository hosting.

Git was used to manage development changes through commits and branches.

## Future Deployment: AWS

AWS deployment is planned as a future enhancement.

The intended deployment architecture will use:

- **Amazon API Gateway:** Exposes REST API endpoints.
- **AWS Lambda:** Runs the Python API application without managing servers.
- **Amazon DynamoDB:** Provides persistence using a NoSQL database.
- **Amazon CloudWatch Logs:** Collects and monitors application logs.

### Planned Deployment Steps

1. Create a DynamoDB table for the required application entities.
2. Adapt the existing persistence layer to use DynamoDB instead of MySQL and SQLAlchemy.
3. Prepare the Flask application for execution in AWS Lambda, using a suitable Lambda adapter.
4. Create an AWS Lambda function and configure its execution role and environment variables.
5. Configure API Gateway routes and integrate them with the Lambda function.
6. Configure CloudWatch logging and verify that application logs are being captured.
7. Deploy and test the API endpoints through the API Gateway URL.

**Note:** AWS deployment has not yet been implemented. The above steps describe the planned future deployment architecture.