# 🍽️ Meal Mate – Food Ordering Web App

Meal Mate is a full-stack food ordering web application built using Django. It allows users to browse restaurants, view menus, add items to a cart, and securely place orders using integrated online payment.

---

## 🚀 Features

* 🔐 User Authentication (Sign Up / Sign In)
* 🍴 Browse Restaurants & Menus
* 🛒 Add to Cart Functionality
* 💳 Online Payment Integration (Razorpay)
* 📦 Order Placement & Summary
* 🧾 Order History Tracking
* 🎨 Clean UI using custom CSS

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS
* **Database:** SQLite (can be upgraded to PostgreSQL)
* **Payment Gateway:** Razorpay
* **Deployment:** Railway (or any cloud platform)

---

## 📸 Screenshots

*Add screenshots of your UI here (Home, Menu, Checkout, Orders)*

---

## ⚙️ Installation (Local Setup)

1. Clone the repository:

```bash
git clone https://github.com/your-username/meal-mate.git
cd meal-mate
```

2. Create virtual environment:

```bash
python -m venv myenv
source myenv/bin/activate   # Linux/Mac
myenv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create `.env` file in root:

```env
SECRET_KEY=your_django_secret
RAZORPAY_KEY_ID=your_key
RAZORPAY_KEY_SECRET=your_secret
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Start server:

```bash
python manage.py runserver
```

---

## 🌐 Deployment

This project can be deployed on platforms like:

* Railway
* Render
* Heroku

Make sure to configure environment variables properly during deployment.

---

## 🔐 Environment Variables

| Variable            | Description         |
| ------------------- | ------------------- |
| SECRET_KEY          | Django secret key   |
| RAZORPAY_KEY_ID     | Razorpay public key |
| RAZORPAY_KEY_SECRET | Razorpay secret key |

---

## 📂 Project Structure

```
meal-mate/
│
├── delivery/        # Main app
├── templates/       # HTML templates
├── static/          # CSS files
├── manage.py
├── requirements.txt
└── .env             # Environment variables (not pushed)
```

---

## 💼 Resume Highlight

**Food Ordering Web App (Django + Razorpay)**

* Developed a full-stack food ordering system with cart and payment integration
* Integrated Razorpay for secure online transactions
* Implemented order management and user authentication
* Deployed on cloud platform

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📧 Contact

Raj Gaurav
📧 [rajgaurav3460@gmail.com](mailto:rajgaurav3460@gmail.com)
🔗 GitHub: https://github.com/your-username

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
