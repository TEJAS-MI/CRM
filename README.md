🚀 Features
🔐 Authentication

User registration & login

Role-based access control (Admin & Customer)

Password reset via email (SMTP configured)

🧑‍💼 Admin Features

Dashboard with total orders, delivered, pending counts

Add / update / delete customers

Add / update / delete products

Add / update / delete orders

Order filtering using Django Filters

Admin-only access to products & dashboard

Auto-create Customer profile when a user registers (signals)

👤 Customer Features

View total orders

View delivered & pending orders

See personal order history

View contact support info in footer

Simple and clean UI

🛠 Tech Stack
Technology	Purpose
Python 3.x	Backend logic
Django 5	Web framework
MySQL	Database
PyMySQL	MySQL Driver
HTML, CSS, Bootstrap	Frontend UI
Django Filters	Search & Filtering
Pillow	Image support
📂 Project Structure

Your folder structure:

CRM/
│── accounts/
│   │── migrations/
│   │── templates/accounts/
│   │   ├── account_settings.html
│   │   ├── customer.html
│   │   ├── dashboard.html
│   │   ├── delete.html
│   │   ├── login.html
│   │   ├── main.html
│   │   ├── navbar.html
│   │   ├── order_form.html
│   │   ├── password_reset.html
│   │   ├── password_reset_done.html
│   │   ├── password_reset_sent.html
│   │   ├── products.html
│   │   ├── register.html
│   │   ├── status.html
│   │   ├── user.html
│   │── admin.py
│   │── apps.py
│   │── decorators.py
│   │── filters.py
│   │── forms.py
│   │── models.py
│   │── signals.py
│   │── urls.py
│   │── views.py
│
│── crm/
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│   │── asgi.py
│
│── static/
│   │── css/main.css
│   │── images/
│       ├── logo.png
│       ├── ML_Profile_pic.jpg
│       ├── profile1.png
│       ├── profile2.png
│       └── YouTube-Subs.png
│
│── .gitignore
│── manage.py
│── db.sqlite3 (only for development)

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/crm.git
cd crm

2️⃣ Create Virtual Environment
python -m venv myenv
myenv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt


If you don’t have requirements.txt, I can generate one for you. ✔️

4️⃣ MySQL Database Setup

Open MySQL & run:

CREATE DATABASE crmdb;
CREATE USER 'crmuser'@'localhost' IDENTIFIED BY 'YourPassword';
GRANT ALL PRIVILEGES ON crmdb.* TO 'crmuser'@'localhost';
FLUSH PRIVILEGES;


Update your crm/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crmdb',
        'USER': 'crmuser',
        'PASSWORD': 'YourPassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Create Superuser (Admin)
python manage.py createsuperuser

7️⃣ Start Development Server
python manage.py runserver


Visit → http://127.0.0.1:8000/

🔐 User Roles Explained
🧑‍💼 Admin (created via createsuperuser)

Full access to dashboard

Can add orders/products/customers

Can see all customers

👤 Customer (registered via register page)

Can login

Can only see their own orders

Cannot access /products/ or /customers/

📞 Support Section (Footer)
📞 Customer Support: 9876543210  
📧 support@crm.com  
⌚ Working Hours: 9 AM – 6 PM  


Added inside user.html or main footer.

🚀 Future Improvements

Customer order placing system

Product catalog

Payment integration (Razorpay)

Admin notifications

Deploy on Render.com / AWS