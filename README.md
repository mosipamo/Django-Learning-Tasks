# Django Learning Tasks

A collection of Django projects demonstrating various web development concepts and features. This repository contains 8 different Django applications, each focusing on specific functionality and learning objectives.

## 📚 Projects Overview

### 1. **Hello World** 
*Basic Django Setup*
- **Path:** `Hello-World/`
- **Description:** A simple Django starter project demonstrating basic Django setup and configuration
- **Purpose:** Introduction to Django project structure and basic concepts

### 2. **Blog**
*Content Management System*
- **Path:** `Blog/`
- **Description:** A blog application with post listing, detail views, and static content management
- **Features:**
  - Post display with images and excerpts
  - Individual post detail pages
  - Static file management for images and CSS
  - Template inheritance and includes
- **Purpose:** Learn Django templates, static files, and basic content display

### 3. **Job Board**
*CRUD Operations & Database Models*
- **Path:** `Job-Board/`
- **Description:** A job posting platform with company listings and job management
- **Features:**
  - Job posting model with title, description, company, salary
  - Active/inactive job status
  - Database operations (CRUD)
- **Purpose:** Master Django models, migrations, and database operations

### 4. **Restaurant**
*REST API Development*
- **Path:** `Restaurant/`
- **Description:** A restaurant menu API built with Django REST Framework
- **Features:**
  - Menu item management
  - RESTful API endpoints
  - Serializers for data handling
- **Purpose:** Learn Django REST Framework and API development

### 5. **Links Shortener**
*URL Management & Custom Logic*
- **Path:** `Links-Shortener/`
- **Description:** A URL shortening service with click tracking
- **Features:**
  - Custom URL slug generation
  - Click counter functionality
  - Form handling for link creation
  - Automatic slug creation from names
- **Purpose:** Understand custom model methods, forms, and business logic

### 6. **Link Plant**
*Relationships & Profile Management*
- **Path:** `Link-Plant/`
- **Description:** A "link in bio" style application for managing personal link collections
- **Features:**
  - User profiles with customizable backgrounds
  - Multiple links per profile
  - One-to-many relationships (Profile → Links)
  - CRUD operations for links
- **Purpose:** Learn Django relationships, advanced models, and profile management

### 7. **PersonaPort**
*Portfolio & File Handling*
- **Path:** `PersonaPort/`
- **Description:** A personal portfolio website with comprehensive profile management
- **Features:**
  - Personal profile with bio and image
  - Social media links management
  - Project showcase
  - Education history
  - CV/Resume file upload
  - Media file handling
- **Purpose:** Master file uploads, complex model relationships, and portfolio development

### 8. **Favorite Books**
*Template & Static Files*
- **Path:** `Favorite-Books/`
- **Description:** A simple application for displaying favorite movies/books
- **Features:**
  - Static content display
  - Template management
  - Basic routing
- **Purpose:** Practice template creation and static file organization

## 🛠️ Technology Stack

- **Framework:** Django
- **Database:** SQLite3 (default for all projects)
- **Frontend:** HTML, CSS, JavaScript
- **API:** Django REST Framework (Restaurant project)
- **File Handling:** Django's built-in file upload system
- **Environment:** Virtual environments for each project

## 🚀 Getting Started

Each project is self-contained with its own virtual environment and dependencies. To run any project:

1. Navigate to the project directory:
   ```bash
   cd [Project-Name]/
   ```

2. Activate the virtual environment:
   ```bash
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations (if applicable):
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## 📖 Learning Progression

These projects are designed to build upon each other, covering:

1. **Basic Django Setup** (Hello World)
2. **Templates & Static Files** (Blog, Favorite Books)
3. **Models & Database** (Job Board)
4. **Forms & Custom Logic** (Links Shortener)
5. **Model Relationships** (Link Plant)
6. **File Handling & Complex Models** (PersonaPort)
7. **API Development** (Restaurant)

## 📁 Project Structure

Each project follows Django's standard structure:
- `config/` - Main project settings and configuration
- `[app_name]/` - Individual Django applications
- `templates/` - HTML templates
- `static/` - CSS, JavaScript, and image files
- `media/` - User-uploaded files (where applicable)
- `requirements.txt` - Python dependencies
- `manage.py` - Django management script

---

<!-- *This repository serves as a comprehensive learning journey through Django web development, from basic concepts to advanced features.* -->