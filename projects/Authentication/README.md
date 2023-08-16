# Flask Authentication using Sessions

This directory provides a basic example of implementing user registration, login, and session-based authentication in a Flask web application.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Introduction

The **Flask Authentication using Sessions** directory demonstrates how to create a simple web application using Flask that incorporates user registration and login functionality. The application uses session-based authentication to manage user sessions and secure access to certain routes.

## Features

1. **User Registration (`register.html`):** This page allows new users to register by providing their username, email, and password.

2. **User Login (`login.html`):** Existing users can log in using their registered credentials.

3. **Session Management:** The application uses session-based authentication to keep users logged in across different routes.

## Getting Started

Follow these steps to get started with the **Flask Authentication using Sessions** application:

1. **Clone the Repository:** Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/bilalmalikkk/Flask-Authentication.git
   ```

2. **Install Dependencies:** Make sure you have Flask and Flask-RESTful installed on your system. You can install these dependencies using the following command:
   ```
   pip install Flask Flask-RESTful
   ```

3. **Configure MongoDB:** Modify the MongoDB host and database settings in the `app.py` file according to your MongoDB configuration.

4. **Run the Application:** Navigate to the repository directory and run the `app.py` file:
   ```
   python app.py
   ```

5. **Access the Application:** Open your web browser and navigate to `http://localhost:5000` to access the application's home page.

## Usage

1. **User Registration:** Click on the "Register" link to access the registration page. Fill in your username, email, and password to create a new account.

2. **User Login:** Click on the "Login" link to access the login page. Enter your registered credentials to log in.

3. **Session Management:** Once logged in, you'll be able to access routes that require authentication. The application uses session-based authentication to maintain your login status.
