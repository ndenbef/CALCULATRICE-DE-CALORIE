from msilib.schema import AppSearch
import sys
import password as pwd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Authentification as au
import CreationCompte as CC
import modify as mod

import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="CALORIES"
)
mycursor = mydb.cursor()

def run_script():
        python = sys.executable
        os.execl(python, python, *sys.argv)
        # if app :
        #app.destroy()
        #os.system("python home.py")

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.create_widgets()
        self.resizable(False, False)
        self.title("CALCULATRICE DE CALORIES")
        self.button_font = ("Helvetica", 12)
        self.configure(bg="#0E4F77")
        
    options = [
    "Petit-Dejeuner",
    "Dejeuner",
    "Dinner",

    ]
    
    options_day = [
    "Selectionner la duree",
    "Semaine",
    "Mois",
    "Annee",

    ]

    def create_widgets(self):
        # Create frame for the sidebar
        sidebar = tk.Frame(self, width=400, bg="gray90")
        sidebar.pack(side="left", fill="y")
        
        # Create buttons for the sidebar

        
        self.eye =tk.PhotoImage(file='openeye.png')

        self.eye_button = tk.Label(sidebar, image=self.eye, width=10, height=100, bd=0, background='black', activebackground='white' )
        self.eye_button.pack(side="top", fill="x", pady=20)
        for i in range(5):
            if (i == 0) :
                
                btn = tk.Button(sidebar, text=f"Enregistrer", font = ("Helvetica", 12), bg="gray80", relief="flat", command=lambda x=i: self.on_button_click(x))
                btn.pack(side="top", fill="x", pady=10)
                
            if (i == 1) :
                
                btn = tk.Button(sidebar, text=f"Mon Graph", font = ("Helvetica", 12), bg="gray80", relief="flat", command=lambda x=i: self.on_button_click(x))
                btn.pack(side="top", fill="x", pady=10)
                
            if (i == 2) :
                
                btn = tk.Button(sidebar, text=f"Exporter", font = ("Helvetica", 12), bg="gray80", relief="flat", command=lambda x=i: self.on_button_click(x))
                btn.pack(side="top", fill="x", pady=10)
                
            if (i == 3) :
                btn = tk.Button(sidebar, text=f"Mon Compte", font = ("Helvetica", 12), bg="gray80", relief="flat", command=lambda x=i: self.on_button_click(x))
                btn.pack(side="bottom", fill="x", pady=10)
                
            if (i == 4):
                
                btn = tk.Button(sidebar, text=f"Deconnexion", font = ("Helvetica", 12), bg="gray80", relief="flat", command=lambda x=i: self.on_button_click(x))
                btn.pack(side="bottom", fill="x", pady=10)
                
    def ajouter(self):
    
    
        # frame2.pack()
        tache = self.repas_entry.get()
        if tache == "":
            messagebox.showinfo("?????", "Veuillez renseigner tout les champs")
        else:
            self.listbox.insert(tk.END, tache)
            self.repas_entry.delete(0, tk.END)


    def completer_tache(self):
        
        global input_user
        
        choice = self.clicked.get()
        #input1 = au.login(self)
        #username = SampleApp.login(self)
        
        if choice == "Petit-Dejeuner" :
        
            total_calories = 0
        
            for i in range(len(self.listbox.get(0, 'end'))):
                select_item = self.listbox.get(i)
                
                mycursor.execute("SELECT categorie FROM ALIMENTS WHERE nom = %s",(str(select_item), ))
                result = mycursor.fetchone()
                
                if result[0] == "Fruits" :
                
                    mycursor.execute("UPDATE USERS SET fruits = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                    
                elif result[0] == "Legumes" :
                    
                    mycursor.execute("UPDATE USERS SET legumes = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                
                elif result[0] == "Cereales" :
                    
                    mycursor.execute("UPDATE USERS SET cereales = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                    
                elif result[0] == "Protéines" :
                    
                    mycursor.execute("UPDATE USERS SET proteines = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                    
                elif result[0] == "Produits_laitiers" :
                    
                    mycursor.execute("UPDATE USERS SET Produits_laitiers = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                    
            
                #selected_items = [self.listbox.get(i) for i in self.listbox.curselection()]
                #total_calories = 0
                
                #for items in selected_items :
                print(select_item)
                mycursor.execute("SELECT calories FROM ALIMENTS WHERE nom = %s",(str(select_item), ))
                result = mycursor.fetchone()
                total_calories += result[0] if result else 0
                    
            print(total_calories)
            
            mycursor.execute("UPDATE USERS SET days = %s WHERE username = %s", (total_calories, input_user))
            mydb.commit()
            
        elif choice == "Dejeuner" :
            
            total_calories = 0
        
            for i in range(len(self.listbox.get(0, 'end'))):
                select_item = self.listbox.get(i)
                
                mycursor.execute("SELECT categorie FROM ALIMENTS WHERE nom = %s",(str(select_item), ))
                result = mycursor.fetchone()
                
                if result[0] == "Fruits" :
                    
                    mycursor.execute("UPDATE USERS SET fruits = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                    
                elif result[0] == "Legumes" :
                    
                    mycursor.execute("UPDATE USERS SET legumes = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                
                elif result[0] == "Cereales" :
                    
                    mycursor.execute("UPDATE USERS SET cereales = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                    
                elif result[0] == "Protéines" :
                    
                    mycursor.execute("UPDATE USERS SET proteines = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                    
                elif result[0] == "Produits_laitiers" :
                    
                    mycursor.execute("UPDATE USERS SET Produits_laitiers = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
            
                #selected_items = [self.listbox.get(i) for i in self.listbox.curselection()]
                #total_calories = 0
                
                #for items in selected_items :
                print(select_item)
                mycursor.execute("SELECT calories FROM ALIMENTS WHERE nom = %s",(str(select_item), ))
                result = mycursor.fetchone()
                total_calories += result[0] if result else 0
                    
            print(total_calories)
            
            mycursor.execute("UPDATE USERS SET midi = %s WHERE username = %s", (total_calories, input_user))
            mydb.commit()
            
        elif choice == "Dinner" :
            
            total_calories = 0
        
            for i in range(len(self.listbox.get(0, 'end'))):
                select_item = self.listbox.get(i)
                
                mycursor.execute("SELECT categorie FROM ALIMENTS WHERE nom = %s",(str(select_item), ))
                result = mycursor.fetchone()
                
                if result[0] == "Fruits" :
                    
                    mycursor.execute("UPDATE USERS SET fruits = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                    
                elif result[0] == "Legumes" :
                    
                    mycursor.execute("UPDATE USERS SET legumes = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                
                elif result[0] == "Cereales" :
                    
                    mycursor.execute("UPDATE USERS SET cereales = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                    
                elif result[0] == "Protéines" :
                    
                    mycursor.execute("UPDATE USERS SET proteines = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
                    
                elif result[0] == "Produits_laitiers" :
                    
                    mycursor.execute("UPDATE USERS SET Produits_laitiers = %s WHERE username = %s", (total_calories, input_user))
                    mydb.commit()
            
                #selected_items = [self.listbox.get(i) for i in self.listbox.curselection()]
                #total_calories = 0
                
                #for items in selected_items :
                print(select_item)
                mycursor.execute("SELECT calories FROM ALIMENTS WHERE nom = %s",(str(select_item), ))
                result = mycursor.fetchone()
                total_calories += result[0] if result else 0
                    
            print(total_calories)
            
            mycursor.execute("UPDATE USERS SET soir = %s WHERE username = %s", (total_calories, input_user))
            mydb.commit()
            
            
                
            
            messagebox.showinfo("Success", "Enregistrement Reussie")
            
        else :
            messagebox.showinfo("?????", "Veuillez renseigner tout les champs")
        
        return total_calories

    
    def completer_taches(self):
            
        total_calories = 0
    
        for i in range(len(self.listbox.get(0, 'end'))):
            select_item = self.listbox.get(i)
        
            #selected_items = [self.listbox.get(i) for i in self.listbox.curselection()]
            #total_calories = 0
            
            #for items in selected_items :
            print(select_item)
            mycursor.execute("SELECT calories FROM ALIMENTS WHERE nom = %s",(str(select_item), ))
            result = mycursor.fetchone()
            total_calories += result[0] if result else 0
                
        print(total_calories)
            
        
        #messagebox.showinfo("Success", "Enregistrement Reussie")
        
        self.listbox.delete(0, tk.END)
        
        return total_calories
        
            
    def supprimer_tache(self):
        selection = self.listbox.curselection()
        print(selection)
        if selection:
            self.listbox.delete(selection)
        else:
            msg = messagebox.askquestion("Delete", " Voulez-vous Supprimer la liste ?")
            if msg == 'yes':
                self.listbox.delete(0, tk.END)
                
    # def update_calorie_labels(self, total_calories):
    #         #self.update_calorie_label(total_calories)
    #         return total_calories
                
    # def update_calorie_label(self, total_calories):
        
    #     global input_user

    #     choice = self.clicked.get()
    #     input1 = input_user
    #     if choice == "Petit-Dejeuner" :
            
    #         mycursor.execute("SELECT days FROM USERS WHERE username = %s",(input1, ))
    #         result = mycursor.fetchone()
            
    #         self.calorie_label_day_petit_dej.config(text= "Petit Dejeuner : "+ result + "Kcal")
    #         self.calorie_label_day_petit_dej.pack(side="top", fill="x", pady=40)
            
    #         self.calorie_label_day_dej.pack(side="top", fill="x", pady=40)
            
    #         self.calorie_label_day_dinner.pack(side="top", fill="x", pady=40)
            
    #     elif choice == "Dejeuner":
            
    #         #self.calorie_label_day_petit_dej.pack(side="top", fill="x", pady=40)
            
    #         self.calorie_label_day_dej.config(text= "Dejeuner : "+ str(total_calories) + "Kcal")
    #         self.calorie_label_day_dej.pack(side="top", fill="x", pady=40)
            
    #         self.calorie_label_day_dinner.pack(side="top", fill="x", pady=40)
            
    #     elif choice == "Dinner":
    #         self.calorie_label_day_petit_dej.pack(side="top", fill="x", pady=40)
            
    #         self.calorie_label_day_dej.pack(side="top", fill="x", pady=40)
            
    #         self.calorie_label_day_dinner.config(text= "Dinner : "+ str(total_calories)+ "Kcal")
    #         self.calorie_label_day_dinner.pack(side="top", fill="x", pady=40)
            
            

                    
                

    def on_button_click(self, button_id):
        
        button = button_id + 1
        
        # sidebar = tk.Frame(self, width=200, bg="gray90")
        # sidebar.pack(side="left", fill="y")
        
        for child in self.winfo_children():
            # if child != sidebar:
            child.pack_forget()
        
        # sidebar.pack(side="left", fill="y")
        self.create_widgets()

        if (button == 1) :
            
            global input_user
            
            # Code for Button 1
            sidebar4 = tk.Frame(self, width=400, bg="#0E4F77")
            sidebar4.pack(side="top", fill="y")
            
            sidebar3 = tk.Frame(self, width=200, bg="#0E4F77")
            sidebar3.pack(side="bottom", fill="x")
            
            sidebar2 = tk.Frame(self, width=400, bg="#0E4F77")
            sidebar2.pack(side="right", fill="y")
            
            self.clicked = tk.StringVar()
            self.clicked.set("Selectionner votre Repas")
            
            drop = tk.OptionMenu(sidebar4, self.clicked, *self.options)
            drop.pack(side="top", pady= 70, padx=20)
            
            value = []

            
            mycursor.execute("SELECT nom FROM ALIMENTS ")
            resultatss = mycursor.fetchall()
            
            for resultats in resultatss:
                value.append(resultats)
            
            
            
            self.repas_entry = ttk.Combobox(sidebar4, values=value)
            self.repas_entry.pack(side="top", fill="y", padx=10)
            
            self.Ajouter_button = tk.Button(sidebar4, text="Ajouter", bg="#0E4F77", fg="white", font = ("Helvetica", 12), pady=10, relief="flat", command=self.ajouter)
            self.Ajouter_button.pack(side="top", fill="y", padx=10)
            
            self.listbox = tk.Listbox(sidebar4, background="#72B6DA", bd=3, font = ("Helvetica", 12))
            self.listbox.pack(side="top", fill="y", padx=10, pady=10)  
            
            self.submit_button = tk.Button(sidebar4, text="Submit", bg="#0E4F77", fg="white", font = ("Helvetica", 12), pady=10, relief="flat", command=self.completer_tache)
            self.submit_button.pack(side="top", fill="y", padx=10)
            
            self.delete_button = tk.Button(sidebar3, text="Effacer", bg="#0E4F77", fg="white", font = ("Helvetica", 12), pady=10, relief="flat", command=self.supprimer_tache)
            self.delete_button.pack(side="bottom", fill="y", padx=10)
            
            # self.calorie_label = tk.Label(sidebar2, text=" Calorie:", bg="#0E4F77", fg="white", font = ("Helvetica", 12))
            # self.calorie_label.pack(side="top", fill="x", pady=1)
            
        if (button == 2) :
            
            # Code for Button 2
            sidebar4 = tk.Frame(self, width=400, bg="#0E4F77")
            sidebar4.pack(side="left", fill="y")
            
            sidebar2 = tk.Frame(self, width=400, bg="#0E4F77")
            sidebar2.pack(side="right", fill="y")
            
            sidebar3 = tk.Frame(self, width=200, bg="#0E4F77")
            sidebar3.pack(side="bottom", fill="x")
            
            fig = Figure(figsize=(6, 6))
            ax = fig.add_subplot(111)
            
            global input_user

            # The categories for the pie chart
            categories = ['Fruits', 'Légumes', 'Céréales', 'Protéines', 'Produits laitiers']

            mycursor.execute("SELECT fruits FROM USERS WHERE username = %s",(input_user, ))
            result1 = mycursor.fetchone()
            
            mycursor.execute("SELECT legumes FROM USERS WHERE username = %s",(input_user, ))
            result2 = mycursor.fetchone()
            
            mycursor.execute("SELECT cereales FROM USERS WHERE username = %s",(input_user, ))
            result3 = mycursor.fetchone()
            
            mycursor.execute("SELECT proteines FROM USERS WHERE username = %s",(input_user, ))
            result4 = mycursor.fetchone()
            
            mycursor.execute("SELECT produits_laitiers FROM USERS WHERE username = %s",(input_user, ))
            result5 = mycursor.fetchone()

            # The portions of each category
            portions = [int(result1[0]), int(result2[0]), int(result3[0]), int(result4[0]), int(result5[0])]
            
            #portions = [0, 0, 0, 0, 0]

            # The colors for each category
            colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#e6b3ff']

            # Plot the pie chart
            ax.pie(portions, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
            ax.axis('equal')
            
            fig.set_facecolor('#0E4F77')

            # Create a tkinter canvas
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            
            
            
            
            click = tk.StringVar()
            click.set("Selectionner la duree")
            
            results = tk.IntVar()
            
            droped = tk.OptionMenu(sidebar4, click, *self.options_day)
            droped.pack(side="top", pady= 20, padx=20)
            
            btn = tk.Button(sidebar4, text="Dessiner", bg="gray80", relief="flat", command=self.on_bottom_button_click)
            btn.pack(side="top", pady=10)
            
            mycursor.execute("SELECT days FROM users WHERE username = %s",(input_user, ))
            result = mycursor.fetchone()

            
            result = "Petit Dejeuner : "+ str(result[0]) + " Kcal" 
            
            self.calorie_label_day_petit_dej = tk.Label(sidebar2, text=result, bg="#0E4F77", fg="white", font = ("Helvetica", 12))
            self.calorie_label_day_petit_dej.pack(side="top", fill="x", pady=80)
            
            
            mycursor.execute("SELECT midi FROM users WHERE username = %s",(input_user, ))
            result = mycursor.fetchone()
        
            
            result = "Dejeuner : "+ str(result[0]) + " Kcal" 
            
            self.calorie_label_day_dej = tk.Label(sidebar2, text=result, bg="#0E4F77", fg="white", font = ("Helvetica", 12))
            self.calorie_label_day_dej.pack(side="top", fill="x", pady=80)
            
            # total_calories = self.completer_taches()
            # #total_calories = self.update_calorie_labels(total_calories)# or any other value
            # self.update_calorie_label(total_calories)
            
            
            mycursor.execute("SELECT soir FROM users WHERE username = %s",(input_user, ))
            result = mycursor.fetchone()
            
            
            result = "Dinner :  "+ str(result[0]) + " Kcal" 
            
            self.calorie_label_day_dinner = tk.Label(sidebar2, text=result , bg="#0E4F77", fg="white", font = ("Helvetica", 12))
            self.calorie_label_day_dinner.pack(side="top", fill="x", pady=80)
            
            # resultat = tk.StringVar()
            
            
            # resultat = "Somme des Calories:   "+ str(results) +" Kcal"
            
            
            # self.calorie_label_sum = tk.Label(sidebar2, text=resultat, bg="#0E4F77", fg="white", font = ("Helvetica", 12))
            # self.calorie_label_sum.pack(side="top", fill="x", pady=10)
            
        if (button == 3) :
            
            sidebar4 = tk.Frame(self, width=400, bg="#0E4F77")
            sidebar4.pack(side="top", fill="y")
            
            #global input_use

            # app = tk.Tk()
            # app.title("Exportateur de données")
            
            self.apercu = tk.Text(sidebar4, height=10, width=40)
            self.apercu.pack(pady=40)
            
            mycursor.execute("SELECT * FROM USERS WHERE username= %s",(input_user, ))
            result = mycursor.fetchall()
            
            for item in result:
                            self.apercu.insert(tk.END, f" Identifiant :{item[0]},\n")
                            self.apercu.insert(tk.END, f" NOM :{item[1]}, \n")
                            self.apercu.insert(tk.END, f" PRENOM :{item[2]}, \n")
                            self.apercu.insert(tk.END, f" AGE :{item[3]} ANS,\n")
                            self.apercu.insert(tk.END, f" TAILLE :{item[4]} CM,\n")
                            self.apercu.insert(tk.END, f" SEXE :{item[8]}, \n")
                            self.apercu.insert(tk.END, f" CALORIES :{item[9]} Kcal.\n")

            button = tk.Button(sidebar4, text="Exporter les données", font = ("Helvetica", 12), command=self.export_data)
            button.pack(pady=10)
                
            
            au.app.after(3000, au.app.deiconify)
                
        if (button == 4) :
            
            
            mod.app = mod.SampleApp()
            mod.app.mainloop()            
            
            
        if(button == 5) :
            
            # app = SampleApp()
            # app.destroy()
            # apps = MainApp()
            # apps.mainloop()
            python = sys.executable
            os.execl(python, os.path.abspath(__file__), *sys.argv)
            
            #app.protocol("WM_DELETE_WINDOW", run_script)
            
            
            
            
        
            # au.app.after(3000, au.app.deiconify)
            
            
            
        
        print(f"Clicked on button {button_id+1}")

    def on_bottom_button_click(self):
        print("Clicked on bottom button")
        
        
    def export_data(self):
                # Replace the following line with your SQL query to fetch the data
                sql_query = "SELECT * FROM "

                # Execute the query and fetch the data
                mycursor.execute("SELECT * FROM USERS WHERE username= %s",(input_user, ))
                result = mycursor.fetchall()

                # Close the connection to the database
                #mydb.close()

                # Save the data to a file
                file = filedialog.asksaveasfilename(defaultextension=".txt")
                if file:
                    with open(file, 'w') as f:
                        for item in result:
                            f.write(f" Identifiant :{item[0]},\n")
                            f.write(f" NOM :{item[1]}, \n")
                            f.write(f" PRENOM :{item[2]}, \n")
                            f.write(f" AGE :{item[3]} ANS,\n")
                            f.write(f" TAILLE :{item[4]} CM,\n")
                            f.write(f" SEXE :{item[8]}, \n")
                            f.write(f" CALORIES :{item[9]} Kcal.\n")
                            
                    messagebox.showinfo("Export réussi", f"Les données ont été exportées dans {file}")
        


    def display():
        global choice
        
        clicked = choice.get()
        
        if (clicked == "Selectionner votre Repas") :
            messagebox.showinfo("Message","Selectionner un repas avant de continuer.")
        else :
            if (clicked == "Petit-Dejeuner") :
                calories = 500
            elif (clicked == "Dejeuner") :
                calories = 1000
            elif (clicked == "Dinner") :
                calories = 1500
            else :
                calories = 2000
                
            repas_calories.set(str(calories))
            choice.set("Selectionner votre Repas")


    def create_calc():
        window = tk.Toplevel(app)
        window.title("CALCULATEUR DE CALORIES")
        window.geometry("800x500")
        
        canvas = tk.Canvas(window, width=400, height=300, bg="#A1E852")
        canvas.pack(side="top", fill="x", pady=30, padx= 40)
        
        data = [2000,2200,1800,2500,1900,2300,2100]
        
        max_calories = max(data)
        
        canvas.create_line(50,250,350,250)
        canvas.create_line(50,250,50,50)
        
        width = 30
        x = 80
        
        for calories in data :
            height = (calories/max_calories)*150
            canvas.create_rectangle(x,250 - height, x + width,250, fill="yellow")
            x += 40
                
        days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        x = 80
        
        for day in days :
            canvas.create_text(x+10,260,text=day)
            x += 40
                
        canvas.create_text(30,50,text=str(max_calories))
        canvas.create_text(30,150,text=str(max_calories // 2))
        canvas.create_text(30,250,text=(max_calories - max_calories)) 
        
        btn = tk.Button(window, text="Calculer Calories", bg="gray80", relief="flat", command=display)
        btn.pack(side="top", pady=10)
        
        
            
        
        
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
        global input_user

        input_user = self.username.get()
        input2 = self.password.get()
        
        mycursor.execute("SELECT * FROM USERS WHERE  (nom = %s AND passwords = %s)", (input_user, input2))
        resultat = mycursor.fetchone()
        #print(resultat)
        #username.get() == user[0] and password.get() == user[1] :
        if resultat :
            messagebox.showinfo("Success", "You have successfully logged in")
            
            app.destroy()
            main()
            
            # app.destroy()
            # app = MainApp()
            # app.mainloop()
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

        

def main():
    global app
    apps = MainApp()
    apps.mainloop()
    
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


# if __name__ == "__main__":
#     main()