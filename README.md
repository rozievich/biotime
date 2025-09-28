# biotime

`biotime` — bu **Python package** bo‘lib, u orqali **ZKBio Time API** bilan qulay ishlash mumkin.
U login, token boshqaruvi va CRUD metodlarini soddalashtirib beradi.

---

## ✨ Xususiyatlar

* 🔐 JWT token orqali avtomatik autentifikatsiya
* 🔄 Token muddati tugasa avtomatik yangilash
* 🧩 Areas, Departments, Positions, Employees uchun CRUD metodlar
* 📊 Hodimlar ish hisobotlarini olish

---

## 📦 O‘rnatish

```bash
pip install biotime
```

---

## 🚀 Boshlash

```python
from biotime import BIOT

# API ga ulanish
bio = BIOT(
    host="http://your-biotime-server.com", 
    username="admin", 
    password="password"
)

# Barcha bo‘limlarni olish
areas = bio.get_all_area()
print(areas)

# Yangi bo‘lim qo‘shish
new_area = bio.create_area(area_name="New Office", area_code="A001")
print(new_area)

# Hodim qo‘shish
employee = bio.create_employee(
    emp_code="EMP001",
    department=1,
    area=[1],
    first_name="Ali",
    last_name="Valiyev",
    gender="M",
    mobile="+998901234567"
)
print(employee)

# Hodim ish hisobotini olish
report = bio.get_work_report(emp_id=1, start_date="2025-01-01", end_date="2025-01-31")
print(report)
```

---

## 📚 Asosiy metodlar

### 🔹 Areas

* `get_all_area(...)` — barcha bo‘limlarni olish
* `create_area(area_name, area_code, parent_area=None)` — yangi bo‘lim qo‘shish
* `get_area(area_id)` — bitta bo‘limni olish
* `update_area(area_id, ...)` — bo‘limni yangilash
* `delete_area(area_id)` — bo‘limni o‘chirish

### 🔹 Departments

* `get_all_department(...)`
* `create_department(...)`
* `update_department(...)`
* `delete_department(...)`

### 🔹 Positions

* `get_all_position(...)`
* `create_position(...)`
* `update_position(...)`
* `delete_position(...)`

### 🔹 Employees

* `get_all_employee(...)`
* `create_employee(...)`
* `update_employee(...)`
* `delete_employee(...)`

### 🔹 Work reports

* `get_work_report(emp_id, start_date, end_date, ...)`

---

## ⚡ Xatoliklarni boshqarish

Paket quyidagi istisnolarni ishlatadi:

* `AuthenticationError` — login muvaffaqiyatsiz bo‘lganda
* `APIRequestError` — API dan noto‘g‘ri javob qaytganida

---

## 📌 Loyihaga hissa qo‘shish

Pull request va fikr-mulohazalar uchun:
👉 [GitHub Repository](https://github.com/rozievich/biotime)

---

## 📝 Litsenziya

Bu loyiha **MIT License** asosida tarqatiladi.
Batafsil: [LICENSE](LICENSE)
