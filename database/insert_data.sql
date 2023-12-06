INSERT INTO Disciplines (discipline_name) VALUES ('Логика'), ('ОАиП'), ('РБД и SQL'), ('ОМО');
INSERT INTO Groups_ (group_name) VALUES ('273902'), ('273901'), ('274001');
INSERT INTO Students (student_name, group_id) VALUES ('Сергей Сацук', 1),('Патрик Бейтман', 1),  ('Теодор Драйзер', 2), ('Окси Мирон', 2), ('Сэм Альтман', 3),('Федор Достоевский', 3);
INSERT INTO Lessons (lesson_date, group_id, discipline_id) VALUES ('2023-01-01', 1, 1), ('2023-01-02', 2, 2), ('2023-01-03', 3, 3);
-- Присутствовал
INSERT INTO Attendance (student_id, lesson_id, present) VALUES (1, 1, true), (2, 1, true), (3, 1, true);

-- Отсутствовал
INSERT INTO Attendance (student_id, lesson_id, present) VALUES (1, 2, false), (2, 2, false), (3, 2, false);