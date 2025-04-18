# 🧭 Project Milestones Overview

> This file tracks all core development milestones for `the-marketplace-project`. Each milestone links to its own checklist and is broken into achievable, testable goals. Stretch goals are included but optional.

---

## ✅ Milestone 1: Project Setup & Role Scaffolding

- [x] Clean and organize monorepo folder structure
- [x] Scaffold Django project in `backend/`
- [x] Scaffold React + Vite project in `frontend/`
- [x] Configure PostgreSQL locally
- [x] Set up custom User model with `is_seller`
- [x] Install and configure DRF
- [x] Create registration serializer and endpoint
- [x] Create basic User viewset and route
- [x] Add `.env` config and environment switching
- [x] Add `AUTH_USER_MODEL` to settings
- [ ] Optional: ESLint, Prettier, basic test setup

---

## 🔐 Milestone 2: Authentication Flow

- [x] Set up `UserCreateSerializer` with password confirmation
- [x] Add registration endpoint with CreateAPIView
- [ ] Install and configure JWT (`djangorestframework-simplejwt`)
- [ ] Add login route (`/api/token/`)
- [ ] Add refresh route (`/api/token/refresh/`)
- [ ] Create `/me/` user detail route (or equivalent)
- [ ] Add view-level access control using DRF permissions
- [ ] Optional: Token blacklist / logout flow
- [ ] Optional: Email/password reset scaffolding

---

## 🛒 Milestone 3: Product Browsing (Buyer UX)

- [ ] Add `Product` model on backend
- [ ] Create product list and detail endpoints:
  - [ ] `GET /products/`
  - [ ] `GET /products/:id`
- [ ] Build product grid + filter UI
- [ ] Add product detail page with "Add to Cart"
- [ ] Optional: Product hover previews or badges

---

## 🛍️ Milestone 4: Shopping Cart & Checkout

- [ ] Create cart context/store (Zustand or Context API)
- [ ] Add item add/remove/modify cart actions
- [ ] Show cart summary in header/nav
- [ ] Build checkout flow:
  - [ ] Address form
  - [ ] Payment placeholder
- [ ] Backend: `POST /orders/` endpoint
- [ ] Optional: Confirmation screen with summary

---

## 🧑‍💼 Milestone 5: Seller Dashboard (Product Management)

- [ ] Add seller-only dashboard route
- [ ] Build `Create Product` form
- [ ] List seller’s active listings
- [ ] Enable edit/delete for own products
- [ ] Backend: Secure write routes for seller role
- [ ] Optional: Product "draft" support

---

## 🧑‍⚖️ Milestone 6: Admin / Staff Capabilities

- [ ] Ensure `is_staff` flag functions correctly
- [ ] Add basic admin moderation panel (MVP or placeholder)
- [ ] Build user/product moderation actions
- [ ] Optional: Staff-only event/notice banner tool

---

## 🌐 Milestone 7: Deployment & Production Readiness

- [ ] Add production `.env`, Procfile, and WSGI/asgi config
- [ ] Deploy backend (Render, Fly.io, or similar)
- [ ] Deploy frontend (Vercel or Netlify)
- [ ] Optional: Subdomain or domain connection
- [ ] Optional: CI/CD pipeline (GitHub Actions)

---

## 🧼 Milestone 8: Polish & Portfolio Readiness

- [ ] Responsive layout and accessibility pass
- [ ] Mobile polish and interactive tweaks
- [ ] Add demo user toggle or login bypass
- [ ] Final README pass w/ project summary
- [ ] Create walkthrough video or screencaps

---

## 📄 Milestone 9: Documentation & Reflection

- [ ] Finalize `README.md` (overview, features, stack, install, usage)
- [ ] Update `notes.md`:
  - [ ] Architecture or design decisions
  - [ ] Challenges + solutions
  - [ ] Stretch thoughts and “what I’d change”
- [ ] Optional: Blog post or devlog write-up
