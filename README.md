# 💊 Pharmacy ERP System

> A modular desktop ERP application for pharmacy management — built entirely in Python with MySQL backend and a Tkinter GUI. Designed for offline-first pharmacy operations with reliable local database management, inventory tracking, billing, reporting, and customer management — all in one system.

---

## 🧩 What It Does

Most small pharmacies in India still manage stock on paper or in Excel sheets. This system replaces all of that with a structured, reliable desktop application that handles every core pharmacy operation in one place.

---

## ⚙️ Key Features

| Module | What It Handles |
|---|---|
| 🏥 **Inventory** | Add medicines, track batch numbers, expiry dates, quantities |
| 💰 **Billing** | Multi-item bill generation with atomic DB transactions |
| 🧾 **Invoice** | Auto-generated invoices per transaction |
| 👥 **Customers** | Customer record management |
| 🚚 **Suppliers** | Supplier tracking and management |
| 📊 **Reports** | Daily/overall sales and inventory reports |
| 🔐 **Auth** | Role-based login and access control |
| 🖥️ **GUI** | Desktop interface built with Tkinter — no browser needed |

---

## 🏗️ Architecture Highlights

- **10 modules** built from scratch with clean separation of concerns
- **Atomic billing** — multi-item transactions committed in a single DB call, zero partial saves
- **Real-time stock validation** — oversell prevention enforced at the query level before every sale
- **Dual-table sync** — `medicines` and `sales` tables updated simultaneously on every transaction
- **MySQL backend** via `mysql-connector-python` for production-grade data reliability

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Database:** MySQL
- **GUI:** Tkinter
- **DB Connector:** mysql-connector-python

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/shambhawikrishnatrya/pharmacy_erp.git
cd pharmacy_erp
```

### 2. Install dependencies
```bash
pip install mysql-connector-python
```

### 3. Set up the MySQL database

Create a MySQL database and update connection credentials in `database.py`:
```python
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="pharmacy_erp"
    )
```

Then create the required tables:
```sql
CREATE TABLE medicines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    batch_no VARCHAR(50),
    quantity INT,
    price FLOAT,
    expiry_date DATE
);

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medicine_name VARCHAR(100),
    quantity_sold INT
);

CREATE TABLE bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    total FLOAT,
    bill_date DATETIME
);

CREATE TABLE bill_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bill_id INT,
    medicine_id INT,
    quantity INT,
    subtotal FLOAT
);
```

### 4. Run the application

For the **CLI version:**
```bash
python app.py
```

For the **GUI version:**
```bash
python gui.py
```

---

## 📁 Project Structure

```
pharmacy_erp/
│
├── app.py          # CLI entry point
├── gui.py          # Tkinter GUI interface
├── auth.py         # Authentication & role management
├── database.py     # DB connection handler
├── inventory.py    # Medicine inventory logic
├── billing.py      # Bill creation & transaction handling
├── invoice.py      # Invoice generation
├── customers.py    # Customer management
├── suppliers.py    # Supplier management
└── reports.py      # Sales & inventory reporting
```

---

## 💡 Real-World Use Case

This system is designed for **small to mid-size pharmacies** that need:
- Structured medicine stock management with expiry tracking
- Fast billing without manual calculation errors
- Supplier and customer records in one place
- Sales reports without using spreadsheets

---

## 👩‍💻 Built By

**Shambhawi**
B.Tech CSE Student
GitHub: [@shambhawikrishnatrya](https://github.com/shambhawikrishnatrya)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
