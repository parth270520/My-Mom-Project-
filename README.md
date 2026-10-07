# 🩺 ASHA Care — Healthcare Portal & Nurse Dashboard

> *A simple, beautiful web application crafted with love for my mom, a dedicated nurse and community healthcare worker, to help her effortlessly manage daily work, family records, health surveys, home visits, maternal follow-ups, and duty attendance.* ❤️

---

## 🌟 What's New in This Release (`feat/new-look-and-features`)

### 1. ⏱️ Daily Attendance & Duty Tracker (Brand New Feature)
Community healthcare workers and ASHA nurses travel across villages every day conducting door-to-door surveys, immunization drives, and maternal checkups. This new module gives mom a complete digital duty register:
- **1-Click Quick Check-In & Check-Out:** Direct check-in when starting duty in the morning, and 1-click check-out at the end of the shift with automatic timestamp recording.
- **Duty Categorization:** Log specific duty types:
  - *Routine Sub-Center Duty*
  - *Home Visits & Door-to-Door Survey*
  - *Maternal & Child Health Checkup*
  - *Pulse Polio / Immunization Drive*
  - *Ayushman / ABHA Registration Camp*
  - *PHC / CHC Meeting & Training*
  - *Emergency Response*
- **Daily Impact Metrics:** Track number of **Home Visits Conducted** and **Patients Screened/Attended** each day.
- **Interactive Monthly Logbook:** Monthly filtering, search, and automatic status badges (`Present`, `Field Duty`, `Health Camp`, `Half Day`, `On Leave`).
- **🖨️ Printable Monthly Duty Register:** Instant export and print-ready PHC duty sheet with nurse signature and Medical Officer sign-off section, formatted specifically for monthly government allowance verification.

---

### 2. 🎨 Beautiful Modern Healthcare UI & Aesthetics
- **Calming Clinical Theme:** Crafted with a professional healthcare color palette featuring medical teals, ocean skies, emerald status indicators, and clean slate neutrals.
- **Premium Typography:** Integrated Google Fonts (`Plus Jakarta Sans` for body text and `Outfit` for display headings).
- **Hero Nurse Status Widget:** Displays real-time date, current shift status, active timings, and instant action buttons right at the top of the dashboard.
- **Visual Status Badges & Quick Action Cards:** High-contrast pill badges and elevated cards with gentle elevation shadows and smooth transitions.
- **Multi-Theme Engine:** Seamless switching between **Light**, **Dark**, and high-contrast **Neon** modes with the floating theme selector.

---

### 3. 💾 Built-In SQLite Database (`db.sqlite3`)
- **Zero-Setup Plug & Play:** The pre-migrated SQLite database (`db.sqlite3`) is now built into the repository.
- **Pre-Seeded Realistic Demo Data:** Comes out-of-the-box with:
  - Default nurse profile (`asha` with PIN `123456`)
  - 3 Village communities (`Shanti Nagar`, `Kalyanpur`, `Sundarpur`)
  - Multiple family households and individual patient records
  - Expectant mothers with upcoming delivery tracking
  - Ayushman card and ABHA digital health ID statuses
  - Pre-populated duty attendance records demonstrating the full workflow
- **Custom Seeder Command:** Easily reset or re-seed data anytime using `python manage.py seed_data`.

---

## 📱 Core Features Overview

| Feature | Description |
| :--- | :--- |
| **⏱️ Daily Attendance** | 1-click check-in/out, duty types, home visit counters, and printable monthly duty registers. |
| **⌂ Family Records** | Census management by village, house number, household head, and contact details. |
| **♙ Member Profiles** | Complete health records, blood groups, DOB, relationships, and medical history. |
| **🤰 Maternal Follow-ups** | Expected delivery date (EDD) tracking with instant alerts for mothers due this month. |
| **💳 Ayushman & ABHA** | Real-time monitoring of approved vs. pending government healthcare cards. |
| **👥 Age Demographics** | Interactive dynamic age-range filter slider to view community segments (e.g. toddlers, elderly). |
| **🔒 6-Digit PIN Security** | Fast, nurse-friendly PIN login designed for simple touch access without complex passwords. |
| **🖥️ Desktop App Mode** | Bundled PyWebView launcher to run as a native desktop window without needing a browser. |

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10+ (Recommended Python 3.12)
- Git

### 1. Clone & Switch to the Feature Branch
```bash
git clone https://github.com/Muneeb-hub411/My-Mom-Project-.git
cd My-Mom-Project-
git checkout feat/new-look-and-features
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Development Server
Because the built-in SQLite database is already migrated and seeded, you can launch immediately:
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

### 4. Login Credentials
- **Username:** `asha`
- **Security PIN:** `123456`

---

## 💻 Running as Native Desktop App

The application includes a desktop launcher powered by `pywebview` and `waitress`:
```bash
python launcher.py
```
This launches ASHA Care in a dedicated, distraction-free desktop window.

---

## 🛠️ Management & Utility Commands

### Re-seed Database Sample Data
To reset or refresh the built-in database with clean test families, pregnant mothers, and attendance records:
```bash
python manage.py seed_data
```

### Run Maternal Delivery Email Alerts
To send automated email reminders for deliveries expected within 2 days:
```bash
python manage.py pregnancy_alert
```

### Run Automated Tests
```bash
python manage.py test
```

---

## 📂 Project Structure

```
My-Mom-Project-/
├── config/                  # Django project configuration (settings, URLs, WSGI/ASGI)
│   ├── settings.py          # App settings (SQLite, WhiteNoise, Static)
│   └── urls.py              # Root URL routing
├── core/                    # Core healthcare application
│   ├── models.py            # Family, Member, Village, Attendance models
│   ├── views.py             # Dashboard, Attendance, Family & Member views
│   ├── urls.py              # Application routes
│   ├── admin.py             # Django admin panel registrations
│   ├── tests.py             # Unit and integration test suite
│   ├── management/commands/
│   │   ├── seed_data.py     # Database seeding command
│   │   └── pregnancy_alert.py # Maternal delivery reminder command
│   └── migrations/          # Database migrations (including Attendance)
├── static/                  # Static assets
│   ├── css/
│   │   ├── theme.css        # Modern healthcare theme & color variables
│   │   ├── style.css        # Base layout, typography & utility classes
│   │   ├── attendance.css   # Attendance widgets, KPIs & register tables
│   │   ├── dashboard.css    # Dashboard grid & pregnancy cards
│   │   └── login.css        # PIN authentication page styling
│   └── js/                  # Interactive JavaScript modules
├── templates/               # Django HTML templates
│   ├── dashboard.html       # Hero duty widget, pregnancy reminders & quick stats
│   ├── attendance_list.html # Attendance tracker & daily shift log
│   ├── attendance_edit.html # Duty entry editor
│   ├── attendance_report.html # Printable official PHC duty register
│   ├── login.html           # 6-digit PIN login
│   ├── family_list.html     # Village households
│   └── member_detail.html   # Detailed patient medical profile
├── db.sqlite3               # Built-in SQLite database (pre-migrated & seeded)
├── launcher.py              # Desktop runner (PyWebView)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🌿 Git Branch & Push Instructions

This work has been completed on the branch:
```bash
feat/new-look-and-features
```

To push this branch to your GitHub fork:
```bash
git push -u origin feat/new-look-and-features
```

---

## ❤️ Dedication

*Dedicated to my mom and to every community healthcare nurse and ASHA worker who selflessly walks the extra mile every single day to care for our villages and communities.*
