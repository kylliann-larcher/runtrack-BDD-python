# 📌 Runtrack BDD - Exercices et Projet SQL  

## 🔍 Description  
Ce repository contient **les exercices et le projet de la runtrack SQL**, permettant d'apprendre et de pratiquer **les bases de données relationnelles avec MySQL**.  

📂 **Structure du dossier** :  
- `Jour-1/` → Initiation à SQL : création et manipulation des bases  
- `Jour-2/` → Requêtes avancées et manipulation des données  
- `Projet-Jour-3-4-5/` → Projet final sur l'analyse et la gestion des données  

---

## 📅 Jour 1 - Introduction à SQL  
### 📌 Objectifs  
✔ Créer une base de données  
✔ Définir des tables avec des clés primaires et étrangères  
✔ Manipuler les enregistrements avec `INSERT`, `UPDATE`, `DELETE`  
✔ Lire les données avec `SELECT`  

### 📂 Fichiers du Jour 1  
| 📄 **Fichier SQL** | 🔍 **Description** |
|--------------|-------------|
| `01-create-database.sql`  | Création de la base de données `LaPlateforme` |
| `02-create-tables.sql`  | Création des tables `etudiant`, `cours`, `professeur` |
| `03-insert-data.sql`  | Insertion de données test |
| `04-update-delete.sql`  | Mise à jour et suppression de données |

### ⚡ Exécuter les fichiers SQL  
```sh
mysql -u root -p < Jour-1/01-create-database.sql
```


## 📅 Jour 2 - Requêtes SQL avancées  
### 📌 Objectifs  
✔ Filtrer les données avec WHERE et LIKE

✔ Trier et classer avec ORDER BY

✔ Compter et calculer des valeurs avec COUNT(), AVG(), SUM()

✔ Utiliser des jointures JOIN

### 📂 Fichiers du Jour 2
|📄 **Fichier SQL**	🔍| **Description** |
|--------------|-------------|
|`01-select.sql`|	Requêtes SELECT avec filtres et conditions
|`02-order-by.sql`|	Tri et classement des données
|`03-count-avg.sql`|	Utilisation des fonctions COUNT(), AVG(), SUM()
|`04-join.sql`|	Requêtes avec jointures (INNER JOIN, LEFT JOIN)

⚡ Exécuter une requête SQL

```sh
mysql -u root -p < Jour-2/01-select.sql
```
## 📅  Jours 3, 4, 5 - Projet Final 
### 📌 Objectifs  

✔ Modéliser une base de données selon un cahier des charges

✔ Écrire des requêtes SQL avancées

✔ Automatiser des analyses de données

✔ Générer des statistiques et rapports

### 📂 Fichiers du Projet
|📄**Fichier SQL**|	🔍 **Description**|
|--------------|-------------|
|`01-schema.sql`|	Création du schéma de la base de données
|`02-insert-data.sql`|	Insertion de données test pour le projet
|`03-queries.sql`|	Requêtes avancées d’analyse et d’exploitation des données
|`04-report.sql`|	Génération de statistiques et rapports SQL

⚡ Exécuter le projet
```sh
mysql -u root -p < Projet-Jour-3-4-5/01-schema.sql
mysql -u root -p < Projet-Jour-3-4-5/02-insert-data.sql
```
📬 Contact
👤 Kylliann Larcher
📧 Email : kylliann.larcher@laplateforme.io



