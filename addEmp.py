from tkinter import *
from tkinter import messagebox

from manageEntry import *

fnt = ("Calibri", 12, "bold")


class AddEmp:

    def __init__(self, w):
        self.fr = Frame(w, height=400, width=500, bg="white", cursor="arrow")
        self.fr.pack()
        self.fr.tkraise()
        self.lb2 = Label(self.fr, height=60, width=500, bg="blue", fg="white", font=("Georgia", 30, "bold"),
                         text="Add Employee")
        self.lb2.place(x=0, y=0, height=60, width=500)
        self.lb3 = Label(self.fr, height=20, width=20, bg="white", fg="grey1", font=fnt,
                         text="Name:")
        self.lb3.place(x=40, y=80, height=20, width=150)
        self.lb4 = Label(self.fr, text="Address", width=100, height=20, font=fnt, fg='grey1',
                         bg='white')
        self.lb4.place(x=40, y=120, width=150, height=20)
        self.lb5 = Label(self.fr, text="e-mail:", width=100, height=20, font=fnt, fg='grey1',
                         bg='white')
        self.lb5.place(x=40, y=160, width=150, height=20)
        self.lb6 = Label(self.fr, text="Mobile Number:", width=100, height=20, font=fnt, fg='grey1',
                         bg='white')
        self.lb6.place(x=40, y=200, width=150, height=20)
        self.lb7 = Label(self.fr, text="Qualification:", width=40, height=20, font=fnt, fg='grey1',
                         bg='white')
        self.lb7.place(x=40, y=240, width=150, height=20)
        self.lb8 = Label(self.fr, text="Date of Joining:", width=40, height=20, font=fnt,
                         fg='grey1',
                         bg='white')
        self.lb8.place(x=40, y=280, width=150, height=20)
        self.e1 = Entry(self.fr, width=50, bg="white", fg="grey", font=fnt)
        self.e1.place(x=210, y=80, width=200)
        self.e2 = Entry(self.fr, width=50, bg="white", fg="grey", font=fnt)
        self.e2.place(x=210, y=120, width=200)
        self.e3 = Entry(self.fr, width=50, bg="white", fg="grey", font=fnt)
        self.e3.place(x=210, y=160, width=200)

        self.e4 = Entry(self.fr, width=50, bg="white", fg="grey", font=fnt)
        self.e4.place(x=210, y=200, width=200)
        self.e5 = Entry(self.fr, width=50, bg="white", fg="grey", font=fnt)
        self.e5.place(x=210, y=240, width=200)

        self.e6 = Entry(self.fr, width=50, bg="white", fg="grey", font=fnt)
        self.e6.place(x=210, y=280, width=200)

        self.b1 = Button(self.fr, width=70, height=20, bg="green", fg="white", font=fnt,
                         text="Submit", activebackground="grey", activeforeground="green", command=self.rsd)
        self.b1.place(x=215, y=340, width=70, height=20)
        self.b1.bind("<Button-1>", self.get_emp)

    def rsd(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)

    def get_emp(self, event):
        c1 = self.e1.get()
        c2 = self.e2.get()
        c3 = self.e3.get()
        c4 = self.e4.get()
        c5 = self.e5.get()
        c6 = self.e6.get()
        for i in c1:
            if i.isdigit():
                messagebox.showinfo("Wrong Entry", "Your Entry Cannot Be Accepted...")
                quit()
        for i in c4:
            if i.isalpha():
                messagebox.showinfo("Wrong Entry", "Your Entry Cannot Be Accepted...")
                quit()
        for i in c5:
            if i.isdigit():
                messagebox.showinfo("Wrong Entry", "Your Entry Cannot Be Accepted...")
                quit()
        n = c3.find('@', 0, len(c3))
        if n == -1:
            messagebox.showinfo("Invalid E-mail", "You have entered wrong E-mail...")
        else:
            s = ManageEntry()
            s.emp_data_entry(c1, c2, c3, c4, c5, c6)

            messagebox.showinfo("Employee Added", "Employee Added Successfully...")


