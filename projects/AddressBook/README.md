# AddressBook Web Application

Welcome to the **AddressBook** web application repository! This application allows you to manage and search contacts, making it easier to keep track of your connections. It's built using the Flask framework and provides various functionalities for adding, displaying, and searching contacts.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Introduction

The **AddressBook** web application is designed to help you organize and access your contact information efficiently. You can add new contacts, view a list of all contacts, and search for specific contacts by name. This application is built using the Flask framework and Python.

## Features

1. **Home Page (`index.html`):** The home page provides a welcome message and serves as the entry point to the application.

2. **Add Contact (`contact.html`):** This page allows you to add new contacts to your address book. Fill in the contact's name, mobile number, city, and profession, and click the "Add Contact" button.

3. **Show Contacts (`showContact.html`):** View all contacts stored in your address book. Contacts are displayed in a tabular format, including their name, mobile number, city, and profession.

4. **Search Contact (`searchContact.html`):** Search for a specific contact by name. Enter the name and click the "Search" button. The result will display the contact's details if found.

5. **Search Result (`searchComp.html`):** Display the details of a searched contact. This page presents the name, mobile number, city, and profession of the contact.

## Getting Started

Follow these steps to get started with the **AddressBook** web application:

1. **Clone the Repository:** Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/bilalmalikkk/AddressBook.git
   ```

2. **Install Dependencies:** Make sure you have Python and Flask installed on your system. You can install Flask using the following command:
   ```
   pip install Flask
   ```

3. **Run the Application:** Navigate to the repository directory and run the `app.py` file:
   ```
   python app.py
   ```

4. **Access the Application:** Open your web browser and navigate to `http://localhost:5000` to access the home page of the application.

## Usage

1. **Adding a Contact:** Click on the "Add Contact" link in the navigation bar to add a new contact. Fill in the details and click "Add Contact."

2. **Viewing Contacts:** Click on the "Show Contacts" link to view all contacts stored in the address book.

3. **Searching Contacts:** Navigate to the "Search Contact" page to search for a specific contact by name. Enter the name and click "Search."
