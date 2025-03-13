/* Job 7: Créer les tables employe et service et gérer les relations */
USE LaPlateforme;

/* Création de la table service */
CREATE TABLE IF NOT EXISTS service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

/* Création de la table employe */
CREATE TABLE IF NOT EXISTS employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    salaire DECIMAL(10,2) NOT NULL,
    id_service INT,
    FOREIGN KEY (id_service) REFERENCES service(id) ON DELETE SET NULL
);

/* Insertion des données dans la table service */
INSERT INTO service (nom) VALUES
    ('Développement'),
    ('Marketing'),
    ('RH')
ON DUPLICATE KEY UPDATE nom=VALUES(nom);

/* Insertion des données dans la table employe */
INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
    ('Dupont', 'Jean', 3200.00, 1),
    ('Martin', 'Sophie', 2800.00, 2),
    ('Durand', 'Paul', 4000.00, 1),
    ('Lemoine', 'Claire', 3500.00, 3)
ON DUPLICATE KEY UPDATE salaire=VALUES(salaire), id_service=VALUES(id_service);

/* Récupérer tous les employés gagnant plus de 3000€ */
SELECT * FROM employe WHERE salaire > 3000;

/* Récupérer les employés et leur service respectif */
SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS service
FROM employe
LEFT JOIN service ON employe.id_service = service.id;
