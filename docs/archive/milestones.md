# 🧭 Project Milestones Overview

> This file tracks all core development milestones for `the-marketplace-project`. Each milestone links to its own checklist and is broken into achievable, testable goals. Stretch goals are included but optional.

---

## ✅ Milestone 1: Project Setup & Role Scaffolding

[View checklist →](docs/milestone-1-setup.md)

- [x] Clean and organize project folder structure
- [ ] Scaffold auth system on both frontend and backend
- [ ] Implement basic role switching and login/logout
- [ ] Establish page routing and role-aware navigation
- [ ] Optional: ESLint, Prettier, basic test setup

---

## 🛒 Milestone 2: Product Browsing (Buyer UX)

- [ ] Add `Product` model on backend
- [ ] Create API endpoints for:
  - [ ] `GET /products/`
  - [ ] `GET /products/:id`
- [ ] Build product list page with filters/sorting
- [ ] Build product detail page with "Add to Cart" button
- [ ] Optional: Product preview hover interactions

---

## 🛍️ Milestone 3: Shopping Cart & Checkout

- [ ] Create cart context or store (Zustand/Context)
- [ ] Allow adding/removing/modifying cart items
- [ ] Display cart summary on navbar
- [ ] Build checkout page:
  - [ ] Address form
  - [ ] Payment placeholder
- [ ] Create order submission endpoint (POST `/orders/`)
- [ ] Optional: Order confirmation with receipt summary

---

## 📦 Milestone 4: Seller Dashboard (Product Management)

- [ ] Create seller-only dashboard route
- [ ] Build `Create Product` form
- [ ] Show list of seller's products
- [ ] Enable editing and deleting own listings
- [ ] Secure backend endpoints by role
- [ ] Optional: Product "draft" save state support

---

## 🧑‍💼 Milestone 5: Admin / Staff Capabilities

- [ ] Add `is_staff` or `is_admin` role to User model
- [ ] Build basic admin panel for moderation
- [ ] Enable deletion/ban/reporting tools (MVP or placeholder only)
- [ ] Optional: Sales/event notice management panel

---

## 🌐 Milestone 6: Deployment & Production Readiness

- [ ] Add `Procfile`, `requirements.txt`, and production config
- [ ] Deploy backend to Render/Fly.io/Vercel function (or preferred)
- [ ] Deploy frontend to Vercel/Netlify
- [ ] Connect domain or subdomain (optional)
- [ ] Optional: CI/CD pipeline (e.g., GitHub Actions)

---

## 🧼 Milestone 7: Polish & Portfolio Readiness

- [ ] Responsive layout and accessibility improvements
- [ ] Mobile UX polish
- [ ] Final README cleanup with feature map
- [ ] Add demo user account or skip login toggle
- [ ] Create project walkthrough video or GIF demo

---

## 📄 Milestone 8: Documentation & Reflection

- [ ] Update `README.md` with:
  - [ ] Overview, stack, features
  - [ ] Installation + usage
  - [ ] Future roadmap
- [ ] Add `docs/notes.md` with:
  - [ ] Challenges + solutions
  - [ ] Design decisions
  - [ ] Stretch ideas + what you’d do differently
- [ ] Optional: Add blog post or devlog summary

---
