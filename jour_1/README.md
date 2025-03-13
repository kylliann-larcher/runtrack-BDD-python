# 📌 SQL Jobs - Automatisation des Requêtes et Gestion des Données Étudiants  

## 🔍 Description  
Ce projet contient une série de **requêtes SQL** permettant d’effectuer diverses opérations sur une base de données `etudiant`.  
Chaque fichier SQL correspond à une tâche spécifique : **tri, calculs statistiques, mises à jour et suppressions conditionnelles**.  

---

## 📂 Structure du Projet  

📁 **Liste des fichiers SQL et leurs fonctions :**  

| 📄 **Fichier SQL** | 🔎 **Description** |
|------------------|----------------|
| `job9.sql`   | Sauvegarde de la base de données `LaPlateforme` |
| `job10.sql`  | Tri des étudiants par âge (ordre croissant) |
| `job11.sql`  | Récupération des informations de Gertrude Dupuis |
| `job12.sql`  | Ajout de Martin Dupuis et récupération des membres d'une famille |
| `job13.sql`  | Récupération des étudiants entre 18 et 25 ans |
| `job14.sql`  | Récupération des étudiants entre 18 et 25 ans (triés par âge) |
| `job15.sql`  | Tri des étudiants par nom (ordre alphabétique) |
| `job16.sql`  | Récupération des étudiants dont le prénom commence par « B » |
| `job17.sql`  | Mise à jour de l'âge de Betty Spaghetti |
| `job18.sql`  | Suppression de John Doe |
| `job19.sql`  | Comptage du nombre total d'étudiants |
| `job20.sql`  | Comptage du nombre d'étudiants mineurs |
| `job21.sql`  | Comptage des étudiants entre 18 et 25 ans |
| `job22.sql`  | Récupération de l'étudiant le plus jeune |
| `job23.sql`  | Récupération de l'étudiant le plus âgé |
| `job24.sql`  | Calcul de la moyenne d'âge des étudiants |

---

## 🛠️ Utilisation  

📌 **Exécuter un fichier SQL spécifique** : 

   `mysql -u root -p LaPlateforme < jobXX.sql`
   🔹 Remplace jobXX.sql par le fichier SQL que tu veux exécuter.

   
📌 Lancer MySQL en mode interactif et exécuter un fichier SQL :
`mysql -u root -p`

Puis dans MySQL :
`SOURCE jobXX.sql;`

#📌 Sauvegarde et restauration de la base de données :
 Sauvegarde
`mysqldump -u root -p LaPlateforme > backup.sql`

 Restauration
`mysql -u root -p LaPlateforme < backup.sql`

🚀 Contribution

📌 Tu veux modifier ou améliorer ce projet ?

1️⃣ Clone le dépôt : `git clone <(https://github.com/kylliann-larcher/runtrack-BDD-python/edit/main/jour_1)>`

📌 Auteur
📅 Projet réalisé en mars 2025

👤 LARCHER Kylliann

📧 Email : kylliann.larcher@laplateforme.io










