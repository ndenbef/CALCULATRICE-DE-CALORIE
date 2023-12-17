import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import home as h
import CreationCompte as CC
import password as pwd


import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password=""
)
mycursor = mydb.cursor()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Login Form")
        self.geometry("700x300")
        self.configure(bg="#0E4F77")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
        mycursor.execute("USE CALORIES")
        mydb.commit()
        #mycursor.execute("DESCRIBE USERS")
        #mycursor.execute("ALTER TABLE USERS ADD UNIQUE (username)")
        #mycursor.execute("DESCRIBE USERS")
        mycursor.execute("SELECT * FROM USERS")
        for x in mycursor:
            print(x)
    

        self.label = tk.Label(self, text="        Enter Login Details", bg="#0E4F77", fg="white", font = ("Helvetica", 28), pady=40, padx=80)
        self.label.grid(row=0, column=0, columnspan=2)
        
        self.label = tk.Label(self, text="Username", bg="#0E4F77", fg="white", font = ("Helvetica", 12), pady=10, padx=120)
        self.label.grid(row=1, column=0)
        
        self.username_entry = tk.Entry(self, textvariable=self.username, font = ("Helvetica", 12))
        self.username_entry.grid(row=1, column=1)
        
        self.label = tk.Label(self, text="Password", bg="#0E4F77", fg="white", font = ("Helvetica", 12), pady=10, padx=80)
        self.label.grid(row=2, column=0)

        self.password_entry = tk.Entry(self, textvariable=self.password, show="*", font = ("Helvetica", 12))
        self.password_entry.grid(row=2, column=1)
        
        self.eye =tk.PhotoImage(file='invisible.png')
        
        self.eye_button = tk.Button(self, image=self.eye, width=10, height=10, bd=0, background='black', activebackground='white', cursor='hand2', command=self.hide_password )
        self.eye_button.grid(row=2, column=2, sticky="e")
        
        self.forgot_button = tk.Button(self, text="I Forgot my password", bg="#0E4F77", fg="white", font = ("Helvetica", 8), relief="flat", command=self.forget)
        self.forgot_button.grid(row=3, column=1, sticky="e")

        self.login_button = tk.Button(self, text="Login", bg="#0E4F77", fg="white", font = ("Helvetica", 12), relief="flat", command=self.login)
        self.login_button.grid(row=4, column=1, sticky="e")
        
        self.create_button = tk.Button(self, text="I don't have an Account", bg="#0E4F77", fg="white", font = ("Helvetica", 12), relief="flat", command=self.create)
        self.create_button.grid(row=4, column=0, sticky="e")
        
    def create(self):
        app.destroy()
        CC.app = CC.SampleApp()
        CC.app.mainloop()
        
        

    def login(self):
        mydb.ping()

        input_user = self.username.get()
        input2 = self.password.get()
        
        mycursor.execute("SELECT * FROM USERS WHERE  (nom = %s AND passwords = %s)", (input_user, input2))
        resultat = mycursor.fetchone()
        #print(resultat)
        #username.get() == user[0] and password.get() == user[1] :
        if resultat :
            messagebox.showinfo("Success", "You have successfully logged in")
            
            app.destroy()
            h.app = h.MainApp()
            h.app.mainloop()
        else:
            messagebox.showerror("Error", "Incorrect username or password")   
            
        return input_user
            
    def forget(self):
        app.destroy()
        pwd.app = pwd.SampleApp()
        pwd.app.mainloop()
        
    def show_password(self):
        self.eye.config(file='invisible.png')
        self.password_entry.config(show='*')
        self.eye_button.config(background='white', activebackground='white', command=self.hide_password)
    
        
    def hide_password(self):
        self.eye.config(file='openeye.png')
        self.password_entry.config(show='')
        self.eye_button.config(background='black', activebackground='black', command=self.show_password)
        

        


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    
