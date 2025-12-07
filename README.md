# CRM Management System (Django)

A fully functional Customer Relationship Management (CRM) web application built using Django.
This project helps admins manage customers, orders, and products, while customers can log in and view their own order dashboard.

This project is ideal for internship showcase, portfolio, or learning Django CRUD, authentication, signals, filters, and relational models.

# Features

# Admin Features

Add / Edit / Delete Customers

Add / Edit / Delete Products

Manage Orders and update their status

Add multiple tags to products

View complete dashboard:

Total Orders

Delivered Orders

Pending Orders

Automatic profile creation for customers via Django signals

Access to Django Admin Panel

# Customer Features

Login using username & password

View personal dashboard with:

Total Orders

Order history

Pending / Delivered order counts

Check order status and order date

Contact support details shown in footer

📂 Folder Structure

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
<<<<<<< HEAD
├── js/
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt

# Installation & Setup

1) Clone the Repository
git clone https://github.com/TEJAS-MI/CRM.git
cd YOUR-REPO

2) Create Virtual Environment

Windows:

python -m venv myenv
myenv\Scripts\activate

3) Install Requirements
pip install -r requirements.txt

4) Apply Migrations
python manage.py migrate

5) Create Superuser
python manage.py createsuperuser

6) Run Server
python manage.py runserver


# Open app → http://127.0.0.1:8000

# Admin panel → http://127.0.0.1:8000/admin/

# Technologies Used

Django

Python 3

SQLite / MySQL

Django Filters

HTML, CSS, Bootstrap

Django Authentication & Signals

* Contact Support (Shown on Customer Dashboard Footer)
* Customer Support: 9876543210  
* support@crm.com  
* Working Hours: 9 AM – 6 PM

# Future Enhancements

Customer product ordering system

Payment gateway integration

Email notifications for order updates

Deployment on Render / AWS

Add user profile images
