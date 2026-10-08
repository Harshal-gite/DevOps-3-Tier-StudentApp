from dotenv import load_dotenv
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "127.0.0.1",
    "user": "studentapp",
    "password": os.getenv("DB_PASSWORD"),
    "database": "studentdb"
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


@app.route("/")
def home():
    return jsonify({
        "message": "DevOps 3-Tier Student App Backend is Running!"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/students", methods=["GET"])
def get_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(students)


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")
    age = data.get("age")

    if not name or not email or not course or not age:
        return jsonify({
            "error": "name, email, course and age are required"
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO students (name, email, course, age)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, email, course, age))
    connection.commit()

    student_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Student added successfully",
        "student_id": student_id
    }), 201

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")
    age = data.get("age")

    if not name or not email or not course or not age:
        return jsonify({
            "error": "name, email, course and age are required"
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        UPDATE students
        SET name = %s, email = %s, course = %s, age = %s
        WHERE id = %s
    """

    cursor.execute(query, (name, email, course, age, student_id))
    connection.commit()

    if cursor.rowcount == 0:
        cursor.close()
        connection.close()

        return jsonify({
            "error": "Student not found"
        }), 404

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Student updated successfully",
        "student_id": student_id
    }), 200
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    connection.commit()

    if cursor.rowcount == 0:
        cursor.close()
        connection.close()

        return jsonify({
            "error": "Student not found"
        }), 404

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Student deleted successfully",
        "student_id": student_id
    }), 200    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
