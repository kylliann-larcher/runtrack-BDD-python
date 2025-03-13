/* Job 8: Créer une base de données pour un zoo et gérer les relations */
CREATE DATABASE IF NOT EXISTS zoo;
USE zoo;

/* Création de la table cage */
CREATE TABLE IF NOT EXISTS cage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    superficie INT NOT NULL,
    capacite_max INT NOT NULL
);

/* Création de la table animal */
CREATE TABLE IF NOT EXISTS animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    race VARCHAR(255) NOT NULL,
    id_cage INT,
    date_naissance DATE,
    pays_origine VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_cage) REFERENCES cage(id) ON DELETE SET NULL
);

/* Insertion des données dans la table cage */
INSERT INTO cage (superficie, capacite_max) VALUES
    (50, 5),
    (100, 10),
    (200, 15)
ON DUPLICATE KEY UPDATE superficie=VALUES(superficie), capacite_max=VALUES(capacite_max);

/* Insertion des données dans la table animal */
INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES
    ('Simba', 'Lion', 1, '2018-06-15', 'Kenya'),
    ('Zazu', 'Perroquet', 2, '2020-03-22', 'Brésil'),
    ('Baloo', 'Ours', 3, '2015-09-10', 'Canada')
ON DUPLICATE KEY UPDATE id_cage=VALUES(id_cage);

/* Calculer la superficie totale des cages */
SELECT SUM(superficie) AS superficie_totale FROM cage;

/* Afficher tous les animaux et leurs cages */
SELECT animal.nom, animal.race, animal.date_naissance, animal.pays_origine, cage.superficie, cage.capacite_max 
FROM animal
LEFT JOIN cage ON animal.id_cage = cage.id;
