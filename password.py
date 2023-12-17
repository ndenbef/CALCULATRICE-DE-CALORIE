import tkinter as tk
from tkinter import messagebox
import home as h
import CreationCompte as CC
import Authentification as au

import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="CALORIES"
)
mycursor = mydb.cursor()


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Login Form")
        self.geometry("700x300")
        self.configure(bg="#0E4F77")

        self.label = tk.Label(self, text="        Change my Password", bg="#0E4F77", fg="white", font = ("Helvetica", 28), pady=40, padx=80)
        self.label.grid(row=0, column=0, columnspan=2)

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.password_new = tk.StringVar()
        
        self.label = tk.Label(self, text="Username", bg="#0E4F77", fg="white", font = ("Helvetica", 12), pady=10, padx=120)
        self.label.grid(row=1, column=0)
        
        self.username_entry = tk.Entry(self, textvariable=self.username, font = ("Helvetica", 12))
        self.username_entry.grid(row=1, column=1)
        
        self.label_password = tk.Label(self, text="New Password", bg="#0E4F77", fg="white", font = ("Helvetica", 12), pady=10, padx=80)
        self.label_password.grid(row=2, column=0)

        self.password_entry = tk.Entry(self, textvariable=self.password, show="*", font = ("Helvetica", 12))
        self.password_entry.grid(row=2, column=1)
        
        self.label_new = tk.Label(self, text="Confirm Password", bg="#0E4F77", fg="white", font = ("Helvetica", 12), pady=10, padx=80)
        self.label_new.grid(row=3, column=0)

        self.password_new_entry = tk.Entry(self, textvariable=self.password_new, show="*", font = ("Helvetica", 12))
        self.password_new_entry.grid(row=3, column=1)
        

        self.login_button = tk.Button(self, text="Next", bg="#0E4F77", fg="white", font = ("Helvetica", 12), relief="flat", command=self.login_next)
        self.login_button.grid(row=5, column=1, sticky="e")
        
        self.create_button = tk.Button(self, text="Login", bg="#0E4F77", fg="white", font = ("Helvetica", 12), relief="flat", command=self.login)
        self.create_button.grid(row=5, column=0, sticky="e")
        
    def create(self):
        app.destroy()
        CC.app = CC.SampleApp()
        CC.app.mainloop()
        
        

    def login(self):
        mydb.ping()
        
        app.destroy()
        au.app = au.SampleApp()
        au.app.mainloop()
        
    def login_next(self):
        mydb.ping()
        
        input1 = self.username_entry.get()
        input2 = self.password_entry.get()
    
        mycursor.execute("SELECT passwords FROM USERS WHERE  username = %s", (input1, ))
        resultat = mycursor.fetchone()

        if resultat:
            
            if self.password_entry.get() != self.password_new_entry.get():
                messagebox.showerror("Error", "Password confirmation failed !!")
                
            else:

                mycursor.execute("UPDATE USERS SET passwords = %s WHERE username = %s", (input2, input1))
                mydb.commit()
                messagebox.showinfo("Success", "You have successfully changed your password")
            
                app.destroy()
                au.app = au.SampleApp()
                au.app.mainloop()
            
        else :

            messagebox.showerror("Error", "Invalid Username !!")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()