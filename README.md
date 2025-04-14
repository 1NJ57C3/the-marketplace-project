# The Marketplace Project

A basic e-commerce site that handles user authentication, product listings, filtering/sorting, shopping carts, and order processing.

## Project Status

This project is currently in the early stages of development. More to come as features get fleshed out.

## Structure

This is a monorepo project with separate frontend and backend directories:

- [`frontend`](./frontend/README.md) - Vite + React + TypeScript UI
- [`backend`](./backend/README.md) - Python + Django + PostgreSQL API

Each subdirectory has its own README with setup instructions and implementation notes.

## Feature Roadmap

The project includes core e-commerce functionality, with features like user profiles, product catalog browsing, a shopping cart, and checkout. For a detailed list of planned features and stretch goals, see the [Feature Roadmap](./docs/roadmap.md).

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

### Expected Challenges

Some of the problems I currently foresee with possible solutions.

#### Race conditions due to abundance of fetch functionalities

- Re-research and strategize later... Something to do with using tokens to no longer accept pending fetch calls?

#### Excessive endpoint hits from autosave features

- Limit features using autosave
- Batch updates to reduce frequency of requests

#### Monthly limits

- Monitor fetch call and bandwidth usage as project develops. As The Marketplace Project is _not_ a live marketplace, this _should_ be a future-me problem.

#### Mocking complex legal/tax/licensing requirements for sellers involves information beyond my scope of knowledge

- Use placeholders to indicate that these details were purposely omitted, rather than overlooked.
- Possibly come back to this at the very end of the project, or only if there is intention to launch The Marketplace Project as a live service.

### Unexpected Obstacles

<!--
TODO
  Add content as we encounter roadblocks
-->

## Tooling & Stack

This section outlines technologies currently being evaluated for deployment, image handling, and other project infrastructure needs.

### Frontend Deployment

- [Vercel](https://vercel.com/)
  - Fast and free
  - Automates deployment via CI/CD Pipeline
    - Easy custom domain (DNS) setup
    > _Neither sponsored nor affilliated with Vercel... yet._ :elmorise:

### Backend Deployment

- [Render](https://render.com/)
- [fly.io](https://fly.io/)

### Backend Image Handling

- ImageField
- Pillow
- Amazon S3

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

You are free to:

- View, download, and use this project’s source code **for personal or educational purposes only.**

Under the following terms:

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests I endorse you or your use.
- **NonCommercial** — You may not use this material for commercial purposes.

For more details, see the [LICENSE](./LICENSE.txt) file or visit the [Creative Commons website](https://creativecommons.org/licenses/by-nc/4.0/).

> **Note:** This license does not grant permission for commercial use or distribution of this project. If you are interested in licensing this project for commercial purposes, please contact me directly.
