from flask import Flask, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

load_dotenv()

app.config["MYSQL_HOST"] = os.getenv("DB_HOST")
app.config["MYSQL_USER"] = os.getenv("DB_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("DB_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("DB_NAME")

mysql = MySQL(app)


@app.route("/api/students", methods=["GET"])
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


@app.route("/api/disciplines", methods=["GET"])
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


@app.route("/api/groups", methods=["GET"])
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


@app.route("/api/lessons", methods=["GET"])
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


@app.route("/api/attendance", methods=["GET"])
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


@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student_info(student_id):
    try:
        cur = mysql.connection.cursor()

        # Выполнение запроса к базе данных для получения информации о студенте по его student_id
        cur.execute(
            "SELECT student_id, student_name FROM Students WHERE student_id = %s",
            (int(student_id),),
        )
        student = cur.fetchone()

        if student:
            # Формирование ответа в формате JSON с информацией о студенте
            student_info = {"student_id": student[0], "student_name": student[1]}
            return jsonify(student_info)
        else:
            return jsonify({"error": "Студент не найден"})

    except Exception as e:
        # Вывод ошибки для отладки
        print("Ошибка:", e)
        return jsonify({"error": str(e)})

    finally:
        cur.close()


@app.route("/api/students", methods=["GET"])
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


@app.route("/api/students", methods=["POST"])
def add_student():
    try:
        cur = mysql.connection.cursor()

        student_name = request.json.get("student_name")
        group_id = request.json.get("group_id")

        cur.execute(
            "INSERT INTO Students (student_name, group_id) VALUES (%s, %s)",
            (student_name, group_id),
        )

        mysql.connection.commit()

        cur.close()

        return jsonify({"message": "Студент успешно добавлен"})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/groups", methods=["POST"])
def add_group():
    try:
        cur = mysql.connection.cursor()

        group_name = request.json.get("group_name")

        cur.execute("INSERT INTO Groups_ (group_name) VALUES (%s)", (group_name,))

        mysql.connection.commit()

        cur.close()

        return jsonify({"message": "Группа успешно добавлена"})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/disciplines", methods=["POST"])
def add_discipline():
    try:
        cur = mysql.connection.cursor()

        discipline_name = request.json.get("discipline_name")

        cur.execute(
            "INSERT INTO Disciplines (discipline_name) VALUES (%s)", (discipline_name,)
        )

        mysql.connection.commit()

        cur.close()

        return jsonify({"message": "Дисциплина успешно добавлена"})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/lessons", methods=["POST"])
def add_lesson():
    try:
        cur = mysql.connection.cursor()

        lesson_date = request.json.get("lesson_date")
        group_id = request.json.get("group_id")
        discipline_id = request.json.get("discipline_id")

        cur.execute(
            "INSERT INTO Lessons (lesson_date, group_id, discipline_id) VALUES (%s, %s, %s)",
            (lesson_date, group_id, discipline_id),
        )

        mysql.connection.commit()

        cur.close()

        return jsonify({"message": "Занятие успешно добавлено"})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/attendance", methods=["POST"])
def add_attendance():
    try:
        cur = mysql.connection.cursor()

        student_id = request.json.get("student_id")
        lesson_id = request.json.get("lesson_id")
        present = request.json.get("present")

        cur.execute(
            "INSERT INTO Attendance (student_id, lesson_id, present) VALUES (%s, %s, %s)",
            (student_id, lesson_id, present),
        )

        mysql.connection.commit()

        cur.close()

        return jsonify({"message": "Запись о посещаемости успешно добавлена"})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/lessons/<int:lesson_id>", methods=["GET"])
def get_lesson_info(lesson_id):
    try:
        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM Lessons WHERE lesson_id = %s", (lesson_id,))

        lesson = cur.fetchone()

        if lesson:
            lesson_info = {
                "lesson_id": lesson[0],
                "lesson_date": lesson[1],
                "group_id": lesson[2],
                "discipline_id": lesson[3],
            }
            return jsonify(lesson_info)
        else:
            return jsonify({"error": "Занятие не найдено"})

    except Exception as e:
        print("Ошибка:", e)
        return jsonify({"error": str(e)})

    finally:
        cur.close()


@app.route("/api/lessons/<int:lesson_id>", methods=["PUT"])
def update_lesson(lesson_id):
    try:
        cur = mysql.connection.cursor()

        lesson_date = request.json.get("lesson_date")
        group_id = request.json.get("group_id")
        discipline_id = request.json.get("discipline_id")

        cur.execute(
            "UPDATE Lessons SET lesson_date = %s, group_id = %s, discipline_id = %s WHERE lesson_id = %s",
            (lesson_date, group_id, discipline_id, lesson_id),
        )

        mysql.connection.commit()

        cur.close()

        return jsonify({"message": "Занятие успешно обновлено"})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/lessons/<int:lesson_id>", methods=["DELETE"])
def delete_lesson(lesson_id):
    try:
        cur = mysql.connection.cursor()

        cur.execute("DELETE FROM Lessons WHERE lesson_id = %s", (lesson_id,))

        mysql.connection.commit()

        cur.close()

        return jsonify({"message": "Занятие успешно удалено"})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run()
