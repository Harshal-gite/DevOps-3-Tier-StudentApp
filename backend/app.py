
import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from mysql.connector import Error


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
CORS(app)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "studentapp"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "studentdb"),
}


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


def error_response(message, status_code):
    return jsonify({"error": message}), status_code


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "DevOps 3-Tier Student App API",
        "status": "running"
    })


@app.route("/health", methods=["GET"])
def health():
    try:
        connection = get_db_connection()
        connection.close()
        return jsonify({"status": "UP", "database": "connected"})
    except Error:
        return error_response("Database connection failed", 503)


@app.route("/students", methods=["GET"])
def get_students():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, name, email, course, age, created_at "
            "FROM students ORDER BY id"
        )
        return jsonify(cursor.fetchall())

    except Error:
        app.logger.exception("Unable to retrieve students")
        return error_response("Unable to retrieve students", 500)

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def validate_student(data):
    if not isinstance(data, dict):
        return None, "A JSON object is required"

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")
    age = data.get("age")

    if not all([name, email, course]) or age is None:
        return None, "name, email, course and age are required"

    if not all(isinstance(value, str) for value in [name, email, course]):
        return None, "name, email and course must be text"

    name, email, course = name.strip(), email.strip(), course.strip()

    if not name or not email or not course:
        return None, "Fields cannot be empty"

    if len(name) > 100 or len(email) > 150 or len(course) > 100:
        return None, "One or more fields exceed the allowed length"

    if isinstance(age, bool):
        return None, "age must be a positive integer"

    try:
        age = int(age)
    except (TypeError, ValueError):
        return None, "age must be a positive integer"

    if age < 1 or age > 120:
        return None, "age must be between 1 and 120"

    return {
        "name": name,
        "email": email,
        "course": course,
        "age": age
    }, None


@app.route("/students", methods=["POST"])
def add_student():
    data, error = validate_student(request.get_json(silent=True))

    if error:
        return error_response(error, 400)

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO students (name, email, course, age) "
            "VALUES (%s, %s, %s, %s)",
            (data["name"], data["email"], data["course"], data["age"])
        )
        connection.commit()

        return jsonify({
            "message": "Student added successfully",
            "student_id": cursor.lastrowid
        }), 201

    except Error as exc:
        if connection and connection.is_connected():
            connection.rollback()

        if getattr(exc, "errno", None) == 1062:
            return error_response("Email already exists", 409)

        app.logger.exception("Unable to add student")
        return error_response("Unable to add student", 500)

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data, error = validate_student(request.get_json(silent=True))

    if error:
        return error_response(error, 400)

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE students SET name=%s, email=%s, course=%s, age=%s "
            "WHERE id=%s",
            (
                data["name"],
                data["email"],
                data["course"],
                data["age"],
                student_id
            )
        )

        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT id FROM students WHERE id=%s",
                (student_id,)
            )

            if cursor.fetchone() is None:
                return error_response("Student not found", 404)

        connection.commit()

        return jsonify({
            "message": "Student updated successfully",
            "student_id": student_id
        })

    except Error as exc:
        if connection and connection.is_connected():
            connection.rollback()

        if getattr(exc, "errno", None) == 1062:
            return error_response("Email already exists", 409)

        app.logger.exception("Unable to update student")
        return error_response("Unable to update student", 500)

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id=%s",
            (student_id,)
        )

        if cursor.rowcount == 0:
            return error_response("Student not found", 404)

        connection.commit()

        return jsonify({
            "message": "Student deleted successfully",
            "student_id": student_id
        })

    except Error:
        if connection and connection.is_connected():
            connection.rollback()

        app.logger.exception("Unable to delete student")
        return error_response("Unable to delete student", 500)

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
