
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="CALORIES"
)
mycursor = mydb.cursor()

# Database schema
schema = '''
CREATE DATABASE IF NOT EXISTS CALORIES;

USE CALORIES;

CREATE TABLE IF NOT EXISTS USERS(
    id INT AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    age INT,
    taille INT,
    poids INT,
    username VARCHAR(50) NOT NULL UNIQUE,
    passwords VARCHAR(50) NOT NULL,
    sexe VARCHAR(10) NOT NULL,
    days INT DEFAULT(0),
    weeks INT DEFAULT(0),
    months INT DEFAULT(0),
    years INT DEFAULT(0),
    fruits INT DEFAULT(5),
    legumes INT DEFAULT(5),
    cereales INT DEFAULT(5),
    proteines INT DEFAULT(5),
    Produits_laitiers INT DEFAULT(5),
    midi INT DEFAULT(0),
    soir INT DEFAULT(0),
    
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ALIMENTS(
    id INT AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL,
    calories VARCHAR(50) NOT NULL,
    categorie VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);
'''

# Execute the schema
mycursor.execute(schema)

# Close the cursor and connection
mycursor.close()


nom = ["Abricot","Ananas","Banane","Citron","Mangue","Orange","Papaye","Pastèque","Pomme","Prune"]
cal = [49,53, 94, 34, 64, 47, 43, 34, 53, 49]
cat = "Fruits"

for i in range(0, len(nom)) :
    mycursor.execute("INSERT INTO ALIMENTS(nom, calories, categorie) VALUES ( %s, %s, %s)",(nom[i], cal[i], cat))
    mydb.commit()

nom = ["Carotte","Champignon", "Chou", "Concombre", "Courgette", "Mais", "Oignon", "Patate", "Poireau", "Poivron", "Pomme de terre", "Tomate"]
cal = [21, 30, 33, 12, 19, 21, 30, 79, 25, 25, 75, 16]
cat = "Legumes"

for i in range(0, len(nom)) :
    mycursor.execute("INSERT INTO ALIMENTS(nom, calories, categorie) VALUES ( %s, %s, %s)",(nom[i], cal[i], cat))
    mydb.commit()

nom = ["Pain au Chocolat", "Croissant", "Madeleine","Gateau au Fruit","Beignet"]
cal = [270, 230, 100, 320, 250]
cat = "Cereales"

for i in range(0, len(nom)) :
    mycursor.execute("INSERT INTO ALIMENTS(nom, calories, categorie) VALUES ( %s, %s, %s)",(nom[i], cal[i], cat))
    mydb.commit()

nom = ["Bifteck de boeuf", "Boeuf", "Porc", "Saucisse", "Cotes de Mouton", "Hamburger", "Jambon Fume", "Lievre", "Mouton", "Rognons", "Canard", "Dinde", "Poulet", "Saucisson", "Foie gras"]
cal = [200, 250, 300, 330, 300, 560, 380, 100, 265, 120, 250, 260, 150, 440, 450]
cat = "Proteines"

for i in range(0, len(nom)) :
    mycursor.execute("INSERT INTO ALIMENTS(nom, calories, categorie) VALUES ( %s, %s, %s)",(nom[i], cal[i], cat))
    mydb.commit()

nom = ["Lait concentré sucré", "Lait concentré", "Lait entier", "Yaourt"]
cal = [330, 130, 65, 55]
cat = "Produits laitiers"

for i in range(0, len(nom)) :
    mycursor.execute("INSERT INTO ALIMENTS(nom, calories, categorie) VALUES ( %s, %s, %s)",(nom[i], cal[i], cat))
    mydb.commit()

mydb.close()
