# 🚀 DevOps 3-Tier Student Management Application

![Project](https://img.shields.io/badge/Project-DevOps%203--Tier-blue)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Backend-Flask-black)
![Database](https://img.shields.io/badge/Database-MariaDB-orange)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

A hands-on DevOps learning project that demonstrates how to build a three-tier Student Management Application using a frontend, Python Flask REST API, and a relational database.

The project is being developed step by step, starting with a working local application and progressing toward containerization, CI/CD, Kubernetes, Infrastructure as Code, and cloud deployment.

---

## 📌 Table of Contents

1. [Project Overview](#-project-overview)
2. [Architecture](#-application-architecture)
3. [Features](#-features)
4. [Technology Stack](#-technology-stack)
5. [Project Structure](#-project-structure)
6. [Prerequisites](#-prerequisites)
7. [Step 1: Clone the Repository](#step-1-clone-the-repository)
8. [Step 2: Install Required Packages](#step-2-install-required-packages)
9. [Step 3: Configure MariaDB](#step-3-configure-mariadb)
10. [Step 4: Create the Python Environment](#step-4-create-the-python-environment)
11. [Step 5: Configure Environment Variables](#step-5-configure-environment-variables)
12. [Step 6: Configure the Backend](#step-6-configure-the-backend)
13. [Step 7: Run the Backend](#step-7-run-the-backend)
14. [Step 8: Test the REST API](#step-8-test-the-rest-api)
15. [Step 9: Configure the Frontend](#step-9-configure-the-frontend)
16. [Step 10: Run the Frontend](#step-10-run-the-frontend)
17. [Step 11: Test the Complete Application](#step-11-test-the-complete-application)
18. [Troubleshooting](#-troubleshooting)
19. [Security Best Practices](#-security-best-practices)
20. [Future Enhancements](#-future-enhancements)
21. [Learning Outcomes](#-learning-outcomes)
22. [Author](#-author)

---

## 📖 Project Overview

The Student Management Application is designed to manage student records through a web interface.

The frontend communicates with a Flask backend using HTTP and JSON. The backend processes requests and interacts with a MariaDB database.

This project helps beginners understand how different application layers communicate with each other.

### Application layers

- **Presentation Layer:** HTML, CSS, and JavaScript.
- **Application Layer:** Python Flask REST API.
- **Database Layer:** MariaDB / MySQL-compatible relational database.

> This repository is a learning project. Complete each setup and verification step before treating a feature as operational.

---

## 🏗️ Application Architecture

```text
                    USER / BROWSER
                          |
                          v
              +------------------------+
              |    FRONTEND LAYER      |
              | HTML, CSS, JavaScript  |
              |      Port: 8080        |
              +------------------------+
                          |
                          | HTTP / JSON
                          v
              +------------------------+
              |   APPLICATION LAYER    |
              |      Python Flask      |
              |      Port: 5000        |
              +------------------------+
                          |
                          | SQL Connection
                          v
              +------------------------+
              |     DATABASE LAYER     |
              |        MariaDB         |
              |      Port: 3306        |
              +------------------------+
```

### Request flow

1. A user opens the frontend in a browser.
2. The frontend sends an HTTP request to the Flask API.
3. Flask validates the request.
4. Flask executes a SQL query against MariaDB.
5. The database returns the result.
6. Flask sends a JSON response to the frontend.
7. JavaScript updates the page.

---

## ✨ Features

### Application features

- Student record management.
- REST API development using Flask.
- Database integration using MariaDB.
- JSON request and response handling.
- Create, Read, Update, and Delete operations.
- Frontend form validation.
- API health endpoint.
- Environment-based database configuration.

### DevOps learning goals

- Linux command-line practice.
- Git and GitHub version control.
- Python virtual environments.
- Dependency management.
- Application configuration and secrets management.
- API testing with curl.
- Containerization with Docker.
- CI/CD using Jenkins.
- Kubernetes deployment.
- Infrastructure as Code using Terraform.
- Configuration management using Ansible.
- AWS cloud deployment and monitoring.

**Note:** DevOps technologies listed as learning goals are planned enhancements until their implementation and testing are documented.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Linux | Development environment |
| Python | Backend programming |
| Flask | REST API framework |
| HTML5 | Frontend structure |
| CSS3 | Frontend styling |
| JavaScript | Frontend logic and API requests |
| MariaDB | Relational database |
| SQL | Database operations |
| Git | Version control |
| GitHub | Source code hosting |
| curl | API testing |

### Planned technologies

| Technology | Planned purpose |
|---|---|
| Docker | Containerize the application |
| Docker Compose | Run multiple services together |
| Jenkins | Automate CI/CD |
| Kubernetes | Orchestrate application containers |
| Terraform | Provision infrastructure as code |
| Ansible | Automate server configuration |
| AWS EC2 | Compute infrastructure |
| AWS RDS | Managed relational database |
| AWS ECR | Container image registry |
| AWS Application Load Balancer | Distribute application traffic |
| AWS CloudWatch | Monitoring and logs |

---

## 📂 Project Structure

The intended project structure is:

```text
DevOps-3-Tier-StudentApp/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env                 # Local only; never commit
│
├── database/
│   └── schema.sql           # Database schema documentation
│
├── docker/                  # Future milestone
├── jenkins/                 # Future milestone
├── kubernetes/              # Future milestone
├── terraform/                # Future milestone
├── ansible/                  # Future milestone
├── monitoring/               # Future milestone
├── screenshots/
│
├── docs/
│   └── STEP_BY_STEP_GUIDE.md
│
├── .gitignore
└── README.md
```

The exact files present in the repository may change as development progresses. Only treat a file as implemented after confirming it exists in the repository.

---

## 💻 Prerequisites

Use a Kali Linux, Debian, or Ubuntu machine with:

- A working internet connection.
- A terminal.
- Git.
- Python 3.
- Python virtual environment support.
- MariaDB server.
- A web browser.
- Basic Linux command-line knowledge.

The commands below are intended for Debian-based Linux distributions.

---

## Step 1: Clone the Repository

If you have not cloned the project, open a terminal and run:

```bash
cd ~
```

Clone the repository:

```bash
git clone https://github.com/Harshal-gite/DevOps-3-Tier-StudentApp.git
```

Open the project directory:

```bash
cd ~/DevOps-3-Tier-StudentApp
```

Check the current branch:

```bash
git branch --show-current
```

Check the repository status:

```bash
git status
```

The default development branch is expected to be `main`.

If you already have the repository locally, do not clone it again into the same directory. Open the existing directory instead.

---

## Step 2: Install Required Packages

Update the package index:

```bash
sudo apt update
```

Install the required packages:

```bash
sudo apt install -y git python3 python3-venv python3-pip mariadb-server curl
```

Check Python:

```bash
python3 --version
```

Check Git:

```bash
git --version
```

Check MariaDB:

```bash
mariadb --version
```

Enable and start MariaDB:

```bash
sudo systemctl enable --now mariadb
```

Check its status:

```bash
sudo systemctl status mariadb --no-pager
```

**Expected result:** MariaDB should show `active (running)`.

If it is not running, resolve the service issue before proceeding.

---

## Step 3: Configure MariaDB

### 3.1 Open the database administrator session

Run:

```bash
sudo mariadb
```

You should see the MariaDB prompt.

### 3.2 Create the database

Execute:

```sql
CREATE DATABASE IF NOT EXISTS studentdb
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

### 3.3 Create a dedicated application user

Replace `REPLACE_WITH_A_STRONG_PASSWORD` with your own strong password.

Do not use this placeholder as your actual password.

```sql
CREATE USER IF NOT EXISTS 'studentapp'@'127.0.0.1'
IDENTIFIED BY 'REPLACE_WITH_A_STRONG_PASSWORD';
```

Grant only the permissions required by the application:

```sql
GRANT SELECT, INSERT, UPDATE, DELETE
ON studentdb.*
TO 'studentapp'@'127.0.0.1';
```

### 3.4 Create the students table

```sql
USE studentdb;
```

Execute:

```sql
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    course VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Verify the table:

```sql
SHOW TABLES;
```

Inspect its structure:

```sql
DESCRIBE students;
```

Exit MariaDB:

```sql
EXIT;
```

**Expected result:** The `students` table should exist inside the `studentdb` database.

### Important database note

The application connects using the host `127.0.0.1`. Therefore, the database account and credentials must match that connection configuration.

If you already created the application user with a different password or host, verify the existing configuration instead of blindly repeating these commands.

---

## Step 4: Create the Python Environment

Open the project directory:

```bash
cd ~/DevOps-3-Tier-StudentApp
```

Open the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

Check which Python executable is active:

```bash
which python
```

The path should point to the project's `backend/venv` directory.

Upgrade pip inside the virtual environment:

```bash
python -m pip install --upgrade pip
```

### Install backend dependencies

Confirm that `requirements.txt` exists and contains the packages used by the application.

The expected dependencies include:

```text
Flask
flask-cors
mysql-connector-python
python-dotenv
```

Install them:

```bash
python -m pip install -r requirements.txt
```

Check the installed packages:

```bash
python -m pip list
```

**Important:** Always activate the virtual environment before installing dependencies or starting the Flask backend.

Do not use `sudo pip install` or bypass the operating system's externally managed Python protection.

---

## Step 5: Configure Environment Variables

Database credentials should not be hardcoded in Python source code.

From the repository root:

```bash
cd ~/DevOps-3-Tier-StudentApp
```

Create the local environment file:

```bash
nano backend/.env
```

Add the following configuration:

```dotenv
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=studentapp
DB_PASSWORD=REPLACE_WITH_A_STRONG_PASSWORD
DB_NAME=studentdb
```

Replace the password placeholder with the same password configured for the MariaDB application user.

Save the file in nano:

1. Press `Ctrl + O`.
2. Press `Enter`.
3. Press `Ctrl + X`.

Restrict access to the file:

```bash
chmod 600 backend/.env
```

### Verify Git ignores the environment file

Open `.gitignore` and ensure it includes:

```gitignore
.env
backend/.env
venv/
backend/venv/
__pycache__/
*.py[cod]
```

Check whether Git is ignoring the file:

```bash
git check-ignore backend/.env
```

Git should print the ignored file path.

**Never commit real database passwords, API keys, access tokens, or cloud credentials.**

---

## Step 6: Configure the Backend

The backend entry point is:

```text
backend/app.py
```

The application is expected to provide these endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Backend information |
| GET | `/health` | Health check |
| GET | `/students` | Retrieve students |
| POST | `/students` | Create a student |
| PUT | `/students/<student_id>` | Update a student |
| DELETE | `/students/<student_id>` | Delete a student |

The backend should:

1. Load environment variables.
2. Connect to MariaDB.
3. Validate incoming JSON.
4. Use parameterized SQL queries.
5. Return JSON responses.
6. Handle invalid requests and database errors.
7. Close database cursors and connections.
8. Enable CORS for local frontend-to-backend requests.

Before running the backend, check that the required imports are present, including `os` if `os.getenv()` is used:

```python
import os
import mysql.connector
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
```

A typical configuration reads values from the environment:

```python
db_config = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "studentapp"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "studentdb"),
}
```

Load the environment file located beside `app.py`:

```python
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
```

Initialize Flask and CORS:

```python
app = Flask(__name__)
CORS(app)
```

**These snippets explain the required configuration. They are not a replacement for the complete API implementation.** Keep the complete CRUD route implementations in `app.py` and verify the file before running it.

---

## Step 7: Run the Backend

Open a terminal:

```bash
cd ~/DevOps-3-Tier-StudentApp/backend
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Check Python syntax:

```bash
python -m py_compile app.py
```

If the command returns no output, the syntax check passed.

Start Flask:

```bash
python app.py
```

The application should listen on:

```text
http://127.0.0.1:5000
```

Leave this terminal open while testing the application.

If the application fails to start, read the complete error message and resolve it before moving forward.

---

## Step 8: Test the REST API

Open a second terminal. Keep the backend running in the first terminal.

### 8.1 Test the root endpoint

```bash
curl -i http://127.0.0.1:5000/
```

Expected: an HTTP success response with JSON describing the backend.

### 8.2 Test the health endpoint

```bash
curl -i http://127.0.0.1:5000/health
```

Expected response:

```json
{
  "status": "UP"
}
```

### 8.3 Retrieve student records

```bash
curl -i http://127.0.0.1:5000/students
```

Expected: an HTTP success response with a JSON array of student records.

An empty array is valid if the table has no records.

### 8.4 Create a test student

Use an email address that does not already exist:

```bash
curl -i -X POST http://127.0.0.1:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Demo Student","email":"demo.student.001@example.com","course":"DevOps","age":22}'
```

Expected: HTTP `201 Created` with a response containing the new student's ID.

Save the returned `student_id`. The ID can differ on every database installation.

### 8.5 Verify the record

```bash
curl -i http://127.0.0.1:5000/students
```

The newly created test student should appear in the response.

### 8.6 Update the test student

Replace `ID_FROM_POST` with the actual numeric ID returned by the POST request.

```bash
curl -i -X PUT http://127.0.0.1:5000/students/ID_FROM_POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Demo Student Updated","email":"demo.student.001@example.com","course":"Cloud and DevOps","age":23}'
```

Expected: HTTP `200 OK` and a success message.

### 8.7 Delete the test student

Delete only the demo record created above.

Replace `ID_FROM_POST` with its actual numeric ID.

```bash
curl -i -X DELETE http://127.0.0.1:5000/students/ID_FROM_POST
```

Expected: HTTP `200 OK` and a success message.

Verify the record is no longer present:

```bash
curl -i http://127.0.0.1:5000/students
```

**Never run the DELETE test against a real student record that you want to keep.**

---

## Step 9: Configure the Frontend

The frontend files are intended to be:

```text
frontend/
├── index.html
├── style.css
└── script.js
```

### `index.html`

The HTML file provides the page structure, including:

- Application heading.
- API status indicator.
- Student count.
- Student form.
- Student records table.
- Edit and Delete buttons.

### `style.css`

The CSS file controls:

- Page layout.
- Forms and buttons.
- Table appearance.
- Status indicators.
- Responsive layout.

### `script.js`

The JavaScript file handles:

- API requests using `fetch()`.
- Student list retrieval.
- Creating student records.
- Updating student records.
- Deleting student records.
- API health checks.
- Updating the page after API responses.

### Configure the API URL

If the JavaScript uses:

```javascript
const API_URL = `http://${window.location.hostname}:5000`;
```

the browser will use the current hostname with port `5000` for API requests.

For local testing, both the frontend server and Flask backend must be running and reachable from the browser.

**Important:** The files must actually exist in the repository and their JavaScript must match the backend API routes. A README description alone does not create these files.

---

## Step 10: Run the Frontend

Keep the backend running.

Open another terminal:

```bash
cd ~/DevOps-3-Tier-StudentApp/frontend
```

Start a simple HTTP server:

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

Open a browser on the same machine:

```text
http://127.0.0.1:8080
```

If testing from another device on the same trusted network, obtain the development machine's LAN IP:

```bash
hostname -I
```

Use the actual IP returned by the command:

```text
http://YOUR_LAN_IP:8080
```

Replace `YOUR_LAN_IP` with the real IP address.

Do not expose this development server to the public internet.

---

## Step 11: Test the Complete Application

Perform these tests in order:

1. Open the frontend.
2. Confirm that the page loads.
3. Confirm that the API status shows connected.
4. Confirm that the student records table loads.
5. Add a test student with a unique email.
6. Confirm the new record appears.
7. Edit the test student.
8. Confirm the updated details appear.
9. Delete only the test student.
10. Confirm that the record disappears.
11. Refresh the page and confirm that the database results remain correct.

### Completion criteria

The local application milestone is complete only after:

- MariaDB starts successfully.
- Flask starts without errors.
- All API endpoints return the expected responses.
- The frontend can communicate with the backend.
- Create, Read, Update, and Delete operations work.
- Local credentials are excluded from Git.

---

## 🧰 Troubleshooting

### Error: `externally-managed-environment`

Activate the project's virtual environment:

```bash
cd ~/DevOps-3-Tier-StudentApp/backend
source venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

### Error: `NameError: name 'os' is not defined`

Check that `app.py` contains:

```python
import os
```

Then run:

```bash
python -m py_compile app.py
```

### Error: `ModuleNotFoundError`

Activate the virtual environment and reinstall the requirements:

```bash
cd ~/DevOps-3-Tier-StudentApp/backend
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Error: database access denied

Check:

- `DB_HOST`
- `DB_PORT`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

Confirm that the MariaDB user exists for the host used by the application.

Never paste passwords into public issues or screenshots.

### Error: table does not exist

Open MariaDB:

```bash
sudo mariadb
```

Select the database:

```sql
USE studentdb;
```

Check the tables:

```sql
SHOW TABLES;
```

If necessary, complete Step 3.

### Error: API disconnected

First test the backend directly:

```bash
curl -i http://127.0.0.1:5000/health
```

If this fails, fix the backend before debugging the frontend.

If the API works but the frontend does not, inspect the browser developer tools and check the Network and Console tabs.

### Error: port already in use

Stop the old server in its terminal with:

```text
Ctrl + C
```

Then restart the required service.

### Error: duplicate email

Email addresses are unique in the database. Use a different email for a new student or update the existing record.

---

## 🔐 Security Best Practices

- Never commit `.env` files.
- Never publish database passwords or cloud credentials.
- Use a dedicated database user rather than the database root account.
- Grant only the database permissions the application requires.
- Use parameterized SQL queries.
- Validate incoming API data.
- Do not expose the Flask development server to the public internet.
- Rotate any credential that has been exposed.
- Use HTTPS, authentication, authorization, managed secrets, backups, logging, and security reviews before production deployment.

This project is intended for learning and development. It is not production-hardened.

---

## 🚀 Future Enhancements

The following milestones are planned:

### Milestone 1: Application foundation

- [x] Repository structure
- [x] Flask CRUD API implementation in the project source
- [ ] Verify all API endpoints
- [ ] Verify frontend integration
- [ ] Document a clean local setup

### Milestone 2: Docker

- [ ] Create a backend Dockerfile
- [ ] Containerize the frontend
- [ ] Configure Docker Compose
- [ ] Configure persistent database storage
- [ ] Test the application in containers

### Milestone 3: CI/CD

- [ ] Create a Jenkins pipeline
- [ ] Automate source checkout
- [ ] Run syntax and application tests
- [ ] Build container images
- [ ] Publish images to a container registry

### Milestone 4: Kubernetes

- [ ] Create Deployments
- [ ] Create Services
- [ ] Configure ConfigMaps and Secrets
- [ ] Configure health probes
- [ ] Test rolling updates and rollbacks

### Milestone 5: Infrastructure as Code

- [ ] Provision infrastructure using Terraform
- [ ] Configure servers using Ansible
- [ ] Store configuration securely
- [ ] Document infrastructure cleanup

### Milestone 6: AWS and monitoring

- [ ] Configure VPC and subnets
- [ ] Configure IAM roles and least-privilege access
- [ ] Deploy application infrastructure
- [ ] Configure managed database connectivity
- [ ] Configure load balancing
- [ ] Add logging and monitoring
- [ ] Document costs and resource cleanup

Only mark a milestone complete after implementing and testing it.

---

## 📚 Learning Outcomes

This project is intended to provide hands-on experience with:

- Linux command-line tools.
- Python application development.
- Flask REST API design.
- Relational database fundamentals.
- SQL CRUD operations.
- Environment configuration.
- Git and GitHub.
- HTTP and JSON communication.
- Frontend-to-backend integration.
- Troubleshooting application errors.
- Containerization and cloud deployment concepts.

---

## 👨‍💻 Author

**Harshal Gite**

GitHub: [Harshal-gite](https://github.com/Harshal-gite)

Project Repository: [DevOps-3-Tier-StudentApp](https://github.com/Harshal-gite/DevOps-3-Tier-StudentApp)

Built as a hands-on DevOps learning project, with an emphasis on practical implementation, documentation, testing, and continuous improvement.

---

## ⭐ Support

If you find this project useful for learning, explore the repository, try the steps in your own development environment, and share constructive feedback.

**Learn. Build. Test. Improve. Repeat.**
