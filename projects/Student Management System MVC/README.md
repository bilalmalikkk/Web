# Student Management System

This Student Management System is designed to manage student records using the Model-View-Controller (MVC) architectural pattern. It provides functionalities for registering students, updating and deleting student records, and user authentication. The project is organized into three main components:

1. **Model**: The `dbHandler` class in the `model` module handles interactions with the MySQL database. It includes methods for various database operations such as student registration, authentication, updating, and deleting records.

2. **View**: The `View` class in the `view` module presents a menu-based interface to the user. Users can select various operations like registering students, logging in, updating student records, and deleting student records.

3. **Controller**: The `Controller` class in the `controller` module acts as an intermediary between the Model and View. It handles user inputs, manages data flow, and orchestrates the interactions between the user interface and the database operations.

## Prerequisites

- Python 3.x
- `pymysql` library for MySQL connectivity

## Getting Started

1. Clone the project repository:

```bash
git clone <repository_url>
```

2. Install the required dependencies:

```bash
pip install pymysql
```

3. Configure the MySQL database connection details in your code:

- In `model.py`, update the `dbh` object creation with your MySQL host, username, password, and database name.

## Usage

1. Run the `View.py` script to start the main menu interface.

2. Choose options from the menu to perform different operations like registering students, logging in, updating records, and deleting records.

3. Follow the prompts provided by the interface to input necessary information.

## MVC Approach

This project follows the Model-View-Controller (MVC) architectural pattern for better code organization and separation of concerns:

- **Model (`model` module)**: The `dbHandler` class handles interactions with the database. It encapsulates database operations like student registration, authentication, updating, and deleting.

- **View (`view` module)**: The `View` class presents a user-friendly menu interface. It provides options for various operations and guides users through inputting required data.

- **Controller (`controller` module)**: The `Controller` class bridges the gap between the Model and View. It handles user inputs, enforces data validation, and coordinates interactions between the user interface and the database operations.
