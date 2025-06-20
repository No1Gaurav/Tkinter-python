# Tkinter Login & Signup System

A clean and modern desktop application that implements a simple user authentication system with login and signup functionality. User credentials are securely stored in a database, and the system includes basic error handling and user validation.

---

## 💡 Features

- 🔐 Login and signup pages with form validation
- 💾 MySQL database integration for secure user data storage
- 🧪 Basic error handling and duplicate user checks
- 🖥️ Intuitive, user-friendly Tkinter interface
- 📦 Organized, modular codebase for easy expansion

---

## 📸 Screenshot


![Image](https://github.com/user-attachments/assets/f7ac86ca-2682-442b-b9cd-e2465a28b995)

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Tkinter** – native GUI library
- **MySQL** – backend user data storage
- **SQLite** – backend user data storage if you don't have or want to use **mysql**
- **mysql-connector-python** – for Python-MySQL communication

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3 installed on your system
- MySQL server running (locally or remotely)
- Create a MySQL database and table:
  
```sql
CREATE DATABASE user_auth;
USE user_auth;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

