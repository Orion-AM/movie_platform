# 🎬 Movie Management Platform

A Django-based web application for managing movies, allowing a platform owner to add/edit/delete movies and view statistics, while users can view all listed movies in a Netflix-style interface.

---

## 📌 Features

### 🔐 Platform Owner
- Add, Edit, Delete movies
- Dashboard with:
  - Total number of movies
  - Movie count by genre
  - Full movie list with actions

### 👥 Public Users
- View all movies in a responsive, Bootstrap-styled layout
- Netflix-style card UI showing title, genre, and release date

### 🛠 Admin Panel
- Login via Django Admin at `/admin`
- Upload poster images
- Manage data through a simple interface

---

## 🗂 Tech Stack

- **Backend:** Django 4.x
- **Frontend:** Bootstrap 5
- **Database:** SQLite (default), Render-compatible
- **Deployment:** Render
- **Image Handling:** Django `ImageField` with local or optional cloud storage (Cloudinary/S3)

---
