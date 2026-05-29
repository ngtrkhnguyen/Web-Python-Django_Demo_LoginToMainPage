# 🔐 Web Python Django - Login To MainPage

A simple web application built with **Python Django** and **IBM DB2 (AS400)** for user authentication.

---

## 📖 Overview

This project demonstrates a basic authentication flow:

```text
Login Page
     │
     ▼
Validate USERID / PASSWD
     │
     ▼
 IBM DB2 (KVXA.XAA0300)
     │
     ▼
 MainPage
```

The application connects to an IBM DB2 database through ODBC and validates user credentials stored in the `KVXA.XAA0300` table.

---

## ✨ Features

* 🔐 User Login Authentication
* 🗄️ IBM DB2 Database Integration
* 🚪 Session-based Authentication
* 🏠 MainPage after Login
* 🔓 Logout Function
* 🐍 Python Django Framework
* 🔌 ODBC Database Connection

---

## 🛠️ Technologies

| Technology  | Version           |
| ----------- | ----------------- |
| Python      | 3.x               |
| Django      | 5.x               |
| IBM DB2     | AS400             |
| ODBC Driver | IBM i Access ODBC |
| HTML        | HTML5             |
| CSS         | CSS3              |

---

## 📂 Project Structure

```text
LoginToMainPage_Python/
│
├── manage.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── db2.py
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── admin.py
│   ├── apps.py
│   │
│   └── templates/
│       └── accounts/
│           ├── login.html
│           └── mainpage.html
│
├── requirements.txt
│
└── README.md
```

---

## 🗄️ Database Configuration

Edit `config/settings.py`

```python
DB2_ODBC = {
    "DSN": "QDSN_10.20.196.7",
    "UID": "SISKJK",
    "PWD": "SISKJK",
}
```

---

## 📋 Database Table

```sql
KVXA.XAA0300
```

Required columns:

```sql
USERID
PASSWD
```

Example:

```sql
SELECT USERID, PASSWD
FROM KVXA.XAA0300
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/ngtrkhnguyen/Web-Python-Django_Demo_LoginToMainPage.git
cd Web-Python-Django_Demo_LoginToMainPage
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / MacOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run Application

Apply migrations:

```bash
python manage.py migrate
```

Start development server:

```bash
python manage.py runserver
```

Open browser:

```text
http://127.0.0.1:8000
```

---

## 🔄 Authentication Flow

```text
User Login
     │
     ▼
login.html
     │
     ▼
views.py
     │
     ▼
db2.py
     │
     ▼
KVXA.XAA0300
     │
     ▼
Session Created
     │
     ▼
MainPage
```

---

## 📸 Screenshots

### Login Page

```text
USERID
PASSWORD

[ LOGIN ]
```

### Main Page

```text
Welcome

Logged in as:
USERID

[ Logout ]
```

---

## 🔒 Security Notes

* Store passwords using hash algorithms in production.
* Never expose database credentials publicly.
* Use environment variables for sensitive information.
* Configure HTTPS when deploying.

---

## 👨‍💻 Author

**Nguyen Truong Khoi Nguyen**

Developed with Python Django and IBM DB2.
