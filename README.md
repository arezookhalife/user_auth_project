# User Auth Project
A Django-based user authentication and post management system.
Features include user registration, login, profile management, avatar upload, post creation/edit/delete, search, and post likes.

---

## Installation

1. Clone the repository
```bash
git clone https://github.com/arezookhalife/user_auth_project.git
cd user_auth_project
```

2. Create a virtual environment
```bash
python -m venv .venv
```

Activate the environment
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Apply migrations
```bash
python manage.py migrate
```

5. Create superuser
```bash
python manage.py createsuperuser
```

---

## Running the project

```bash
python manage.py runserver
```

- The project will be available at:
http://127.0.0.1:8000

---

## Routes (URLs)

- Home: /accounts/home/
- Register: /accounts/register/
- Login: /accounts/login/
- Logout: /accounts/logout/
- Profile: /accounts/profile/
- Edit profile: /accounts/profile/edit/
- Upload avatar: /accounts/profile/avatar/
- Delete avatar: /accounts/profile/avatar/delete/
- Create post: /accounts/posts/create/
- Edit post: /accounts/posts/<id>/edit/
- Delete post: /accounts/posts/<id>/delete/
- Post detail: /accounts/posts/<id>/
- Like post: /accounts/posts/<id>/like/
- Search: /accounts/search/

---

## API Endpoints (HTML Views)

### General
- GET	/accounts/home/	→ Home page
- GET	/accounts/ → Redirect to home/login
- 
### Authentication & Profile
- GET	/accounts/register/ → Registration form
- POST	/accounts/register/ → Submit registration
- GET	/accounts/login/ → Login form
- POST	/accounts/login/ → Submit login
- GET	/accounts/logout/ → Logout
- GET	/accounts/profile/ → View user profile
- GET	/accounts/profile/edit/	→ Edit profile form
- POST	/accounts/profile/edit/	→ Save profile changes
- GET	/accounts/profile/avatar/ →	Upload avatar form
- POST	/accounts/profile/avatar/ → Upload new avatar
- POST	/accounts/profile/avatar/delete/ → Delete avatar

### Posts
- GET	/accounts/posts/create/	→ Create post form
- POST	/accounts/posts/create/	→ Submit new post
- GET	/accounts/posts/<id>/edit/ → Edit post form
- POST	/accounts/posts/<id>/edit/ → Save edited post
- POST	/accounts/posts/<id>/delete/ → Delete post
- GET	/accounts/posts/<id>/ → View post details
- POST	/accounts/posts/<id>/like/ → Like/Unlike a post

### Search
- GET	/accounts/search/?query=<term> → Search posts

### Password Reset
- GET	/accounts/password_reset/ → Request password reset form
- POST	/accounts/password_reset/ → Send password reset email
- GET	/accounts/password_reset/done/ → Email sent confirmation
- GET	/accounts/reset/<uidb64>/<token>/ →	Reset password form
- POST	/accounts/reset/<uidb64>/<token>/ → Save new password
- GET	/accounts/reset/done/ → Password reset successful

---

## Tests

Run tests:
```bash
python manage.py test
```

Test coverage: **85%+** (models, views, security, and permissions).

---

## Load Testing

- Performed with Locust.
- Focus: Response Time and Throughput analysis under concurrent user load.

---

## Author

- Name: Arezoo Khalife
- GitHub: arezookhalife
