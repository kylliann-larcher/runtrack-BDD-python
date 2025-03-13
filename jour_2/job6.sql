/* Job 6: Calculer la capacité totale des salles */
USE LaPlateforme;
SELECT CONCAT('La capacité de toutes les salles est de : ', SUM(capacite), ' places') AS resultat
FROM salle;
