import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import getpass

class DatabaseManager:
    def __init__(self):
        """ Connexion à la base MySQL """
        try:
            password = getpass.getpass('Entrez votre mot de passe MySQL : ')
            self.conn = mysql.connector.connect(
                host="localhost",
                user="Kylliann",  # Mets ton utilisateur MySQL
                password=password,
                database="store"
            )
            self.cursor = self.conn.cursor()
            print("✅ Connexion réussie à MySQL")
        except mysql.connector.Error as err:
            print(f"❌ Erreur de connexion : {err}")
            self.conn = None

    def get_products(self):
        """ Récupère tous les produits """
        if self.conn:
            self.cursor.execute("SELECT * FROM product")
            return self.cursor.fetchall()
        return []

    def insert_product(self, name, description, price, quantity, id_category):
        """ Insère un produit """
        if self.conn:
            query = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (name, description, price, quantity, id_category))
            self.conn.commit()

    def delete_product(self, product_id):
        """ Supprime un produit """
        if self.conn:
            query = "DELETE FROM product WHERE id = %s"
            self.cursor.execute(query, (product_id,))
            self.conn.commit()

    def update_product_price(self, product_id, new_price):
        """ Met à jour le prix """
        if self.conn:
            query = "UPDATE product SET price = %s WHERE id = %s"
            self.cursor.execute(query, (new_price, product_id))
            self.conn.commit()

class StockManagerApp:
    def __init__(self, root):
        self.db = DatabaseManager()
        self.root = root
        self.root.title("Gestion de Stock")
        self.root.geometry("700x500")

        # Tableau des produits
        self.tree = ttk.Treeview(root, columns=("ID", "Nom", "Description", "Prix", "Stock", "Catégorie"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Catégorie", text="Catégorie")
        self.tree.pack(pady=20)

        # Boutons
        self.add_button = tk.Button(root, text="Ajouter un produit", command=self.add_product)
        self.add_button.pack()

        self.delete_button = tk.Button(root, text="Supprimer un produit", command=self.delete_product)
        self.delete_button.pack()

        self.update_button = tk.Button(root, text="Modifier le prix", command=self.update_price)
        self.update_button.pack()

        # Charger les produits
        self.load_products()

    def load_products(self):
        """ Charge les produits dans le tableau """
        for row in self.tree.get_children():
            self.tree.delete(row)

        for product in self.db.get_products():
            self.tree.insert("", "end", values=product)

    def add_product(self):
        """ Ajoute un produit """
        name = tk.simpledialog.askstring("Nom du produit", "Entrez le nom du produit :")
        description = tk.simpledialog.askstring("Description", "Entrez la description :")
        price = tk.simpledialog.askinteger("Prix", "Entrez le prix :")
        quantity = tk.simpledialog.askinteger("Quantité", "Entrez la quantité :")
        id_category = tk.simpledialog.askinteger("Catégorie", "Entrez l'ID de la catégorie :")

        if name and description and price and quantity and id_category:
            self.db.insert_product(name, description, price, quantity, id_category)
            self.load_products()
            messagebox.showinfo("Succès", "Produit ajouté avec succès !")

    def delete_product(self):
        """ Supprime le produit sélectionné """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erreur", "Veuillez sélectionner un produit à supprimer.")
            return

        product_id = self.tree.item(selected_item[0])["values"][0]
        self.db.delete_product(product_id)
        self.load_products()
        messagebox.showinfo("Succès", "Produit supprimé avec succès !")

    def update_price(self):
        """ Met à jour le prix du produit sélectionné """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erreur", "Veuillez sélectionner un produit à modifier.")
            return

        product_id = self.tree.item(selected_item[0])["values"][0]
        new_price = tk.simpledialog.askinteger("Modifier le prix", "Entrez le nouveau prix :")

        if new_price is not None:
            self.db.update_product_price(product_id, new_price)
            self.load_products()
            messagebox.showinfo("Succès", "Prix mis à jour avec succès !")

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = StockManagerApp(root)
    root.mainloop()
