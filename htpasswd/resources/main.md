# HTPASSWD

Le fichier htpasswd permet de créer et de maintenir les fichiers textes où sont stockés les
noms d'utilisateurs et mots de passe pour l'authentification de base des utilisateurs HTTP.

    + d'infos ici : https://httpd.apache.org/docs/2.4/fr/programs/htpasswd.html

1. Le script urlBuster.py nous indiquait l'existence d'une ressource /admin ici : http://192.168.1.16/admin

On arrive sur un formulaire qui, à priori, n'authorise que les administrateurs à se connecter.
En supposant que les credentials des admins sont stockés dans le fameux fichier htpasswd, nous savons quel fichier chercher

2. Toujours grâce au scrip urlBuster.py, il indiquait une ressource à l'URL : http://192.168.1.16/robots.txt

En s'y rendant, nous comprenons qu'il existe une autre ressource, du nom de whatever, donc http://192.168.1.16/whatever/

Sur cette page, il y a un fichier disponible du nom de htpasswd, intéressant.

On le télécharge et l'on voit qu'il contient : root:8621ffdbc5698829397d97767ac13db3

C'est du MD5. 8621ffdbc5698829397d97767ac13db3 = dragon

3. On revient sur /admin et on se connecte avec root:dragon, et voilà 

 