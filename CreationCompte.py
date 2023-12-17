import tkinter as tk
from tkinter import ttk
import io
from tkinter import filedialog
from tkinter import messagebox
import PIL.Image
import PIL.ImageTk
import Authentification as au

import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password=""
)
mycursor = mydb.cursor()

mycursor.execute("USE CALORIES")
mydb.commit()

class SampleApp(tk.Tk):
    def __init__(self):
        #self.master = master
        tk.Tk.__init__(self)
        self.title("Create Account")
        self.geometry("300x500")
        self.resizable(width=False, height=False)
        self.configure(bg="#0E4F77")

        self.label = tk.Label(self, text="ADD NEW ACCOUNT", bg="#0E4F77", fg="white", font = ("Helvetica", 18), pady=20, padx=30)
        self.label.grid(row=0, column=0, columnspan=2)

        self.name = tk.StringVar()
        self.surname = tk.StringVar()
        self.sexe = tk.StringVar()
        self.sexe.set("")
        self.age = tk.IntVar()
        self.age.set("")
        self.height = tk.DoubleVar()
        self.height.set("")
        self.weight = tk.DoubleVar()
        self.weight.set("")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.image = None
        
        options_sex = [
            "M",
            "F"
        ]

        self.name_label = tk.Label(self, text="Name:", bg="#0E4F77", fg="white", font = ("Helvetica", 12))
        self.name_label.grid(row=1, column=0)
        self.name_entry = tk.Entry(self, textvariable=self.name, font = ("Helvetica", 12))
        self.name_entry.grid(row=1, column=1)

        self.surname_label = tk.Label(self, text="Surname:", bg="#0E4F77", fg="white", font = ("Helvetica", 12))
        self.surname_label.grid(row=2, column=0)
        self.surname_entry = tk.Entry(self, textvariable=self.surname, font = ("Helvetica", 12))
        self.surname_entry.grid(row=2, column=1)
        
        self.sexe_label = tk.Label(self, text="Sexe:", bg="#0E4F77", fg="white", font = ("Helvetica", 12))
        self.sexe_label.grid(row=3, column=0)
        self.sexe_entry = ttk.Combobox(self, textvariable= self.sexe, values= options_sex, width=27, state=tk.OptionMenu)
        self.sexe_entry.grid(row=3, column=1)
        self.sexe_entry.bind('<Key>', lambda event: 'break')

        self.age_label = tk.Label(self, text="Age:", bg="#0E4F77", fg="white", font = ("Helvetica", 12))
        self.age_label.grid(row=4, column=0)
        self.age_entry = tk.Entry(self, textvariable=self.age, font = ("Helvetica", 12))
        self.age_entry.grid(row=4, column=1)
        self.age_entry.bind("<KeyRelease>", self.key)

        self.height_label = tk.Label(self, text="Height:", bg="#0E4F77", fg="white", font = ("Helvetica", 12))
        self.height_label.grid(row=5, column=0)
        
        self.height_entry = tk.Entry(self, textvariable=self.height, font = ("Helvetica", 12))
        self.height_entry.grid(row=5, column=1)
        self.height_entry.bind("<KeyRelease>", self.key)

        self.weight_label = tk.Label(self, text="Weight:", bg="#0E4F77", fg="white", font = ("Helvetica", 12))
        self.weight_label.grid(row=6, column=0)
        self.weight_entry = tk.Entry(self, textvariable=self.weight, font = ("Helvetica", 12))
        self.weight_entry.grid(row=6, column=1)
        self.weight_entry.bind("<KeyRelease>", self.key)
        
        self.username_label = tk.Label(self, text="Username:", bg="#0E4F77", fg="white", font = ("Helvetica", 12))
        self.username_label.grid(row=7, column=0)
        self.username_entry = tk.Entry(self, textvariable=self.username, font = ("Helvetica", 12))
        self.username_entry.grid(row=7, column=1)
        
        self.password_label = tk.Label(self, text="Password:", bg="#0E4F77", fg="white", font = ("Helvetica", 12))
        self.password_label.grid(row=8, column=0)
        self.password_entry = tk.Entry(self, textvariable=self.password, font = ("Helvetica", 12))
        self.password_entry.grid(row=8, column=1)

        self.image_button = tk.Button(self, text="Load Image", bg="#0E4F77", fg="white", font = ("Helvetica", 12), command=self.load_image)
        self.image_button.grid(row=9, column=0, rowspan=2)
        self.image_label = tk.Label(self, text="Your image will appear here", font = ("Helvetica", 12), state="disabled")
        self.image_label.grid(row=9, column=1, rowspan=2)

        self.submit_button = tk.Button(self, text="Submit", bg="#0E4F77", fg="white", font = ("Helvetica", 12), pady=10, command=self.submit)
        self.submit_button.grid(row=11, column=1)
        
            # bind keyboard events
        #self.bind("<KeyPress>", self.key)
        # self.master.bind("<KeyRelease>", self.key_release)

    def load_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.image = PIL.Image.open(path)
            self.image = self.image.resize((150, 150), PIL.Image.NEAREST)
            self.image = PIL.ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.image)
            
                    

    def submit(self):
        mydb.ping()
        if not self.name.get() or not self.surname.get() or not self.age.get() or not self.height.get() or not self.weight.get() or not self.username.get() or not self.password.get() or not self.sexe.get() :
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        print("Name:", self.name.get())
        print("Surname:", self.surname.get())
        print("Age:", self.age.get())
        print("Height:", self.height.get())
        print("Weight:", self.weight.get())
        print("Image:", self.image)
        print("Username:", self.username.get())
        print("Password:", self.password.get())
        
        mycursor.execute("INSERT INTO USERS(nom, prenom, age, taille, poids, username, passwords, sexe) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)",(self.name.get(), self.surname.get(), self.age.get(), self.height.get(), self.weight.get(), self.username.get(), self.password.get(), self.sexe.get()))
        mydb.commit()
        

        messagebox.showinfo("Success", "Account created successfully")
        
        app.destroy()
        au.app = au.SampleApp()
        au.app.mainloop()
        
    # def add_char(self, char):
    #     self.display.configure(state=tk.NORMAL)
    #     if self.clear_text:
    #         self.display.delete(0, tk.END)
    #         if char in "123456789":
    #             self.dec_button.config(state=tk.NORMAL)
    #     if char == ".":
    #         self.dec_button.config(state=tk.DISABLED)
    #     self.display.insert(tk.END, char)
    #     self.clear_text = False
    #     self.display.configure(state=tk.DISABLED)
        
    def key(self, event):
        entry_widget = event.widget
        current_text = entry_widget.get()
        #current_text not in "0123456789.0123456789"
        if not current_text.isdigit():
            # self.add_char(event.char)
            #self.age_entry.config(state=tk.DISABLED)
            messagebox.showerror("Error", "Please Enter a Number")
            entry_widget.delete(0, tk.END)
            #self.age_entry.config(state=tk.NORMAL)
            
    
    # def key_release(self, event):
    #     if event.char == "c" or event.char == "C":
    #         self.clear_button.invoke()
    #     elif event.char == "q" or event.char == "Q":
    #         self.master.quit()
    #     elif event.char == "e" or event.char == "E":
    #         self.eq_button.invoke()


        
        

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()