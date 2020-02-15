from tkinter import *
from tkinter import simpledialog
from manageEntry import *

#from SecPage import ManageEmployee


class loginPage:

    def __init__(self, rt):
        self.f = Frame(rt, height=400, width=500, bg="white", cursor="arrow")
        self.f.pack()
        #self.f.tkraise()
        self.lb1 = Label(self.f, text="Login", width=20, height=20, font=('Calibri', 30, 'bold'), fg='white',
                         bg="blue")
        self.lb1.place(x=0, y=0, width=500, height=50)
        self.lb2 = Label(self.f, text="Username:", width=40, height=20, font=('Calibri', 12, 'bold'), fg='grey1',
                         bg='white')
        self.lb2.place(x=20, y=80, width=100, height=20)
        self.lb3 = Label(self.f, text="Password:", width=40, height=20, font=('Calibri', 12, 'bold'), fg='grey1',
                         bg='white')
        self.lb3.place(x=20, y=130, width=100, height=20)
        self.e1 = Entry(self.f, width=40, fg='grey', bg='white', font=('Calibri', 12))
        self.e1.place(x=140, y=80, width=200, height=20)
        self.e2 = Entry(self.f, width=40, fg='grey', bg='white', font=('Calibri', 12), show="*")
        self.e2.place(x=140, y=130, width=200, height=20)
        self.b1 = Button(self.f, text="Login", width=70, height=30, bg="blue", fg="white", activebackground="grey",
                         activeforeground="blue")
        self.b1.place(x=70, y=200, width=70, height=30)
        self.b1.bind("<Button-1>", self.display_login)
        self.b2 = Button(self.f, text="Cancel", width=70, height=30, bg="red", fg="white", activebackground="grey",
                         activeforeground="red", command=quit)
        self.b2.place(x=360, y=200, width=70, height=30)

    def display_login(self, event):
        str1 = self.e1.get()
        str2 = self.e2.get()
        if str1 == "namra" and str2 == "namra":
            root = Tk()
            root.title("Employee Management")
            #ManageEmployee(root)
            #root.mainloop()


        else:
            lb4 = Label(self.f, text="wrong Username or Password", width=40, height=20,
                        font=('Calibri', 12, 'bold'), fg='grey1', bg='white')
            lb4.place(x=30, y=270, width=40, height=20)


root = Tk()
root.title("Employee Management Project")

lp = loginPage(root)
root.mainloop()
root.withdraw()


