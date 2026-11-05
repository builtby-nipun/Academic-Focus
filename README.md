# Academic Focus

> A full-stack academic task management application built with Flask, SQLite, Jinja2, and JavaScript.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Pytest](https://img.shields.io/badge/Tests-Pytest-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)

## Overview

Academic Focus is designed to give students a simple place to organize coursework, deadlines, priorities, and progress.

The application combines a Flask backend with a lightweight SQLite database and a responsive browser interface. Task actions are handled through backend endpoints and JavaScript requests, keeping the workflow fast and straightforward.

## Features

- 🔐 Session-based login/logout
- 📝 Create and manage academic tasks
- 📅 Track due dates
- 🚦 Low, Normal, and High priorities
- 🎓 Organize tasks by course
- ✅ Mark tasks as completed
- 🗑️ Delete tasks
- 🔎 Filter tasks by status and priority
- ↕️ Sort tasks by due date, priority, or course
- 📊 Dashboard progress and task statistics
- 📤 Export task data to CSV
- 📱 Responsive UI
- 🧪 Automated tests with Pytest

## Tech Stack

| Area | Technologies |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript, Jinja2 |
| Database | SQLite |
| Testing | Pytest |
| Data Export | CSV |
| Development | Git, GitHub, VS Code |

## Architecture

```text
┌───────────────┐
│    Browser    │
│ HTML/CSS/JS   │
└───────┬───────┘
        │
        │ HTTP / Fetch
        ▼
┌────────────────────┐
│   Flask Backend    │
│ Routes + Logic     │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│   SQLite Database  │
│   Persistent Tasks │
└────────────────────┘
```

## Project Structure

```text
Academic-Focus-Task-Planner/
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── static/
├── templates/
├── tests/
├── assets/
├── routes/
├── services/
└── utils/
```

## Getting Started

### Prerequisites

- Python 3.11+
- Git

### 1. Clone

```bash
git clone https://github.com/Iamaditya9/Academic-Focus-Task-Planner.git
cd Academic-Focus-Task-Planner
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

### 5. Run tests

```bash
pytest -v
```

## API

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Application dashboard |
| `GET` | `/login` | Login page |
| `POST` | `/login` | Create session |
| `GET` | `/logout` | End session |
| `GET` | `/tasks` | Retrieve tasks |
| `POST` | `/tasks` | Create a task |
| `PATCH` | `/tasks/<id>` | Update task completion |
| `DELETE` | `/tasks/<id>` | Delete a task |
| `GET` | `/export` | Export tasks as CSV |

## Testing

The project includes automated tests for the core task workflow, including:

- Creating tasks
- Retrieving tasks
- Updating completion status
- Deleting tasks

Run the complete test suite with:

```bash
pytest -v
```

## Engineering Focus

This project demonstrates practical software engineering concepts:

- REST-style backend endpoints
- CRUD operations
- Relational data persistence
- Server-side rendering with Jinja2
- Client-server communication with JavaScript `fetch`
- Input validation and error handling
- Automated API/application testing
- CSV data export
- Modular project organization

## Security Note

The current authentication is intended for a local/demo application. A production deployment would require stronger authentication and authorization, password hashing, CSRF protection, user-specific data ownership, secure secret management, and a production database.

## Future Improvements

- [ ] Real user authentication
- [ ] User-specific task ownership
- [ ] Task editing
- [ ] PostgreSQL support
- [ ] Calendar integration
- [ ] Deadline notifications
- [ ] Docker deployment
- [ ] CI/CD with GitHub Actions
- [ ] Cloud deployment

## Author

**Nipun Wadyalkar**

Bachelor of Applied Computer Science student focused on software development, backend engineering, APIs, databases, testing, and full-stack development.

- **GitHub:** [builtby-nipun](https://github.com/builtby-nipun)
- **LinkedIn:** www.linkedin.com/in/nipun-wadyalkar
- **Email:** nipunwadyalkar@gmail.com

If you find this project useful, feel free to ⭐ the repository.