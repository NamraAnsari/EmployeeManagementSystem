from tkinter import *
from tkinter import simpledialog, messagebox

from addEmp import *
from manageEntry import *


class ManageEmployee:

    def __init__(self, rt):
        self.f = Frame(rt, height=768, width=1360, bg='white', cursor='arrow')
        self.f.pack()
        self.f.tkraise()
        self.lb1 = Label(self.f, text="Manage Employee", width=1360, height=60, font=("Georgia", 30, "bold"),
                         bg="blue", fg="white")
        self.lb1.place(x=0, y=0, width=1360, height=60)
        self.b1 = Button(self.f, text="Add Employee", width=100, height=40, bg="blue", fg="white",
                         font=("Calibri", 12, "bold"), activebackground="grey", activeforeground="blue")
        self.b1.place(x=300, y=220, width=200, height=40)
        self.b1.bind("<Button-1>", self.add_emp)
        self.b2 = Button(self.f, text="Delete Employee", width=100, height=40, bg="blue", fg="white",
                         font=("Calibri", 12, "bold"), activebackground="grey", activeforeground="blue")
        self.b2.place(x=300, y=460, width=200, height=40)
        self.b2.bind("<Button-1>", self.del_employee)
        self.b3 = Button(self.f, text="Update Phone Number", width=100, height=40, bg="blue", fg="white",
                         font=("Calibri", 12, "bold"), activebackground="grey", activeforeground="blue")
        self.b3.place(x=910, y=220, width=200, height=40)
        self.b3.bind("<Button-1>", self.up_emp)
        self.b4 = Button(self.f, text="View Profile", width=100, height=40, bg="blue", fg="white",
                         font=("Calibri", 12, "bold"), activebackground="grey", activeforeground="blue")
        self.b4.place(x=910, y=460, width=200, height=40)
        self.b4.bind("<Button-1>", self.dis_emp)

    def del_employee(self, event):
        name = simpledialog.askstring("Delete Employee", "Enter Employee's name: ")
        d = ManageEntry()
        d.del_emp(name)
        messagebox.showinfo("Delete Employee!!", "Employee has been deleted.")

    def add_emp(self, event):
        w = Tk()
        w.title("Employee Management")
        AddEmp(w)
        w.mainloop()

    def up_emp(self, event):
        w = Tk()
        w.title("Employee Management")
        UpEmp(w)
        w.mainloop()


    def dis_emp(self, event):
        w = Tk()
        w.title("Employee Management")
        Display(w)
        w.mainloop()


root = Tk()
root.title("Employee Management Project")

lp = ManageEmployee(root)
root.mainloop()
