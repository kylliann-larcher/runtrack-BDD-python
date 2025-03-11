# README - SQL Jobs

## 📌 Description
Ce projet contient une série de requêtes SQL permettant d'effectuer différentes opérations sur une base de données `etudiant`. Chaque fichier SQL correspond à un job spécifique et exécute une requête bien définie.

## 📂 Structure du projet

Le projet est organisé en fichiers SQL numérotés de `job1.sql` à `job24.sql`, chacun correspondant à une tâche spécifique.

### 🔹 Liste des Jobs et leurs fonctions :

| Fichier       | Description |
|--------------|-------------|
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

## 🛠️ Utilisation
1. **Exécuter un fichier SQL** :
   ```sh
   mysql -u root -p LaPlateforme < jobXX.sql
   ```
   Remplace `jobXX.sql` par le fichier SQL que tu veux exécuter.

2. **Lancer MySQL en mode interactif** et exécuter un fichier SQL :
   ```sh
   mysql -u root -p
   ```
   Puis, dans MySQL :
   ```sql
   SOURCE jobXX.sql;
   ```

3. **Sauvegarde et restauration de la base** :
   ```sh
   mysqldump -u root -p LaPlateforme > backup.sql
   mysql -u root -p LaPlateforme < backup.sql
   ```

## 🚀 Contribution
Si tu veux modifier ou améliorer ce projet :
1. Clone le dépôt :
   ```sh
   git clone <URL_GITHUB>
   ```
2. Ajoute tes modifications et commit :
   ```sh
   git add .
   git commit -m "Ajout d'une nouvelle requête SQL"
   ```
3. Pousse tes changements sur GitHub :
   ```sh
   git push origin main
   ```

## 📌 Auteur
Projet réalisé par **LARCHER** dans le cadre de l'apprentissage des bases de données SQL.

📅 Date : [MARS, 2025]

