import sqlite3
from sqlite3 import Error


class student:

    def __init__(self, grade, average, passing):
        self.grade = grade
        self.average = average
        self.passing = passing

    def db_conn():
        conn = None

        try:
            conn= sqlite3.connect(grades_db.db)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

