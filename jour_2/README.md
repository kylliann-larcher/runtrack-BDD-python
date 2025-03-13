# runtrack_jour_2
# 📌 Projet SQL - LaPlateforme

## 📂 Organisation des fichiers
Ce projet contient une série de fichiers SQL organisés dans un dossier **jourXX**, chacun correspondant à une tâche spécifique pour gérer une base de données.

### 📑 **Structure des fichiers**
- `job01.sql` → Récupération des étudiants.
- `job02.sql` → Création des tables `etage` et `salle`.
- `job03.sql` → Insertion de données.
- `job04.sql` → Récupération des salles et capacités.
- `job05.sql` → Calcul de la superficie des étages.
- `job06.sql` → Calcul de la capacité des salles.
- `job07.sql` → Gestion des employés et des services.
- `job08.sql` → Gestion d'un zoo avec des animaux et des cages.

## 🚀 **Installation et utilisation**

### 🔹 **Prérequis**
- MySQL installé sur votre machine.
- Un terminal ou un outil comme MySQL Workbench ou l'extension MySQL pour VS Code.

### 🔹 **Exécution des scripts SQL**
1. **Se connecter à MySQL** :
   ```sh
   mysql -u root -p
   ```
2. **Sélectionner la base de données** (si nécessaire) :
   ```sql
   USE LaPlateforme;
   ```
3. **Exécuter un fichier SQL** :
   ```sh
   SOURCE chemin/vers/job01.sql;
   ```

## 🛠 **Développement et gestion du projet**
### 🔹 **Organisation des fichiers sur GitHub**
1. **Ajouter et enregistrer les fichiers** :
   ```sh
   git add jourXX/
   git commit -m "Ajout des fichiers SQL pour jourXX"
   git push origin main
   ```
2. **Créer une nouvelle branche pour des modifications** :
   ```sh
   git checkout -b nouvelle-fonctionnalite
   ```

## ✨ **Fonctionnalités principales**
- Création et manipulation de bases de données.
- Utilisation de relations entre les tables (`FOREIGN KEY`).
- Calculs avancés (`SUM()`, `JOIN`).
- Gestion des employés et des services.
- Gestion d’un zoo avec des relations entre animaux et cages.

## 🤝 **Contributions**
Les contributions sont les bienvenues ! Pour proposer une modification :
1. Forkez le projet.
2. Créez une nouvelle branche.
3. Proposez une pull request.

📧 **Contact** : Si vous avez des questions, ouvrez une issue ou contactez-moi sur GitHub ! 🚀

