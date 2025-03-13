import mysql.connector

# Connexion à la base de données
try:
    conn = mysql.connector.connect(
        host="localhost",  # Adresse du serveur MySQL
        user="root",       # Ton utilisateur MySQL
        password="Kylliann2110",  # Remplace par ton mot de passe
        database="LaPlateforme"  # Nom de la base de données
    )

    if conn.is_connected():
        print("Connexion réussie à la base de données LaPlateforme")

        # Création d'un curseur pour exécuter des requêtes SQL
        cursor = conn.cursor()

        # Exécuter la requête pour récupérer les étudiants
        query = "SELECT * FROM etudiant;"
        cursor.execute(query)

        # Récupérer et afficher les résultats
        etudiants = cursor.fetchall()

        print("\nListe des étudiants :")
        for etudiant in etudiants:
            print(etudiant)

        # Fermer le curseur et la connexion
        cursor.close()
        conn.close()

except mysql.connector.Error as err:
    print(f"Erreur: {err}")

