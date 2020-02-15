import sqlite3


class ManageEntry:

    def __init__(self):
        self.conn = sqlite3.connect('project.db')
        self.c = self.conn.cursor()

    def emp_data_entry(self, b, a, d, e, f, g):
        self.c.execute("INSERT INTO EMPLOYEE (E_NAME,E_ADDRESS,E_EMAIL,E_MOBILE,E_QUAL,E_JOINDATE) VALUES(?,?,?,?,?,?)",
                       (b, a, d, e, f, g))
        self.conn.commit()

    def del_emp(self, a):
        self.c.execute("DELETE FROM EMPLOYEE WHERE E_NAME = (?)", (a,))
        self.conn.commit()

    def upd_emp(self, a, b):
        self.c.execute("UPDATE EMPLOYEE SET E_MOBILE = (?) WHERE E_NAME = (?)", (b, a))
        self.conn.commit()

    def display_data(self, a):
        self.c.execute('SELECT E_ADDRESS, E_MOBILE FROM EMPLOYEE WHERE E_NAME = (?)', (a,))
        for row in self.c.fetchall():
            return row

    def __del__(self):
        self.conn.close()

