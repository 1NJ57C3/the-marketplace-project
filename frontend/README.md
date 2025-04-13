# Frontend – React + TypeScript

## Installation and Setup

### Installation

To install project dependencies, navigate to the project repo in your CLI and use the following commands according to your package manager:

**Note**: This project uses [`pnpm`](https://pnpm.io/) by default, but fallback commands for `npm` are also included for compatibility.

`pnpm`:

```shell
pnpm install
```

`npm`:

```shell
npm install
```

### Setup - Running the App Server

Once installed, start the app server to demo the app locally.

`pnpm`:

```shell
pnpm run dev
```

`npm`:

```shell
npm run dev
```

### Open App UI

Open your preferred browser and navigate to `localhost:5173`.

> _Note_: As a general rule of thumb, I recommend always using an Incognito tab if localStorage or persistent cookies aren't essential. This will help minimize necessary maintenance.

## Frontend Component Structure

A high-level overview of anticipated key UI components (e.g., ProductCard, SellerProfile) to capture my front-end approach.  

- UI logic is modularized using the `features/` and `shared/components/` pattern for scalability and reuse.  

### Navigation

- **Main Header**: Displays promotional sales or important notices.
- **Nav Bar**: Logo links to root, product categories.
- **Search Bar**: Autocomplete suggestions based on user input.

### User Profile

- **Profile Info**: Includes name, contact details, shipping and billing addresses and payment preferences.
- **Order History**: Displays past purchases and pending orders.
- **User Preferences**: Site configuration settings.
- **Support**: Access to support ticket management.

### Product Display

- **Product Grid**: Shows featured items by default with sorting and pagination options.
- **_Stretch Goal_**: Design "algorithm" for recommendations features and default product sorting.
- **Filter Menu**: Allows filtering by brand, seller, color, category, subcategories, etc.

### Shopping Cart

- **Cart Sidebar**: Lists items in cart, including product name, image, price, and desired quantities.
- **Subtotal & Total**: Dynamically updated with cart changes.

### Payment Processing

- **Payment Form**: Placeholder integration for Stripe or PayPal, simulating payment confirmation.

## Tooling & Stack

This section outlines the tools and libraries used in the frontend, including build tools, testing frameworks, and runtime libraries — and why they were chosen.

- ### [Vite](https://vite.dev/)

  - Fast and efficient way to scaffold JavaScript projects.

- ### [Vitest](https://vitest.dev/)

  - Vite-native unit testing framework.
  - Streamlines testing.
  - Testing XP gainz.

- ### [testing-library/react](https://testing-library.com/docs/react-testing-library/intro/)

  - Expands Vitest functionality by providing means to test UI components as rendered by client.
  - Moar testing/integration XP gainz!

- ### [Cypress](https://cypress.io/)

  - Browser-based (end-to-end/component) testing.
  - A strong contender where Vitest is weak.
  - Moar testing gainz.

- ### [React](https://react.dev/) + [TypeScript](https://typescriptlang.org/)

  - TypeScript for scalability and to help ensure dynamic data retains the correct shapes through lifecycle.
  - Deepen frontend mastery.

- ### [SWC](https://swc.rs/)

  - Reduces build times over Babel by 20x.
  - Experiment with alternative tooling.

<!--
- ### [styled-components](https://styled-components.com/)

  - Modularizes CSS by coupling stylesheets with JS components, simplifying maintenance.
  - Facilitates learning and best practices in component-driven styling.
 -->
