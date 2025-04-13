# Backend – Django API

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Development Server

```bash
python manage.py runserver
```

## Backend Design & Architecture

A high-level overview of user data, product data, order processing, and other features that drive the platform.

### Data Models

- **User**: Handles profile information, authentication roles (e.g., buyer, seller), and user-specific preferences.
- **Product**: Stores details on each listing, including price, description, categories, and images.
- **Order**: Tracks items in the user's cart, order status, and payment confirmation.

<!-- 
TODO
  ### API Structure
TODO
  - **Endpoints**: Main API routes supporting user actions, product queries, and checkout processing.
  ? - `/products`:
    ? - Regular users can only retrieve product information
    ? - Vendors can also post products
  ? - `/[:user]/`: Manage client profile, preferences, history, vendor status, etc.
  ? - `/cart/`: Manage items in user's cart (add/remove items, modify quantities)
  ? - `/checkout`: Mock order processing
    - etc
-->

### Authentication

- **Flow**: Manages secure login and registration, with role-based permissions to differentiate access levels for buyers and sellers.
- **Permissions**: Differentiates features for user roles, like product management for sellers.

### Integrations

- **Payment Processors**: Integrations with services like Stripe to handle simulated payment flow.
- **Image Storage**: Stores or caches images using services like Amazon S3 or placeholders for scalability.

## Tooling & Stack

This section outlines the key technologies used to build and manage the backend, including framework choices, database, and planned third-party integrations.

- ### [Django](https://djangoproject.com/)

  - Reinforce [Python](https://python.org/) skills whilst building familiarity with Django methodologies.

- ### [Django REST Framework](https://www.django-rest-framework.org/)

  - Enables robust API development and serializer-based data handling for frontend integration.

- ### [PostgreSQL](https://postgresql.org/)

  - A robust, scalable relational database, suitable for managing complex data structures.

- ### [**Stripe**](https://stripe.com/) or [**PayPal**](https://paypal.com/)

  - Demonstrate ability to integrate real-world third party services.
  - Leverage Stripe API's Test Mode as a safeguard against accidental payment processing.
  - Build practical knowledge of payment API methodologies and best practices.
