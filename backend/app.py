from flask import Flask, jsonify
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config["MYSQL_HOST"] = os.getenv("DB_HOST")
app.config["MYSQL_USER"] = os.getenv("DB_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("DB_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("DB_NAME")

mysql = MySQL(app)


@app.route("/students", methods=["GET"])
def get_students():
    try:
        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM Students")

        students = cur.fetchall()

        students_list = []
        for student in students:
            student_dict = {
                "student_id": student[0],
                "student_name": student[1],
                "group_id": student[2],
            }
            students_list.append(student_dict)

        cur.close()

        return jsonify(students_list)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/disciplines", methods=["GET"])
def get_disciplines():
    try:
        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM Disciplines")

        disciplines = cur.fetchall()

        disciplines_list = []
        for discipline in disciplines:
            discipline_dict = {
                "discipline_id": discipline[0],
                "discipline_name": discipline[1],
            }
            disciplines_list.append(discipline_dict)

        cur.close()

        return jsonify(disciplines_list)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/groups", methods=["GET"])
def get_groups():
    try:
        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM Groups_")

        groups = cur.fetchall()

        groups_list = []
        for group in groups:
            group_dict = {"group_id": group[0], "group_name": group[1]}
            groups_list.append(group_dict)

        cur.close()

        return jsonify(groups_list)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/lessons", methods=["GET"])
def get_lessons():
    try:
        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM Lessons")

        lessons = cur.fetchall()

        lessons_list = []
        for lesson in lessons:
            lesson_dict = {
                "lesson_id": lesson[0],
                "lesson_date": lesson[1],
                "group_id": lesson[2],
                "discipline_id": lesson[3],
            }
            lessons_list.append(lesson_dict)

        cur.close()

        return jsonify(lessons_list)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/attendance", methods=["GET"])
def get_attendance():
    try:
        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM Attendance")

        attendance = cur.fetchall()

        attendance_list = []
        for record in attendance:
            record_dict = {
                "attendance_id": record[0],
                "student_id": record[1],
                "lesson_id": record[2],
                "present": record[3],
            }
            attendance_list.append(record_dict)

        cur.close()

        return jsonify(attendance_list)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run()
