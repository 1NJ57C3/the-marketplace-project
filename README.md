# The Marketplace Project

A basic e-commerce site that handles user authentication, product listings, filtering/sorting, shopping carts, and order processing.

## Project Status

This project is currently in the early stages of development. More to come as features get fleshed out.

### Feature Roadmap

The project includes core e-commerce functionality, with features like user profiles, product catalog browsing, a shopping cart, and checkout. For a detailed list of planned features and stretch goals, see the [Feature Roadmap](./docs/roadmap.md).

## Installation and Setup

### Installation

To install project dependencies, navigate to the project repo in your CLI and use the following commands according to your package manager:

`pnpm`:

```shell
pnpm install
```

`npm`:

```shell
npm install
```

### Test Suite

<!-- TODO -->

### Run App Server

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

## Notes/Reflections

### Motivation

I felt my current collection of personal projects were somewhat outdated, and wanted to create something new and somewhat more practical than I have in the past.

My idea is to build an e-commerce site, drawing inspiration from eBay or Amazon, where users can shop for products sold by various vendors, organized by categories, brands, reviews, etc. This style of project offers flexibility to showcase business-oriented backend data management, complex fetch requests, and structured front-end interactions.

### Objective

Showcase a range of proven skills including, but not limited to:

#### Backend knowledge

- Database management
- Secure authentication
  - User permissions (e.g., user vs. admin roles)
- Integrations with third-party services
- Product filtering
- Transaction handling

#### Ability to

- Create convincing mock workflows and user experiences
- Independently develop complex production-level projects

<!-- // VISUAL BREAK -->

### Frontend Component Structure

A high-level overview of anticipated key UI components (e.g., ProductCard, SellerProfile) to capture my front-end approach.

#### Navigation

- **Main Header**: Displays promotional sales or important notices.
- **Nav Bar**: Logo links to root, product categories.
- **Search Bar**: Autocomplete suggestions based on user input.

#### User Profile

- **Profile Info**: Includes name, contact details, shipping and billing addresses and payment preferences.
- **Order History**: Displays past purchases and pending orders.
- **User Preferences**: Site configuration settings.
- **Support**: Access to support ticket management.

#### Product Display

- **Product Grid**: Shows featured items by default with sorting and pagination options.
- **_Stretch Goal_**: Design "algorithm" for recommendations features and default product sorting.
- **Filter Menu**: Allows filtering by brand, seller, color, category, subcategories, etc.

#### Shopping Cart

- **Cart Sidebar**: Lists items in cart, including product name, image, price, and desired quantities.
- **Subtotal & Total**: Dynamically updated with cart changes.

#### Payment Processing

- **Payment Form**: Placeholder integration for Stripe or PayPal, simulating payment confirmation.

<!-- // VISUAL BREAK -->

### Backend Design & Architecture

A high-level overview of user data, product data, order processing, and other features that drive the platform.

#### Data Models

- **User**: Handles profile information, authentication roles (e.g., buyer, seller), and user-specific preferences.
- **Product**: Stores details on each listing, including price, description, categories, and images.
- **Order**: Tracks items in the user's cart, order status, and payment confirmation.

<!-- 
TODO
  #### API Structure
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

#### Authentication

- **Flow**: Manages secure login and registration, with role-based permissions to differentiate access levels for buyers and sellers.
- **Permissions**: Differentiates features for user roles, like product management for sellers.

#### Integrations

- **Payment Processors**: Integrations with services like Stripe to handle simulated payment flow.
- **Image Storage**: Stores or caches images using services like Amazon S3 or placeholders for scalability.

<!-- // VISUAL BREAK -->

### Expected Challenges

Some of the problems I currently foresee with possible solutions.

#### Race conditions due to abundance of fetch functionalities

- Re-research and strategize later... Something to do with using tokens to no longer accept pending fetch calls?

#### Excessive endpoint hits from autosave features

- Limit features using autosave
- Batch updates to reduce frequency of reqeusts

#### Monthly limits

- Monitor fetch call and bandwidth usage as project develops. As The Marketplace Project is _not_ a live marketplace, this _should_ be a future-me problem.

#### Mocking complex legal/tax/licensing requirements for sellers involves information beyond my scope of knowledge

- Use placeholders to indicate that these details were purposely omitted, rather than overlooked.
- Possibly come back to this at the very end of the project, or only if there is intention to launch The Marketplace Project as a live service.

<!-- // VISUAL BREAK -->

### Unexpected Obstacles

<!--
TODO
  Add content as we encounter roadblocks
-->

### Tools/Tech Selection

These are the technologies I have chosen for this project, along with some of the reasons they were selected.

- #### [Vite](https://vite.dev/)

  - Fast and efficient way to scaffold JavaScript projects.

- #### [Vitest](https://vitest.dev/)

  - Vite-native unit testing framework.
  - Streamlines testing.
  - Testing XP gainz.

- [testing-library/react](https://testing-library.com/docs/react-testing-library/intro/)

  - Expands Vitest functionality by providing means to test UI components as rendered by client.
  - Moar testing/integration XP gainz!

- #### [Cypress](https://cypress.io/)

  - Browser-based (end-to-end/component) testing.
  - A strong contender where Vitest is weak.
  - Moar testing gainz.

- #### [React](https://react.dev/) + [TypeScript](https://typescriptlang.org/)

  - TypeScript for scalability and to help ensure dynamic data retains the correct shapes through lifecycle.
  - Deepen frontend mastery.

- #### [SWC](https://swc.rs/)

  - Reduces build times over Babel by 20x.
  - Experiment with alternative tooling.

<!--
- #### [styled-components](https://styled-components.com/)

  - Modularizes CSS by coupling stylesheets with JS components, simplifying maintenance.
  - Facilitates learning and best practices in component-driven styling.
 -->

- #### [Django](https://djangoproject.com/)

  - Reinforce [Python](https://python.org/) skills whilst building familiarity with Django methodologies.

- #### [PostgreSQL](https://postgresql.org/)

  - A robust, scalable relational database, suitable for managing complex data structures.

- #### [**Stripe**](https://stripe.com/) or [**PayPal**](https://paypal.com/)

  - Demonstrate ability to integrate real-world third party services.
  - Leverage Stripe API's Test Mode as a safeguard against accidental payment processing.
  - Build practical knowledge of payment API methodologies and best practices.

<!--
- #### [Vercel](https://vercel.com/)

  - Fast and free
  - Automates deployment via CI/CD Pipeline
  - Easy custom domain (DNS) setup

    > _Neither sponsored nor affilliated with Vercel... yet._ :elmorise:
-->

<!--
Researching:
  for backend image handling:
  - ImageField
  - Pillow
  - Amazon S3
-->

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

You are free to:

- View, download, and use this project’s source code **for personal or educational purposes only.**

Under the following terms:

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests I endorse you or your use.
- **NonCommercial** — You may not use this material for commercial purposes.

For more details, see the [LICENSE](./LICENSE.txt) file or visit the [Creative Commons website](https://creativecommons.org/licenses/by-nc/4.0/).

> **Note:** This license does not grant permission for commercial use or distribution of this project. If you are interested in licensing this project for commercial purposes, please contact me directly.
