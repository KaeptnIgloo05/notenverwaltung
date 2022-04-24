import sqlite3
from sqlite3 import Error


"""
class Student:

    def __init__(self, surname, name, students_class, mark, subject):
        self.surname = surname
        self.name = name
        self.students_class = students_class
        self.mark = mark
        self.subjectject = subject
"""


def create_student(surname, name, students_class, class_teacher):
    global con
    try:
        con = sqlite3.connect('marking_system.db')  # connecting to database
        cur = con.cursor()  # creating cursor

        cur.execute(f'''INSERT INTO students(surname, name, class, teacher) VALUES
        ("{surname}", "{name}", "{students_class}",  "{class_teacher}")''')  # adding new student to overview table

        student_id = cur.execute(f"SELECT id FROM students WHERE surname = {surname} AND name = {name}").fetchone()  # getting new students id
        cur.execute(f"CREATE TABLE {student_id} (mark CHAR, subject-id INTEGER, exam boolean")  # table for new student

    except Error as e:
        print(e)
    finally:
        if con:
            con.close()


# con = sqlite3.connect('marking_system.db')
# cur = con.cursor()

"""
cur.execute('''CREATE TABLE students
            (id INTEGER PRIMARY KEY,
            surname varchar(20),
            name varchar(20),
            class char,
            teacher varchar(20))''')
"""

# con.commit()
# con.close()

create_student('Doe', 'John', '7B', 'Jane Doe')
