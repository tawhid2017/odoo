# Mini Odoo Project (Portfolio Ready)

This repository is a **beginner-friendly Odoo 17 project** designed to showcase entry-level expertise in:

- **Python** (Odoo ORM model + validation + sequence handling)
- **PostgreSQL** (Odoo DB backend with Docker)
- **Custom Odoo module development** (`library_member` addon)

---

## Project Structure

```text
.
├── config/
│   └── odoo.conf
├── custom_addons/
│   └── library_member/
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── data/
│       │   └── library_member_sequence.xml
│       ├── models/
│       │   ├── __init__.py
│       │   └── library_member.py
│       ├── security/
│       │   └── ir.model.access.csv
│       └── views/
│           └── library_member_views.xml
├── docker-compose.yml
└── README.md
```

---

## What This Custom Module Does

Module: **`library_member`**

It introduces a new model called `library.member` with practical business fields:

- `member_code` (auto-generated using an Odoo sequence)
- `name`, `email`, `phone`
- `join_date`
- `membership_type` (`basic` / `premium`)
- `active`
- `notes`

### Implemented Odoo Concepts

- Model creation with `_name`, `_description`, and mixins (`mail.thread`, `mail.activity.mixin`)
- Form, tree, and search views
- Menu and action registration
- Access rights via `ir.model.access.csv`
- Sequence generation via XML data
- Python validation (`@api.constrains`) for email format

---

## Quick Start (Docker)

### 1) Prerequisites

- Docker
- Docker Compose

### 2) Run services

```bash
docker compose up -d
```

### 3) Open Odoo

Go to: [http://localhost:8069](http://localhost:8069)

### 4) Create database

On first load, create a new database from the Odoo UI.

### 5) Install the module

1. Activate **Developer Mode** in Odoo.
2. Go to **Apps**.
3. Click **Update Apps List**.
4. Search for **Library Member Management**.
5. Install it.

### 6) Test feature

- Navigate to **Library → Members**
- Create a new member
- Verify generated `member_code` (e.g., `MEM00001`)

---

## Useful Commands

```bash
# Start
docker compose up -d

# View logs
docker compose logs -f odoo

# Stop
docker compose down
```

---

## Why This Is Good for a Portfolio

This project clearly demonstrates you can:

- Run Odoo with PostgreSQL in a reproducible environment
- Build and register a custom addon
- Write Python business logic and validations
- Configure permissions and views
- Document setup and usage clearly for recruiters/interviewers

---

## Suggested Next Improvements

- Add a related model for borrowed books (`library.book.loan`)
- Add smart buttons and computed fields
- Add unit tests for model constraints
- Add a CI workflow (lint + tests)

---

## License

This mini project is provided for learning and portfolio purposes.
