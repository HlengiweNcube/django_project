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

## Final Architecture

django_project/
│
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
│
├── django_final/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── users/
├── inventory/
├── imports/
├── exports/
├── messaging/
│
├── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── images/

# PostgreSQL Integration

The application uses PostgreSQL as the primary relational database management system instead of SQLite.

A PostgreSQL database was provisioned using Render and connected securely to the Django application using environment variables.

---

## PostgreSQL Packages Installed

```bash
pip install psycopg2-binary dj-database-url python-dotenv
```

---

## Django Database Configuration

The default SQLite configuration was replaced with PostgreSQL configuration using `dj-database-url`.

```python
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
}
```

---

## Environment Variable Configuration

Sensitive database credentials were stored securely using environment variables.

A `.env` file was used locally:

```text
DATABASE_URL=postgresql://african_fashion_db_oxzx_user:CB7HtJEe8YqMAow2aVpo95nV1jCM7oNC@dpg-d7tib1egvqtc73cpf1eg-a.frankfurt-postgres.render.com/african_fashion_db_oxzx
```

Render environment variables were also configured for production deployment.

---

## Migration Process

Database migrations were successfully applied to PostgreSQL using:

```bash
python manage.py migrate
```


## Issue : PostgreSQL Host Translation Error

### Error

```text
could not translate host name
```

### Cause

The Render Internal Database URL was incorrectly used for local development.

### Solution

The External Database URL was used locally inside the `.env` file, while the Internal Database URL remained configured on Render.

This created all required authentication and session tables inside PostgreSQL.

---

## Benefits of PostgreSQL Integration

- Improved scalability
- Better production readiness
- Secure remote database hosting
- Strong relational database support
- Better alignment with enterprise web applications

The application was successfully deployed on Render and connected to a PostgreSQL production database using secure environment variables.

# Authentication and Authorization

The system uses Django's built-in authentication framework to manage user accounts securely.

## Features Implemented

- User registration
- User login/logout
- Session management
- Protected dashboard
- Password hashing
- Authentication validation

## Security Features

Django automatically hashes passwords before storing them in PostgreSQL using secure cryptographic hashing algorithms.

Protected routes were implemented using:

```python
@login_required
```

This prevents unauthorized users from accessing restricted pages.

# Inventory Management Setup

The inventory management module was initialized using Django models and PostgreSQL integration.

## Product Model

A Product model was created to store:

- Product name
- Category
- Quantity
- Price
- Description
- Creation date

## Database Integration

The inventory data is stored in PostgreSQL using Django ORM migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

This automatically generated the required PostgreSQL tables.

## Inventory Database Integration

The inventory module was developed using Django models integrated with PostgreSQL.

### Product Model

The Product model stores:

- Product name
- Category
- Quantity
- Price
- Description
- Creation timestamp

### Features Implemented

- Add products
- View products
- Store products in PostgreSQL
- Bootstrap inventory tables
- Authentication-protected inventory routes

### Database Migrations

Database tables were created using Django migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Authentication Protection

Inventory pages are protected using:

```python
@login_required
```

Unauthorized users are redirected to the login page.

### URLs

| Route | Description |
|---|---|
| `/products/` | Product list |
| `/products/add/` | Add new product |

### Technologies Used

- Django ORM
- PostgreSQL
- Bootstrap 5
- HTML Templates
- Python

# CRUD Operations Demonstration

The inventory system supports full CRUD functionality using Django ORM and PostgreSQL.

## Create

Products can be added through the Django form interface.

```sql
SELECT * FROM inventory_product;
```

New products appear immediately in PostgreSQL.

---

## Read

Products are displayed dynamically using Bootstrap tables.

The data is retrieved directly from PostgreSQL using Django ORM queries.

---

## Update

Existing products can be edited using the Update Product feature.

Updated values are immediately reflected in PostgreSQL.

---

## Delete

Products can be removed using the Delete Product feature.

Deleted records are removed from PostgreSQL permanently.

---

## PostgreSQL Verification

CRUD functionality was verified using SQL queries against the PostgreSQL database.

### Example Query

```sql
SELECT * FROM inventory_product;
```

# Import Management System

The application includes a complete Import Management module integrated with PostgreSQL and Django ORM.

## Features Implemented

- Add import records
- Link imports to inventory products
- Track supplier information
- Record import quantities
- Store import dates
- Automatic stock quantity updates

