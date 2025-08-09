# PersonaPort 🚀

A modern, elegant one-page portfolio website built with Django. PersonaPort allows you to showcase your professional profile, projects, education, and social links in a clean, responsive design.

## ✨ Features

- **Professional Profile Display**: Name, title, bio, and profile image
- **Project Showcase**: Display your projects with descriptions and links
- **Education Section**: Highlight your educational background
- **Social Media Integration**: Add social media links with Font Awesome icons
- **CV/Resume Upload**: Allow visitors to download your CV
- **Admin Interface**: Easy content management through Django Admin
- **Responsive Design**: Looks great on desktop and mobile devices
- **Media File Support**: Upload and serve images and documents

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite (default, easily configurable for PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, Font Awesome icons
- **Image Processing**: Pillow for image handling
- **File Uploads**: Support for profile images and CV documents

## 📋 Requirements

- Python 3.8+
- Django 5.2.5
- Pillow 11.3.0

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd PersonaPort
```

### 2. Create Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your portfolio site!

## 🎯 Usage

### Setting Up Your Profile

1. Navigate to the admin panel at `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Create your profile by adding:
   - **Profile**: Your basic information (name, title, bio, profile image)
   - **Projects**: Your portfolio projects with descriptions and URLs
   - **Education**: Your educational background
   - **Social Links**: Your social media profiles with icons
   - **CV**: Upload your resume/CV file

### Content Management

The project includes several models for organizing your content:

- **Profile**: Core profile information
- **Project**: Individual projects with title, description, and URL
- **Education**: Educational entries
- **SocialLink**: Social media links with customizable icons
- **CV**: Downloadable resume files

## 📁 Project Structure

```
PersonaPort/
├── config/                 # Django settings and configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── onepage_app/            # Main application
│   ├── models.py          # Data models
│   ├── views.py           # View logic
│   ├── admin.py           # Admin configuration
│   └── ...
├── templates/              # HTML templates
│   └── onepage_app/
│       └── index.html     # Main portfolio template
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User-uploaded files
├── requirements.txt        # Python dependencies
└── manage.py              # Django management script
```

## 🎨 Customization

### Styling
- Modify `static/css/style.css` to customize the appearance
- The design uses Font Awesome icons for social links
- Responsive design adapts to different screen sizes

### Adding New Sections
1. Update the models in `onepage_app/models.py`
2. Add corresponding admin configurations in `admin.py`
3. Update the template in `templates/onepage_app/index.html`
4. Run migrations: `python manage.py makemigrations && python manage.py migrate`

## 🔧 Configuration

### Media Files
The project is configured to handle media uploads:
- Profile images are stored in `media/profile/`
- CV files are stored in `media/documents/`
- Static files are served during development

---

**PersonaPort** - Showcase your professional journey with style! ✨ 