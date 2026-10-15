# ArtVista 

ArtVista is a Django-powered art portfolio web application designed to showcase artwork and give artists a place to share their creative work.

##  Features

- **User Registration** — Create an account with a username, email, and password.
- **User Login** — Sign in to your account securely.
- **Artwork Gallery** — Display artwork with titles, descriptions, images, and artist names.
- **Artwork Management** — Manage artwork through Django's administration panel.
- **Artwork Upload** — Planned feature allowing logged-in artists to upload artwork directly through the website.

##  Technologies Used

- Python
- Django
- HTML and CSS
- SQLite (default Django development database)

##  Project Structure

```text
ArtVista/
├── manage.py
├── README.md
├── ArtVista/
│   ├── settings.py
│   └── urls.py
└── gallery/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── admin.py
    └── templates/
        └── gallery/
            ├── home.html
            ├── register.html
            └── login.html
```

## Getting Started

### Prerequisites

- Python 3 installed
- pip installed
- Git installed (optional, for version control)

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ArtVista
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows using Git Bash:

```bash
source venv/Scripts/activate
```

### 3. Install dependencies

```bash
python -m pip install Django Pillow
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your administrator account.

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

Access the Django administration panel at:

http://127.0.0.1:8000/admin/

##  Roadmap

- [x] User registration
- [x] User login
- [x] Artwork database model
- [x] Django admin integration
- [x] Display artwork on the home page
- [ ] Complete website-based artwork uploads
- [ ] Artist profile pages
- [ ] Artwork search and filtering
- [ ] Responsive design improvements

## Security Notes

This project is currently intended for development and learning. Before deploying it publicly, configure production settings, protect secret keys, use appropriate database and media storage settings, and enable HTTPS.

## Author

Created as a Django portfolio project to practice web development and build an online art showcase.

## License

No license has been specified yet. Add a license if you intend to distribute or allow others to reuse this project.