class UpEmp:

    def __init__(self, w):
        self.fr = Frame(w, height=200, width=500, bg="white", cursor="arrow")
        self.fr.pack()
        self.fr.tkraise()
        self.lb2 = Label(self.fr, height=60, width=500, bg="blue", fg="white", font=("Georgia", 30, "bold"),
                         text="Update Mobile Number")
        self.lb2.place(x=0, y=0, height=60, width=500)
        self.lb3 = Label(self.fr, height=20, width=20, bg="white", fg="grey1", font=fnt,
                         text="Name:")
        self.lb3.place(x=40, y=80, height=20, width=150)
        self.lb6 = Label(self.fr, text="New Mobile Number:", width=100, height=20, font=fnt,
                         fg='grey1',
                         bg='white')
        self.lb6.place(x=40, y=120, width=150, height=20)
        self.e1 = Entry(self.fr, width=50, bg="white", fg="grey", font=fnt)
        self.e1.place(x=210, y=80, width=200)
        self.e2 = Entry(self.fr, width=50, bg="white", fg="grey", font=fnt)
        self.e2.place(x=210, y=120, width=200)
        self.b1 = Button(self.fr, width=70, height=20, bg="green", fg="white", font=fnt,
                         text="Submit", activebackground="grey", activeforeground="green")
        self.b1.place(x=215, y=160, width=70, height=20)
        self.b1.bind("<Button-1>", self.up_emp)

    def up_emp(self, event):
        c1 = self.e1.get()
        c2 = self.e2.get()
        for i in c1:
            if i.isdigit():
                messagebox.showinfo("Wrong Entry", "Your Entry Cannot Be Accepted...")
                quit()
        for i in c2:
            if i.isalpha():
                messagebox.showinfo("Wrong Entry", "Your Entry Cannot Be Accepted...")
                quit()
        s = ManageEntry()
        s.upd_emp(c1, c2)
        messagebox.showinfo("Mobile Number Updated", "Mobile Number Update Successfully...")


class Display:
    def __init__(self, w):
        self.fr = Frame(w, height=400, width=500, bg="white", cursor="arrow")
        self.fr.pack()
        self.fr.tkraise()
        self.lb2 = Label(self.fr, height=60, width=500, bg="blue", fg="white", font=("Georgia", 30, "bold"),
                         text="Profile")
        self.lb2.place(x=0, y=0, height=60, width=500)
        self.lb3 = Label(self.fr, height=80, width=150, bg="white", fg="grey1", font=fnt,
                         text="Enter employee's name:")
        self.lb3.place(x=20, y=80, height=20, width=200)
        self.e1 = Entry(self.fr, width=150, bg="white", fg="grey1", font=fnt)
        self.e1.place(x=250, y=80, width=200)
        self.e1.bind("<Return>", self.retri)

    def retri(self, event):
        s1 = self.e1.get()
        for i in s1:
            if i.isdigit():
                messagebox.showinfo("Wrong Entry", "Your Entry Cannot Be Accepted...")
                quit()
        try:
            s2 = ManageEntry()
            lst = s2.display_data(s1)
            lb4 = Label(self.fr, height=120, width=150, bg="white", fg="grey1", font=fnt,
                        text="Address:")
            lb4.place(x=20, y=120, height=20, width=200)
            lb5 = Label(self.fr, height=60, width=500, bg="white", fg="grey1", font=fnt,
                        text="Mobile Number:")
            lb5.place(x=20, y=160, height=20, width=200)
            lb7 = Label(self.fr, height=60, width=500, bg="white", fg="grey1", font=fnt,
                        text=lst[0])
            lb7.place(x=250, y=120, height=20, width=150)
            lb8 = Label(self.fr, height=60, width=500, bg="white", fg="grey1", font=fnt,
                        text=lst[1])
            lb8.place(x=250, y=160, height=20, width=150)
        except TypeError:
            messagebox.showerror("Entry not found", "Oops, no such entry found...")