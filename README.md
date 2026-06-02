# Frameworks Assignment: Django Stock Management System

A modular Django web application that uses PostgreSQL for persistent data storage and includes authentication, authorization, inventory operations, import/export tracking, and internal messaging.

## Live Deployment

- Hosted URL: https://django-project-e9gn.onrender.com
- Hosting provider: Render

## Core Features Implemented

### 1) User Management

- User registration and login/logout
- Profile update (username, email, first/last name)
- Contact details update (phone, address, city, country, postal code)
- Password reset flow using Django auth views and email backend
- Protected routes using Django authentication decorators

### 2) Data Storage and Categorization

- Products with category, quantity, price, and description
- Projects with name, description, start/end dates, stakeholders, status, and category
- Import records linked to products and suppliers
- Export records linked to products and customers
- Internal messages (sender, receiver, subject, content, archive flag)

### 3) Inbox Functionality

- Send messages to other users
- Receive messages in inbox
- Archive messages
- Archive action restricted to intended receiver

### 4) Authorization (Roles and Permissions)

- Roles implemented with Django Groups:
  - `Manager`: full CRUD permissions for products, projects, imports, exports, and messages
  - `Staff`: view-only inventory/project/import/export permissions, plus send/view messages
- New users are assigned to `Staff` by default at registration
- Write actions are protected with `permission_required` decorators

### 5) Frontend Stack

- Django Templates with a shared base layout
- Bootstrap 5 responsive UI
- JavaScript product search (`static/js/product_search.js`)
- JavaScript form validation (`static/js/form_validation.js`)
- Responsive profile update layout with clearer labels, helper text, and larger tap targets
- Accessibility improvements including skip links, visible focus states, and descriptive form labels

### 6) Security Controls

- Password storage handled by Django's built-in hashing
- Environment-based `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS`
- Secure cookie/HTTPS/HSTS settings enabled in production
- Whitenoise static file pipeline for production

### 7) Static File Naming (Why You See Multiple CSS Files)

After running `collectstatic`, Django/Whitenoise can generate multiple versions of the same asset in `staticfiles/`.

Example:

- `autocomplete.css`: normal file name
- `autocomplete.css.gz`: pre-compressed gzip version for faster transfer
- `autocomplete.d24f10bdee41.css`: hashed file name used for cache busting
- `autocomplete.d24f10bdee41.css.gz`: gzipped version of the hashed file

Why this exists:

- Hash in filename ensures browsers fetch updated assets when content changes
- `.gz` versions let the server send smaller files when supported by the browser
- These are build/deployment artifacts and are usually not edited manually

You may also see generated admin JavaScript files in `staticfiles/admin/js/` (for example hashed and `.gz` variants of `jquery.init.js`). These are produced by Django static collection and should be treated as generated output.

### 8) Development Workspace Note (Explorer Noise)

To keep the project view clean during development, generated folders are hidden in VS Code Explorer via workspace settings:

- `staticfiles/`
- `venv/`
- `__pycache__/`
- `*.pyc`

These files/folders are build or environment artifacts and are not part of the app source code.

## Project Structure

```text
django_project/
  manage.py
  requirements.txt
  .env.example
  Procfile
  runtime.txt
  render.yaml
  django_final/
    settings.py
    urls.py
    wsgi.py
  user_management/
  inventory/
  imports/
  exports/
  messaging/
  templates/
  static/
```

Full generated structure evidence is included in this repository as:

- `project_structure_tree.txt`

This file was generated from the project root and provides a complete tree listing that can be used for submission review.

## Local Setup

### 1) Clone and enter project

```bash
git clone https://github.com/HlengiweNcube/django_project.git
cd django_project
```

### 2) Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

Copy `.env.example` to `.env` and update values.

```bash
copy .env.example .env
```

### 5) Apply migrations

```bash
python manage.py migrate
```

### 6) Create superuser (admin account)

```bash
python manage.py createsuperuser
```

You will be prompted for:

- Username
- Email address (optional)
- Password

After creation, log in to Django Admin at:

- http://127.0.0.1:8000/admin/

Use this superuser account to:

- Manage users and groups
- Assign users to `Manager` or `Staff`
- Access all admin-managed data

### 7) Run the app

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000

## PostgreSQL Configuration

Set `DATABASE_URL` in `.env`:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/django_final
```

Example psql commands:

```sql
CREATE DATABASE django_final;
CREATE USER django_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE django_final TO django_user;
```

Then use:

```env
DATABASE_URL=postgresql://django_user:your_password@localhost:5432/django_final
```

## Email Configuration (Password Reset)

Use SMTP settings in `.env`:

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=your_email@gmail.com
```

For local development, console backend is supported:

```env
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

## Deployment on Render

### Required files

- `Procfile`
- `runtime.txt`
- `render.yaml`

### Render settings

- Build command:

```bash
pip install -r requirements.txt
```

- Start command:

```bash
gunicorn django_final.wsgi:application
```

### Render Environment Variables

- SECRET_KEY
- DEBUG=False
- DATABASE_URL
- ALLOWED_HOSTS
- EMAIL_HOST
- EMAIL_PORT
- EMAIL_HOST_USER=your_email@gmail.com
- EMAIL_HOST_PASSWORD=your_gmail_app_password
- EMAIL_USE_TLS
- DEFAULT_FROM_EMAIL

### Post-deployment checks

```bash
python manage.py migrate
python manage.py createsuperuser
```

Verify:

- Login/register flow
- Password reset pages and email send
- Product, import, export, messaging screens
- Static assets loaded correctly

## Tests

Run all tests:

```bash
python manage.py test
```

Coverage includes:

- Registration and auth gate checks
- Permission boundaries for product creation
- Stock changes from import/export records
- Message archive authorization

## Assignment Rubric Mapping

- Django key concepts: multi-app architecture, forms, views, templates, URL routing, admin
- Database integration: PostgreSQL via `dj-database-url` and relational models with foreign keys
- Authentication/authorization: login/register/password reset, role permissions using Django groups
- Frontend quality: Bootstrap templates + JavaScript interactions
- Hosted app evidence: Render deployment and live URL

## Included in the ZIP File

- All Django source files
- Deployment files (`Procfile`, `runtime.txt`, `render.yaml`)
- `requirements.txt`
- `README.md`
