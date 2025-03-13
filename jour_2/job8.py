import mysql.connector

# Connexion à la base de données
def connecter():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kylliann2110",  
        database="zoo"
    )

# Ajouter une cage
def ajouter_cage():
    superficie = int(input("Superficie de la cage : "))
    capacite = int(input("Capacité max de la cage : "))

    conn = connecter()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)", (superficie, capacite))
    conn.commit()
    conn.close()
    print("✅ Cage ajoutée avec succès !")

# Supprimer une cage
def supprimer_cage():
    id_cage = int(input("ID de la cage à supprimer : "))

    conn = connecter()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cage WHERE id = %s", (id_cage,))
    conn.commit()
    conn.close()
    print("✅ Cage supprimée !")

# Ajouter un animal
def ajouter_animal():
    nom = input("Nom de l'animal : ")
    race = input("Race de l'animal : ")
    id_cage = int(input("ID de la cage : "))
    date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
    pays_origine = input("Pays d'origine : ")

    conn = connecter()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)",
                   (nom, race, id_cage, date_naissance, pays_origine))
    conn.commit()
    conn.close()
    print("✅ Animal ajouté avec succès !")

# Supprimer un animal
def supprimer_animal():
    id_animal = int(input("ID de l'animal à supprimer : "))

    conn = connecter()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM animal WHERE id = %s", (id_animal,))
    conn.commit()
    conn.close()
    print("✅ Animal supprimé !")

# Modifier un animal
def modifier_animal():
    id_animal = int(input("ID de l'animal à modifier : "))
    nouveau_nom = input("Nouveau nom : ")
    nouvelle_race = input("Nouvelle race : ")
    nouvelle_cage = int(input("Nouvel ID de cage : "))
    nouvelle_date = input("Nouvelle date de naissance (YYYY-MM-DD) : ")
    nouveau_pays = input("Nouveau pays d'origine : ")

    conn = connecter()
    cursor = conn.cursor()
    cursor.execute("UPDATE animal SET nom=%s, race=%s, id_cage=%s, date_naissance=%s, pays_origine=%s WHERE id=%s",
                   (nouveau_nom, nouvelle_race, nouvelle_cage, nouvelle_date, nouveau_pays, id_animal))
    conn.commit()
    conn.close()
    print("✅ Animal modifié avec succès !")

# Afficher tous les animaux
def afficher_animaux():
    conn = connecter()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal")
    animaux = cursor.fetchall()
    conn.close()

    print("\n📜 Liste des animaux :")
    for animal in animaux:
        print(f"ID: {animal[0]}, Nom: {animal[1]}, Race: {animal[2]}, Cage: {animal[3]}, Date de naissance: {animal[4]}, Origine: {animal[5]}")

# Afficher les animaux et leurs cages
def afficher_animaux_et_cages():
    conn = connecter()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT animal.nom, animal.race, animal.date_naissance, animal.pays_origine, cage.superficie, cage.capacite_max
        FROM animal
        LEFT JOIN cage ON animal.id_cage = cage.id
    """)
    resultats = cursor.fetchall()
    conn.close()

    print("\n📜 Animaux et leurs cages :")
    for row in resultats:
        print(f"Animal: {row[0]}, Race: {row[1]}, Naissance: {row[2]}, Origine: {row[3]}, Cage: {row[4]}m², Capacité: {row[5]}")

# Calculer la superficie totale des cages
def calculer_superficie_totale():
    conn = connecter()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(superficie) FROM cage")
    superficie_totale = cursor.fetchone()[0]
    conn.close()
    print(f"\n📏 Superficie totale des cages : {superficie_totale} m²")

# Menu interactif
def menu():
    while True:
        print("\n📌 Gestion du Zoo 📌")
        print("1. Ajouter une cage")
        print("2. Supprimer une cage")
        print("3. Ajouter un animal")
        print("4. Supprimer un animal")
        print("5. Modifier un animal")
        print("6. Afficher tous les animaux")
        print("7. Afficher les animaux et leurs cages")
        print("8. Calculer la superficie totale des cages")
        print("9. Quitter")

        choix = input("\n🔹 Faites un choix : ")

        if choix == "1":
            ajouter_cage()
        elif choix == "2":
            supprimer_cage()
        elif choix == "3":
            ajouter_animal()
        elif choix == "4":
            supprimer_animal()
        elif choix == "5":
            modifier_animal()
        elif choix == "6":
            afficher_animaux()
        elif choix == "7":
            afficher_animaux_et_cages()
        elif choix == "8":
            calculer_superficie_totale()
        elif choix == "9":
            print("👋 Fermeture du programme.")
            break
        else:
            print("❌ Choix invalide, veuillez réessayer.")

# Exécuter le menu
if __name__ == "__main__":
    menu()
