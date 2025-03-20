/* Job 1 Créer une base de données nommée “store” et les tables “product” et
“category”.*/
 mysql -u root -p
 mysql> CREATE DATABASE store
    -> ;
mysql> USE store;  

mysql> CREATE TABLE product (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(255),
    -> description TEXT,
    -> price INT,
    -> quantity INT,
    -> id_category INT
    -> );

mysql> CREATE TABLE category (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(255)
    -> );
mysql> SHOW COLUMNS FROM category ;           
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |       
+-------+--------------+------+-----+---------+----------------+       
| id    | int          | NO   | PRI | NULL    | auto_increment |       
| name  | varchar(255) | YES  |     | NULL    |                |       
+-------+--------------+------+-----+---------+----------------+    

mysql> SHOW COLUMNS FROM product ; 
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          | 
+-------------+--------------+------+-----+---------+----------------+ 
| id          | int          | NO   | PRI | NULL    | auto_increment | 
| name        | varchar(255) | YES  |     | NULL    |                | 
| description | text         | YES  |     | NULL    |                | 
| price       | int          | YES  |     | NULL    |                | 
| quantity    | int          | YES  |     | NULL    |                | 
| id_category | int          | YES  |     | NULL    |                | 
+-------------+--------------+------+-----+---------+----------------+ 
6 rows in set (0.00 sec)