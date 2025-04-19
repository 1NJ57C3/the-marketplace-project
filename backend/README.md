# Backend – Django API

## Setup

### Install Project and Dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip-compile requirements.in
pip install -r requirements.txt
```

---

## Database Setup

### Make and Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Configuring Environmental Variables

Use the included [`.env.example`](./.env.example) file as a template to create your own `.env` file. Name your file according to its environment type (e.g. `.env.dev`, `.env.prod`, `.env.test`).

This project defaults to `.env.dev.` If you want to use a different file, prepend Django commands with an `ENV` variable like so:

```bash
ENV=prod python manage.py runserver
```

> **Note**: This project comes with its own ENV-based config loader.

---

## Run Development Server

```bash
python manage.py runserver
```

---

## Backend Design & Architecture

A high-level overview of user data, product data, order processing, and other key features that drive the platform.

### Data Models

- **User** - Manages profile info, authentication roles (buyer/seller/staff), and preferences.
- **Product** - Stores listing data: title, description, price, category, tags, images.
- **Order** - Tracks cart contents, order status, and payment confirmation.

<!-- 
TODO
  ### API Structure
TODO
  - **Endpoints**: Main API routes supporting user actions, product queries, and checkout processing.
  // - `/[:user]/`: Manage client profile, preferences, history, vendor status, etc. // this is the frontend route 🤦🏻‍♂️
  ? - `/users/`: Profile, preferences, vendor info, etc. 
  ? - `/products`: Read-only for users, full CRUD for vendors
  ? - `/cart/`: Add/remove/edit cart contents
  ? - `/checkout`: Mock payment flow
-->

### Authentication

- **Flow**: Secure login and registration using token-based auth
- **Permissions**: Role-based access control (RBAC) to separate seller/buyer capabilities.

### Integrations

- **Payment Processors**: Intended Stripe integration using Test Mode
- **Image Storage**: Placeholder or S3-compatible image handling, depending on hosting requirements

---

## Tooling & Stack

This section outlines the key technologies used to build and manage the backend, including framework choices, database, and planned third-party integrations.

- ### [Django](https://djangoproject.com/)

  - Popular, proven Python web framework
  - Batteries-included conventions and ORMs

- ### [Django REST Framework](https://www.django-rest-framework.org/)

  - Serializer-based API framework
  - Clean separation of concerns between views, logic, and I/O

- ### [PostgreSQL](https://postgresql.org/)

  - Scalable, feature-rich SQL database
  - Strong compatibility with Django and complex rational data

- ### [**Stripe**](https://stripe.com/) or [**PayPal**](https://paypal.com/)

  - Intended to showcase real-world API integration
  - Stripe Test Mode is the planned approach for simulating payment safely
