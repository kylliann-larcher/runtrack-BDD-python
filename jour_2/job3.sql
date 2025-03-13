/* Job 3: Insérer des données dans les tables */
USE LaPlateforme;

INSERT INTO etage (nom, numero, superficie) VALUES
    ('RDC', 0, 500),
    ('R+1', 1, 500)
ON DUPLICATE KEY UPDATE superficie=VALUES(superficie);

INSERT INTO salle (nom, id_etage, capacite) VALUES
    ('Lounge', 1, 100),
    ('Studio Son', 1, 5),
    ('Broadcasting', 2, 50),
    ('Bocal Peda', 2, 4),
    ('Coworking', 2, 80),
    ('Studio Video', 2, 5)
ON DUPLICATE KEY UPDATE capacite=VALUES(capacite);
