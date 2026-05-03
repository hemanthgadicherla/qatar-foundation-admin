# 🌐 Qatar Foundation Admin Portal (Backend)

## 📌 Project Overview

This project is a **Flask-based backend system** for the Qatar Foundation Admin Portal.

The frontend UI was **pre-built and not modified**, and this backend was developed to fully support it by implementing authentication, session management, and opportunity CRUD operations.

---

## 🚀 Features

### 🔐 Authentication

* Admin Signup
* Admin Login
* Secure Password Hashing
* Session-based Authentication (Flask-Login)
* Forgot Password (Mock implementation)

---

### 📊 Opportunity Management

* Create Opportunity
* View Opportunities
* Edit Opportunity
* Delete Opportunity
* Data persists in database (SQLite)
* Each admin sees only their own data

---

### 🔒 Security

* Passwords stored using hashing (Werkzeug)
* Protected routes using `login_required`
* Session-based authentication
* Unauthorized access handling

---

## 🛠 Tech Stack

| Technology  | Usage             |
| ----------- | ----------------- |
| Python      | Backend language  |
| Flask       | Web framework     |
| SQLite      | Database          |
| SQLAlchemy  | ORM               |
| Flask-Login | Authentication    |
| Flask-CORS  | API handling      |
| Gunicorn    | Production server |

---

## 📂 Project Structure

```
qatar-foundation-admin/
│
├── app.py
├── config.py
├── models.py
├── routes.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── admin.html
│
├── static/
│   ├── admin.js
│   └── admin.css
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/qatar-foundation-admin.git
cd qatar-foundation-admin
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```
python app.py
```

---

### 🌐 Open in Browser

```
http://127.0.0.1:5000/login
```

---

## 📡 API Endpoints

### 🔐 Authentication

* `POST /login`
* `POST /signup`
* `POST /logout`
* `POST /forgot-password`

---

### 📊 Opportunities

* `GET /opportunities`
* `POST /opportunities`
* `PUT /opportunities/<id>`
* `DELETE /opportunities/<id>`

---

## 🧪 Testing

Use **Browser DevTools → Network tab**

Check:

* `POST /login → 200`
* `POST /signup → 201`
* `GET /opportunities → 200`

---

## 📸 Screenshots (Add These)

* Login Page
* Dashboard
* Add Opportunity
* Opportunity List
* Edit/Delete
* Network Tab API Calls

---

## 🎥 Demo (Optional)

Include a short video showing:

* Login
* Add opportunity
* Edit/Delete
* Data persistence after refresh

---

## 🚀 Deployment

This project can be deployed on:

* Render
* Railway
* Vercel (Backend via serverless)

---

## 👨‍💻 Author

**Hemanth**

---

## ⭐ Notes

* Frontend UI was **not modified**
* Backend strictly follows given assignment requirements
* Fully functional and production-ready structure

---
