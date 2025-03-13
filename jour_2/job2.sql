/* Job 2: Créer les tables etage et salle */
USE LaPlateforme;

CREATE TABLE IF NOT EXISTS etage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    numero INT,
    superficie INT
);

CREATE TABLE IF NOT EXISTS salle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    id_etage INT,
    capacite INT,
    FOREIGN KEY (id_etage) REFERENCES etage(id) ON DELETE CASCADE
);
