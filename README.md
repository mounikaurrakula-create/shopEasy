# 🛍️ Mounika Mart – Django E-Commerce Website

Mounika Mart is a full-stack e-commerce web application developed using **Python and Django**. The application allows users to browse products, view product details, add products to a shopping cart, and manage their cart.

The project uses **Django** for the backend, **Neon PostgreSQL** for production database storage, and **Cloudinary** for persistent product image storage. The application is deployed on **Render**.

---

## 🌐 Live Demo

🔗 **Live Website:**  
https://shopeasy-1-trg9.onrender.com/

🔗 **Products:**  
https://shopeasy-1-trg9.onrender.com/products/

---

## ✨ Features

- 🏠 Home page
- 🛍️ Product listing
- 🔎 Product details
- 🛒 Add products to cart
- ➕ Increase product quantity
- ➖ Decrease product quantity
- ❌ Remove products from cart
- 💰 Automatic subtotal calculation
- 💵 Automatic total calculation
- 🖼️ Cloudinary-based product image storage
- 👨‍💼 Django Admin panel
- 🗄️ PostgreSQL production database
- 📱 Responsive user interface
- ☁️ Cloud deployment using Render

---

## 🛠️ Technologies Used

### Backend

- Python
- Django
- Django ORM
- Gunicorn

### Frontend

- HTML5
- CSS3
- Django Templates

### Database

- SQLite – Local development
- PostgreSQL – Production
- Neon PostgreSQL – Cloud database

### Image Storage

- Cloudinary
- django-cloudinary-storage

### Deployment

- GitHub
- Render

---

## 📂 Project Structure

```text
Shopeasy/
│
├── ecommerce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── store/
│   ├── migrations/
│   ├── templates/
│   │   └── store/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── products/
│
├── media/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
