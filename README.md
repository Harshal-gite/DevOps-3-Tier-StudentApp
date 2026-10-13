# 🚀 DevOps 3-Tier Student Management Application

<p align="center">
  <strong>A Full-Stack Application with a DevOps Roadmap</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-REST%20API-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/MariaDB-Database-orange?logo=mariadb" alt="MariaDB">
  <img src="https://img.shields.io/badge/JavaScript-Frontend-yellow?logo=javascript" alt="JavaScript">
  <img src="https://img.shields.io/badge/DevOps-Learning%20Project-purple" alt="DevOps">
</p>

A practical Student Management Application built to learn full-stack development and DevOps fundamentals through a real-world project.

The application uses a web frontend, a Python Flask REST API, and a MariaDB database. The project will progressively incorporate containerization, CI/CD, cloud deployment, and infrastructure automation.

---

## 📌 Project Overview

**Project:** DevOps 3-Tier Student Management Application

**Objective:** Build and deploy a student management system while learning application development and DevOps practices.

### 🏗️ Architecture

```text
             USER / BROWSER
                    |
                    v
          +-------------------+
          |   PRESENTATION    |
          |   HTML / CSS / JS |
          |     Port 8080     |
          +-------------------+
                    |
                 HTTP / JSON
                    |
                    v
          +-------------------+
          |  APPLICATION API  |
          |   Python + Flask  |
          |     Port 5000     |
          +-------------------+
                    |
                SQL Queries
                    |
                    v
          +-------------------+
          |    DATABASE       |
          |     MariaDB       |
          |     Port 3306     |
          +-------------------+
```

## ✨ Features

- Student record management
- REST API using Flask
- MariaDB database integration
- Create, Read, Update and Delete operations
- Environment-based database configuration
- API health-check endpoint
- Responsive web interface

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Linux | Development environment |
| Python | Backend programming |
| Flask | REST API |
| HTML, CSS, JavaScript | Frontend |
| MariaDB | Database |
| Git & GitHub | Version control |
| Docker | Planned containerization |
| Jenkins | Planned CI/CD |
| Kubernetes | Planned orchestration |
| Terraform | Planned infrastructure automation |
| AWS | Planned cloud deployment |

## 📂 Project Structure

```text
DevOps-3-Tier-StudentApp/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env              # Local configuration; never commit
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── .gitignore
└── README.md
```

## ⚙️ Step-by-Step Setup

### Step 1: Prerequisites

Install the following on Ubuntu, Debian, or Kali Linux:

- Python 3
- Python virtual environment support
- MariaDB Server
- Git
- A modern web browser

### Step 2: Clone the Repository

```bash
git clone https://github.com/Harshal-gite/DevOps-3-Tier-StudentApp.git
cd DevOps-3-Tier-StudentApp
```

### Step 3: Install Required Packages

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip mariadb-server
```

Start MariaDB:

```bash
sudo systemctl enable --now mariadb
```

### Step 4: Create the Database

Open MariaDB:

```bash
sudo mariadb
```

Create the database and application user:

```sql
CREATE DATABASE IF NOT EXISTS studentdb;

CREATE USER IF NOT EXISTS 'studentapp'@'127.0.0.1'
IDENTIFIED BY 'CHANGE_THIS_PASSWORD';

GRANT SELECT, INSERT, UPDATE, DELETE
ON studentdb.*
TO 'studentapp'@'127.0.0.1';
```

Create the student table:

```sql
USE studentdb;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    course VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Exit MariaDB:

```sql
EXIT;
```

Replace `CHANGE_THIS_PASSWORD` with your own strong password. Use the same password in the backend environment configuration.

### Step 5: Configure the Backend

Open the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create the environment file:

```bash
nano .env
```

Add:

```dotenv
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=studentapp
DB_PASSWORD=CHANGE_THIS_PASSWORD
DB_NAME=studentdb
```

Save the file and return to the project root when needed.

**Security:** Never commit `.env` or real credentials to GitHub.

### Step 6: Start the Backend

From the `backend` directory, run:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

Keep this terminal running.

### Step 7: Start the Frontend

Open a second terminal in the project root:

```bash
cd ~/DevOps-3-Tier-StudentApp
```

Start the frontend server:

```bash
python3 -m http.server 8080 --directory frontend
```

Open the application in your browser:

```text
http://127.0.0.1:8080
```

### Step 8: Verify the API

Check the API:

```bash
curl http://127.0.0.1:5000/
```

Check the database health endpoint:

```bash
curl http://127.0.0.1:5000/health
```

Retrieve student records:

```bash
curl http://127.0.0.1:5000/students
```

The database health endpoint should report a successful connection, and the students endpoint should return JSON.

## 🔐 Security Practices

- Store database credentials in environment variables.
- Keep `.env` out of version control.
- Use parameterized SQL queries.
- Grant the database user only the required permissions.
- Do not enable Flask debug mode in production.
- Use HTTPS and appropriate network restrictions when deploying.

## 🗺️ DevOps Roadmap

- [x] Flask backend and REST API foundation
- [x] MariaDB integration foundation
- [ ] Complete frontend integration and testing
- [ ] Docker and Docker Compose
- [ ] Jenkins CI/CD pipeline
- [ ] Kubernetes deployment
- [ ] Terraform infrastructure automation
- [ ] Ansible configuration management
- [ ] AWS deployment
- [ ] Monitoring and logging

Roadmap items will be marked complete after implementation and verification.

## 🎯 Learning Outcomes

This project provides practical experience with:

- Linux administration
- Python backend development
- REST API fundamentals
- SQL and relational databases
- Git and GitHub
- Application configuration
- Containerization and CI/CD concepts
- Cloud deployment fundamentals

## 👨‍💻 Author

**Harshal Gite**

GitHub: [Harshal-gite](https://github.com/Harshal-gite)

---

<p align="center">
  <strong>Built for learning. Designed for continuous improvement. 🚀</strong>
</p>
