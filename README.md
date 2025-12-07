# CRM Management System (Django)

A fully functional Customer Relationship Management (CRM) web application built using Django.
Admins can manage customers, products, and orders, while customers can log in to view their personal dashboard and track order status.

This project is ideal for internships, portfolio projects, and learning Django CRUD, authentication, filters, signals, and relational models.

# Features

# Admin Features

Add / Edit / Delete Customers

Add / Edit / Delete Products

Manage Orders and update status

Assign multiple tags to products

View powerful dashboard:

Total Orders

Delivered Orders

Pending Orders

Automatic customer profile creation using Django Signals

Access to Django Admin Panel

# Customer Features

Register & Login using username/password

View personal dashboard with:

Total Orders

Order History

Delivered / Pending Status

Order Date

Contact Support shown in footer

## 📁 Project Folder Structure

```text
CRM/
│── accounts/
│   ├── templates/accounts/
│   │   ├── account_setting.html
│   │   ├── customer.html
│   │   ├── dashboard.html
│   │   ├── delete.html
│   │   ├── login.html
│   │   ├── main.html
│   │   ├── navbar.html
│   │   ├── order_form.html
│   │   ├── password_reset.html
│   │   ├── password_reset_done.html
│   │   ├── password_reset_email.html
│   │   ├── password_reset_form.html
│   │   ├── products.html
│   │   ├── register.html
│   │   ├── status.html
│   │   └── user.html
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── filters.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── crm/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   ├── css/main.css
│   └── images/
│       ├── logo.png
│       ├── ML_profile_pic1.png
│       ├── ML_profile_pic2.png
│       └── profile.png
│
├── js/
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```


# Installation & Setup

1️) Clone the Repository
git clone https://github.com/TEJAS-MI/CRM.git
cd CRM

2️) Create Virtual Environment

Windows:

python -m venv myenv
myenv\Scripts\activate

3️) Install Dependencies
pip install -r requirements.txt

4️) Apply Migrations
python manage.py migrate

5) Create Superuser
python manage.py createsuperuser

6️) Run Server
python manage.py runserver

# URLs

Feature	URL
Application	http://127.0.0.1:8000

Admin Panel	http://127.0.0.1:8000/admin

# Technologies Used

Django

Python 3

SQLite / MySQL

Django Filters

Authentication System

Bootstrap, HTML, CSS

Django Signals

# Contact Support (Displayed on Customer Dashboard Footer)

Customer Support: 9876543210

Email: support@crm.com

Working Hours: 9 AM – 6 PM

# Future Enhancements

Online product ordering system for customers

Payment gateway integration

Email notifications for order updates

Deployment on Render / AWS

User profile pictures
