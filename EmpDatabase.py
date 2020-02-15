import sqlite3


class EmpData:

    @staticmethod
    def create_tables():
        conn = sqlite3.connect('project.db')
        c = conn.cursor()

        c.execute("CREATE TABLE EMPLOYEE (E_ID INTEGER PRIMARY KEY AUTOINCREMENT,E_NAME VARCHAR(40) NOT NULL,"
                  "E_ADDRESS VARCHAR(50) NOT NULL,E_EMAIL VARCHAR(20),E_MOBILE VARCHAR(15) NOT NULL,"
                  "E_QUAL VARCHAR(10) NOT NULL, E_JOINDATE DATE)")


EmpData.create_tables()
