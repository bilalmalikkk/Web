# Product Management Web Application

This provides an overview and instructions for setting up and using the Product Management Web Application. This application is built using Flask, a Python web framework, and MongoDB as the database. The application allows users to manage product information, including adding, updating, and deleting products through a web-based user interface.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.6 or higher)
- MongoDB (running on `localhost` at port `27017`)

## Installation

1. Clone or download the repository to your local machine.

```bash
git clone <repository_url>
```

2. Navigate to the project directory.

```bash
cd product-management-app
```

3. Install the required Python packages using `pip`.

```bash
pip install -r requirements.txt
```

## Configuration

1. Open the `app.py` file in a text editor.

2. Modify the MongoDB connection settings if needed. By default, the application assumes MongoDB is running on `localhost` at port `27017` and using a database named `product`.

```python
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/product'
}
```

## Running the Application

1. Make sure your MongoDB server is up and running.

2. In the project directory, execute the following command to start the Flask application.

```bash
python app.py
```

3. The application should now be running at `http://localhost:5000/`.

## Usage

- Access the homepage at `http://localhost:5000/`. You should see "Hello World!" indicating that the application is running.

- Use the following routes to manage products:

  - `/showProducts`: View a list of products.
  - `/addProducts`: Add a new product.
  - `/updateProducts`: Update an existing product.
  - `/deleteProducts`: Delete a product.

- Each route corresponds to a template (`showProducts.html`, `addProducts.html`, `updateProducts.html`, `deleteProduct.html`) that provides a user interface for interacting with products.
