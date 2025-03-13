/* Job 5: Calculer la superficie totale des étages */
USE LaPlateforme;
SELECT CONCAT('La superficie de La Plateforme est de ', SUM(superficie), ' m2') AS resultat
FROM etage;
