# ATM System

Welcome to the **ATM System**! This lab provides a simple simulation of an ATM system where users can register accounts, login, check balance, withdraw cash, and deposit funds.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Introduction

The **ATM System** lab demonstrates a basic ATM system implemented in Python. Users can register accounts, log in using a PIN, and perform operations such as checking balance, withdrawing cash, and depositing funds.

## Features

1. **Account Registration:** The system generates unique account numbers and allows users to register with a 4-digit PIN.

2. **Login:** Registered users can log in using their account number and PIN.

3. **Check Balance:** Logged-in users can check their account balance.

4. **Withdraw Cash:** Users can withdraw cash from their accounts, with checks for insufficient balance and negative withdrawal amounts.

5. **Deposit Funds:** Users can deposit funds into their accounts, with a check for negative deposit amounts.

## Getting Started

Follow these steps to get started with the **ATM System** application:

1. **Clone the Repository:** Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/bilalmalikkk/ATM-System.git
   ```

2. **Run the Application:** Navigate to the repository directory and run the `atm.py` file using a Python interpreter:
   ```
   python atm.py
   ```

## Usage

1. **Account Registration:** Run the application and follow the prompts to register an account. You will be asked to set a 4-digit PIN.

2. **Login:** After registration, you can log in using your account number and PIN.

3. **Operations:** Once logged in, you can choose from the following operations:
   - Enter `1` to check your account balance.
   - Enter `2` to withdraw cash. Make sure to enter a non-negative and valid withdrawal amount.
   - Enter `3` to deposit funds. Make sure to enter a non-negative deposit amount.
