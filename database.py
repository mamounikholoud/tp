import sqlite3
import re
import hashlib

conn = sqlite3.connect('basedata.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    nom TEXT,
    password TEXT,
    age INTEGER,  
    email TEXT        
)
''')

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[@#$%^&+=]', password):
        return False
    return True

def ajouter_utilisateur():
    nom = input("Entrez le nom de l'utilisateur : ")
    
    while True:
        password = input("Entrez le mot de passe de l'utilisateur (minimum 8 caractères, 1 majuscule, 1 minuscule, 1 chiffre) : ")
        if is_valid_password(password):
            break
        else:
            print("La mot de passe doit contenir au moins 8 caractères, 1 lettre majuscule, 1 lettre minuscule et 1 chiffre.")
    
    password_hash = hash_password(password) 
    
  
    try:
        age = int(input("Entrez l'âge de l'utilisateur : "))
    except ValueError:
        print("L'âge doit être un nombre entier.")
        return

    email = input("Entrez l'email de l'utilisateur : ")
    if not is_valid_email(email):
        print("L'email n'est pas valide.")
        return

    cursor.execute("INSERT INTO utilisateurs (nom, password, age, email) VALUES (?, ?, ?, ?)", (nom, password_hash, age, email))
    conn.commit()
    print("Utilisateur ajouté avec succès !")
    with open("utilisateurs.txt", "a") as file:
        file.write(f"Nom: {nom}, Password: {password_hash}\n")
    with open("utilisateurs2.txt", "a") as file:
        file.write(f"Nom: {nom},  Age: {age}\n")
    with open("utilisateurs3.txt", "a") as file:
        file.write(f"Nom: {nom},  Email: {email}\n")
    
    print("Utilisateur ajouté avec succès dans la base de données et le fichier !")


def afficher_utilisateurs():
    cursor.execute("SELECT * FROM utilisateurs")
    rows = cursor.fetchall()
    if rows:
        print("\nUtilisateurs enregistrés :")
        for row in rows:
            print(f"ID : {row[0]}, Nom : {row[1]}, Age : {row[3]}, Email : {row[4]}")
    else:
        print("Aucun utilisateur enregistré.")


def menu():
    while True:
        print("\n1. Ajouter un utilisateur")
        print("2. Afficher les utilisateurs")
        print("3. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == '1':
            ajouter_utilisateur()
        elif choix == '2':
            afficher_utilisateurs()
        elif choix == '3':
            print("Fermeture du programme...")
            break
        else:
            print("Option incorrecte, essayez à nouveau.")


menu()

conn.close()



