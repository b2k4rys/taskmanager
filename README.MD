## Technology Stack

- **Language**: Python 3.13
- **Framework**: Django 5.2.1, Django REST Framework 3.16.0
- **Authentication**: `djangorestframework-simplejwt` for JWT
- **Database**: PostgreSQL
- **Environment Management**: Python `venv`, `.env` file for configuration
- **Dependencies**: Managed via `requirements.txt`

### Prerequisites

- Python 3.13
- PostgreSQL (installed and running)
- Git
- A code editor (e.g., VS Code)

### Installation

1. **Clone the Repository**:
```
   git clone <repository-url>
   cd task_manager
```
2. **Create and Activate a Virtual Environment:**
```
python -m venv env
source env/bin/activate  # On Mac/Linux
env\Scripts\activate  # On Windows
```
3. **Install Dependencies:**
```
pip install -r requirements.txt
```
4. **Set Up Environment Variables:**
- Create a .env file in the task_manager directory.
- Add the following:
```
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>
SECRET_KEY=<your-secret-key>
```
- Replace <username>, <password>, <database_name>, and <your-secret-key> with your PostgreSQL credentials and a secure Django secret key.

5. **Apply Database Migrations**
```
python manage.py makemigrations
python manage.py migrate
```

6. **Create a Superuser (for Admin Access):**
```
python manage.py createsuperuser
```
- Follow the prompts to set a username, email, and password.


## Example API Requests
- Register:
```
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "email": "test@example.com", "password": "testpassword123"}'
```

- Login:
```
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpassword123"}'
```

- Create Task:

```
curl -X POST http://127.0.0.1:8000/api/tasks/ \
-H "Authorization: Bearer <access-token>" \
-H "Content-Type: application/json" \
-d '{"title": "New Task", "description": "Details", "status": "todo"}'
```

- List Tasks (Filtered)

```
curl -X GET http://127.0.0.1:8000/api/tasks/?status=todo \
-H "Authorization: Bearer <access-token>"
```