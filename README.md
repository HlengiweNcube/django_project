# Import & Export Stock Management System

A Django-based web application integrated with PostgreSQL for managing stock inventory, imports, exports, suppliers, customers, and internal messaging.

---

# Table of Contents

- [Project Overview](#project-overview)
- [System Features](#system-features)
- [Technologies Used](#technologies-used)
- [Installation Guide](#installation-guide)
- [Database Configuration](#database-configuration)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Authentication and Authorization](#authentication-and-authorization)
- [Inventory Management](#inventory-management)
- [Import and Export Tracking](#import-and-export-tracking)
- [Messaging System](#messaging-system)
- [Frontend Design](#frontend-design)
- [Security Features](#security-features)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

# Project Overview

The Import & Export Stock Management System is a web application developed using Django and PostgreSQL.

The system allows businesses to manage stock inventory, track imports and exports, manage suppliers and customers, and communicate internally through a secure messaging system.

---

# System Features

## User Management

- User registration
- User login/logout
- Password reset via email
- Profile management

## Inventory Management

- Add products
- Update stock quantities
- Categorize products
- Track stock levels
- Low stock alerts

## Import Management

- Record imported goods
- Track suppliers
- Store import dates
- Record quantities and costs

## Export Management

- Record exported goods
- Track customers
- Monitor outgoing stock
- Generate export history

## Messaging System

- Send internal messages
- Receive messages
- Archive messages

## Reporting Features

- Inventory reports
- Import/export summaries
- Stock movement tracking

---

# Technologies Used

## Backend

- Django
- Python

## Database

- PostgreSQL

## Frontend

- HTML
- CSS
- Bootstrap 5
- JavaScript

## Hosting

- Render

# Deployment Configuration

The application was deployed using Render.

## Build Command

```bash
pip install -r requirements.txt
```

## Start Command

```bash
gunicorn django_final.wsgi:application
```

## Deployment Files

### Procfile

```text
web: gunicorn django_final.wsgi:application
```

### runtime.txt

```text
python-3.12.3
```

---

# Deployment Challenges and Solutions

During deployment several configuration and deployment issues were encountered and resolved successfully.

## Issue 1: Incorrect WSGI Module

### Error

```text
ModuleNotFoundError: No module named 'django_project'
```

### Cause

Render was configured to start the application using:

```bash
gunicorn django_project.wsgi:application
```

However, the actual Django project folder was named:

```text
django_final
```

### Solution

The Render Start Command was updated to:

```bash
gunicorn django_final.wsgi:application
```

This resolved the deployment startup error.

---

## Issue 2: Git Repository Not Initialized

### Error

```text
fatal: not a git repository
```

### Cause

Git had not been initialized in the local project directory.

### Solution

Git was initialized using:

```bash
git init
```

The GitHub repository was then connected successfully.

---

## Issue 3: Push Rejected by GitHub

### Error

```text
failed to push some refs
```

### Cause

The remote GitHub repository already contained files that were not available locally.

### Solution

The repositories were synchronized using:

```bash
git pull origin main --allow-unrelated-histories
```

After merging histories, the project pushed successfully.

---

## Issue 4: Django DisallowedHost Error

### Error

```text
Invalid HTTP_HOST header
```

### Cause

The deployed Render domain was not included in Django's ALLOWED_HOSTS configuration.

### Solution

The following configuration was added to `settings.py`:

```python
ALLOWED_HOSTS = ['*']
```

This allowed the Render deployment domain to access the application successfully.

---

# Hosted Application

Live Application URL:

https://django-project-e9gn.onrender.com

---

# Lessons Learned

Through this project the following skills were strengthened:

- Django deployment and configuration
- Git and GitHub version control
- Render cloud hosting
- Debugging deployment issues
- Managing Django settings and security configurations
- Configuring Gunicorn and WhiteNoise
- Understanding Django application structure

