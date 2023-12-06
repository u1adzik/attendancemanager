CREATE TABLE Disciplines (
    discipline_id INT PRIMARY KEY AUTO_INCREMENT,
    discipline_name VARCHAR(255) NOT NULL
);

CREATE TABLE Groups_ (
    group_id INT PRIMARY KEY AUTO_INCREMENT,
    group_name VARCHAR(50) NOT NULL
);

CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100) NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES Groups_(group_id)
);

CREATE TABLE Lessons (
    lesson_id INT PRIMARY KEY AUTO_INCREMENT,
    lesson_date DATE NOT NULL,
    group_id INT,
    discipline_id INT,
    FOREIGN KEY (group_id) REFERENCES Groups_(group_id),
    FOREIGN KEY (discipline_id) REFERENCES Disciplines(discipline_id)
);

CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    lesson_id INT,
    present BOOLEAN NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (lesson_id) REFERENCES Lessons(lesson_id)
);