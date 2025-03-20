import mysql.connector
import getpass
from tabulate import tabulate
#TEST
class DatabaseManager:
    def __init__(self):
        """ Initialise la connexion à la base de données MySQL """
        try:
            password = getpass.getpass('Entrer votre mot de passe MySQL : ')
            self.conn = mysql.connector.connect(
                host="localhost",
                user="Kylliann",
                password=password,
                database="store"
            )
            self.cursor = self.conn.cursor()
            print("✅ Connexion réussie à la base de données MySQL")
        except mysql.connector.Error as err:
            print(f"❌ Erreur de connexion : {err}")
            self.conn = None

    def insert_product(self, name, description, price, quantity, id_category):
        """ Insère un produit dans la table product """
        if self.conn is None:
            print("🚨 Connexion non établie. Impossible d'insérer un produit.")
            return
        try:
            query = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
            values = (name, description, price, quantity, id_category)
            self.cursor.execute(query, values)
            self.conn.commit()
            print(f"✅ Produit '{name}' ajouté avec succès !")
        except mysql.connector.Error as err:
            print(f"❌ Erreur : {err}")

    def show_products(self):
        """ Affiche tous les produits dans la base """
        if self.conn is None:
            print("🚨 Connexion non établie. Impossible d'afficher les produits.")
            return
        try:
            self.cursor.execute("SELECT * FROM product")
            products = self.cursor.fetchall()
            if products:
                print(tabulate(products, headers=["ID", "Nom", "Description", "Prix", "Stock", "Catégorie"], tablefmt="grid"))
            else:
                print("📭 Aucun produit trouvé.")
        except mysql.connector.Error as err:
            print(f"❌ Erreur : {err}")

    def update_product_price(self, product_id, new_price):
        """ Met à jour le prix d'un produit via son ID """
        if self.conn is None:
            print("🚨 Connexion non établie. Impossible de mettre à jour le produit.")
            return
        try:
            query = "UPDATE product SET price = %s WHERE id = %s"
            values = (new_price, product_id)
            self.cursor.execute(query, values)
            self.conn.commit()
            print(f"✅ Prix du produit ID {product_id} mis à jour à {new_price}€")
        except mysql.connector.Error as err:
            print(f"❌ Erreur : {err}")

    def delete_product(self, product_id):
        """ Supprime un produit via son ID """
        if self.conn is None:
            print("🚨 Connexion non établie. Impossible de supprimer le produit.")
            return
        try:
            query = "DELETE FROM product WHERE id = %s"
            self.cursor.execute(query, (product_id,))
            self.conn.commit()
            print(f"🗑 Produit ID {product_id} supprimé avec succès.")
        except mysql.connector.Error as err:
            print(f"❌ Erreur : {err}")

    def close_connection(self):
        """ Ferme proprement la connexion à la base de données """
        if self.conn is not None:
            self.conn.close()
            print("🔌 Connexion fermée proprement.")

# Initialisation de la base de données
db = DatabaseManager()

# Liste de produits de sport
Product_sports = [
    ("Haltères ajustables", "Paire de haltères réglables 2-24 kg", 120, 10, 3),
    ("Tapis de yoga", "Tapis antidérapant épais 6mm", 30, 20, 3),
    ("Ballon de football", "Ballon taille 5, cuir synthétique", 25, 15, 4),
    ("Gants de boxe", "Gants de boxe 12 oz en cuir", 50, 8, 5),
    ("Vélo d’appartement", "Vélo d’intérieur avec écran LCD", 300, 5, 3),
    ("Chaussures de running", "Chaussures respirantes, amorti performant", 90, 12, 6),
    ("Raquette de tennis", "Raquette légère en graphite", 110, 7, 7),
    ("Short de sport", "Short respirant en polyester", 20, 25, 8),
    ("Bouteille isotherme", "Bouteille en inox 500ml", 15, 30, 9),
    ("Corde à sauter", "Corde ajustable, roulements à billes", 18, 18, 3)
]

# Insertion des produits de sport
for product in Product_sports:
    db.insert_product(*product)

# Affichage des produits
db.show_products()

# Mise à jour du prix d'un produit (ex: produit ID 1 à 99€)
db.update_product_price(1, 99)

# Suppression d'un produit (ex: produit ID 2)
db.delete_product(2)

# Fermeture propre de la connexion
db.close_connection()