---

# Relational Database Design

The project demonstrates relational database principles using Django ForeignKey relationships.

## PostgreSQL Tables

| Table | Purpose |
|---|---|
| inventory_product | Stores product inventory |
| imports_importrecord | Stores import transactions |

---

# Foreign Key Relationship

The import system links products using:

```python
product = models.ForeignKey(Product, on_delete=models.CASCADE)
```

This creates a relational database relationship between imports and inventory products.

---

# Automatic Stock Updates

When a new import record is created:

1. A transaction is stored in `imports_importrecord`
2. The linked product quantity is automatically updated

Example:

| Product | Before Import | Imported | Final Quantity |
|---|---|---|---|
| T-Shirt | 50 | 20 | 70 |

This demonstrates backend business logic integration using Django ORM.

---

# PostgreSQL Verification

The following SQL query was used to verify import records:

```sql
SELECT * FROM imports_importrecord;
```

The following SQL query was used to verify inventory updates:

```sql
SELECT * FROM inventory_product;
```

---

# Frontend Features

The Import Management module includes:

- Bootstrap forms
- Bootstrap tables
- HTML5 date picker
- Authentication-protected routes

---

# CRUD Operations Demonstrated

| Operation | Description |
|---|---|
| Create | Add import records |
| Read | View import history |
| Update | Inventory quantities automatically updated |
| Delete | Records removable from PostgreSQL |

# Export Management System

The application includes a complete Export Management module integrated with Django and PostgreSQL.

## Features Implemented

- Add export records
- Track customer information
- Record exported quantities
- Store export dates
- Link exports to inventory products
- Automatic stock quantity reduction

---

# Relational Database Design

The export system uses Django ForeignKey relationships to connect export records with products stored in the inventory system.

## PostgreSQL Tables

| Table | Purpose |
|---|---|
| inventory_product | Stores current inventory products |
| exports_exportrecord | Stores export transactions |

---

# Automatic Inventory Reduction

When an export record is created:

1. A transaction is stored in `exports_exportrecord`
2. The linked product quantity is automatically reduced

### Example

| Product | Before Export | Exported | Remaining Stock |
|---|---|---|---|
| T-Shirt | 70 | 10 | 60 |

This demonstrates backend business logic integration using Django ORM and PostgreSQL.

---

# PostgreSQL Verification

The following SQL queries were used to verify export transactions and stock updates:

```sql
SELECT * FROM exports_exportrecord;
```
![alt text](image.png)

```sql
SELECT * FROM inventory_product;
```
![alt text](image-1.png)
---

# Frontend Features

The Export Management module includes:

- Bootstrap forms
- Bootstrap tables
- HTML5 date picker
- Authentication-protected routes

---

# CRUD Operations Demonstrated

| Operation | Description |
|---|---|
| Create | Add export records |
| Read | View export history |
| Update | Inventory quantities automatically reduced |
| Delete | Export records removable from PostgreSQL |

---

# Business Logic Demonstration

The system automatically synchronizes inventory quantities with import and export transactions.

- Imports increase stock quantities
- Exports reduce stock quantities

This demonstrates real-world inventory management functionality using relational databases and Django ORM.

# Dashboard and Inventory Monitoring

The system includes a dynamic dashboard for inventory monitoring and business analytics.

## Dashboard Features

- Total products counter
- Total imports counter
- Total exports counter
- Low stock alerts
- Dynamic inventory statistics

---

# Business Logic

The dashboard automatically retrieves data from PostgreSQL using Django ORM queries.

## Example ORM Queries

```python
Product.objects.count()

ImportRecord.objects.count()

ExportRecord.objects.count()
```

---

# Low Stock Monitoring

Products with stock quantities below 10 are automatically flagged as low stock items.

### Example Alert

```text
⚠ T-Shirt has low stock (7 remaining)
```
![alt text](image-2.png)

![alt text](image-3.png)
This demonstrates:

- Conditional rendering
- Real-time inventory monitoring
- Backend business logic
- Dynamic frontend updates

---

# Frontend Technologies

The dashboard interface uses:

- Bootstrap cards
- Bootstrap alerts
- Dynamic Django templates
- Responsive design

---

# PostgreSQL Integration

Dashboard statistics are generated directly from PostgreSQL tables using Django ORM aggregation queries.

## Additional Features

- User profile management
- Password reset functionality
- Email recovery support